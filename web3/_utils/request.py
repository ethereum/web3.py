from typing import (
    Any,
)

from eth_typing import (
    URI,
)
import lru
import requests

from web3._utils.caching import (
    generate_cache_key,
)


def _remove_session(key: str, session: requests.Session) -> None:
    session.close()


_session_cache = lru.LRU(8, callback=_remove_session)


def _get_session(*args: Any, **kwargs: Any) -> requests.Session:
    cache_key = generate_cache_key((args, kwargs))
    if cache_key not in _session_cache:
        session = requests.Session()
        print(f"adapter kwargs are: {extract_adapter_kwargs(**kwargs)}")
        adapter = requests.adapters.HTTPAdapter(**extract_adapter_kwargs(**kwargs))
        session.mount('https://', adapter)
        session.mount('http://', adapter)

        _session_cache[cache_key] = session
    return _session_cache[cache_key]


def make_post_request(endpoint_uri: URI, data: bytes, *args: Any, **kwargs: Any) -> bytes:
    kwargs.setdefault('timeout', 10)
    # print(f"passed kwargs are: {kwargs}")
    session = _get_session(endpoint_uri, **kwargs)
    # https://github.com/python/mypy/issues/2582
    response = session.post(endpoint_uri, data=data, *args, **extract_request_kwargs(**kwargs))  # type: ignore
    response.raise_for_status()

    return response.content


def extract_adapter_kwargs(**kwargs: Any):
    adapter_args = ['pool_connections', 'pool_maxsize', 'max_retries', 'pool_block']
    return {key: value for key, value in kwargs.items() if key in adapter_args}


def extract_request_kwargs(**kwargs: Any):
    request_args = ['params', 'params', 'data', 'headers', 'cookies', 'files',
            'auth', 'timeout', 'allow_redirects', 'proxies',
            'hooks', 'stream', 'verify', 'cert', 'json']
    return {key: value for key, value in kwargs.items() if key in request_args}
