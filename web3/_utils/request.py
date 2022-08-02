import asyncio
from collections import (
    OrderedDict,
)
from concurrent.futures import (
    ThreadPoolExecutor,
)
import contextlib
import logging
import os
import threading
from typing import (
    Any,
    AsyncGenerator,
    Dict,
    List,
    Union,
)

from aiohttp import (
    ClientResponse,
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

logger = logging.Logger(__file__)
logger.addHandler(logging.StreamHandler())

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


_session_cache = SessionCache(size=20)
_session_cache_lock = threading.Lock()


def cache_session(endpoint_uri: URI, session: requests.Session) -> None:
    get_session(endpoint_uri, session)


def get_session(
    endpoint_uri: URI, session: requests.Session = None
) -> requests.Session:
    cache_key = generate_cache_key(endpoint_uri)
    with _session_cache_lock:
        evicted_items = None
        if session is not None:
            evicted_items = _session_cache.cache(cache_key, session)
        elif cache_key not in _session_cache:
            evicted_items = _session_cache.cache(cache_key, requests.Session())

        if evicted_items is not None:
            for _key, session in evicted_items.items():
                session.close()
        return _session_cache.get_cache_entry(cache_key)


def get_response_from_get_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> requests.Response:
    kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
    session = get_session(endpoint_uri)
    response = session.get(endpoint_uri, *args, **kwargs)
    return response


def get_response_from_post_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> requests.Response:
    kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
    session = get_session(endpoint_uri)
    response = session.post(endpoint_uri, *args, **kwargs)
    return response


def make_post_request(
    endpoint_uri: URI, data: Union[bytes, Dict[str, Any]], *args: Any, **kwargs: Any
) -> bytes:
    response = get_response_from_post_request(endpoint_uri, data=data, *args, **kwargs)
    response.raise_for_status()
    return response.content


# --- async --- #


_async_session_cache = SessionCache(size=20)
_async_session_cache_lock = threading.Lock()
_pool = ThreadPoolExecutor(max_workers=1)


async def cache_async_session(endpoint_uri: URI, session: ClientSession) -> None:
    await get_async_session(endpoint_uri, session)


@contextlib.asynccontextmanager
async def async_lock(lock: threading.Lock) -> AsyncGenerator[None, None]:
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(_pool, lock.acquire)
    try:
        yield
    finally:
        lock.release()


async def get_async_session(
    endpoint_uri: URI, session: ClientSession = None
) -> ClientSession:
    cache_key = generate_cache_key(endpoint_uri)
    async with async_lock(_async_session_cache_lock):
        evicted_items = None
        if session is not None:
            evicted_items = _async_session_cache.cache(cache_key, session)
        elif cache_key not in _async_session_cache:
            evicted_items = _async_session_cache.cache(
                cache_key, ClientSession(raise_for_status=True)
            )

        session = _async_session_cache.get_cache_entry(cache_key)
        logger.debug(f"Session cached: {endpoint_uri}, {session}")

    if evicted_items is not None:
        # At this point the evicted sessions (if any) are already popped out of the
        # cache and just stored in the `evicted_sessions` dict. So we can kick off a
        # future task to close them and it should be safe to pop out of the lock here.
        evicted_sessions = [session for _key, session in evicted_items.items()]
        for session in evicted_sessions:
            logger.debug(
                f"Session cache full. Session evicted from cache: {session}",
            )
        # Kick off a future task, in a separate thread, to close the evicted
        # sessions. In the case that the cache filled very quickly and some
        # sessions have been evicted before their original request has been made,
        # we set the timer to a bit more than the `DEFAULT_TIMEOUT` for a call. This
        # should guarantee that any call from an evicted session can still be made
        # before the session is closed.
        threading.Timer(
            DEFAULT_TIMEOUT + 0.1, _close_evicted_sessions, args=[evicted_sessions]
        ).start()

    return session


def _close_evicted_sessions(evicted_sessions: List[ClientSession]) -> None:
    loop = asyncio.new_event_loop()
    for i, evicted_session in enumerate(evicted_sessions):
        loop.run_until_complete(evicted_session.close())
        logger.debug(f"Closed evicted session: {evicted_session}")
        evicted_sessions.pop(i)
    assert len(evicted_sessions) == 0
    loop.close()


async def async_get_response_from_get_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> ClientResponse:
    kwargs.setdefault("timeout", ClientTimeout(DEFAULT_TIMEOUT))
    session = await get_async_session(endpoint_uri)
    response = await session.get(endpoint_uri, *args, **kwargs)
    return response


async def async_get_response_from_post_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> ClientResponse:
    kwargs.setdefault("timeout", ClientTimeout(DEFAULT_TIMEOUT))
    session = await get_async_session(endpoint_uri)
    response = await session.post(endpoint_uri, *args, **kwargs)
    return response


async def async_make_post_request(
    endpoint_uri: URI, data: Union[bytes, Dict[str, Any]], *args: Any, **kwargs: Any
) -> bytes:
    response = await async_get_response_from_post_request(
        endpoint_uri, data=data, *args, **kwargs
    )
    return await response.read()


async def async_get_json_from_client_response(
    response: ClientResponse,
) -> Dict[str, Any]:
    return await response.json()
