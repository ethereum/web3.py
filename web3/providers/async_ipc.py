import asyncio
import logging
import socket
import sys
import threading

from json import (
    JSONDecodeError,
)

from pathlib import (
    Path,
)
from types import (
    TracebackType,
)

from typing import (
    Union,
    Type,
    Any,
)
from web3._utils.windows import (
    NamedPipe,
)
from .base import (
    JSONBaseProvider,
)
from .ipc import (
    get_default_ipc_path,
    has_valid_json_rpc_ending,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from web3._utils.threads import (
    Timeout,
)


async def async_get_ipc_socket(
        ipc_path: str, timeout: float = 2.0
) -> Union[socket.socket, NamedPipe]:
    if sys.platform == "win32":
        return NamedPipe(ipc_path)
    else:
        reader, writer = await asyncio.open_unix_connection(ipc_path)
        writer.write_eof()
        sock = writer.get_extra_info('socket')
        sock.settimeout(timeout)
        return sock


class PersistantSocket:
    sock = None

    def __init__(self, ipc_path: str) -> None:
        self.ipc_path = ipc_path

    async def __aenter__(self) -> socket.socket:
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
                self.sock.close()
            except Exception:
                pass
            self.sock = None

    async def _open(self) -> socket.socket:
        return await async_get_ipc_socket(self.ipc_path)

    async def reset(self) -> socket.socket:
        self.sock.close()
        self.sock = await self._open()
        return self.sock


class AsyncIPCProvider(JSONBaseProvider):
    logger = logging.getLogger("web3.providers.AsyncIPCProvider")
    _socket = None

    def __init__(
            self,
            ipc_path: Union[str, Path] = None,
            timeout: int = 10,
            *args: Any,
            **kwargs: Any,
    ) -> None:
        if ipc_path is None:
            self.ipc_path = get_default_ipc_path()
        elif isinstance(ipc_path, str) or isinstance(ipc_path, Path):
            self.ipc_path = str(Path(ipc_path).expanduser().resolve())
        else:
            raise TypeError("ipc_path must be of type string or pathlib.Path")

        self.timeout = timeout
        self._lock = threading.Lock()
        self._socket = PersistantSocket(self.ipc_path)
        super().__init__()

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {self.ipc_path}>"

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        self.logger.debug(
            f"Making request IPC. Path: {self.ipc_path}, Method: {method}"
        )
        request = self.encode_rpc_request(method, params)

        with self._lock, self._socket as sock:
            try:
                sock.sendall(request)
            except BrokenPipeError:
                # one extra attempt, then give up
                sock = self._socket.reset()
                sock.sendall(request)

            raw_response = b""
            with Timeout(self.timeout) as timeout:
                while True:
                    try:
                        raw_response += await sock.sock_recv(sock, 4096)
                    except socket.timeout:
                        timeout.sleep(0)
                        continue
                    if raw_response == b"":
                        timeout.sleep(0)
                    elif has_valid_json_rpc_ending(raw_response):
                        try:
                            response = self.decode_rpc_response(raw_response)
                        except JSONDecodeError:
                            timeout.sleep(0)
                            continue
                        else:
                            return response
                    else:
                        timeout.sleep(0)
                        continue
