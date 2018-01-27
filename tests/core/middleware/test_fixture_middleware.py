import pytest

from web3 import Web3
from web3.middleware import (
    construct_error_generator_middleware,
    construct_fixture_middleware,
    construct_result_generator_middleware,
)
from web3.providers.base import (
    BaseProvider,
)


class DummyProvider(BaseProvider):
    def make_request(self, method, params):
        raise NotImplementedError("Cannot make request for {0}:{1}".format(
            method,
            params,
        ))


@pytest.fixture
def w3():
    return Web3(providers=[DummyProvider()], middlewares=[])


@pytest.mark.parametrize(
    'method,expected',
    (
        ('test_endpoint', 'value-a'),
        ('not_implemented', NotImplementedError),
    )
)
def test_fixture_middleware(w3, method, expected):
    w3.middleware_stack.add(construct_fixture_middleware({'test_endpoint': 'value-a'}))

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            w3.manager.request_blocking(method, [])
    else:
        actual = w3.manager.request_blocking(method, [])
        assert actual == expected


@pytest.mark.parametrize(
    'method,expected',
    (
        ('test_endpoint', 'value-a'),
        ('not_implemented', NotImplementedError),
    )
)
def test_result_middleware(w3, method, expected):
    def _callback(method, params):
        return params[0]

    w3.middleware_stack.add(construct_result_generator_middleware({
        'test_endpoint': _callback,
    }))

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            w3.manager.request_blocking(method, [expected])
    else:
        actual = w3.manager.request_blocking(method, [expected])
        assert actual == expected


@pytest.mark.parametrize(
    'method,expected',
    (
        ('test_endpoint', 'value-a'),
        ('not_implemented', NotImplementedError),
    )
)
def test_error_middleware(w3, method, expected):
    def _callback(method, params):
        return params[0]

    w3.middleware_stack.add(construct_error_generator_middleware({
        'test_endpoint': _callback,
    }))

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            w3.manager.request_blocking(method, [expected])
    else:
        with pytest.raises(ValueError) as err:
            w3.manager.request_blocking(method, [expected])
        assert expected in str(err)
