import asyncio
import errno
import json
from json import (
    JSONDecodeError,
)
import logging
from pathlib import (
    Path,
)
import sys
from typing import (
    Any,
    Optional,
    Tuple,
    Union,
)

from eth_utils import (
    to_text,
)

from web3.types import (
    RPCResponse,
)

from . import (
    PersistentConnectionProvider,
)
from ...exceptions import (
    ProviderConnectionError,
    Web3TypeError,
)
from ..ipc import (
    get_default_ipc_path,
)


async def async_get_ipc_socket(
    ipc_path: str,
) -> Tuple[asyncio.StreamReader, asyncio.StreamWriter]:
    if sys.platform == "win32":
        # On Windows named pipe is used. Simulate socket with it.
        from web3._utils.windows import (
            NamedPipe,
        )

        return NamedPipe(ipc_path)
    else:
        return await asyncio.open_unix_connection(ipc_path)


class AsyncIPCProvider(PersistentConnectionProvider):
    logger = logging.getLogger("web3.providers.AsyncIPCProvider")

    _reader: Optional[asyncio.StreamReader] = None
    _writer: Optional[asyncio.StreamWriter] = None
    _decoder: json.JSONDecoder = json.JSONDecoder()
    _raw_message: str = ""

    def __init__(
        self,
        ipc_path: Optional[Union[str, Path]] = None,
        # `PersistentConnectionProvider` kwargs can be passed through
        **kwargs: Any,
    ) -> None:
        if ipc_path is None:
            self.ipc_path = get_default_ipc_path()
        elif isinstance(ipc_path, str) or isinstance(ipc_path, Path):
            self.ipc_path = str(Path(ipc_path).expanduser().resolve())
        else:
            raise Web3TypeError("ipc_path must be of type string or pathlib.Path")

        super().__init__(**kwargs)

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {self.ipc_path}>"

    async def is_connected(self, show_traceback: bool = False) -> bool:
        if not self._writer or not self._reader:
            return False

        try:
            await self.make_request("web3_clientVersion", [])
            return True
        except (OSError, ProviderConnectionError) as e:
            if show_traceback:
                raise ProviderConnectionError(
                    f"Problem connecting to provider with error: {type(e)}: {e}"
                )
            return False

    async def socket_send(self, request_data: bytes) -> None:
        if self._writer is None:
            raise ProviderConnectionError(
                "Connection to ipc socket has not been initiated for the provider."
            )

        return await asyncio.wait_for(
            self._socket_send(request_data), timeout=self.request_timeout
        )

    async def socket_recv(self) -> RPCResponse:
        while True:
            # yield to the event loop to allow other tasks to run
            await asyncio.sleep(0)

            try:
                response, pos = self._decoder.raw_decode(self._raw_message)
                self._raw_message = self._raw_message[pos:].lstrip()
                return response
            except JSONDecodeError:
                # read more data from the socket if the current raw message is
                # incomplete
                self._raw_message += to_text(await self._reader.read(4096)).lstrip()

    # -- private methods -- #

    async def _socket_send(self, request_data: bytes) -> None:
        try:
            self._writer.write(request_data)
            await self._writer.drain()
        except OSError as e:
            # Broken pipe
            if e.errno == errno.EPIPE:
                # one extra attempt, then give up
                await self._reset_socket()
                self._writer.write(request_data)
                await self._writer.drain()

    async def _reset_socket(self) -> None:
        self._writer.close()
        await self._writer.wait_closed()
        self._reader, self._writer = await async_get_ipc_socket(self.ipc_path)

    async def _provider_specific_connect(self) -> None:
        self._reader, self._writer = await async_get_ipc_socket(self.ipc_path)

    async def _provider_specific_disconnect(self) -> None:
        if self._writer and not self._writer.is_closing():
            self._writer.close()
            await self._writer.wait_closed()
            self._writer = None
        if self._reader:
            self._reader = None

    async def _provider_specific_socket_reader(self) -> RPCResponse:
        return await self.socket_recv()

    def _error_log_listener_task_exception(self, e: Exception) -> None:
        super()._error_log_listener_task_exception(e)
        # reset the raw message buffer on exception when error logging
        self._raw_message = ""
