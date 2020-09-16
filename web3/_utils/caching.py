import collections
import hashlib
from typing import (
    Any,
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
        return generate_cache_key((
            (key, value[key])
            for key
            in sorted(value.keys())
        ))
    elif is_list_like(value) or isinstance(value, collections.abc.Generator):
        return generate_cache_key("".join((
            generate_cache_key(item)
            for item
            in value
        )))
    else:
        raise TypeError("Cannot generate cache key for value {0} of type {1}".format(
            value,
            type(value),
        ))
