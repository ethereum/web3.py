from collections import (
    OrderedDict,
)
from typing import (
    Any,
    Dict,
    Optional,
    Tuple,
)


class SimpleCache:
    def __init__(self, size: int = 100):
        self._size = size
        self._data: OrderedDict[str, Any] = OrderedDict()

    def cache(self, key: str, value: Any) -> Tuple[Any, Dict[str, Any]]:
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

        # Return the cached value along with the evicted items at the same time. No
        # need to reach back into the cache to grab the value.
        return value, evicted_items

    def get_cache_entry(self, key: str) -> Optional[Any]:
        return self._data[key] if key in self._data else None

    def clear(self) -> None:
        self._data.clear()

    def items(self) -> Dict[str, Any]:
        return self._data

    def __contains__(self, key: str) -> bool:
        return key in self._data

    def __len__(self) -> int:
        return len(self._data)
