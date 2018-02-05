import pytest

from web3 import Web3
from web3.providers.base import BaseProvider
from web3.gas_strategies.time_based import (
    construct_time_based_gas_price_strategy,
)
from web3.middleware import (
    construct_result_generator_middleware,
)


def _get_block_by_something(method, params):
    block_identifier = params[0]
    if (
        block_identifier == 'latest' or
        block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000005'
    ):
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000005',
            'number': 5,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000004',
            'transactions': [
                {'gasPrice': 70},
                {'gasPrice': 60},
            ],
            'miner': '0xA',
            'timestamp': 100,
        }
    elif block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000004':
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000004',
            'number': 4,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000003',
            'transactions': [
                {'gasPrice': 100},
                {'gasPrice': 80},
                {'gasPrice': 60},
            ],
            'miner': '0xB',
            'timestamp': 80,
        }
    elif block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000003':
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000003',
            'number': 3,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000002',
            'transactions': [
                {'gasPrice': 10},
                {'gasPrice': 50},
                {'gasPrice': 100},
            ],
            'miner': '0xC',
            'timestamp': 60,
        }
    elif block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000002':
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000002',
            'number': 2,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000001',
            'transactions': [
                {'gasPrice': 50},
                {'gasPrice': 70},
                {'gasPrice': 100},
            ],
            'miner': '0xB',
            'timestamp': 40,
        }
    elif block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000001':
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000001',
            'number': 1,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000000',
            'transactions': [
                {'gasPrice': 30},
                {'gasPrice': 35},
                {'gasPrice': 65},
            ],
            'miner': '0xA',
            'timestamp': 20,
        }
    elif (
        block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000000' or
        block_identifier == 0
    ):
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000000',
            'number': 0,
            'parentHash': None,
            'transactions': [
                {'gasPrice': 30},
                {'gasPrice': 50},
                {'gasPrice': 60},
            ],
            'miner': '0xA',
            'timestamp': 0,
        }
    else:
        assert False


@pytest.mark.parametrize(
    'strategy_params,expected',
    (
        # 120 second wait times
        (dict(max_wait_seconds=80, sample_size=5, probability=98), 50),
        (dict(max_wait_seconds=80, sample_size=5, probability=90), 48),
        (dict(max_wait_seconds=80, sample_size=5, probability=50), 39),
        # 60 second wait times
        (dict(max_wait_seconds=60, sample_size=5, probability=98), 50),
        (dict(max_wait_seconds=60, sample_size=5, probability=90), 48),
        (dict(max_wait_seconds=60, sample_size=5, probability=50), 38),
        # 40 second wait times
        (dict(max_wait_seconds=40, sample_size=5, probability=98), 50),
        (dict(max_wait_seconds=40, sample_size=5, probability=90), 47),
        (dict(max_wait_seconds=40, sample_size=5, probability=50), 35),
        # 20 second wait times
        (dict(max_wait_seconds=20, sample_size=5, probability=98), 49),
        (dict(max_wait_seconds=20, sample_size=5, probability=90), 45),
        (dict(max_wait_seconds=20, sample_size=5, probability=50), 25),
    ),
)
def test_time_based_gas_price_strategy(strategy_params, expected):
    fixture_middleware = construct_result_generator_middleware({
        'eth_getBlockByHash': _get_block_by_something,
        'eth_getBlockByNumber': _get_block_by_something,
    })

    w3 = Web3(
        providers=[BaseProvider()],
        middlewares=[fixture_middleware],
    )

    time_based_gas_price_strategy = construct_time_based_gas_price_strategy(
        **strategy_params,
    )
    w3.eth.setGasPriceStrategy(time_based_gas_price_strategy)
    actual = w3.eth.generateGasPrice()
    assert actual == expected
