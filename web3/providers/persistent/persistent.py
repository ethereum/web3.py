from abc import (
    ABC,
)
import asyncio
import logging
from typing import (
    Optional,
)

from web3._utils.caching import (
    generate_cache_key,
)
from web3.exceptions import (
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
    ) -> None:
        super().__init__()
        self._request_processor = RequestProcessor(
            self,
            subscription_response_queue_size=subscription_response_queue_size,
        )
        self.request_timeout = request_timeout
        self.silence_listener_task_exceptions = silence_listener_task_exceptions

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
        raise NotImplementedError("Must be implemented by subclasses")

    async def disconnect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def _message_listener(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def _get_response_for_request_id(
        self, request_id: RPCId, timeout: Optional[float] = None
    ) -> RPCResponse:
        if timeout is None:
            timeout = self.request_timeout

        async def _match_response_id_to_request_id() -> RPCResponse:
            request_cache_key = generate_cache_key(request_id)

            while True:
                # sleep(0) here seems to be the most efficient way to yield control
                # back to the event loop while waiting for the response to be in the
                # queue.
                await asyncio.sleep(0)

                if request_cache_key in self._request_processor._request_response_cache:
                    self.logger.debug(
                        f"Popping response for id {request_id} from cache."
                    )
                    popped_response = await self._request_processor.pop_raw_response(
                        cache_key=request_cache_key,
                    )
                    return popped_response

        try:
            # Add the request timeout around the while loop that checks the request
            # cache and tried to recv(). If the request is neither in the cache, nor
            # received within the request_timeout, raise ``TimeExhausted``.
            return await asyncio.wait_for(_match_response_id_to_request_id(), timeout)
        except asyncio.TimeoutError:
            raise TimeExhausted(
                f"Timed out waiting for response with request id `{request_id}` after "
                f"{self.request_timeout} second(s). This may be due to the provider "
                "not returning a response with the same id that was sent in the "
                "request or an exception raised during the request was caught and "
                "allowed to continue."
            )
