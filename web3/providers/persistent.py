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
    Tuple,
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
    RPCEndpoint,
    RPCResponse,
)
from web3.utils import (
    SimpleCache,
)

DEFAULT_PERSISTENT_CONNECTION_TIMEOUT = 20


class PersistentConnectionProvider(AsyncJSONBaseProvider, ABC):
    logger = logging.getLogger("web3.providers.PersistentConnectionProvider")
    has_persistent_connection = True
    ws: Optional[WebSocketClientProtocol] = None

    def __init__(
        self,
        endpoint_uri: str,
        request_cache_size: int = 100,
        call_timeout: int = DEFAULT_PERSISTENT_CONNECTION_TIMEOUT,
    ) -> None:
        super().__init__()
        self.endpoint_uri = endpoint_uri
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
        method: RPCEndpoint,
        params: Any,
        response_formatters: Tuple[Callable[..., Any], ...],
    ) -> str:
        # copy the request counter and find the next request id without incrementing
        # since this is done when / if the request is successfully sent
        request_id = next(copy(self.request_counter))
        cache_key = generate_cache_key(request_id)

        self._bump_cache_if_key_present(cache_key, request_id)

        request_info = RequestInformation(method, params, response_formatters)
        self.logger.debug(
            f"Caching request info:\n    request_id={request_id},\n"
            f"    cache_key={cache_key},\n    request_info={request_info.__dict__}"
        )
        self._async_response_processing_cache.cache(
            cache_key,
            request_info,
        )
        return cache_key

    def _bump_cache_if_key_present(self, cache_key: str, request_id: int) -> None:
        """
        If the cache key is present in the cache, bump the cache key and request id
        by one to make room for the new request. This behavior is necessary when a
        request is made but inner requests, say to `eth_estimateGas` if the `gas` is
        missing, are made before the original request is sent.
        """
        if cache_key in self._async_response_processing_cache:
            original_request_info = (
                self._async_response_processing_cache.get_cache_entry(cache_key)
            )
            bump = generate_cache_key(request_id + 1)

            # recursively bump the cache if the new key is also present
            self._bump_cache_if_key_present(bump, request_id + 1)

            self.logger.debug(
                f"Caching internal request. Bumping original request in cache:\n"
                f"    request_id=[{request_id}] -> [{request_id + 1}],\n"
                f"    cache_key=[{cache_key}] -> [{bump}],\n"
                f"    request_info={original_request_info.__dict__}"
            )
            self._async_response_processing_cache.cache(bump, original_request_info)

    def _pop_cached_request_information(
        self, cache_key: str
    ) -> Optional[RequestInformation]:
        request_info = self._async_response_processing_cache.pop(cache_key)
        if request_info is not None:
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
            if (
                request_info is not None
                and request_info.method == "eth_unsubscribe"
                and response.get("result") is True
            ):
                # if successful unsubscribe request, remove the subscription request
                # information from the cache since it is no longer needed
                subscription_id = request_info.params[0]
                subscribe_cache_key = generate_cache_key(subscription_id)
                self._pop_cached_request_information(subscribe_cache_key)

        return request_info

    def _append_middleware_response_processor(
        self,
        middleware_response_processor: Callable[..., Any],
    ) -> None:
        request_id = next(copy(self.request_counter)) - 1
        cache_key = generate_cache_key(request_id)
        current_request_cached_info: RequestInformation = (
            self._async_response_processing_cache.get_cache_entry(cache_key)
        )
        if current_request_cached_info:
            current_request_cached_info.middleware_response_processors.append(
                middleware_response_processor
            )
