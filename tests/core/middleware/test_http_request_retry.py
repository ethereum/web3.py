import pytest
from unittest.mock import (
    Mock,
    patch,
)

import aiohttp
import pytest_asyncio
from requests.exceptions import (
    ConnectionError,
    HTTPError,
    Timeout,
    TooManyRedirects,
)

import web3
from web3 import (
    AsyncHTTPProvider,
    AsyncWeb3,
)
from web3.middleware.exception_retry_request import (
    async_exception_retry_middleware,
    check_if_retry_on_failure,
    exception_retry_middleware,
)
from web3.providers import (
    HTTPProvider,
    IPCProvider,
)


@pytest.fixture
def exception_retry_request_setup():
    w3 = Mock()
    provider = HTTPProvider()
    errors = (ConnectionError, HTTPError, Timeout, TooManyRedirects)
    setup = exception_retry_middleware(provider.make_request, w3, errors, 5)
    setup.w3 = w3
    return setup


def test_check_if_retry_on_failure_false():
    methods = [
        "eth_sendTransaction",
        "personal_signAndSendTransaction",
        "personal_sendTransaction",
    ]

    for method in methods:
        assert not check_if_retry_on_failure(method)


def test_check_if_retry_on_failure_true():
    method = "eth_getBalance"
    assert check_if_retry_on_failure(method)


@patch("web3.providers.rpc.make_post_request", side_effect=ConnectionError)
def test_check_send_transaction_called_once(
    make_post_request_mock, exception_retry_request_setup
):
    method = "eth_sendTransaction"
    params = [
        {
            "to": "0x0",
            "value": 1,
        }
    ]

    with pytest.raises(ConnectionError):
        exception_retry_request_setup(method, params)
    assert make_post_request_mock.call_count == 1


@patch("web3.providers.rpc.make_post_request", side_effect=ConnectionError)
def test_valid_method_retried(make_post_request_mock, exception_retry_request_setup):
    method = "eth_getBalance"
    params = []

    with pytest.raises(ConnectionError):
        exception_retry_request_setup(method, params)
    assert make_post_request_mock.call_count == 5


def test_is_strictly_default_http_middleware():
    w3 = HTTPProvider()
    assert "http_retry_request" in w3.middlewares

    w3 = IPCProvider()
    assert "http_retry_request" not in w3.middlewares


@patch("web3.providers.rpc.make_post_request", side_effect=ConnectionError)
def test_check_with_all_middlewares(make_post_request_mock):
    provider = HTTPProvider()
    w3 = web3.Web3(provider)
    with pytest.raises(ConnectionError):
        w3.eth.block_number
    assert make_post_request_mock.call_count == 5


# -- async -- #


ASYNC_TEST_RETRY_COUNT = 3


@pytest_asyncio.fixture
async def async_exception_retry_request_setup():
    w3 = Mock()
    provider = AsyncHTTPProvider()
    setup = await async_exception_retry_middleware(
        provider.make_request,
        w3,
        (TimeoutError, aiohttp.ClientError),
        ASYNC_TEST_RETRY_COUNT,
        0.1,
    )
    setup.w3 = w3
    return setup


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "error",
    (
        TimeoutError,
        aiohttp.ClientError,  # general base class for all aiohttp errors
        # ClientError subclasses
        aiohttp.ClientConnectionError,
        aiohttp.ServerTimeoutError,
        aiohttp.ClientOSError,
    ),
)
async def test_check_retry_middleware(error, async_exception_retry_request_setup):
    with patch(
        "web3.providers.async_rpc.async_make_post_request"
    ) as make_post_request_mock:
        make_post_request_mock.side_effect = error

        with pytest.raises(error):
            await async_exception_retry_request_setup("eth_getBalance", [])
        assert make_post_request_mock.call_count == ASYNC_TEST_RETRY_COUNT


@pytest.mark.asyncio
async def test_check_without_retry_middleware():
    with patch(
        "web3.providers.async_rpc.async_make_post_request"
    ) as make_post_request_mock:
        make_post_request_mock.side_effect = TimeoutError
        provider = AsyncHTTPProvider()
        w3 = AsyncWeb3(provider)
        w3.provider._middlewares = ()

        with pytest.raises(TimeoutError):
            await w3.eth.block_number
        assert make_post_request_mock.call_count == 1
