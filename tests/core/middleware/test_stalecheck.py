import pytest
from unittest.mock import (
    Mock,
    patch,
)

import pytest_asyncio

from web3.datastructures import (
    AttributeDict,
)
from web3.middleware import (
    StalecheckMiddlewareBuilder,
)
from web3.middleware.stalecheck import (
    StaleBlockchain,
    _is_fresh,
)


@pytest.fixture
def now():
    return 3141592653


@pytest.fixture
def allowable_delay():
    return 3 * 24 * 60 * 60


@pytest.fixture
def request_middleware(allowable_delay):
    web3 = Mock()
    middleware = StalecheckMiddlewareBuilder.build(allowable_delay, web3)
    middleware._w3.provider.make_request = Mock()
    return middleware


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
        make_request = Mock()
        inner = request_middleware.wrap_make_request(make_request)

        method, params = object(), object()
        inner(method, params)

        make_request.assert_called_once_with(method, params)


def test_stalecheck_fail(request_middleware, now):
    with patch("web3.middleware.stalecheck._is_fresh", return_value=False):
        request_middleware._w3.eth.get_block.return_value = stub_block(now)

        response = object()
        inner = request_middleware.wrap_make_request(lambda *_: response)
        with pytest.raises(StaleBlockchain):
            inner("", [])


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
        inner = request_middleware.wrap_make_request(lambda *_: None)
        inner(rpc_method, [])
        assert not request_middleware._w3.eth.get_block.called


def test_stalecheck_calls_is_fresh_with_empty_cache(
    request_middleware, allowable_delay
):
    with patch(
        "web3.middleware.stalecheck._is_fresh", side_effect=[False, True]
    ) as fresh_spy:
        block = object()
        request_middleware._w3.eth.get_block.return_value = block
        inner = request_middleware.wrap_make_request(lambda *_: None)
        inner("", [])
        cache_call, live_call = fresh_spy.call_args_list
        assert cache_call[0] == (None, allowable_delay)
        assert live_call[0] == (block, allowable_delay)


def test_stalecheck_adds_block_to_cache(request_middleware, allowable_delay):
    with patch(
        "web3.middleware.stalecheck._is_fresh", side_effect=[False, True, True]
    ) as fresh_spy:
        block = object()
        request_middleware._w3.eth.get_block.return_value = block

        # cache miss
        inner = request_middleware.wrap_make_request(lambda *_: None)
        inner("", [])
        cache_call, live_call = fresh_spy.call_args_list
        assert fresh_spy.call_count == 2
        assert cache_call == ((None, allowable_delay),)
        assert live_call == ((block, allowable_delay),)

        # cache hit
        inner("", [])
        assert fresh_spy.call_count == 3
        assert fresh_spy.call_args == ((block, allowable_delay),)


# -- async -- #


async def _coro(_method, _params):
    return None


@pytest_asyncio.fixture
async def async_request_middleware(allowable_delay):
    from unittest.mock import (
        AsyncMock,
    )

    async_web3 = AsyncMock()
    middleware = StalecheckMiddlewareBuilder.build(allowable_delay, async_web3)
    middleware._w3.provider.make_request = Mock()
    return middleware


@pytest.mark.asyncio
async def test_async_stalecheck_pass(async_request_middleware):
    from unittest.mock import (
        AsyncMock,
    )

    with patch("web3.middleware.stalecheck._is_fresh", return_value=True):
        make_request = AsyncMock()
        inner = await async_request_middleware.async_wrap_make_request(make_request)

        method, params = object(), object()
        await inner(method, params)

        make_request.assert_called_once_with(method, params)


@pytest.mark.asyncio
async def test_async_stalecheck_fail(async_request_middleware, now):
    with patch("web3.middleware.stalecheck._is_fresh", return_value=False):
        async_request_middleware._w3.eth.get_block.return_value = stub_block(now)

        with pytest.raises(StaleBlockchain):
            inner = await async_request_middleware.async_wrap_make_request(_coro)
            await inner("", [])


@pytest.mark.asyncio
@pytest.mark.parametrize("rpc_method", ["eth_getBlockByNumber"])
async def test_async_stalecheck_ignores_get_by_block_methods(
    async_request_middleware, rpc_method
):
    # This is especially critical for get_block("latest") which would cause
    # infinite recursion
    with patch("web3.middleware.stalecheck._is_fresh", side_effect=[False, True]):
        inner = await async_request_middleware.async_wrap_make_request(_coro)
        await inner(rpc_method, [])
        assert not async_request_middleware._w3.eth.get_block.called


@pytest.mark.asyncio
async def test_async_stalecheck_calls_is_fresh_with_empty_cache(
    async_request_middleware, allowable_delay
):
    with patch(
        "web3.middleware.stalecheck._is_fresh", side_effect=[False, True]
    ) as fresh_spy:
        block = object()
        async_request_middleware._w3.eth.get_block.return_value = block
        inner = await async_request_middleware.async_wrap_make_request(_coro)
        await inner("", [])
        cache_call, live_call = fresh_spy.call_args_list
        assert cache_call[0] == (None, allowable_delay)
        assert live_call[0] == (block, allowable_delay)


@pytest.mark.asyncio
async def test_async_stalecheck_adds_block_to_cache(
    async_request_middleware, allowable_delay
):
    with patch(
        "web3.middleware.stalecheck._is_fresh", side_effect=[False, True, True]
    ) as fresh_spy:
        block = object()
        async_request_middleware._w3.eth.get_block.return_value = block

        inner = await async_request_middleware.async_wrap_make_request(_coro)

        # cache miss
        await inner("", [])
        cache_call, live_call = fresh_spy.call_args_list
        assert fresh_spy.call_count == 2
        assert cache_call == ((None, allowable_delay),)
        assert live_call == ((block, allowable_delay),)

        # cache hit
        await inner("", [])
        assert fresh_spy.call_count == 3
        assert fresh_spy.call_args == ((block, allowable_delay),)
