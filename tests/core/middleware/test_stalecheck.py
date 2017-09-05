
import pytest
import sys

from web3.middleware.stalecheck import (
    _isfresh,
    make_stalecheck_middleware,
    StaleBlockchain,
)
from web3.utils.datastructures import AttributeDict

if sys.version_info >= (3, 3):
    from unittest.mock import Mock, patch


pytestmark = pytest.mark.skipif(sys.version_info < (3, 3), reason="needs Mock library from 3.3")


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
        method, params = Mock(), Mock()
        request_middleware(method, params)
        request_middleware.make_request.assert_called_once_with(method, params)


def test_stalecheck_fail(request_middleware, now):
    with patch('web3.middleware.stalecheck._isfresh', return_value=False):
        method, params = Mock(), Mock()
        request_middleware.web3.eth.getBlock.return_value = stub_block(now)
        with pytest.raises(StaleBlockchain):
            request_middleware(method, params)


@pytest.mark.parametrize(
    'rpc_method',
    [
        'eth_getBlockByHash',
        'eth_getBlockByNumber',
        'eth_getBlockTransactionCountByHash',
        'eth_getBlockTransactionCountByNumber',
        'eth_getTransactionByBlockHashAndIndex',
        'eth_getTransactionByBlockNumberAndIndex',
        'eth_getUncleCountByBlockHash',
        'eth_getUncleCountByBlockNumber',
    ]
)
def test_stalecheck_ignores_get_by_block_methods(request_middleware, rpc_method):
    # This is especially critical for getBlock('latest') which would cause infinite recursion
    with patch('web3.middleware.stalecheck._isfresh', return_value=True):
        params = Mock()
        request_middleware(rpc_method, params)
        assert not request_middleware.web3.eth.getBlock.called


def test_stalecheck_calls_isfresh_with_empty_cache(request_middleware, allowable_delay):
    with patch('web3.middleware.stalecheck._isfresh', side_effect=[False, True]) as freshspy:
        method, params, block = Mock(), Mock(), Mock()
        request_middleware.web3.eth.getBlock.return_value = block
        request_middleware(method, params)
        cache_call, live_call = freshspy.call_args_list
        assert cache_call[0] == (None, allowable_delay)
        assert live_call[0] == (block, allowable_delay)
