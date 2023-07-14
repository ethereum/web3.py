from abc import ABC
from copy import copy
from typing import (
    Any,
    Callable,
    Tuple,
)

from web3._utils.caching import (
    PersistentConnectionResponseProcessor,
    generate_cache_key,
)
from web3.providers.async_base import AsyncJSONBaseProvider
from web3.utils import SimpleCache


class PersistentConnectionProvider(AsyncJSONBaseProvider, ABC):
    def __init__(
        self,
        request_cache_size=1000,
    ) -> None:
        super().__init__()
        self.async_response_processing_cache: SimpleCache = SimpleCache(
            request_cache_size
        )

    def cache_request_information(
        self,
        method: Any,
        params: Any,
        response_formatters: Tuple[Callable[..., Any]],
    ) -> None:
        # copy the request counter and find the next request id without incrementing
        # since this is done when / if the request is successfully sent
        request_id = next(copy(self.request_counter))
        cache_key = generate_cache_key(request_id)
        self.async_response_processing_cache.cache(
            cache_key,
            PersistentConnectionResponseProcessor(method, params, response_formatters),
        )

    def _append_middleware_response_formatter(
        self,
        middleware_response_handler: Callable[..., Any],
    ):
        request_id = next(copy(self.request_counter)) - 1
        cache_key = generate_cache_key(request_id)
        current_request_cached_info: PersistentConnectionResponseProcessor = (
            self.async_response_processing_cache.get_cache_entry(cache_key)
        )
        current_request_cached_info.middleware_response_processors.append(
            middleware_response_handler
        )
