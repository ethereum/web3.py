def test_no_gas_price_strategy_returns_none(web3):
    assert web3.eth.getGasPrice() is None


def test_set_gas_price_strategy(web3):
    def my_gas_price_strategy(web3, transaction_params):
        return 5
    web3.eth.setGasPriceStrategy(my_gas_price_strategy)
    assert web3.eth.getGasPrice() == 5
