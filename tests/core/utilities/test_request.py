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
from web3._utils.request import (
    SessionCache,
)


class MockedResponse:
    def __init__(self, text="", status_code=200):
        assert (isinstance(text, str))
        assert (isinstance(status_code, int))
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
    response = request.make_post_request(URI, b'request')
    assert response == "content"
    assert len(request._session_cache) == 1
    session = request._session_cache.values()[0]
    session.post.assert_called_once_with(URI, data=b'request', timeout=10)

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
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    request.cache_session(URI, session)

    # Submit a second request with different arguments
    assert len(request._session_cache) == 1
    response = request.make_post_request(URI, b'request', timeout=60)
    assert response == "content"
    assert len(request._session_cache) == 1

    # Ensure the timeout was passed to the request
    session = request._get_session(URI)
    session.post.assert_called_once_with(URI, data=b'request', timeout=60)

    # Ensure the adapter parameters match those we specified
    check_adapters_mounted(session)
    adapter = session.get_adapter(URI)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == 100
    assert adapter._pool_maxsize == 100


@pytest.mark.asyncio
async def test_async_precached_session(mocker):
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

    with pytest.raises(KeyError):
        # This should throw a KeyError since the cache size was 2 and 3 were inserted
        # the first inserted cached item was removed and returned in evicted items
        cache.get_cache_entry("1")
