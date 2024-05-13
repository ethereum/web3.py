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
    List,
    Optional,
    Tuple,
    Union,
    cast,
)

from eth_utils import (
    to_text,
)

from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from . import (
    PersistentConnectionProvider,
)
from ..._utils.batching import (
    BATCH_REQUEST_ID,
    sort_batch_response_by_response_ids,
)
from ..._utils.caching import (
    async_handle_request_caching,
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
            request_data = self.encode_rpc_request(
                RPCEndpoint("web3_clientVersions"), []
            )
            self._writer.write(request_data)
            current_request_id = json.loads(request_data)["id"]
            await self._get_response_for_request_id(current_request_id, timeout=2)
            return True
        except (OSError, ProviderConnectionError) as e:
            if show_traceback:
                raise ProviderConnectionError(
                    f"Problem connecting to provider with error: {type(e)}: {e}"
                )
            return False

    async def _provider_specific_connect(self) -> None:
        self._reader, self._writer = await async_get_ipc_socket(self.ipc_path)

    async def _provider_specific_disconnect(self) -> None:
        if self._writer and not self._writer.is_closing():
            self._writer.close()
            await self._writer.wait_closed()
            self._writer = None
        if self._reader:
            self._reader = None

    async def _reset_socket(self) -> None:
        self._writer.close()
        await self._writer.wait_closed()
        self._reader, self._writer = await async_get_ipc_socket(self.ipc_path)

    @async_handle_request_caching
    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        if self._writer is None:
            raise ProviderConnectionError(
                "Connection to ipc socket has not been initiated for the provider."
            )

        request_data = self.encode_rpc_request(method, params)
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

        current_request_id = json.loads(request_data)["id"]
        response = await self._get_response_for_request_id(current_request_id)

        return response

    async def make_batch_request(
        self, requests: List[Tuple[RPCEndpoint, Any]]
    ) -> List[RPCResponse]:
        if self._writer is None:
            raise ProviderConnectionError(
                "Connection to ipc socket has not been initiated for the provider."
            )

        request_data = self.encode_batch_rpc_request(requests)
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

        response = cast(
            List[RPCResponse], await self._get_response_for_request_id(BATCH_REQUEST_ID)
        )
        return response

    async def _provider_specific_message_listener(self) -> None:
        self._raw_message += to_text(await self._reader.read(4096)).lstrip()

        while self._raw_message:
            try:
                response, pos = self._decoder.raw_decode(self._raw_message)
            except JSONDecodeError:
                break

            if isinstance(response, list):
                response = sort_batch_response_by_response_ids(response)

            is_subscription = (
                response.get("method") == "eth_subscription"
                if not isinstance(response, list)
                else False
            )
            await self._request_processor.cache_raw_response(
                response, subscription=is_subscription
            )
            self._raw_message = self._raw_message[pos:].lstrip()

    def _error_log_listener_task_exception(self, e: Exception) -> None:
        super()._error_log_listener_task_exception(e)
        # reset the raw message buffer on exception when error logging
        self._raw_message = ""
