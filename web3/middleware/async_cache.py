from concurrent.futures import (
    ThreadPoolExecutor,
)
import threading
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
)

from web3._utils.async_caching import (
    async_lock,
)
from web3._utils.caching import (
    generate_cache_key,
)
from web3.middleware.cache import (
    SIMPLE_CACHE_RPC_WHITELIST,
    _should_cache_response,
)
from web3.types import (
    AsyncMiddleware,
    AsyncMiddlewareCoroutine,
    Middleware,
    RPCEndpoint,
    RPCResponse,
)
from web3.utils.caching import (
    SimpleCache,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )

_async_request_thread_pool = ThreadPoolExecutor()


async def async_construct_simple_cache_middleware(
    cache: SimpleCache = None,
    rpc_whitelist: Collection[RPCEndpoint] = SIMPLE_CACHE_RPC_WHITELIST,
    should_cache_fn: Callable[
        [RPCEndpoint, Any, RPCResponse], bool
    ] = _should_cache_response,
) -> AsyncMiddleware:
    """
    Constructs a middleware which caches responses based on the request
    ``method`` and ``params``

    :param cache: A ``SimpleCache`` class.
    :param rpc_whitelist: A set of RPC methods which may have their responses cached.
    :param should_cache_fn: A callable which accepts ``method`` ``params`` and
        ``response`` and returns a boolean as to whether the response should be
        cached.
    """

    async def async_simple_cache_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], _async_w3: "AsyncWeb3"
    ) -> AsyncMiddlewareCoroutine:
        lock = threading.Lock()

        # It's not imperative that we define ``_cache`` here rather than in
        # ``async_construct_simple_cache_middleware``. Due to the nature of async,
        # construction is awaited and doesn't happen at import. This means separate
        # instances would still get unique caches. However, to keep the code consistent
        # with the synchronous version, and provide less ambiguity, we define it
        # similarly to the synchronous version here.
        _cache = cache if cache else SimpleCache(256)

        async def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method in rpc_whitelist:
                cache_key = generate_cache_key(
                    f"{threading.get_ident()}:{(method, params)}"
                )
                cached_request = _cache.get_cache_entry(cache_key)
                if cached_request is not None:
                    return cached_request

                response = await make_request(method, params)
                if should_cache_fn(method, params, response):
                    async with async_lock(_async_request_thread_pool, lock):
                        _cache.cache(cache_key, response)
                return response
            else:
                return await make_request(method, params)

        return middleware

    return async_simple_cache_middleware


async def _async_simple_cache_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], async_w3: "AsyncWeb3"
) -> Middleware:
    middleware = await async_construct_simple_cache_middleware()
    return await middleware(make_request, async_w3)
