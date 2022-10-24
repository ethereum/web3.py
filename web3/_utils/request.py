from collections import (
    OrderedDict,
)
import logging
import os
import threading
from typing import (
    Any,
    Dict,
    List,
)

from aiohttp import (
    ClientSession,
    ClientTimeout,
)
from eth_typing import (
    URI,
)
import requests

from web3._utils.caching import (
    generate_cache_key,
)

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10


class SessionCache:
    def __init__(self, size: int):
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

    def __contains__(self, item: str) -> bool:
        return item in self._data

    def __len__(self) -> int:
        return len(self._data)


def get_default_http_endpoint() -> URI:
    return URI(os.environ.get("WEB3_HTTP_PROVIDER_URI", "http://localhost:8545"))


_session_cache = SessionCache(size=100)
_session_cache_lock = threading.Lock()


def cache_session(endpoint_uri: URI, session: requests.Session) -> None:
    # cache key should have a unique thread identifier
    cache_key = generate_cache_key(f"{threading.get_ident()}:{endpoint_uri}")

    evicted_items = None
    with _session_cache_lock:
        if cache_key not in _session_cache:
            if session is None:
                session = requests.Session()

            evicted_items = _session_cache.cache(cache_key, session)
            logger.debug(f"Session cached: {endpoint_uri}, {session}")

    if evicted_items is not None:
        evicted_sessions = evicted_items.values()
        for evicted_session in evicted_sessions:
            logger.debug(
                f"Session cache full. Session evicted from cache: {evicted_session}",
            )
        threading.Timer(
            DEFAULT_TIMEOUT + 0.1,
            _close_evicted_sessions,
            args=[evicted_sessions],
        ).start()


def _get_session(endpoint_uri: URI) -> requests.Session:
    # cache key should have a unique thread identifier
    cache_key = generate_cache_key(f"{threading.get_ident()}:{endpoint_uri}")
    if cache_key not in _session_cache:
        cache_session(endpoint_uri, requests.Session())
    return _session_cache.get_cache_entry(cache_key)


def make_post_request(
    endpoint_uri: URI, data: bytes, *args: Any, **kwargs: Any
) -> bytes:
    kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
    session = _get_session(endpoint_uri)
    # https://github.com/python/mypy/issues/2582
    response = session.post(endpoint_uri, data=data, *args, **kwargs)  # type: ignore
    response.raise_for_status()

    return response.content


def _close_evicted_sessions(evicted_sessions: List[requests.Session]) -> None:
    for evicted_session in evicted_sessions:
        evicted_session.close()
        logger.debug(f"Closed evicted session: {evicted_session}")


# --- async --- #

_async_session_cache = SessionCache(size=100)
_async_session_cache_lock = threading.Lock()


async def cache_async_session(endpoint_uri: URI, session: ClientSession) -> None:
    # cache key should have a unique thread identifier
    cache_key = generate_cache_key(f"{threading.get_ident()}:{endpoint_uri}")

    with _async_session_cache_lock:
        evicted_items = _async_session_cache.cache(cache_key, session)
        if evicted_items is not None:
            for key, session in evicted_items.items():
                await session.close()


async def _get_async_session(endpoint_uri: URI) -> ClientSession:
    # cache key should have a unique thread identifier
    cache_key = generate_cache_key(f"{threading.get_ident()}:{endpoint_uri}")

    if cache_key not in _async_session_cache:
        await cache_async_session(endpoint_uri, ClientSession(raise_for_status=True))
    return _async_session_cache.get_cache_entry(cache_key)


async def async_make_post_request(
    endpoint_uri: URI, data: bytes, *args: Any, **kwargs: Any
) -> bytes:
    kwargs.setdefault("timeout", ClientTimeout(DEFAULT_TIMEOUT))
    # https://github.com/ethereum/go-ethereum/issues/17069
    session = await _get_async_session(endpoint_uri)
    async with session.post(endpoint_uri, data=data, *args, **kwargs) as response:
        return await response.read()
