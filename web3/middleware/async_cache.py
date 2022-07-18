from concurrent.futures import (
    ThreadPoolExecutor,
)
import functools
import threading
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
    Type,
    Union,
    cast,
)

from web3._utils.async_caching import (
    async_lock,
)
from web3._utils.caching import (
    SimpleCache,
    generate_cache_key,
    type_aware_cache_entry,
    type_aware_get_cache_entry,
)
from web3.middleware.cache import (
    SIMPLE_CACHE_RPC_WHITELIST,
    _should_cache_response,
)
from web3.types import (
    AsyncMiddleware,
    Middleware,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401

_async_request_thread_pool = ThreadPoolExecutor()


async def async_construct_simple_cache_middleware(
    cache_class: Union[Type[Dict[str, Any]], Type[SimpleCache]],
    rpc_whitelist: Collection[RPCEndpoint] = SIMPLE_CACHE_RPC_WHITELIST,
    should_cache_fn: Callable[
        [RPCEndpoint, Any, RPCResponse], bool
    ] = _should_cache_response,
) -> Middleware:
    """
    Constructs a middleware which caches responses based on the request
    ``method`` and ``params``

    :param cache_class: A ``SimpleCache`` class or any dictionary-like object.
    :param rpc_whitelist: A set of RPC methods which may have their responses cached.
    :param should_cache_fn: A callable which accepts ``method`` ``params`` and
        ``response`` and returns a boolean as to whether the response should be
        cached.
    """

    async def async_simple_cache_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], _async_w3: "Web3"
    ) -> AsyncMiddleware:
        cache = cache_class()
        lock = threading.Lock()

        async def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method in rpc_whitelist:
                async with async_lock(_async_request_thread_pool, lock):
                    cache_key = generate_cache_key(
                        f"{threading.get_ident()}:{(method, params)}"
                    )
                    if not type_aware_get_cache_entry(cache, cache_key):
                        response = await make_request(method, params)
                        if should_cache_fn(method, params, response):
                            type_aware_cache_entry(cache, cache_key, response)
                        return response
                    return type_aware_get_cache_entry(cache, cache_key)
            else:
                return await make_request(method, params)

        return middleware

    return async_simple_cache_middleware


async def _async_simple_cache_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], async_w3: "Web3"
) -> Middleware:
    middleware = await async_construct_simple_cache_middleware(
        cache_class=cast(Type[SimpleCache], functools.partial(SimpleCache, 256)),
    )
    return await middleware(make_request, async_w3)
