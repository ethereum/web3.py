import asyncio
import pytest

from aiohttp import (
    ClientSession,
)
from requests import (
    Session,
    adapters,
)
from requests.adapters import (
    DEFAULT_POOLSIZE,
    HTTPAdapter,
)

from web3._utils import (
    request,
)
from web3._utils.caching import (
    generate_cache_key,
)
from web3._utils.request import (
    SessionCache,
    get_async_session,
)


class MockedResponse:
    def __init__(self, text="", status_code=200):
        assert isinstance(text, str)
        assert isinstance(status_code, int)
        self.status_code = status_code
        self.ok = 200 <= status_code < 400
        self.text = text
        self.reason = None
        self.content = "content"

    def raise_for_status(self):
        pass


URI = "http://mynode.local:8545"


def check_adapters_mounted(session: Session):
    assert isinstance(session, Session)
    assert len(session.adapters) == 2


def test_make_post_request_no_args(mocker):
    mocker.patch("requests.Session.post", return_value=MockedResponse())
    request._session_cache.clear()

    # Submit a first request to create a session with default parameters
    assert len(request._session_cache) == 0
    response = request.make_post_request(URI, data=b"request")
    assert response == "content"
    assert len(request._session_cache) == 1
    cache_key = generate_cache_key(URI)
    session = request._session_cache.get_cache_entry(cache_key)
    session.post.assert_called_once_with(URI, data=b"request", timeout=10)

    # Ensure the adapter was created with default values
    check_adapters_mounted(session)
    adapter = session.get_adapter(URI)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == DEFAULT_POOLSIZE
    assert adapter._pool_maxsize == DEFAULT_POOLSIZE


def test_precached_session(mocker):
    mocker.patch("requests.Session.post", return_value=MockedResponse())

    # Update the cache with a handcrafted session
    adapter = adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
    session = Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    request.cache_session(URI, session)

    # Submit a second request with different arguments
    assert len(request._session_cache) == 1
    response = request.make_post_request(URI, data=b"request", timeout=60)
    assert response == "content"
    assert len(request._session_cache) == 1

    # Ensure the timeout was passed to the request
    session = request.get_session(URI)
    session.post.assert_called_once_with(URI, data=b"request", timeout=60)

    # Ensure the adapter parameters match those we specified
    check_adapters_mounted(session)
    adapter = session.get_adapter(URI)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == 100
    assert adapter._pool_maxsize == 100


def test_cache_session_class():
    cache = SessionCache(2)
    evicted_items = cache.cache("1", "Hello1")
    assert cache.get_cache_entry("1") == "Hello1"
    assert evicted_items is None

    evicted_items = cache.cache("2", "Hello2")
    assert cache.get_cache_entry("2") == "Hello2"
    assert evicted_items is None

    # Changing what is stored at a given cache key should not cause the
    # anything to be evicted
    evicted_items = cache.cache("1", "HelloChanged")
    assert cache.get_cache_entry("1") == "HelloChanged"
    assert evicted_items is None

    evicted_items = cache.cache("3", "Hello3")
    assert "2" in cache
    assert "3" in cache

    assert "1" not in cache
    assert "1" in evicted_items

    with pytest.raises(KeyError):
        # This should throw a KeyError since the cache size was 2 and 3 were inserted
        # the first inserted cached item was removed and returned in evicted items
        cache.get_cache_entry("1")


# -- async -- #


@pytest.mark.asyncio
async def test_async_precached_session():
    # Add a session
    session = ClientSession()
    await request.cache_async_session(URI, session)
    assert len(request._async_session_cache) == 1

    # Make sure the session isn't duplicated
    await request.cache_async_session(URI, session)
    assert len(request._async_session_cache) == 1

    # Make sure a request with a different URI adds another cached session
    await request.cache_async_session(f"{URI}/test", session)
    assert len(request._async_session_cache) == 2


@pytest.mark.asyncio
async def test_async_cache_does_not_close_session_before_a_call():
    unique_uris = [
        "https://www.test1.com",
        "https://www.test2.com",
        "https://www.test3.com",
        "https://www.test4.com",
        "https://www.test5.com",
    ]

    # save default values
    session_cache_default = request._async_session_cache
    timeout_default = request.DEFAULT_TIMEOUT

    # set cache size to 1 + set future session close thread time to 0.01s
    request._async_session_cache = SessionCache(1)
    _timeout_for_testing = 0.01
    request.DEFAULT_TIMEOUT = _timeout_for_testing

    async def cache_uri_and_return_evicted_session(uri):
        _session = await get_async_session(uri)

        # sort of simulate a call taking 0.01s to return a response
        await asyncio.sleep(0.01)

        assert not _session.closed
        return _session

    tasks = [cache_uri_and_return_evicted_session(uri) for uri in unique_uris]

    evicted_sessions = await asyncio.gather(*tasks)
    assert len(evicted_sessions) == len(unique_uris)
    assert all(isinstance(s, ClientSession) for s in evicted_sessions)

    # last session remains in cache
    cache_data = request._async_session_cache._data
    assert len(cache_data) == 1

    # -- teardown -- #

    # appropriately close the cached session before exiting test
    _key, cached_session = cache_data.popitem()
    await cached_session.close()

    # reset to default values
    request._async_session_cache = session_cache_default
    request.DEFAULT_TIMEOUT = timeout_default

    # assert all evicted sessions were closed
    await asyncio.sleep(_timeout_for_testing + 0.1)
    assert all(session.closed for session in evicted_sessions)
