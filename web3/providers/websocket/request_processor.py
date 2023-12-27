import asyncio
from copy import (
    copy,
)
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Optional,
    Tuple,
)

from web3._utils.caching import (
    RequestInformation,
    generate_cache_key,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)
from web3.utils import (
    SimpleCache,
)

if TYPE_CHECKING:
    from web3.providers.persistent import (
        PersistentConnectionProvider,
    )


class RequestProcessor:
    _subscription_queue_synced_with_ws_stream: bool = False

    def __init__(
        self,
        provider: "PersistentConnectionProvider",
        subscription_response_queue_size: int = 500,
    ) -> None:
        self._provider = provider

        self._request_information_cache: SimpleCache = SimpleCache(500)
        self._request_response_cache: SimpleCache = SimpleCache(500)
        self._subscription_response_queue: asyncio.Queue[RPCResponse] = asyncio.Queue(
            maxsize=subscription_response_queue_size
        )

    @property
    def active_subscriptions(self) -> Dict[str, Any]:
        return {
            value.subscription_id: {"params": value.params}
            for key, value in self._request_information_cache.items()
            if value.method == "eth_subscribe"
        }

    # request information cache

    def cache_request_information(
        self,
        method: RPCEndpoint,
        params: Any,
        response_formatters: Tuple[Callable[..., Any], ...],
    ) -> str:
        # copy the request counter and find the next request id without incrementing
        # since this is done when / if the request is successfully sent
        request_id = next(copy(self._provider.request_counter))
        cache_key = generate_cache_key(request_id)

        self._bump_cache_if_key_present(cache_key, request_id)

        request_info = RequestInformation(
            method,
            params,
            response_formatters,
        )
        self._provider.logger.debug(
            f"Caching request info:\n    request_id={request_id},\n"
            f"    cache_key={cache_key},\n    request_info={request_info.__dict__}"
        )
        self._request_information_cache.cache(
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
        if cache_key in self._request_information_cache:
            original_request_info = self._request_information_cache.get_cache_entry(
                cache_key
            )
            bump = generate_cache_key(request_id + 1)

            # recursively bump the cache if the new key is also present
            self._bump_cache_if_key_present(bump, request_id + 1)

            self._provider.logger.debug(
                "Caching internal request. Bumping original request in cache:\n"
                f"    request_id=[{request_id}] -> [{request_id + 1}],\n"
                f"    cache_key=[{cache_key}] -> [{bump}],\n"
                f"    request_info={original_request_info.__dict__}"
            )
            self._request_information_cache.cache(bump, original_request_info)

    def pop_cached_request_information(
        self, cache_key: str
    ) -> Optional[RequestInformation]:
        request_info = self._request_information_cache.pop(cache_key)
        if request_info is not None:
            self._provider.logger.debug(
                "Request info popped from cache:\n"
                f"    cache_key={cache_key},\n    request_info={request_info.__dict__}"
            )
        return request_info

    def get_request_information_for_response(
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
                self._request_information_cache.get_cache_entry(cache_key)
            )

        else:
            # retrieve the request info from the cache using the request id
            cache_key = generate_cache_key(response["id"])
            request_info = (
                # pop the request info from the cache since we don't need to keep it
                # this keeps the cache size bounded
                self.pop_cached_request_information(cache_key)
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
                self.pop_cached_request_information(subscribe_cache_key)

        return request_info

    def append_middleware_response_processor(
        self,
        response: RPCResponse,
        middleware_response_processor: Callable[..., Any],
    ) -> None:
        response_id = response.get("id", None)

        if response_id is not None:
            cache_key = generate_cache_key(response_id)
            cached_request_info_for_id: RequestInformation = (
                self._request_information_cache.get_cache_entry(cache_key)
            )
            if cached_request_info_for_id is not None:
                cached_request_info_for_id.middleware_response_processors.append(
                    middleware_response_processor
                )
            else:
                self._provider.logger.debug(
                    f"No cached request info for response id `{response_id}`. Cannot "
                    f"append middleware response processor for response: {response}"
                )
        else:
            self._provider.logger.debug(
                "No response `id` in response. Cannot append middleware response "
                f"processor for response: {response}"
            )

    # raw response cache

    async def cache_raw_response(
        self, raw_response: Any, subscription: bool = False
    ) -> None:
        if subscription:
            if self._subscription_response_queue.full():
                self._provider.logger.info(
                    "Subscription queue is full. Waiting for provider to consume "
                    "messages before caching."
                )
                await self._provider._listen_event.wait()

            self._provider.logger.debug(
                f"Caching subscription response:\n    response={raw_response}"
            )
            await self._subscription_response_queue.put(raw_response)
        else:
            response_id = raw_response.get("id")
            cache_key = generate_cache_key(response_id)
            self._provider.logger.debug(
                f"Caching response:\n    response_id={response_id},\n"
                f"    cache_key={cache_key},\n    response={raw_response}"
            )
            self._request_response_cache.cache(cache_key, raw_response)

    def pop_raw_response(
        self, cache_key: str = None, subscription: bool = False
    ) -> Any:
        if subscription:
            qsize = self._subscription_response_queue.qsize()
            if qsize == 0:
                return None

            if not self._provider._listen_event.is_set():
                self._provider._listen_event.set()

            raw_response = self._subscription_response_queue.get_nowait()
            if qsize == 1:
                if not self._subscription_queue_synced_with_ws_stream:
                    self._subscription_queue_synced_with_ws_stream = True
                    self._provider.logger.info(
                        "Subscription response queue synced with websocket message "
                        "stream."
                    )
            else:
                if self._subscription_queue_synced_with_ws_stream:
                    self._subscription_queue_synced_with_ws_stream = False
                self._provider.logger.info(
                    f"Subscription response queue has {qsize} subscriptions. "
                    "Processing as FIFO."
                )

            self._provider.logger.debug(
                "Subscription response popped from queue to be processed:\n"
                f"    raw_response={raw_response}"
            )
        else:
            if not cache_key:
                raise ValueError(
                    "Must provide cache key when popping a non-subscription response."
                )

            raw_response = self._request_response_cache.pop(cache_key)
            if raw_response is not None:
                self._provider.logger.debug(
                    "Cached response popped from cache to be processed:\n"
                    f"    cache_key={cache_key},\n"
                    f"    raw_response={raw_response}"
                )

        return raw_response

    # request processor class methods

    def clear_caches(self) -> None:
        """
        Clear the request processor caches.
        """

        self._request_information_cache.clear()
        self._request_response_cache.clear()
        self._subscription_response_queue = asyncio.Queue(
            maxsize=self._subscription_response_queue.maxsize
        )
