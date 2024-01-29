from abc import (
    ABC,
)
import asyncio
import logging
from typing import (
    Optional,
)

from websockets.legacy.client import (
    WebSocketClientProtocol,
)

from web3.providers.async_base import (
    AsyncJSONBaseProvider,
)
from web3.providers.websocket.request_processor import (
    RequestProcessor,
)

DEFAULT_PERSISTENT_CONNECTION_TIMEOUT = 50.0


class PersistentConnectionProvider(AsyncJSONBaseProvider, ABC):
    logger = logging.getLogger("web3.providers.PersistentConnectionProvider")
    has_persistent_connection = True
    endpoint_uri: Optional[str] = None

    _ws: Optional[WebSocketClientProtocol] = None
    _request_processor: RequestProcessor
    _message_listener_task: Optional["asyncio.Task[None]"] = None
    _listen_event: asyncio.Event = asyncio.Event()

    def __init__(
        self,
        request_timeout: float = DEFAULT_PERSISTENT_CONNECTION_TIMEOUT,
        subscription_response_queue_size: int = 500,
    ) -> None:
        super().__init__()
        self._request_processor = RequestProcessor(
            self,
            subscription_response_queue_size=subscription_response_queue_size,
        )
        self.request_timeout = request_timeout

    async def connect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def disconnect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def _ws_message_listener(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")
