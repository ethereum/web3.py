import itertools
import pytest
import uuid

from web3 import Web3
from web3.middleware import (
    construct_error_generator_middleware,
    construct_result_generator_middleware,
    construct_simple_cache_middleware,
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
def w3(w3_base, result_generator_middleware):
    w3_base.middleware_stack.add(result_generator_middleware)
    return w3_base


def test_simple_cache_middleware_pulls_from_cache(w3):
    def cache_class():
        return {
            generate_cache_key(('fake_endpoint', [1])): {'result': 'value-a'},
        }

    w3.middleware_stack.add(construct_simple_cache_middleware(
        cache_class=cache_class,
        rpc_whitelist={'fake_endpoint'},
    ))

    assert w3.manager.request_blocking('fake_endpoint', [1]) == 'value-a'


def test_simple_cache_middleware_populates_cache(w3):
    w3.middleware_stack.add(construct_simple_cache_middleware(
        cache_class=dict,
        rpc_whitelist={'fake_endpoint'},
    ))

    result = w3.manager.request_blocking('fake_endpoint', [])

    assert w3.manager.request_blocking('fake_endpoint', []) == result
    assert w3.manager.request_blocking('fake_endpoint', [1]) != result


def test_simple_cache_middleware_does_not_cache_none_responses(w3_base):
    counter = itertools.count()
    w3 = w3_base

    def result_cb(method, params):
        next(counter)
        return None

    w3.middleware_stack.add(construct_result_generator_middleware({
        'fake_endpoint': result_cb,
    }))

    w3.middleware_stack.add(construct_simple_cache_middleware(
        cache_class=dict,
        rpc_whitelist={'fake_endpoint'},
    ))

    w3.manager.request_blocking('fake_endpoint', [])
    w3.manager.request_blocking('fake_endpoint', [])

    assert next(counter) == 2


def test_simple_cache_middleware_does_not_cache_error_responses(w3_base):
    w3 = w3_base
    w3.middleware_stack.add(construct_error_generator_middleware({
        'fake_endpoint': lambda *_: 'msg-{0}'.format(str(uuid.uuid4())),
    }))

    w3.middleware_stack.add(construct_simple_cache_middleware(
        cache_class=dict,
        rpc_whitelist={'fake_endpoint'},
    ))

    with pytest.raises(ValueError) as err_a:
        w3.manager.request_blocking('fake_endpoint', [])
    with pytest.raises(ValueError) as err_b:
        w3.manager.request_blocking('fake_endpoint', [])

    assert str(err_a) != str(err_b)


def test_simple_cache_middleware_does_not_cache_endpoints_not_in_whitelist(w3):
    w3.middleware_stack.add(construct_simple_cache_middleware(
        cache_class=dict,
        rpc_whitelist={'fake_endpoint'},
    ))

    result_a = w3.manager.request_blocking('not_whitelisted', [])
    result_b = w3.manager.request_blocking('not_whitelisted', [])

    assert result_a != result_b
