from abc import (
    ABC,
)
import asyncio
import logging
from typing import (
    Optional,
)

from websockets import (
    ConnectionClosed,
    WebSocketException,
)

from web3._utils.caching import (
    generate_cache_key,
)
from web3.exceptions import (
    ProviderConnectionError,
    TimeExhausted,
)
from web3.providers.async_base import (
    AsyncJSONBaseProvider,
)
from web3.providers.persistent.request_processor import (
    RequestProcessor,
)
from web3.types import (
    RPCId,
    RPCResponse,
)

DEFAULT_PERSISTENT_CONNECTION_TIMEOUT = 30.0


class PersistentConnectionProvider(AsyncJSONBaseProvider, ABC):
    logger = logging.getLogger("web3.providers.PersistentConnectionProvider")
    has_persistent_connection = True

    _request_processor: RequestProcessor
    _message_listener_task: Optional["asyncio.Task[None]"] = None
    _listen_event: asyncio.Event = asyncio.Event()

    def __init__(
        self,
        request_timeout: float = DEFAULT_PERSISTENT_CONNECTION_TIMEOUT,
        subscription_response_queue_size: int = 500,
        silence_listener_task_exceptions: bool = False,
        max_connection_retries: int = 5,
    ) -> None:
        super().__init__()
        self._request_processor = RequestProcessor(
            self,
            subscription_response_queue_size=subscription_response_queue_size,
        )
        self.request_timeout = request_timeout
        self.silence_listener_task_exceptions = silence_listener_task_exceptions
        self._max_connection_retries = max_connection_retries

    def get_endpoint_uri_or_ipc_path(self) -> str:
        if hasattr(self, "endpoint_uri"):
            return str(self.endpoint_uri)
        elif hasattr(self, "ipc_path"):
            return str(self.ipc_path)
        else:
            raise AttributeError(
                "`PersistentConnectionProvider` must have either `endpoint_uri` or "
                "`ipc_path` attribute."
            )

    async def connect(self) -> None:
        _connection_attempts = 0
        _backoff_rate_change = 1.75
        _backoff_time = 1.75

        while _connection_attempts != self._max_connection_retries:
            try:
                _connection_attempts += 1
                await self._provider_specific_connect()
                self._message_listener_task = asyncio.create_task(
                    self._message_listener()
                )
                self._message_listener_task.add_done_callback(
                    self._message_listener_callback
                )
                break
            except (WebSocketException, OSError) as e:
                if _connection_attempts == self._max_connection_retries:
                    raise ProviderConnectionError(
                        f"Could not connect to: {self.get_endpoint_uri_or_ipc_path()}. "
                        f"Retries exceeded max of {self._max_connection_retries}."
                    ) from e
                self.logger.info(
                    f"Could not connect to: {self.get_endpoint_uri_or_ipc_path()}. "
                    f"Retrying in {round(_backoff_time, 1)} seconds.",
                    exc_info=True,
                )
                await asyncio.sleep(_backoff_time)
                _backoff_time *= _backoff_rate_change

    async def disconnect(self) -> None:
        if self._message_listener_task is not None:
            try:
                self._message_listener_task.cancel()
                await self._message_listener_task
            except (asyncio.CancelledError, StopAsyncIteration, ConnectionClosed):
                pass
        await self._provider_specific_disconnect()
        self.logger.debug(
            f'Successfully disconnected from: "{self.get_endpoint_uri_or_ipc_path()}'
        )

    # -- private methods -- #

    async def _provider_specific_connect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def _provider_specific_disconnect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def _provider_specific_message_listener(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    def _message_listener_callback(
        self, _message_listener_task: "asyncio.Task[None]"
    ) -> None:
        # Since we await subscription messages in the queue, subscription message
        # streams don't know when the listener task is done and would hang indefinitely.
        # This puts a `None` in the queue to signal that the listener task is done.
        self._request_processor._subscription_response_queue.put_nowait(None)

    async def _message_listener(self) -> None:
        self.logger.info(
            f"{self.__class__.__qualname__} listener background task started. Storing "
            "all messages in appropriate request processor queues / caches to be "
            "processed."
        )
        while True:
            # the use of sleep(0) seems to be the most efficient way to yield control
            # back to the event loop to share the loop with other tasks.
            await asyncio.sleep(0)
            try:
                await self._provider_specific_message_listener()
            except Exception as e:
                if not self.silence_listener_task_exceptions:
                    raise e
                else:
                    self._error_log_listener_task_exception(e)

    def _error_log_listener_task_exception(self, e: Exception) -> None:
        """
        When silencing listener task exceptions, this method is used to log the
        exception and keep the listener task alive. Override this method to fine-tune
        error logging behavior for the implementation class.
        """
        self.logger.error(
            "Exception caught in listener, error logging and keeping "
            "listener background task alive."
            f"\n    error={e.__class__.__name__}: {e}"
        )

    def _handle_listener_task_exceptions(self) -> None:
        """
        Should be called every time a `PersistentConnectionProvider` is polling for
        messages in the main loop. If the message listener task has completed and an
        exception was recorded, raise the exception in the main loop.
        """
        msg_listener_task = getattr(self, "_message_listener_task", None)
        if (
            msg_listener_task
            and msg_listener_task.done()
            and msg_listener_task.exception()
        ):
            raise msg_listener_task.exception()

    async def _get_response_for_request_id(
        self, request_id: RPCId, timeout: Optional[float] = None
    ) -> RPCResponse:
        if timeout is None:
            timeout = self.request_timeout

        async def _match_response_id_to_request_id() -> RPCResponse:
            request_cache_key = generate_cache_key(request_id)

            while True:
                # check if an exception was recorded in the listener task and raise it
                # in the main loop if so
                self._handle_listener_task_exceptions()

                if request_cache_key in self._request_processor._request_response_cache:
                    self.logger.debug(
                        f"Popping response for id {request_id} from cache."
                    )
                    popped_response = await self._request_processor.pop_raw_response(
                        cache_key=request_cache_key,
                    )
                    return popped_response
                else:
                    await asyncio.sleep(0)

        try:
            # Add the request timeout around the while loop that checks the request
            # cache. If the request is not in the cache within the request_timeout,
            # raise ``TimeExhausted``.
            return await asyncio.wait_for(_match_response_id_to_request_id(), timeout)
        except asyncio.TimeoutError:
            raise TimeExhausted(
                f"Timed out waiting for response with request id `{request_id}` after "
                f"{self.request_timeout} second(s). This may be due to the provider "
                "not returning a response with the same id that was sent in the "
                "request or an exception raised during the request was caught and "
                "allowed to continue."
            )
