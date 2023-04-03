from abc import ABC
from copy import copy
from typing import Any, Dict, Optional, Tuple

from websockets.legacy.client import WebSocketClientProtocol

from web3._utils.caching import generate_cache_key
from web3.providers.async_base import AsyncJSONBaseProvider


class PersistentConnectionProvider(AsyncJSONBaseProvider, ABC):
    ws: Optional[WebSocketClientProtocol] = None
    websocket_timeout: Optional[int] = 20

    # process request responses asynchronously by storing formatters and
    # result processing fxns
    async_response_processing_cache: Dict[Any, Dict[str, Any]] = {}

    def cache_request_information(
        self,
        method: Any,
        params: Any,
        response_formatters: Tuple[Any, Any, Any],
    ) -> None:
        # copy the request counter and find the next request id without incrementing
        # since this is done when / if the request is successfully sent
        request_id = next(copy(self.request_counter))
        cache_key = generate_cache_key(request_id)
        self.async_response_processing_cache[cache_key] = {
            "method": method,
            "params": params,
            "response_formatters": response_formatters,
            "middleware_processing": [],  # handled in each middleware
        }
