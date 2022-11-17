import asyncio
from concurrent.futures import (
    ThreadPoolExecutor,
)
import json
import pytest
import threading
import time

from aiohttp import (
    ClientSession,
    ClientTimeout,
)
from eth_typing import (
    URI,
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
    async_cache_and_return_session,
    cache_and_return_session,
)
from web3.utils.caching import (
    SimpleCache,
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

    @staticmethod
    def json():
        return json.dumps({"data": "content"})

    def raise_for_status(self):
        pass


TEST_URI = URI("http://mynode.local:8545")
UNIQUE_URIS = [
    "https://www.test1.com",
    "https://www.test2.com",
    "https://www.test3.com",
    "https://www.test4.com",
    "https://www.test5.com",
]


def check_adapters_mounted(session: Session):
    assert isinstance(session, Session)
    assert len(session.adapters) == 2


def _simulate_call(uri):
    _session = cache_and_return_session(uri)

    # simulate a call taking 0.01s to return a response
    time.sleep(0.01)
    return _session


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # clear session caches before and after each test
    request._session_cache.clear()
    request._async_session_cache.clear()
    yield
    request._session_cache.clear()
    request._async_session_cache.clear()


def test_json_make_get_request(mocker):
    mocker.patch("requests.Session.get", return_value=MockedResponse())

    # Submit a first request to create a session with default parameters
    assert len(request._session_cache) == 0
    response = request.json_make_get_request(TEST_URI)
    assert response == json.dumps({"data": "content"})
    assert len(request._session_cache) == 1
    cache_key = generate_cache_key(f"{threading.get_ident()}:{TEST_URI}")
    session = request._session_cache.get_cache_entry(cache_key)
    session.get.assert_called_once_with(TEST_URI, timeout=10)

    # Ensure the adapter was created with default values
    check_adapters_mounted(session)
    adapter = session.get_adapter(TEST_URI)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == DEFAULT_POOLSIZE
    assert adapter._pool_maxsize == DEFAULT_POOLSIZE


def test_make_post_request_no_args(mocker):
    mocker.patch("requests.Session.post", return_value=MockedResponse())

    # Submit a first request to create a session with default parameters
    assert len(request._session_cache) == 0
    response = request.make_post_request(TEST_URI, data=b"request")
    assert response == "content"
    assert len(request._session_cache) == 1
    cache_key = generate_cache_key(f"{threading.get_ident()}:{TEST_URI}")
    session = request._session_cache.get_cache_entry(cache_key)
    session.post.assert_called_once_with(TEST_URI, data=b"request", timeout=10)

    # Ensure the adapter was created with default values
    check_adapters_mounted(session)
    adapter = session.get_adapter(TEST_URI)
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
    request.cache_and_return_session(TEST_URI, session)

    # Submit a second request with different arguments
    assert len(request._session_cache) == 1
    response = request.make_post_request(TEST_URI, data=b"request", timeout=60)
    assert response == "content"
    assert len(request._session_cache) == 1

    # Ensure the timeout was passed to the request
    session = request.cache_and_return_session(TEST_URI)
    session.post.assert_called_once_with(TEST_URI, data=b"request", timeout=60)

    # Ensure the adapter parameters match those we specified
    check_adapters_mounted(session)
    adapter = session.get_adapter(TEST_URI)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == 100
    assert adapter._pool_maxsize == 100


def test_cache_session_class():
    cache = SimpleCache(2)
    _, evicted_items = cache.cache("1", "Hello1")
    assert cache.get_cache_entry("1") == "Hello1"
    assert evicted_items is None

    _, evicted_items = cache.cache("2", "Hello2")
    assert cache.get_cache_entry("2") == "Hello2"
    assert evicted_items is None

    # Changing what is stored at a given cache key should not cause the
    # anything to be evicted
    _, evicted_items = cache.cache("1", "HelloChanged")
    assert cache.get_cache_entry("1") == "HelloChanged"
    assert evicted_items is None

    _, evicted_items = cache.cache("3", "Hello3")
    assert "2" in cache
    assert "3" in cache

    assert "1" not in cache
    assert "1" in evicted_items

    # Cache size is `3`. We should have "2" and "3" in the cache and "1" should have
    # been evicted.
    assert cache.get_cache_entry("1") is None


def test_cache_does_not_close_session_before_a_call_when_multithreading():
    # save default values
    session_cache_default = request._session_cache
    timeout_default = request.DEFAULT_TIMEOUT

    # set cache size to 1 + set future session close thread time to 0.01s
    request._session_cache = SimpleCache(1)
    _timeout_for_testing = 0.01
    request.DEFAULT_TIMEOUT = _timeout_for_testing

    with ThreadPoolExecutor(max_workers=len(UNIQUE_URIS)) as exc:
        all_sessions = [exc.submit(_simulate_call, uri) for uri in UNIQUE_URIS]

    # assert last session remains in cache, all others evicted
    cache_data = request._session_cache._data
    assert len(cache_data) == 1
    _key, cached_session = cache_data.popitem()
    assert cached_session == all_sessions[-1].result()  # result of the `Future`

    # -- teardown -- #

    # close the cached session before exiting test
    cached_session.close()

    # reset default values
    request._session_cache = session_cache_default
    request.DEFAULT_TIMEOUT = timeout_default


def test_unique_cache_keys_created_per_thread_with_same_uri():
    # somewhat inspired by issue #2680

    with ThreadPoolExecutor(max_workers=2) as exc:
        test_sessions = [exc.submit(_simulate_call, TEST_URI) for _ in range(2)]

    # assert unique keys are generated per thread for the same uri
    assert len(request._session_cache._data) == 2

    # -- teardown -- #

    # appropriately close the test sessions
    [session.result().close() for session in test_sessions]


# -- async -- #


class AsyncMockedResponse:
    status_code = 200

    def __await__(self):
        yield
        return self

    @staticmethod
    async def read():
        return "content"

    @staticmethod
    async def json():
        return json.dumps({"data": "content"})

    @staticmethod
    def raise_for_status() -> None:
        pass


@pytest.mark.asyncio
async def test_async_json_make_get_request(mocker):
    mocker.patch("aiohttp.ClientSession.get", return_value=AsyncMockedResponse())

    # Submit a first request to create a session with default parameters
    assert len(request._async_session_cache) == 0
    response = await request.async_json_make_get_request(TEST_URI)
    assert response == json.dumps({"data": "content"})
    assert len(request._async_session_cache) == 1
    cache_key = generate_cache_key(f"{threading.get_ident()}:{TEST_URI}")
    session = request._async_session_cache.get_cache_entry(cache_key)
    assert isinstance(session, ClientSession)
    session.get.assert_called_once_with(
        TEST_URI,
        timeout=ClientTimeout(
            total=10, connect=None, sock_read=None, sock_connect=None
        ),
    )


@pytest.mark.asyncio
async def test_async_make_post_request(mocker):
    mocker.patch("aiohttp.ClientSession.post", return_value=AsyncMockedResponse())

    # Submit a first request to create a session with default parameters
    assert len(request._async_session_cache) == 0
    response = await request.async_make_post_request(TEST_URI, data=b"request")
    assert response == "content"
    assert len(request._async_session_cache) == 1
    cache_key = generate_cache_key(f"{threading.get_ident()}:{TEST_URI}")
    session = request._async_session_cache.get_cache_entry(cache_key)
    assert isinstance(session, ClientSession)
    session.post.assert_called_once_with(
        TEST_URI,
        data=b"request",
        timeout=ClientTimeout(
            total=10, connect=None, sock_read=None, sock_connect=None
        ),
    )


@pytest.mark.asyncio
async def test_async_precached_session():
    # Add a session
    session = ClientSession()
    await request.async_cache_and_return_session(TEST_URI, session)
    assert len(request._async_session_cache) == 1

    # Make sure the session isn't duplicated
    await request.async_cache_and_return_session(TEST_URI, session)
    assert len(request._async_session_cache) == 1

    # Make sure a request with a different URI adds another cached session
    await request.async_cache_and_return_session(URI(f"{TEST_URI}/test"), session)
    assert len(request._async_session_cache) == 2

    # -- teardown -- #

    # appropriately close the cached sessions
    [await session.close() for session in request._async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cache_does_not_close_session_before_a_call_when_multithreading():
    # save default values
    session_cache_default = request._async_session_cache
    timeout_default = request.DEFAULT_TIMEOUT

    # set cache size to 1 + set future session close thread time to 0.01s
    request._async_session_cache = SimpleCache(1)
    _timeout_for_testing = 0.01
    request.DEFAULT_TIMEOUT = _timeout_for_testing

    async def cache_uri_and_return_session(uri):
        _session = await async_cache_and_return_session(uri)

        # simulate a call taking 0.01s to return a response
        await asyncio.sleep(0.01)

        assert not _session.closed
        return _session

    tasks = [cache_uri_and_return_session(uri) for uri in UNIQUE_URIS]

    all_sessions = await asyncio.gather(*tasks)
    assert len(all_sessions) == len(UNIQUE_URIS)
    assert all(isinstance(s, ClientSession) for s in all_sessions)

    # last session remains in cache, all others evicted
    cache_data = request._async_session_cache._data
    assert len(cache_data) == 1
    _key, cached_session = cache_data.popitem()
    assert cached_session == all_sessions[-1]

    # assert all evicted sessions were closed
    await asyncio.sleep(_timeout_for_testing + 0.1)
    assert all(session.closed for session in all_sessions[:-1])

    # -- teardown -- #

    # appropriately close the cached session
    await cached_session.close()

    # reset default values
    request._async_session_cache = session_cache_default
    request.DEFAULT_TIMEOUT = timeout_default


@pytest.mark.asyncio
async def test_async_unique_cache_keys_created_per_thread_with_same_uri():
    # inspired by issue #2680
    # Note: unique event loops for each thread are important here

    # capture the test sessions to appropriately close them in teardown
    test_sessions = []

    def target_function(endpoint_uri):
        event_loop = asyncio.new_event_loop()
        unique_session = event_loop.run_until_complete(
            async_cache_and_return_session(endpoint_uri)
        )
        test_sessions.append(unique_session)

    threads = []

    for _ in range(2):
        thread = threading.Thread(
            target=target_function,
            args=(TEST_URI,),
            daemon=True,
        )
        thread.start()
        threads.append(thread)

    [thread.join() for thread in threads]

    # assert unique keys are generated per thread, w/ unique event loops,
    # for the same uri
    assert len(request._async_session_cache._data) == 2

    # -- teardown -- #

    # appropriately close the test sessions
    [await session.close() for session in test_sessions]


@pytest.mark.asyncio
async def test_async_use_new_session_if_loop_closed_for_cached_session():
    # create new loop, cache a session wihin the loop, close the loop
    loop1 = asyncio.new_event_loop()

    session1 = ClientSession(raise_for_status=True)
    session1._loop = loop1

    await async_cache_and_return_session(TEST_URI, session=session1)

    # assert session1 was cached
    cache_key = generate_cache_key(f"{threading.get_ident()}:{TEST_URI}")

    assert len(request._async_session_cache) == 1
    cached_session = request._async_session_cache.get_cache_entry(cache_key)
    assert cached_session == session1

    # close loop that was used with session1
    loop1.close()

    # assert we create a new session when trying to retrieve the session at the
    # cache key for TEST_URI
    session2 = await async_cache_and_return_session(TEST_URI)
    assert not session2._loop.is_closed()
    assert session2 != session1

    # assert we appropriately closed session1, evicted it from the cache, and cached
    # the new session2 at the cache key
    assert session1.closed
    assert len(request._async_session_cache) == 1
    cached_session = request._async_session_cache.get_cache_entry(cache_key)
    assert cached_session == session2

    # -- teardown -- #

    # appropriately close the new session
    await session2.close()


@pytest.mark.asyncio
async def test_async_use_new_session_if_session_closed_for_cached_session():
    # create a session, close it, and cache it at the cache key for TEST_URI
    session1 = ClientSession(raise_for_status=True)
    await session1.close()
    await async_cache_and_return_session(TEST_URI, session=session1)

    # assert session1 was cached
    cache_key = generate_cache_key(f"{threading.get_ident()}:{TEST_URI}")

    assert len(request._async_session_cache) == 1
    cached_session = request._async_session_cache.get_cache_entry(cache_key)
    assert cached_session == session1

    # assert we create a new session when trying to retrieve closed session from cache
    session2 = await async_cache_and_return_session(TEST_URI)
    assert not session2.closed
    assert session2 != session1

    # assert we evicted session1 from the cache, and cached the new session2
    # at the cache key
    assert len(request._async_session_cache) == 1
    cached_session = request._async_session_cache.get_cache_entry(cache_key)
    assert cached_session == session2

    # -- teardown -- #

    # appropriately close the new session
    await session2.close()
