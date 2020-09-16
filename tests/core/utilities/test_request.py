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
