import pytest
from unittest.mock import Mock

from web3.middleware import http_retry_request_middleware
from web3.middleware.http_retry_request import check_method


@pytest.fixture
def http_retry_request_setup():
    make_request, web3 = Mock(), Mock()
    setup = http_retry_request_middleware(make_request, web3)
    setup.web3 = web3
    setup.make_request = make_request
    setup.check_method = check_method
    return setup


def test_check_method_false(http_retry_request_setup):
    methods = ['eth_sendTransaction', 'eth_sendRawTransaction',
                'personal_signAndSendTransaction', 'personal_sendTRansaction']

    for method in methods:
        assert check_method(method) == False


def test_check_send_transaction_called_once(http_retry_request_setup):
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
    }]

    http_retry_request_setup(method, params)
    http_retry_request_setup.make_request.assert_called_once_with(method, params)
