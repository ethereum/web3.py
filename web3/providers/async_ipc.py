import asyncio
from concurrent.futures import (
    ThreadPoolExecutor,
)
import errno
from json import (
    JSONDecodeError,
)
import logging
from pathlib import (
    Path,
)
import sys
import threading
from types import (
    TracebackType,
)
from typing import (
    Any,
    Optional,
    Tuple,
    Type,
    Union,
)

from web3._utils.async_caching import (
    async_lock,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from .async_base import (
    AsyncJSONBaseProvider,
)
from .ipc import (
    get_default_ipc_path,
    has_valid_json_rpc_ending,
)


async def async_get_ipc_socket(
    ipc_path: str, timeout: float = 2.0
) -> Tuple[asyncio.StreamReader, asyncio.StreamWriter]:
    if sys.platform == "win32":
        # On Windows named pipe is used. Simulate socket with it.
        from web3._utils.windows import (
            NamedPipe,
        )

        return NamedPipe(ipc_path)
    else:
        return await asyncio.open_unix_connection(ipc_path)


class PersistantSocket:
    sock: Optional[Tuple[asyncio.StreamReader, asyncio.StreamWriter]] = None

    def __init__(self, ipc_path: str) -> None:
        self.ipc_path = ipc_path

    async def __aenter__(self) -> Tuple[asyncio.StreamReader, asyncio.StreamWriter]:
        if not self.ipc_path:
            raise FileNotFoundError(
                f"cannot connect to IPC socket at path: {self.ipc_path!r}"
            )

        if not self.sock:
            self.sock = await self._open()
        return self.sock

    async def __aexit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        # only close the socket if there was an error
        if exc_value is not None:
            try:
                reader, writer = self.sock
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
            self.sock = None

    async def _open(self) -> Tuple[asyncio.StreamReader, asyncio.StreamWriter]:
        return await async_get_ipc_socket(self.ipc_path)

    async def reset(self) -> Tuple[asyncio.StreamReader, asyncio.StreamWriter]:
        reader, writer = self.sock
        writer.close()
        await writer.wait_closed()
        self.sock = await self._open()
        return self.sock


_async_session_cache_lock = threading.Lock()
_async_session_pool = ThreadPoolExecutor(max_workers=1)


class AsyncIPCProvider(AsyncJSONBaseProvider):
    logger = logging.getLogger("web3.providers.AsyncIPCProvider")
    _socket = None

    def __init__(
        self,
        ipc_path: Union[str, Path] = None,
        timeout: int = 10,
    ) -> None:
        if ipc_path is None:
            self.ipc_path = get_default_ipc_path()
        elif isinstance(ipc_path, str) or isinstance(ipc_path, Path):
            self.ipc_path = str(Path(ipc_path).expanduser().resolve())
        else:
            raise TypeError("ipc_path must be of type string or pathlib.Path")

        self.timeout = timeout
        self._socket = PersistantSocket(self.ipc_path)
        super().__init__()

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {self.ipc_path}>"

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        self.logger.debug(
            f"Making async request IPC. Path: {self.ipc_path}, Method: {method}"
        )
        request = self.encode_rpc_request(method, params)

        async with self._socket as sock:
            reader, writer = sock
            try:
                writer.write(request)
                await writer.drain()
            except OSError as e:
                # Broken pipe
                if e.errno == errno.EPIPE:
                    # one extra attempt, then give up
                    new_sock = await self._socket.reset()
                    reader, writer = new_sock
                    writer.write(request)
                    await writer.drain()

            async def decode_response() -> RPCResponse:
                raw_response = b""
                while True:
                    async with async_lock(
                        _async_session_pool, _async_session_cache_lock
                    ):
                        raw_response += await reader.readline()
                    if raw_response == b"":
                        await asyncio.sleep(0)
                    elif has_valid_json_rpc_ending(raw_response):
                        try:
                            response = self.decode_rpc_response(raw_response)
                        except JSONDecodeError:
                            await asyncio.sleep(0)
                        else:
                            return response
                    else:
                        await asyncio.sleep(0)

            return await asyncio.wait_for(decode_response(), self.timeout)
