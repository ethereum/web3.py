from web3._utils import request
from requests import Session, Response
from requests.adapters import (
    DEFAULT_POOLSIZE,
    HTTPAdapter
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


uri = "http://mynode.local:8545"


def check_adapters_mounted(session: Session):
    assert isinstance(session, Session)
    print(session.adapters)
    assert len(session.adapters) == 2
    assert isinstance(session.adapters['http://'], HTTPAdapter)
    assert isinstance(session.adapters['https://'], HTTPAdapter)
    assert session.adapters['http://'] == session.adapters['https://']


def test_make_post_request_no_args(mocker):
    mocker.patch("requests.Session.post", return_value=MockedResponse())

    # Submit a first request to create a session with default parameters
    assert len(request._session_cache) == 0
    response = request.make_post_request(uri, b'request')
    assert response == "content"
    assert len(request._session_cache) == 1
    session = request._session_cache.values()[0]
    session.post.assert_called_once_with(uri, data=b'request', timeout=10)

    # Ensure the adapter was created with default values
    check_adapters_mounted(session)
    adapter = session.get_adapter(uri)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == DEFAULT_POOLSIZE
    assert adapter._pool_maxsize == DEFAULT_POOLSIZE


def test_make_post_request_with_pool_size(mocker):
    mocker.patch("requests.Session.post", return_value=MockedResponse())

    # Submit a second request with different arguments
    assert len(request._session_cache) == 1
    request_kwargs = {"timeout": 60, "pool_connections": 100, "pool_maxsize": 100}
    response = request.make_post_request(uri, b'request', **request_kwargs)
    assert response == "content"

    # Ensure a new session was cached with the alternate args
    assert len(request._session_cache) == 2
    session = request._get_session(**request_kwargs)

    # Ensure the timeout was passed to the request
    session.post.assert_called_once_with(uri, data=b'request', timeout=60)

    # Ensure the pool size was passed to the adapter
    check_adapters_mounted(session)
    adapter = session.get_adapter(uri)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == 100
    assert adapter._pool_maxsize == 100
