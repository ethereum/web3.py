from web3.gas_strategies.rpc import rpc_gas_pricing_strategy


def test_default_gas_pricing_strategy(web3):
    assert web3.gas_pricing_strategy == rpc_gas_pricing_strategy


def test_default_gas_priceing_strategy_returns_(web3):
    assert web3.getGasPrice() == 1
