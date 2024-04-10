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
    RPCEndpoint,
    RPCResponse,
)

from . import (
    PersistentConnectionProvider,
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

    def __init__(
        self,
        ipc_path: Optional[Union[str, Path]] = None,
        max_connection_retries: int = 5,
        # `PersistentConnectionProvider` kwargs can be passed through
        **kwargs: Any,
    ) -> None:
        if ipc_path is None:
            self.ipc_path = get_default_ipc_path()
        elif isinstance(ipc_path, str) or isinstance(ipc_path, Path):
            self.ipc_path = str(Path(ipc_path).expanduser().resolve())
        else:
            raise Web3TypeError("ipc_path must be of type string or pathlib.Path")

        self._max_connection_retries = max_connection_retries
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

    async def connect(self) -> None:
        _connection_attempts = 0
        _backoff_rate_change = 1.75
        _backoff_time = 1.75

        while _connection_attempts != self._max_connection_retries:
            try:
                _connection_attempts += 1
                self._reader, self._writer = await async_get_ipc_socket(self.ipc_path)
                self._message_listener_task = asyncio.create_task(
                    self._message_listener()
                )
                break
            except OSError as e:
                if _connection_attempts == self._max_connection_retries:
                    raise ProviderConnectionError(
                        f"Could not connect to: {self.ipc_path}. "
                        f"Retries exceeded max of {self._max_connection_retries}."
                    ) from e
                self.logger.info(
                    f"Could not connect to: {self.ipc_path}. Retrying in "
                    f"{round(_backoff_time, 1)} seconds.",
                    exc_info=True,
                )
                await asyncio.sleep(_backoff_time)
                _backoff_time *= _backoff_rate_change

    async def disconnect(self) -> None:
        if self._writer and not self._writer.is_closing():
            self._writer.close()
            await self._writer.wait_closed()
            self._writer = None
            self.logger.debug(f'Successfully disconnected from : "{self.ipc_path}')

        try:
            self._message_listener_task.cancel()
            await self._message_listener_task
            self._reader = None
        except (asyncio.CancelledError, StopAsyncIteration):
            pass

        self._request_processor.clear_caches()

    async def _reset_socket(self) -> None:
        self._writer.close()
        await self._writer.wait_closed()
        self._reader, self._writer = await async_get_ipc_socket(self.ipc_path)

    @async_handle_request_caching
    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        request_data = self.encode_rpc_request(method, params)

        if self._writer is None:
            raise ProviderConnectionError(
                "Connection to ipc socket has not been initiated for the provider."
            )

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

    async def _message_listener(self) -> None:
        self.logger.info(
            "IPC socket listener background task started. Storing all messages in "
            "appropriate request processor queues / caches to be processed."
        )
        raw_message = ""
        decoder = json.JSONDecoder()

        while True:
            # the use of sleep(0) seems to be the most efficient way to yield control
            # back to the event loop to share the loop with other tasks.
            await asyncio.sleep(0)

            try:
                raw_message += to_text(await self._reader.read(4096)).lstrip()

                while raw_message:
                    try:
                        response, pos = decoder.raw_decode(raw_message)
                    except JSONDecodeError:
                        break

                    is_subscription = response.get("method") == "eth_subscription"
                    await self._request_processor.cache_raw_response(
                        response, subscription=is_subscription
                    )
                    raw_message = raw_message[pos:].lstrip()
            except Exception as e:
                if not self.silence_listener_task_exceptions:
                    loop = asyncio.get_event_loop()
                    for task in asyncio.all_tasks(loop=loop):
                        task.cancel()
                    raise e

                self.logger.error(
                    "Exception caught in listener, error logging and keeping listener "
                    f"background task alive.\n    error={e}"
                )
                # if only error logging, reset the ``raw_message`` buffer and continue
                raw_message = ""
