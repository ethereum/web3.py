import collections
import hashlib
import threading
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Dict,
    List,
    Set,
    Tuple,
    TypeVar,
    Union,
    cast,
)

from eth_utils import (
    is_boolean,
    is_bytes,
    is_dict,
    is_list_like,
    is_null,
    is_number,
    is_text,
    to_bytes,
)

from web3.exceptions import (
    Web3TypeError,
)

if TYPE_CHECKING:
    from web3.providers import (  # noqa: F401
        AsyncBaseProvider,
        BaseProvider,
    )
    from web3.types import (  # noqa: F401
        AsyncMakeRequestFn,
        MakeRequestFn,
        RPCEndpoint,
        RPCResponse,
    )


SYNC_PROVIDER_TYPE = TypeVar("SYNC_PROVIDER_TYPE", bound="BaseProvider")
ASYNC_PROVIDER_TYPE = TypeVar("ASYNC_PROVIDER_TYPE", bound="AsyncBaseProvider")


def generate_cache_key(value: Any) -> str:
    """
    Generates a cache key for the *args and **kwargs
    """
    if is_bytes(value):
        return hashlib.md5(value).hexdigest()
    elif is_text(value):
        return generate_cache_key(to_bytes(text=value))
    elif is_boolean(value) or is_null(value) or is_number(value):
        return generate_cache_key(repr(value))
    elif is_dict(value):
        return generate_cache_key((key, value[key]) for key in sorted(value.keys()))
    elif is_list_like(value) or isinstance(value, collections.abc.Generator):
        return generate_cache_key("".join(generate_cache_key(item) for item in value))
    else:
        raise Web3TypeError(
            f"Cannot generate cache key for value {value} of type {type(value)}"
        )


class RequestInformation:
    def __init__(
        self,
        method: "RPCEndpoint",
        params: Any,
        response_formatters: Tuple[
            Union[Dict[str, Callable[..., Any]], Callable[..., Any]],
            Callable[..., Any],
            Callable[..., Any],
        ],
        subscription_id: str = None,
    ):
        self.method = method
        self.params = params
        self.response_formatters = response_formatters
        self.subscription_id = subscription_id
        self.middleware_response_processors: List[Callable[..., Any]] = []


def is_cacheable_request(
    provider: Union[ASYNC_PROVIDER_TYPE, SYNC_PROVIDER_TYPE], method: "RPCEndpoint"
) -> bool:
    if provider.cache_allowed_requests and method in provider.cacheable_requests:
        return True
    return False


# -- request caching -- #


CACHEABLE_REQUESTS = cast(
    Set["RPCEndpoint"],
    (
        "eth_chainId",
        "eth_getBlockByHash",
        "eth_getBlockTransactionCountByHash",
        "eth_getRawTransactionByHash",
        "eth_getTransactionByBlockHashAndIndex",
        "eth_getTransactionByHash",
        "eth_getUncleByBlockHashAndIndex",
        "eth_getUncleCountByBlockHash",
        "net_version",
        "web3_clientVersion",
    ),
)


def _should_cache_response(response: "RPCResponse") -> bool:
    return (
        "error" not in response
        and "result" in response
        and not is_null(response["result"])
    )


def handle_request_caching(
    func: Callable[[SYNC_PROVIDER_TYPE, "RPCEndpoint", Any], "RPCResponse"]
) -> Callable[..., "RPCResponse"]:
    def wrapper(
        provider: SYNC_PROVIDER_TYPE, method: "RPCEndpoint", params: Any
    ) -> "RPCResponse":
        if is_cacheable_request(provider, method):
            request_cache = provider._request_cache
            cache_key = generate_cache_key(
                f"{threading.get_ident()}:{(method, params)}"
            )
            cache_result = request_cache.get_cache_entry(cache_key)
            if cache_result is not None:
                return cache_result
            else:
                response = func(provider, method, params)
                if _should_cache_response(response):
                    with provider._request_cache_lock:
                        request_cache.cache(cache_key, response)
                return response
        else:
            return func(provider, method, params)

    # save a reference to the decorator on the wrapped function
    wrapper._decorator = handle_request_caching  # type: ignore
    return wrapper


# -- async -- #


def async_handle_request_caching(
    func: Callable[
        [ASYNC_PROVIDER_TYPE, "RPCEndpoint", Any], Coroutine[Any, Any, "RPCResponse"]
    ],
) -> Callable[..., Coroutine[Any, Any, "RPCResponse"]]:
    async def wrapper(
        provider: ASYNC_PROVIDER_TYPE, method: "RPCEndpoint", params: Any
    ) -> "RPCResponse":
        if is_cacheable_request(provider, method):
            request_cache = provider._request_cache
            cache_key = generate_cache_key(
                f"{threading.get_ident()}:{(method, params)}"
            )
            cache_result = request_cache.get_cache_entry(cache_key)
            if cache_result is not None:
                return cache_result
            else:
                response = await func(provider, method, params)
                if _should_cache_response(response):
                    async with provider._request_cache_lock:
                        request_cache.cache(cache_key, response)
                return response
        else:
            return await func(provider, method, params)

    # save a reference to the decorator on the wrapped function
    wrapper._decorator = async_handle_request_caching  # type: ignore
    return wrapper
