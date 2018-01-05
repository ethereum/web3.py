import time
import uuid

import pytest

from cytoolz import assoc

from web3.middleware.cache import (  # noqa: F401
    construct_latest_block_based_cache_middleware,
)
from web3.utils.caching import (
    generate_cache_key,
)


@pytest.fixture(autouse=True)
def _time_travel_to_now(web3):
    web3.testing.timeTravel(int(time.time()))


def test_latest_block_based_cache_middleware_pulls_from_cache(web3):
    current_block_hash = web3.eth.getBlock('latest')['hash']

    cache = {
        generate_cache_key((current_block_hash, 'fake_endpoint', [1])): 'value-a',
    }

    middleware = construct_latest_block_based_cache_middleware(
        cache=cache,
        rpc_whitelist={'fake_endpoint'},
    )(None, web3)

    assert middleware('fake_endpoint', [1]) == 'value-a'


def test_latest_block_based_cache_middleware_populates_cache(web3):
    def make_request(method, params):
        return {
            'result': str(uuid.uuid4()),
        }

    current_block_hash = web3.eth.getBlock('latest')['hash']

    cache = {
        generate_cache_key((current_block_hash, 'fake_endpoint', [1])): 'value-a',
    }

    middleware = construct_latest_block_based_cache_middleware(
        cache=cache,
        rpc_whitelist={'fake_endpoint'},
    )(make_request, web3)

    response = middleware('fake_endpoint', [])
    assert 'result' in response

    assert middleware('fake_endpoint', []) == response
    assert not middleware('fake_endpoint', [1]) == response


@pytest.mark.parametrize(
    'response',
    (
        {},
        {'result': None},
        {'error': 'some error message'},
    )
)
def test_latest_block_cache_middleware_does_not_cache_bad_responses(web3, response):
    def make_request(method, params):
        return assoc(response, 'id', str(uuid.uuid4()))

    middleware = construct_latest_block_based_cache_middleware(
        cache={},
        rpc_whitelist={'fake_endpoint'},
    )(make_request, web3)

    response_a = middleware('fake_endpoint', [])
    assert 'id' in response_a

    response_b = middleware('fake_endpoint', [])
    assert 'id' in response_b

    assert not response_a['id'] == response_b['id']


def test_latest_block_based_cache_middleware_caches_latest_block(web3):
    for _ in range(2):
        web3.testing.mine()

    def make_request(method, params):
        return {
            'result': str(uuid.uuid4()),
        }

    middleware = construct_latest_block_based_cache_middleware(
        cache={},
        average_block_time_sample_size=10,
        default_average_block_time=10,
        rpc_whitelist={'fake_endpoint'},
    )(make_request, web3)

    # prime the internal latest block cache.
    middleware('fake_endpoint', [])

    response = middleware('fake_endpoint', [])
    assert 'result' in response

    assert middleware('fake_endpoint', []) == response

    web3.testing.mine()

    if not middleware('fake_endpoint', []) == response:
        assert False, "Cache unexpectedly busted"
