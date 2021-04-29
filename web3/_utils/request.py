import os
from typing import (
    Any,
)

from aiohttp import (
    ClientSession,
    ClientTimeout,
)
from eth_typing import (
    URI,
)
import lru
import requests

from web3._utils.caching import (
    generate_cache_key,
)


def get_default_http_endpoint() -> URI:
    return URI(os.environ.get('WEB3_HTTP_PROVIDER_URI', 'http://localhost:8545'))


def cache_session(endpoint_uri: URI, session: requests.Session) -> None:
    cache_key = generate_cache_key(endpoint_uri)
    _session_cache[cache_key] = session


def _remove_session(key: str, session: requests.Session) -> None:
    session.close()


_session_cache = lru.LRU(8, callback=_remove_session)


def _get_session(endpoint_uri: URI) -> requests.Session:
    cache_key = generate_cache_key(endpoint_uri)
    if cache_key not in _session_cache:
        _session_cache[cache_key] = requests.Session()
    return _session_cache[cache_key]


def make_post_request(endpoint_uri: URI, data: bytes, *args: Any, **kwargs: Any) -> bytes:
    kwargs.setdefault('timeout', 10)
    session = _get_session(endpoint_uri)
    # https://github.com/python/mypy/issues/2582
    response = session.post(endpoint_uri, data=data, *args, **kwargs)  # type: ignore
    response.raise_for_status()

    return response.content


async def async_make_post_request(
    endpoint_uri: URI, data: bytes, *args: Any, **kwargs: Any
) -> bytes:
    kwargs.setdefault('timeout', ClientTimeout(10))
    async with ClientSession(raise_for_status=True) as session:
        async with session.post(endpoint_uri,
                                data=data,
                                *args,
                                **kwargs) as response:
            return await response.read()
