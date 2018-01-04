import pytest
from unittest.mock import Mock

from web3.middleware import http_retry_request_middleware


@pytest.fixture
def http_retry_request_setup():
    make_request, web3, check_method = Mock(), Mock(), Mock()
    setup = http_retry_request_middleware(make_request, web3)
    setup.web3 = web3
    setup.make_request = make_request
    setup.check_method = check_method
    return setup


def test_check_method_false(http_retry_request_setup):
    method = 'eth_sendTransaction'
    params = None

    http_retry_request_setup(method, params)
    http_retry_request_setup.check_method.assert_called_once_with(method)
    #assert http_retry_request_setup.check_method == False


def test_check_send_transaction_called_once(http_retry_request_setup):
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
    }]

    http_retry_request_setup(method, params)
    http_retry_request_setup.make_request.assert_called_once_with(method, params)
