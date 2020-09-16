
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


def test_stalecheck_pass(request_middleware):
    with patch('web3.middleware.stalecheck._isfresh', return_value=True):
        method, params = object(), object()
        request_middleware(method, params)
        request_middleware.make_request.assert_called_once_with(method, params)


def test_stalecheck_fail(request_middleware, now):
    with patch('web3.middleware.stalecheck._isfresh', return_value=False):
        request_middleware.web3.eth.getBlock.return_value = stub_block(now)
        with pytest.raises(StaleBlockchain):
            request_middleware('', [])


@pytest.mark.parametrize(
    'rpc_method',
    [
        'eth_getBlockByNumber',
    ]
)
def test_stalecheck_ignores_get_by_block_methods(request_middleware, rpc_method):
    # This is especially critical for getBlock('latest') which would cause infinite recursion
    with patch('web3.middleware.stalecheck._isfresh', side_effect=[False, True]):
        request_middleware(rpc_method, [])
        assert not request_middleware.web3.eth.getBlock.called


def test_stalecheck_calls_isfresh_with_empty_cache(request_middleware, allowable_delay):
    with patch('web3.middleware.stalecheck._isfresh', side_effect=[False, True]) as freshspy:
        block = object()
        request_middleware.web3.eth.getBlock.return_value = block
        request_middleware('', [])
        cache_call, live_call = freshspy.call_args_list
        assert cache_call[0] == (None, allowable_delay)
        assert live_call[0] == (block, allowable_delay)


def test_stalecheck_adds_block_to_cache(request_middleware, allowable_delay):
    with patch('web3.middleware.stalecheck._isfresh', side_effect=[False, True, True]) as freshspy:
        block = object()
        request_middleware.web3.eth.getBlock.return_value = block

        # cache miss
        request_middleware('', [])
        cache_call, live_call = freshspy.call_args_list
        assert freshspy.call_count == 2
        assert cache_call == ((None, allowable_delay), )
        assert live_call == ((block, allowable_delay), )

        # cache hit
        request_middleware('', [])
        assert freshspy.call_count == 3
        assert freshspy.call_args == ((block, allowable_delay), )
