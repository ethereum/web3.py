from web3.gas_strategies.rpc import (
    rpc_gas_price_strategy,
)


def test_default_rpc_gas_price_strategy(web3):
    assert rpc_gas_price_strategy(web3, {
        'to': '0x0',
        'value': 1
    }) == 1


def test_default_rpc_gas_price_strategy_callable_without_transaction(web3):
    assert rpc_gas_price_strategy(web3) == 1
