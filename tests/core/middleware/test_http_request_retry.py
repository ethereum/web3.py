import asyncio
import pytest
from unittest.mock import (
    Mock,
    patch,
)

from aiohttp.client_exceptions import (
    ClientConnectorError,
    ClientResponseError,
    ServerTimeoutError,
    TooManyRedirects,
)

import web3
from web3.middleware.exception_retry_request import (
    check_if_retry_on_failure,
    exception_retry_middleware,
)
from web3.providers import (
    HTTPProvider,
    IPCProvider,
)


def async_return(result):
    f = asyncio.Future()
    f.set_result(result)
    return f


@pytest.fixture
def exception_retry_request_setup():
    web3 = Mock()
    provider = HTTPProvider()
    errors = (ClientConnectorError, ClientResponseError, ServerTimeoutError, TooManyRedirects)
    setup = exception_retry_middleware(provider.make_request, web3, errors, 5)
    setup.web3 = web3
    return setup


def test_check_if_retry_on_failure_false():
    methods = ['eth_sendTransaction', 'personal_signAndSendTransaction', 'personal_sendTRansaction']

    for method in methods:
        assert not check_if_retry_on_failure(method)


def test_check_if_retry_on_failure_true():
    method = 'eth_getBalance'
    assert check_if_retry_on_failure(method)


@pytest.mark.asyncio
async def test_check_send_transaction_called_once(exception_retry_request_setup):
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
    }]
    with patch(
            'web3.providers.rpc.make_post_request',
            side_effect=ClientConnectorError(None, OSError),
            return_value=async_return(None)) as make_post_request_mock:
        with pytest.raises(ClientConnectorError):
            await exception_retry_request_setup(method, params)
        assert make_post_request_mock.call_count == 1


@pytest.mark.asyncio
async def test_valid_method_retried(exception_retry_request_setup):
    method = 'eth_getBalance'
    params = []

    with patch(
            'web3.providers.rpc.make_post_request',
            side_effect=ClientConnectorError(None, OSError),
            return_value=async_return(None)) as make_post_request_mock:
        with pytest.raises(ClientConnectorError):
            await exception_retry_request_setup(method, params)
        assert make_post_request_mock.call_count == 5


def test_is_strictly_default_http_middleware():
    web3 = HTTPProvider()
    assert 'http_retry_request' in web3.middlewares

    web3 = IPCProvider()
    assert 'http_retry_request' not in web3.middlewares


@patch(
    'web3.providers.rpc.make_post_request',
    side_effect=ClientConnectorError(None, OSError))
def test_check_with_all_middlewares(make_post_request_mock):
    provider = HTTPProvider()
    w3 = web3.Web3(provider)
    with pytest.raises(ClientConnectorError):
        w3.eth.blockNumber()
    assert make_post_request_mock.call_count == 5
