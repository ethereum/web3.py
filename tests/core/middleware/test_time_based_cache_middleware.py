import time
import uuid

from cytoolz import assoc

import pytest

from web3.middleware.cache import (  # noqa: F401
    construct_time_based_cache_middleware,
)
from web3.utils.caching import (
    generate_cache_key,
)


def test_time_based_cache_middleware_pulls_from_cache():
    cache = {
        generate_cache_key(('fake_endpoint', [1])): (
            time.time(),
            'value-a',
        ),
    }

    middleware = construct_time_based_cache_middleware(
        cache=cache,
        cache_expire_seconds=10,
        rpc_whitelist={'fake_endpoint'},
    )(None, None)

    assert middleware('fake_endpoint', [1]) == 'value-a'


def test_time_based_cache_middleware_populates_cache():
    def make_request(method, params):
        return {
            'result': str(uuid.uuid4()),
        }

    middleware = construct_time_based_cache_middleware(
        cache={},
        cache_expire_seconds=10,
        rpc_whitelist={'fake_endpoint'},
    )(make_request, None)

    response = middleware('fake_endpoint', [])
    assert 'result' in response

    assert middleware('fake_endpoint', []) == response
    assert not middleware('fake_endpoint', [1]) == response


def test_time_based_cache_middleware_expires_old_values():
    def make_request(method, params):
        return {
            'result': str(uuid.uuid4())
        }

    cache = {
        generate_cache_key(('fake_endpoint', [1])): (
            time.time() - 10,
            'value-a',
        ),
    }

    middleware = construct_time_based_cache_middleware(
        cache=cache,
        cache_expire_seconds=10,
        rpc_whitelist={'fake_endpoint'},
    )(make_request, None)

    response = middleware('fake_endpoint', [1])
    assert not response == 'value-a'
    assert 'result' in response

    assert middleware('fake_endpoint', [1]) == response


@pytest.mark.parametrize(
    'response',
    (
        {},
        {'result': None},
        {'error': 'some error message'},
    )
)
def test_time_based_cache_middleware_does_not_cache_bad_responses(response):
    def make_request(method, params):
        return assoc(response, 'id', str(uuid.uuid4()))

    middleware = construct_time_based_cache_middleware(
        cache={},
        cache_expire_seconds=10,
        rpc_whitelist={'fake_endpoint'},
    )(make_request, None)

    response_a = middleware('fake_endpoint', [])
    assert 'id' in response_a

    response_b = middleware('fake_endpoint', [])
    assert 'id' in response_b

    assert not response_a['id'] == response_b['id']


def test_time_based_cache_middleware_does_not_endpoints_not_in_whitelist():
    def make_request(method, params):
        return {
            'result': str(uuid.uuid4())
        }

    middleware = construct_time_based_cache_middleware(
        cache={},
        cache_expire_seconds=10,
        rpc_whitelist={'fake_endpoint'},
    )(make_request, None)

    response_a = middleware('not_whitelisted', [])
    assert 'result' in response_a

    response_b = middleware('not_whitelisted', [])
    assert 'result' in response_b

    assert not response_a['result'] == response_b['result']
