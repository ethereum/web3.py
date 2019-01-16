import pytest

from eth_utils.toolz import (
    identity,
)

from web3 import Web3
from web3.method import (
    Method,
)
from web3.middleware.fixture import (
    construct_result_generator_middleware,
)
from web3.module import (
    ModuleV2,
)
from web3.providers import (
    BaseProvider,
)


def result_formatter(result):
    if result == 'ok':
        return 'OKAY'
    return result


def formatters(method):
    return ((identity,), ((result_formatter,), None))


def test_method():
    method = Method(
        'test_method',
        formatter_lookup_fn=formatters)
    return method


class DummyProvider(BaseProvider):
    def make_request(method, params):
        raise NotImplementedError


result_middleware = construct_result_generator_middleware(
    {
        'test_method': lambda m, p: 'ok',
    })


class TestModule(ModuleV2):
    method = test_method()


@pytest.fixture
def dummy_w3():
    w3 = Web3(
        DummyProvider(),
        middlewares=[result_middleware],
        modules={'module': TestModule})
    return w3


def test_result_formatter(dummy_w3):
    assert dummy_w3.module.method() == 'OKAY'
