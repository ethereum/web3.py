from abc import (
    ABC,
)
from copy import (
    copy,
)
import logging
from typing import (
    Any,
    Callable,
    Optional,
)

from websockets.legacy.client import (
    WebSocketClientProtocol,
)

from web3._utils.caching import (
    RequestInformation,
    generate_cache_key,
)
from web3.providers.async_base import (
    AsyncJSONBaseProvider,
)
from web3.types import (
    FormattersDict,
    RPCResponse,
)
from web3.utils import (
    SimpleCache,
)

DEFAULT_PERSISTENT_CONNECTION_TIMEOUT = 20


class PersistentConnectionProvider(AsyncJSONBaseProvider, ABC):
    logger = logging.getLogger("web3.providers.PersistentConnectionProvider")
    ws: Optional[WebSocketClientProtocol] = None

    def __init__(
        self,
        request_cache_size: int = 100,
        call_timeout: int = DEFAULT_PERSISTENT_CONNECTION_TIMEOUT,
    ) -> None:
        super().__init__()
        self._async_response_processing_cache: SimpleCache = SimpleCache(
            request_cache_size
        )
        self.call_timeout = call_timeout

    async def connect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    async def disconnect(self) -> None:
        raise NotImplementedError("Must be implemented by subclasses")

    def _cache_request_information(
        self,
        method: Any,
        params: Any,
        response_formatters: FormattersDict,
    ) -> str:
        # copy the request counter and find the next request id without incrementing
        # since this is done when / if the request is successfully sent
        request_id = next(copy(self.request_counter))
        cache_key = generate_cache_key(request_id)
        request_info = RequestInformation(method, params, response_formatters)
        self.logger.debug(
            f"Caching request info:\n"
            f"    cache_key={cache_key},\n    request_info={request_info.__dict__}"
        )
        self._async_response_processing_cache.cache(
            cache_key,
            request_info,
        )
        return cache_key

    def _pop_cached_request_information(self, cache_key) -> RequestInformation:
        request_info = self._async_response_processing_cache.pop(cache_key)
        self.logger.debug(
            f"Request info popped from cache:\n"
            f"    cache_key={cache_key},\n    request_info={request_info.__dict__}"
        )
        return request_info

    def _get_request_information_for_response(
        self,
        response: RPCResponse,
    ) -> RequestInformation:
        if "method" in response and response["method"] == "eth_subscription":
            if "params" not in response:
                raise ValueError("Subscription response must have params field")
            if "subscription" not in response["params"]:
                raise ValueError(
                    "Subscription response params must have subscription field"
                )

            # retrieve the request info from the cache using the subscription id
            cache_key = generate_cache_key(response["params"]["subscription"])
            request_info = (
                # don't pop the request info from the cache, since we need to keep it
                # to process future subscription responses
                # i.e. subscription request information remains in the cache
                self._async_response_processing_cache.get_cache_entry(cache_key)
            )

        else:
            # retrieve the request info from the cache using the request id
            cache_key = generate_cache_key(response["id"])
            request_info = (
                # pop the request info from the cache since we don't need to keep it
                # this keeps the cache size bounded
                self._pop_cached_request_information(cache_key)
            )

        return request_info

    def _append_middleware_response_formatter(
        self,
        middleware_response_handler: Callable[..., Any],
    ) -> None:
        request_id = next(copy(self.request_counter)) - 1
        cache_key = generate_cache_key(request_id)
        current_request_cached_info: RequestInformation = (
            self._async_response_processing_cache.get_cache_entry(cache_key)
        )
        current_request_cached_info.middleware_response_processors.append(
            middleware_response_handler
        )
