import asyncio
from asynctest import (
    CoroutineMock,
)
import pytest
from unittest.mock import (
    Mock,
    patch,
)

from web3.datastructures import (
    AttributeDict,
)
from web3.middleware import (
    make_stalecheck_middleware,
)
from web3.middleware.stalecheck import (
    StaleBlockchain,
    _isfresh,
)


@pytest.fixture
def now():
    return 3141592653


@pytest.fixture
def allowable_delay():
    return 3 * 24 * 60 * 60


def async_return(result):
    f = asyncio.Future()
    f.set_result(result)
    return f


@pytest.fixture
def request_middleware(allowable_delay):
    middleware = make_stalecheck_middleware(allowable_delay)
    make_request = Mock(return_value=async_return(None))
    web3 = Mock(return_value=async_return(None))
    initialized = middleware(make_request, web3)
    # for easier mocking, later:
    initialized.web3 = web3
    initialized.make_request = make_request
    return initialized


def stub_block(timestamp):
    return AttributeDict({
        'timestamp': timestamp,
        'number': 123,
    })


def test_is_not_fresh_with_no_block():
    assert not _isfresh(None, 1)


def test_is_not_fresh(now):
    with patch('time.time', return_value=now):
        SECONDS_ALLOWED = 2 * 86400
        stale = stub_block(now - SECONDS_ALLOWED - 1)
        assert not _isfresh(stale, SECONDS_ALLOWED)


def test_is_fresh(now):
    with patch('time.time', return_value=now):
        SECONDS_ALLOWED = 2 * 86400
        stale = stub_block(now - SECONDS_ALLOWED)
        assert _isfresh(stale, SECONDS_ALLOWED)


@pytest.mark.asyncio
async def test_stalecheck_pass(request_middleware):
    with patch('web3.middleware.stalecheck._isfresh', return_value=True):
        method, params = object(), object()
        await request_middleware(method, params)
        request_middleware.make_request.assert_called_once_with(method, params)


@pytest.mark.asyncio
async def test_stalecheck_fail(request_middleware, now):
    with patch('web3.middleware.stalecheck._isfresh', return_value=False):
        request_middleware.web3.eth.coro_getBlock = CoroutineMock(
            return_value=stub_block(now))
        with pytest.raises(StaleBlockchain):
            await request_middleware('', [])


@pytest.mark.parametrize(
    'rpc_method',
    [
        'eth_getBlockByNumber',
    ]
)
@pytest.mark.asyncio
async def test_stalecheck_ignores_get_by_block_methods(request_middleware, rpc_method):
    # This is especially critical for getBlock('latest') which would cause infinite recursion
    with patch('web3.middleware.stalecheck._isfresh', side_effect=[False, True]):
        await request_middleware(rpc_method, [])
        assert not request_middleware.web3.eth.coro_getBlock.called


@pytest.mark.asyncio
async def test_stalecheck_calls_isfresh_with_empty_cache(request_middleware, allowable_delay):
    with patch('web3.middleware.stalecheck._isfresh', side_effect=[False, True]) as freshspy:
        block = object()
        request_middleware.web3.eth.coro_getBlock = CoroutineMock(return_value=block)
        await request_middleware('', [])
        cache_call, live_call = freshspy.call_args_list
        assert cache_call[0] == (None, allowable_delay)
        assert live_call[0] == (block, allowable_delay)


@pytest.mark.asyncio
async def test_stalecheck_adds_block_to_cache(request_middleware, allowable_delay):
    with patch('web3.middleware.stalecheck._isfresh', side_effect=[False, True, True]) as freshspy:
        block = object()
        request_middleware.web3.eth.coro_getBlock = CoroutineMock(return_value=block)

        # cache miss
        await request_middleware('', [])
        cache_call, live_call = freshspy.call_args_list
        assert freshspy.call_count == 2
        assert cache_call == ((None, allowable_delay), )
        assert live_call == ((block, allowable_delay), )

        # cache hit
        await request_middleware('', [])
        assert freshspy.call_count == 3
        assert freshspy.call_args == ((block, allowable_delay), )
