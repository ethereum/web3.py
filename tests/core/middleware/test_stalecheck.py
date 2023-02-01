import pytest
import sys
from unittest.mock import (
    Mock,
    patch,
)

import pytest_asyncio

from web3.datastructures import (
    AttributeDict,
)
from web3.middleware import (
    make_stalecheck_middleware,
)
from web3.middleware.stalecheck import (
    StaleBlockchain,
    _is_fresh,
    async_make_stalecheck_middleware,
)


@pytest.fixture
def now():
    return 3141592653


@pytest.fixture
def allowable_delay():
    return 3 * 24 * 60 * 60


@pytest.fixture
def request_middleware(allowable_delay):
    middleware = make_stalecheck_middleware(allowable_delay)
    make_request, web3 = Mock(), Mock()
    initialized = middleware(make_request, web3)
    # for easier mocking, later:
    initialized.web3 = web3
    initialized.make_request = make_request
    return initialized


def stub_block(timestamp):
    return AttributeDict(
        {
            "timestamp": timestamp,
            "number": 123,
        }
    )


def test_is_not_fresh_with_no_block():
    assert not _is_fresh(None, 1)


def test_is_not_fresh(now):
    with patch("time.time", return_value=now):
        SECONDS_ALLOWED = 2 * 86400
        stale = stub_block(now - SECONDS_ALLOWED - 1)
        assert not _is_fresh(stale, SECONDS_ALLOWED)


def test_is_fresh(now):
    with patch("time.time", return_value=now):
        SECONDS_ALLOWED = 2 * 86400
        stale = stub_block(now - SECONDS_ALLOWED)
        assert _is_fresh(stale, SECONDS_ALLOWED)


def test_stalecheck_pass(request_middleware):
    with patch("web3.middleware.stalecheck._is_fresh", return_value=True):
        method, params = object(), object()
        request_middleware(method, params)
        request_middleware.make_request.assert_called_once_with(method, params)


def test_stalecheck_fail(request_middleware, now):
    with patch("web3.middleware.stalecheck._is_fresh", return_value=False):
        request_middleware.web3.eth.get_block.return_value = stub_block(now)
        with pytest.raises(StaleBlockchain):
            request_middleware("", [])


@pytest.mark.parametrize(
    "rpc_method",
    [
        "eth_getBlockByNumber",
    ],
)
def test_stalecheck_ignores_get_by_block_methods(request_middleware, rpc_method):
    # This is especially critical for get_block('latest')
    # which would cause infinite recursion
    with patch("web3.middleware.stalecheck._is_fresh", side_effect=[False, True]):
        request_middleware(rpc_method, [])
        assert not request_middleware.web3.eth.get_block.called


def test_stalecheck_calls_is_fresh_with_empty_cache(
    request_middleware, allowable_delay
):
    with patch(
        "web3.middleware.stalecheck._is_fresh", side_effect=[False, True]
    ) as fresh_spy:
        block = object()
        request_middleware.web3.eth.get_block.return_value = block
        request_middleware("", [])
        cache_call, live_call = fresh_spy.call_args_list
        assert cache_call[0] == (None, allowable_delay)
        assert live_call[0] == (block, allowable_delay)


def test_stalecheck_adds_block_to_cache(request_middleware, allowable_delay):
    with patch(
        "web3.middleware.stalecheck._is_fresh", side_effect=[False, True, True]
    ) as fresh_spy:
        block = object()
        request_middleware.web3.eth.get_block.return_value = block

        # cache miss
        request_middleware("", [])
        cache_call, live_call = fresh_spy.call_args_list
        assert fresh_spy.call_count == 2
        assert cache_call == ((None, allowable_delay),)
        assert live_call == ((block, allowable_delay),)

        # cache hit
        request_middleware("", [])
        assert fresh_spy.call_count == 3
        assert fresh_spy.call_args == ((block, allowable_delay),)


# -- async -- #


min_version = pytest.mark.skipif(
    sys.version_info < (3, 8), reason="AsyncMock requires python3.8 or higher"
)


@pytest_asyncio.fixture
async def request_async_middleware(allowable_delay):
    from unittest.mock import (
        AsyncMock,
    )

    middleware = await async_make_stalecheck_middleware(allowable_delay)
    make_request, web3 = AsyncMock(), AsyncMock()
    initialized = await middleware(make_request, web3)
    # for easier mocking, later:
    initialized.web3 = web3
    initialized.make_request = make_request
    return initialized


@pytest.mark.asyncio
@min_version
async def test_async_stalecheck_pass(request_async_middleware):
    with patch("web3.middleware.stalecheck._is_fresh", return_value=True):
        method, params = object(), object()
        await request_async_middleware(method, params)
        request_async_middleware.make_request.assert_called_once_with(method, params)


@pytest.mark.asyncio
@min_version
async def test_async_stalecheck_fail(request_async_middleware, now):
    with patch("web3.middleware.stalecheck._is_fresh", return_value=False):
        request_async_middleware.web3.eth.get_block.return_value = stub_block(now)
        with pytest.raises(StaleBlockchain):
            await request_async_middleware("", [])


@pytest.mark.asyncio
@pytest.mark.parametrize("rpc_method", ["eth_getBlockByNumber"])
@min_version
async def test_async_stalecheck_ignores_get_by_block_methods(
    request_async_middleware, rpc_method
):
    # This is especially critical for get_block("latest") which would cause
    # infinite recursion
    with patch("web3.middleware.stalecheck._is_fresh", side_effect=[False, True]):
        await request_async_middleware(rpc_method, [])
        assert not request_async_middleware.web3.eth.get_block.called


@pytest.mark.asyncio
@min_version
async def test_async_stalecheck_calls_is_fresh_with_empty_cache(
    request_async_middleware, allowable_delay
):
    with patch(
        "web3.middleware.stalecheck._is_fresh", side_effect=[False, True]
    ) as fresh_spy:
        block = object()
        request_async_middleware.web3.eth.get_block.return_value = block
        await request_async_middleware("", [])
        cache_call, live_call = fresh_spy.call_args_list
        assert cache_call[0] == (None, allowable_delay)
        assert live_call[0] == (block, allowable_delay)


@pytest.mark.asyncio
@min_version
async def test_async_stalecheck_adds_block_to_cache(
    request_async_middleware, allowable_delay
):
    with patch(
        "web3.middleware.stalecheck._is_fresh", side_effect=[False, True, True]
    ) as fresh_spy:
        block = object()
        request_async_middleware.web3.eth.get_block.return_value = block

        # cache miss
        await request_async_middleware("", [])
        cache_call, live_call = fresh_spy.call_args_list
        assert fresh_spy.call_count == 2
        assert cache_call == ((None, allowable_delay),)
        assert live_call == ((block, allowable_delay),)

        # cache hit
        await request_async_middleware("", [])
        assert fresh_spy.call_count == 3
        assert fresh_spy.call_args == ((block, allowable_delay),)
