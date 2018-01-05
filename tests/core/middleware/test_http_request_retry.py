import pytest
from unittest.mock import Mock

from web3.middleware import http_retry_request_middleware
from web3.middleware.http_retry_request import check_method
from requests.exceptions import ConnectionError
from web3.providers import HTTPProvider, IPCProvider


@pytest.fixture
def http_retry_request_setup():
    make_request, web3 = Mock(), Mock()
    setup = http_retry_request_middleware(make_request, web3)
    setup.web3 = web3
    setup.make_request = make_request
    setup.check_method = check_method
    return setup


def test_check_method_false(http_retry_request_setup):
    methods = ['eth_sendTransaction', 'personal_signAndSendTransaction', 'personal_sendTRansaction']

    for method in methods:
        assert check_method(method) == False


def test_check_method_true(http_retry_request_setup):
    method = 'eth_getBalance'
    assert check_method(method) == True


def test_check_send_transaction_called_once(http_retry_request_setup):
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
    }]

    http_retry_request_setup.make_request.side_effect = ConnectionError
    with pytest.raises(ConnectionError):
        http_retry_request_setup(method, params)
    assert http_retry_request_setup.make_request.call_count == 1


def test_valid_method_retried(http_retry_request_setup):
    method = 'eth_getBalance'
    params = []
    http_retry_request_setup.make_request.side_effect = ConnectionError

    with pytest.raises(ConnectionError):
        http_retry_request_setup(method, params)
    assert http_retry_request_setup.make_request.call_count == 5


def test_is_strictly_default_http_middleware():
    web3 = HTTPProvider()
    assert 'http_retry_request' in web3.middlewares

    web3 = IPCProvider()
    assert 'http_retry_request' not in web3.middlewares
