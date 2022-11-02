import asyncio
from concurrent.futures import (
    ThreadPoolExecutor,
)
import logging
import os
import threading
from typing import (
    Any,
    Dict,
    List,
    Optional,
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

from web3._utils.async_caching import (
    async_lock,
)
from web3._utils.caching import (
    generate_cache_key,
)
from web3.utils.caching import (
    SimpleCache,
)

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10


def get_default_http_endpoint() -> URI:
    return URI(os.environ.get("WEB3_HTTP_PROVIDER_URI", "http://localhost:8545"))


_session_cache = SimpleCache()
_session_cache_lock = threading.Lock()


def cache_and_return_session(
    endpoint_uri: URI, session: requests.Session = None
) -> requests.Session:
    # cache key should have a unique thread identifier
    cache_key = generate_cache_key(f"{threading.get_ident()}:{endpoint_uri}")

    evicted_items = None
    with _session_cache_lock:
        if cache_key not in _session_cache:
            if session is None:
                session = requests.Session()

            evicted_items = _session_cache.cache(cache_key, session)
            logger.debug(f"Session cached: {endpoint_uri}, {session}")

        cached_session = _session_cache.get_cache_entry(cache_key)

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

    return cached_session


def get_response_from_get_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> requests.Response:
    kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
    session = cache_and_return_session(endpoint_uri)
    response = session.get(endpoint_uri, *args, **kwargs)
    return response


def json_make_get_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> Dict[str, Any]:
    response = get_response_from_get_request(endpoint_uri, *args, **kwargs)
    response.raise_for_status()
    return response.json()


def get_response_from_post_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> requests.Response:
    kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
    session = cache_and_return_session(endpoint_uri)
    response = session.post(endpoint_uri, *args, **kwargs)
    return response


def make_post_request(
    endpoint_uri: URI, data: Union[bytes, Dict[str, Any]], *args: Any, **kwargs: Any
) -> bytes:
    response = get_response_from_post_request(endpoint_uri, data=data, *args, **kwargs)
    response.raise_for_status()
    return response.content


def _close_evicted_sessions(evicted_sessions: List[requests.Session]) -> None:
    for evicted_session in evicted_sessions:
        evicted_session.close()
        logger.debug(f"Closed evicted session: {evicted_session}")


# --- async --- #


_async_session_cache = SimpleCache()
_async_session_cache_lock = threading.Lock()
_async_session_pool = ThreadPoolExecutor(max_workers=1)


async def cache_and_return_async_session(
    endpoint_uri: URI,
    session: Optional[ClientSession] = None,
) -> ClientSession:
    # cache key should have a unique thread identifier
    cache_key = generate_cache_key(f"{threading.get_ident()}:{endpoint_uri}")

    evicted_items = None
    async with async_lock(_async_session_pool, _async_session_cache_lock):
        if cache_key not in _async_session_cache:
            if session is None:
                session = ClientSession(raise_for_status=True)

            evicted_items = _async_session_cache.cache(cache_key, session)
            logger.debug(f"Async session cached: {endpoint_uri}, {session}")

        cached_session = _async_session_cache.get_cache_entry(cache_key)

    if evicted_items is not None:
        # At this point the evicted sessions are already popped out of the cache and
        # just stored in the `evicted_sessions` dict. So we can kick off a future task
        # to close them and it should be safe to pop out of the lock here.
        evicted_sessions = evicted_items.values()
        for evicted_session in evicted_sessions:
            logger.debug(
                "Async session cache full. Session evicted from cache: "
                f"{evicted_session}",
            )
        # Kick off a future task, in a separate thread, to close the evicted
        # sessions. In the case that the cache filled very quickly and some
        # sessions have been evicted before their original request has been made,
        # we set the timer to a bit more than the `DEFAULT_TIMEOUT` for a call. This
        # should make it so that any call from an evicted session can still be made
        # before the session is closed.
        threading.Timer(
            DEFAULT_TIMEOUT + 0.1,
            _async_close_evicted_sessions,
            args=[evicted_sessions],
        ).start()

    return cached_session


async def async_get_response_from_get_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> ClientResponse:
    kwargs.setdefault("timeout", ClientTimeout(DEFAULT_TIMEOUT))
    session = await cache_and_return_async_session(endpoint_uri)
    response = await session.get(endpoint_uri, *args, **kwargs)
    return response


async def async_json_make_get_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> Dict[str, Any]:
    response = await async_get_response_from_get_request(endpoint_uri, *args, **kwargs)
    response.raise_for_status()
    return await response.json()


async def async_get_response_from_post_request(
    endpoint_uri: URI, *args: Any, **kwargs: Any
) -> ClientResponse:
    kwargs.setdefault("timeout", ClientTimeout(DEFAULT_TIMEOUT))
    session = await cache_and_return_async_session(endpoint_uri)
    response = await session.post(endpoint_uri, *args, **kwargs)
    return response


async def async_make_post_request(
    endpoint_uri: URI, data: Union[bytes, Dict[str, Any]], *args: Any, **kwargs: Any
) -> bytes:
    response = await async_get_response_from_post_request(
        endpoint_uri, data=data, *args, **kwargs
    )
    response.raise_for_status()
    return await response.read()


async def async_get_json_from_client_response(
    response: ClientResponse,
) -> Dict[str, Any]:
    return await response.json()


def _async_close_evicted_sessions(evicted_sessions: List[ClientSession]) -> None:
    loop = asyncio.new_event_loop()

    for evicted_session in evicted_sessions:
        loop.run_until_complete(evicted_session.close())
        logger.debug(f"Closed evicted async session: {evicted_session}")

    if any(not evicted_session.closed for evicted_session in evicted_sessions):
        logger.warning(
            f"Some evicted async sessions were not properly closed: {evicted_sessions}"
        )
    loop.close()
