import collections
import hashlib
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    List,
    Tuple,
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

if TYPE_CHECKING:
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
    ):
        self.method = method
        self.params = params
        self.response_formatters = response_formatters
        self.middleware_response_processors: List[Callable[..., Any]] = []
