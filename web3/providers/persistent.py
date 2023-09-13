from abc import (
    ABC,
)
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

DEFAULT_PERSISTENT_CONNECTION_TIMEOUT = 20


class PersistentConnectionProvider(AsyncJSONBaseProvider, ABC):
    logger = logging.getLogger("web3.providers.PersistentConnectionProvider")
    has_persistent_connection = True
    ws: Optional[WebSocketClientProtocol] = None

    _request_processor: RequestProcessor

    def __init__(
        self,
        endpoint_uri: str,
        request_cache_size: int = 100,
        call_timeout: int = DEFAULT_PERSISTENT_CONNECTION_TIMEOUT,
    ) -> None:
        super().__init__()
        self.endpoint_uri = endpoint_uri
        self._request_processor = RequestProcessor(
            self,
            request_cache_size=request_cache_size,
        )
        self.call_timeout = call_timeout

    async def connect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def disconnect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")
