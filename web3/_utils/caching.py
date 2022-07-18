import collections
from collections import (
    OrderedDict,
)
import hashlib
from typing import (
    Any,
    Dict,
    Union,
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
        return generate_cache_key(((key, value[key]) for key in sorted(value.keys())))
    elif is_list_like(value) or isinstance(value, collections.abc.Generator):
        return generate_cache_key("".join((generate_cache_key(item) for item in value)))
    else:
        raise TypeError(
            f"Cannot generate cache key for value {value} of type {type(value)}"
        )


class SimpleCache:
    def __init__(self, size: int = 100):
        self._size = size
        self._data: OrderedDict[str, Any] = OrderedDict()

    def cache(self, key: str, value: Any) -> Dict[str, Any]:
        evicted_items = None
        # If the key is already in the OrderedDict just update it
        # and don't evict any values. Ideally, we could still check to see
        # if there are too many items in the OrderedDict but that may rearrange
        # the order it should be unlikely that the size could grow over the limit
        if key not in self._data:
            while len(self._data) >= self._size:
                if evicted_items is None:
                    evicted_items = {}
                k, v = self._data.popitem(last=False)
                evicted_items[k] = v
        self._data[key] = value
        return evicted_items

    def get_cache_entry(self, key: str) -> Any:
        return self._data[key]

    def clear(self) -> None:
        self._data.clear()

    def items(self) -> Dict[str, Any]:
        return self._data

    def __contains__(self, item: str) -> bool:
        return item in self._data

    def __len__(self) -> int:
        return len(self._data)


def type_aware_cache_entry(
    cache: Union[Dict[str, Any], SimpleCache], cache_key: str, value: Any
) -> None:
    """
    Commit an entry to a dictionary-based cache or to a `SimpleCache` class.
    """
    if isinstance(cache, SimpleCache):
        cache.cache(cache_key, value)
    else:
        cache[cache_key] = value


def type_aware_get_cache_entry(
    cache: Union[Dict[str, Any], SimpleCache],
    cache_key: str,
) -> Any:
    """
    Get a cache entry, with `cache_key`, from a dictionary-based cache or a
    `SimpleCache` class.
    """
    if isinstance(cache, SimpleCache) and cache_key in cache.items():
        return cache.get_cache_entry(cache_key)
    elif isinstance(cache, dict) and cache_key in cache:
        return cache[cache_key]
    return None
