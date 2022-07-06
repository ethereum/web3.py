from web3.gas_strategies.rpc import (
    rpc_gas_price_strategy,
)


def test_default_rpc_gas_price_strategy(w3):
    assert rpc_gas_price_strategy(w3, {"to": "0x0", "value": 1}) == 10**9


def test_default_rpc_gas_price_strategy_callable_without_transaction(w3):
    assert rpc_gas_price_strategy(w3) == 10**9
