import pytest

from eth_utils.toolz import (
    compose,
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


def result_formatter(method, module):
    def formatter(self):
        return 'OKAY'
    return compose(formatter)


class DummyProvider(BaseProvider):
    def make_request(method, params):
        raise NotImplementedError


result_middleware = construct_result_generator_middleware({
    'method_for_test': lambda m, p: 'ok',
})


class ModuleForTest(ModuleV2):
    method = Method(
        'method_for_test',
        result_formatters=result_formatter)


@pytest.fixture
def dummy_w3():
    w3 = Web3(
        DummyProvider(),
        middlewares=[result_middleware],
        modules={"module": (ModuleForTest,)})
    return w3


def test_result_formatter(dummy_w3):
    assert dummy_w3.module.method() == 'OKAY'
