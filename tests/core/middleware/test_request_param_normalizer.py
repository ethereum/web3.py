import pytest

from hexbytes import HexBytes
from web3 import Web3
from web3.datastructures import (
    AttributeDict,
)
from web3.middleware import (  # noqa: F401
    construct_result_generator_middleware,
    request_parameter_normalizer,
)
from web3.providers.base import (
    BaseProvider,
)


@pytest.fixture
def w3_base():
    return Web3(provider=BaseProvider(), middlewares=[])


@pytest.fixture
def result_generator_middleware():
    result = [AttributeDict({
            'address': '0x2F141Ce366a2462f02cEA3D12CF93E4DCa49e4Fd',
            'blockHash': HexBytes('0x919e1d4b2e0cae57084bcb9ccf4b46553fee48fe1422f7c58765095cd43d9f2c'),
            'blockNumber': 9346779,
            'data': '0x0000000000000000000000000000000000000000000002e820b216795fe09280',
            'logIndex': 67,
            'removed': False,
            'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'),
            HexBytes('0x000000000000000000000000d58b159801499d9b7d56629e4606ae51a1b4fb28'),
            HexBytes('0x0000000000000000000000001f84683e962b7dec4a6a3bd382b8adfc554da8a7')],
            'transactionHash': HexBytes('0x081a7bfd0943d8b3ba7e15e3d905e60340f0f5559171b4b18d42ee166a27d4a1'),
            'transactionIndex': 62})]
    return construct_result_generator_middleware({
        'eth_getLogs': lambda _, params: result
    })


@pytest.fixture
def w3(w3_base, result_generator_middleware):
    w3_base.middleware_onion.add(result_generator_middleware)
    w3_base.middleware_onion.add(request_parameter_normalizer)
    return w3_base


def test_eth_getLogs_param_normalization(w3):
    result = w3.eth.getLogs({
        'from': 'latest', 'address': '0x1111111111111111111111111111111111111111'})
    assert isinstance(result[0]['address'], str)
