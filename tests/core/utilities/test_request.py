import asyncio
import threading
from threading import Thread
import pytest

from aiohttp import (
    ClientSession,
    client,
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
    request.cache_async_session(URI, session)
    assert len(request._async_session_cache) == 1

    # Make sure the session isn't duplicated
    request.cache_async_session(URI, session)
    assert len(request._async_session_cache) == 1

    # Make sure a request with a different URI adds another cached session
    request.cache_async_session(f"{URI}/test", session)
    assert len(request._async_session_cache) == 2

def test_async_session_cache_threads(mocker):
    thread1_exception = False
    thread2_exception = False
    def test_request_cache():
        for client_seesion in range(10000):
            try:
                request.cache_async_session(f"{client_seesion}", MockSession())
            except Exception as e:
                thread1_exception = True
                raise Exception("Test Failed")
        return True
    def test_request_cache2():
        for client_seesion in range(10000):
            try:
                request.cache_async_session(f"{client_seesion}", MockSession())
            except Exception as e:
                thread2_exception = True
                raise Exception("Test Failed")
        return True

    class MockSession:
        def close(test=None):
            pass
    thread1 = Thread(target=test_request_cache)
    thread2 = Thread(target=test_request_cache2)
    hey = thread1.start()
    hey2 = thread2.start()
    hey3 = thread1.join()
    hey4 = thread2.join()
    assert thread1_exception == False
    assert thread2_exception == False