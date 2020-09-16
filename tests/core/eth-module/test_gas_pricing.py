from unittest.mock import (
    Mock,
)


def test_no_gas_price_strategy_returns_none(web3):
    assert web3.eth.generateGasPrice() is None


def test_set_gas_price_strategy(web3):
    def my_gas_price_strategy(web3, transaction_params):
        return 5
    web3.eth.setGasPriceStrategy(my_gas_price_strategy)
    assert web3.eth.generateGasPrice() == 5


def test_gas_price_strategy_calls(web3):
    transaction = {
        'to': '0x0',
        'value': 1000000000
    }
    my_gas_price_strategy = Mock(return_value=5)
    web3.eth.setGasPriceStrategy(my_gas_price_strategy)
    assert web3.eth.generateGasPrice(transaction) == 5
    my_gas_price_strategy.assert_called_once_with(web3, transaction)
