import itertools
import pytest
import time
import uuid

from web3 import Web3
from web3.middleware import (  # noqa: F401
    construct_error_generator_middleware,
    construct_result_generator_middleware,
    construct_time_based_cache_middleware,
)
from web3.providers.base import (
    BaseProvider,
)
from web3.utils.caching import (
    generate_cache_key,
)


@pytest.fixture
def w3_base():
    return Web3(providers=[BaseProvider()], middlewares=[])


@pytest.fixture
def result_generator_middleware():
    return construct_result_generator_middleware({
        'fake_endpoint': lambda *_: str(uuid.uuid4()),
        'not_whitelisted': lambda *_: str(uuid.uuid4()),
    })


@pytest.fixture
def time_cache_middleware():
    return construct_time_based_cache_middleware(
        cache_class=dict,
        cache_expire_seconds=10,
        rpc_whitelist={'fake_endpoint'},
    )


@pytest.fixture
def w3(w3_base, result_generator_middleware, time_cache_middleware):
    w3_base.middleware_stack.add(result_generator_middleware)
    w3_base.middleware_stack.add(time_cache_middleware)
    return w3_base


def test_time_based_cache_middleware_pulls_from_cache(w3_base):
    w3 = w3_base

    def cache_class():
        return {
            generate_cache_key(('fake_endpoint', [1])): (
                time.time(),
                {'result': 'value-a'},
            ),
        }

    w3.middleware_stack.add(construct_time_based_cache_middleware(
        cache_class=cache_class,
        cache_expire_seconds=10,
        rpc_whitelist={'fake_endpoint'},
    ))

    assert w3.manager.request_blocking('fake_endpoint', [1]) == 'value-a'


def test_time_based_cache_middleware_populates_cache(w3):
    result = w3.manager.request_blocking('fake_endpoint', [])

    assert w3.manager.request_blocking('fake_endpoint', []) == result
    assert w3.manager.request_blocking('fake_endpoint', [1]) != result


def test_time_based_cache_middleware_expires_old_values(w3_base, result_generator_middleware):
    w3 = w3_base
    w3.middleware_stack.add(result_generator_middleware)

    def cache_class():
        return {
            generate_cache_key(('fake_endpoint', [1])): (
                time.time() - 10,
                {'result': 'value-a'},
            ),
        }

    w3.middleware_stack.add(construct_time_based_cache_middleware(
        cache_class=cache_class,
        cache_expire_seconds=10,
        rpc_whitelist={'fake_endpoint'},
    ))

    result = w3.manager.request_blocking('fake_endpoint', [1])
    assert result != 'value-a'
    assert w3.manager.request_blocking('fake_endpoint', [1]) == result


@pytest.mark.parametrize(
    'response',
    (
        {},
        {'result': None},
    )
)
def test_time_based_cache_middleware_does_not_cache_bad_responses(
        w3_base,
        response,
        time_cache_middleware):
    w3 = w3_base
    counter = itertools.count()

    def mk_result(method, params):
        next(counter)
        return None

    w3.middleware_stack.add(construct_result_generator_middleware({'fake_endpoint': mk_result}))
    w3.middleware_stack.add(time_cache_middleware)

    w3.manager.request_blocking('fake_endpoint', [])
    w3.manager.request_blocking('fake_endpoint', [])

    assert next(counter) == 2


def test_time_based_cache_middleware_does_not_cache_error_response(
        w3_base,
        time_cache_middleware):
    w3 = w3_base
    counter = itertools.count()

    def mk_error(method, params):
        return "error-number-{0}".format(next(counter))

    w3.middleware_stack.add(construct_error_generator_middleware({
        'fake_endpoint': mk_error,
    }))
    w3.middleware_stack.add(time_cache_middleware)

    with pytest.raises(ValueError) as err:
        w3.manager.request_blocking('fake_endpoint', [])
    assert 'error-number-0' in str(err)

    with pytest.raises(ValueError) as err:
        w3.manager.request_blocking('fake_endpoint', [])
    assert 'error-number-1' in str(err)


def test_time_based_cache_middleware_does_not_cache_endpoints_not_in_whitelist(w3):
    result_a = w3.manager.request_blocking('not_whitelisted', [])
    result_b = w3.manager.request_blocking('not_whitelisted', [])

    assert result_a != result_b
