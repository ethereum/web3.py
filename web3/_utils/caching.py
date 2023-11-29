import collections
import copy
import hashlib
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    List,
    Tuple,
)

from toolz import merge

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

if TYPE_CHECKING:
    from web3.providers import (  # noqa: F401
        BaseProvider,
    )
    from web3.types import (
        RPCEndpoint,
    )


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
        return generate_cache_key(((key, value[key]) for key in sorted(value.keys())))
    elif is_list_like(value) or isinstance(value, collections.abc.Generator):
        return generate_cache_key("".join((generate_cache_key(item) for item in value)))
    else:
        raise TypeError(
            f"Cannot generate cache key for value {value} of type {type(value)}"
        )


class RequestInformation:
    def __init__(
        self,
        method: "RPCEndpoint",
        params: Any,
        response_formatters: Tuple[Callable[..., Any], ...],
        subscription_id: str = None,
    ):
        self.method = method
        self.params = params
        self.response_formatters = response_formatters
        self.subscription_id = subscription_id
        self.middleware_response_processors: List[Callable[..., Any]] = []


def is_cacheable_request(provider: "BaseProvider", method: "RPCEndpoint") -> bool:
    if provider.cache_allowed_requests and method in provider.cacheable_requests:
        return True


# -- request caching decorators -- #


def handle_request_caching(func):
    def wrapper(*args, **kwargs):
        # args=(self, method, params) - where "self" should be BaseProvider instance
        provider, method, params = args

        if is_cacheable_request(provider, method):
            request_cache = provider._request_cache
            cache_key = generate_cache_key((method, params, kwargs))
            cache_result = request_cache.get_cache_entry(cache_key)
            if cache_result is not None:
                return cache_result
            else:
                response = func(*args, **kwargs)
                request_cache.cache(cache_key, response)
                return response
        else:
            return func(*args, **kwargs)

    return wrapper


def async_handle_request_caching(func):
    async def wrapper(*args, **kwargs):
        # args=(self, method, params) - where "self" should be the provider instance
        provider, method, params = args

        if is_cacheable_request(provider, method):
            request_cache = provider._request_cache
            cache_key = generate_cache_key((method, params))
            cache_result = request_cache.get_cache_entry(cache_key)
            if cache_result is not None:
                return cache_result
            else:
                response = await func(*args, **kwargs)
                request_cache.cache(cache_key, response)
                return response
        else:
            return await func(*args, **kwargs)

    return wrapper
