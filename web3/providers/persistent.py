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
from web3.types import (
    RPCResponse,
)

DEFAULT_PERSISTENT_CONNECTION_TIMEOUT = 50


class PersistentConnectionProvider(AsyncJSONBaseProvider, ABC):
    logger = logging.getLogger("web3.providers.PersistentConnectionProvider")
    has_persistent_connection = True

    _ws: Optional[WebSocketClientProtocol] = None
    _ws_lock: asyncio.Lock = asyncio.Lock()
    _request_processor: RequestProcessor

    def __init__(
        self,
        endpoint_uri: str,
        request_timeout: float = DEFAULT_PERSISTENT_CONNECTION_TIMEOUT,
        subscription_response_deque_size: int = 500,
    ) -> None:
        super().__init__()
        self.endpoint_uri = endpoint_uri
        self._request_processor = RequestProcessor(
            self,
            subscription_response_deque_size=subscription_response_deque_size,
        )
        self.request_timeout = request_timeout

    async def connect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def disconnect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def _ws_recv(self, timeout: float = None) -> RPCResponse:
        raise NotImplementedError("Must be implemented by subclasses")
