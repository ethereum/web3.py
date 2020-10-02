import pytest

from web3 import Web3
from web3.exceptions import (
    ValidationError,
)
from web3.gas_strategies.time_based import (
    construct_time_based_gas_price_strategy,
)
from web3.middleware import (
    construct_result_generator_middleware,
)
from web3.providers.base import (
    BaseProvider,
)


def _get_block_by_something(method, params):
    block_identifier = params[0]
    if (
        block_identifier == 'latest'
        or block_identifier == '0x5'
    ):
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000005',
            'number': 5,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000004',
            'transactions': [
                {'gasPrice': 70},
                {'gasPrice': 60},
                {'gasPrice': 60},
                {'gasPrice': 60},
                {'gasPrice': 15},
                {'gasPrice': 5},
                {'gasPrice': 50},
            ],
            'miner': '0x' + 'AA' * 20,
            'timestamp': 120,
        }
    elif (
        block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000004'
        or block_identifier == '0x4'
    ):
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000004',
            'number': 4,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000003',
            'transactions': [
                {'gasPrice': 100},
                {'gasPrice': 80},
                {'gasPrice': 60},
            ],
            'miner': '0x' + 'BB' * 20,
            'timestamp': 90,
        }
    elif (
        block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000003'
        or block_identifier == '0x3'
    ):
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000003',
            'number': 3,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000002',
            'transactions': [
                {'gasPrice': 100},
            ],
            'miner': '0x' + 'Cc' * 20,
            'timestamp': 60,
        }
    elif (
        block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000002'
        or block_identifier == '0x2'
    ):
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000002',
            'number': 2,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000001',
            'transactions': [
            ],
            'miner': '0x' + 'Bb' * 20,
            'timestamp': 30,
        }
    elif (
        block_identifier == '0x0000000000000000000000000000000000000000000000000000000000000001'
        or block_identifier == '0x1'
    ):
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000001',
            'number': 1,
            'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000000',
            'transactions': [
                {'gasPrice': 30},
                {'gasPrice': 35},
                {'gasPrice': 65},
            ],
            'miner': '0x' + 'Aa' * 20,
            'timestamp': 15,
        }
    elif (
        block_identifier == '0x0'
    ):
        return {
            'hash': '0x0000000000000000000000000000000000000000000000000000000000000000',
            'number': 0,
            'parentHash': None,
            'transactions': [
                {'gasPrice': 30},
                {'gasPrice': 50},
                {'gasPrice': 60},
                {'gasPrice': 30},
                {'gasPrice': 50},
                {'gasPrice': 60},
                {'gasPrice': 30},
                {'gasPrice': 50},
                {'gasPrice': 60},
                {'gasPrice': 30},
                {'gasPrice': 54},
                {'gasPrice': 10000000000000000000000},
            ],
            'miner': '0x' + 'Aa' * 20,
            'timestamp': 0,
        }
    else:
        assert False


@pytest.mark.parametrize(
    'strategy_params,expected',
    (
        # 80 second wait times
        (dict(max_wait_seconds=80, sample_size=5, probability=98), 70),
        (dict(max_wait_seconds=80, sample_size=5, probability=90), 25),
        (dict(max_wait_seconds=80, sample_size=5, probability=50), 11),
        # 60 second wait times
        (dict(max_wait_seconds=60, sample_size=5, probability=98), 92),
        (dict(max_wait_seconds=60, sample_size=5, probability=90), 49),
        (dict(max_wait_seconds=60, sample_size=5, probability=50), 11),
        # 40 second wait times
        (dict(max_wait_seconds=40, sample_size=5, probability=98), 100),
        (dict(max_wait_seconds=40, sample_size=5, probability=90), 81),
        (dict(max_wait_seconds=40, sample_size=5, probability=50), 11),
        # 20 second wait times
        (dict(max_wait_seconds=20, sample_size=5, probability=98), 100),
        (dict(max_wait_seconds=20, sample_size=5, probability=90), 100),
        (dict(max_wait_seconds=20, sample_size=5, probability=50), 36),
        # 80 second wait times, weighted
        (dict(max_wait_seconds=80, sample_size=5, probability=98, weighted=True), 92),
        (dict(max_wait_seconds=80, sample_size=5, probability=90, weighted=True), 49),
        (dict(max_wait_seconds=80, sample_size=5, probability=50, weighted=True), 11),
    ),
)
def test_time_based_gas_price_strategy(strategy_params, expected):
    fixture_middleware = construct_result_generator_middleware({
        'eth_getBlockByHash': _get_block_by_something,
        'eth_getBlockByNumber': _get_block_by_something,
    })

    w3 = Web3(
        provider=BaseProvider(),
        middlewares=[fixture_middleware],
    )

    time_based_gas_price_strategy = construct_time_based_gas_price_strategy(
        **strategy_params,
    )
    w3.eth.setGasPriceStrategy(time_based_gas_price_strategy)
    actual = w3.eth.generateGasPrice()
    assert actual == expected


@pytest.mark.parametrize(
    'strategy_params_zero,expected_exception_message',
    (
        # 120 second wait times, 0 sample_size
        (dict(max_wait_seconds=80, sample_size=0, probability=98),
            'Constrained sample size is 0'),
        (dict(max_wait_seconds=80, sample_size=0, probability=90),
            'Constrained sample size is 0'),
        (dict(max_wait_seconds=80, sample_size=0, probability=50),
            'Constrained sample size is 0'),
        # 60 second wait times, 0 sample_size
        (dict(max_wait_seconds=60, sample_size=0, probability=98),
            'Constrained sample size is 0'),
        (dict(max_wait_seconds=60, sample_size=0, probability=90),
            'Constrained sample size is 0'),
        (dict(max_wait_seconds=60, sample_size=0, probability=50),
            'Constrained sample size is 0'),
        # 40 second wait times, 0 sample_size
        (dict(max_wait_seconds=40, sample_size=0, probability=98),
            'Constrained sample size is 0'),
        (dict(max_wait_seconds=40, sample_size=0, probability=90),
            'Constrained sample size is 0'),
        (dict(max_wait_seconds=40, sample_size=0, probability=50),
            'Constrained sample size is 0'),
        # 20 second wait times, 0 sample_size
        (dict(max_wait_seconds=20, sample_size=0, probability=98),
            'Constrained sample size is 0'),
        (dict(max_wait_seconds=20, sample_size=0, probability=90),
            'Constrained sample size is 0'),
        (dict(max_wait_seconds=20, sample_size=0, probability=50),
            'Constrained sample size is 0'),
    ),
)
def test_time_based_gas_price_strategy_zero_sample(strategy_params_zero,
                                                   expected_exception_message):
    with pytest.raises(ValidationError) as excinfo:
        fixture_middleware = construct_result_generator_middleware({
            'eth_getBlockByHash': _get_block_by_something,
            'eth_getBlockByNumber': _get_block_by_something,
        })

        w3 = Web3(
            provider=BaseProvider(),
            middlewares=[fixture_middleware],
        )
        time_based_gas_price_strategy_zero = construct_time_based_gas_price_strategy(
            **strategy_params_zero,
        )
        w3.eth.setGasPriceStrategy(time_based_gas_price_strategy_zero)
        w3.eth.generateGasPrice()
    assert str(excinfo.value) == expected_exception_message
