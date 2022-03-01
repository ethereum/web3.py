import pytest
from unittest.mock import (
    Mock,
)


def test_get_set_gas_price(w3):
    assert w3.eth.gas_price > 0


def test_get_set_gasPrice(w3):
    with pytest.warns(DeprecationWarning):
        assert w3.eth.gasPrice > 0


def test_no_gas_price_strategy_returns_none(w3):
    assert w3.eth.generate_gas_price() is None


def test_generateGasPrice_deprecated(w3):
    with pytest.warns(DeprecationWarning,
                      match='generateGasPrice is deprecated in favor of generate_gas_price'):
        gas_price = w3.eth.generateGasPrice()
    assert gas_price is None


def test_set_gas_price_strategy(w3):
    def my_gas_price_strategy(w3, transaction_params):
        return 5
    w3.eth.set_gas_price_strategy(my_gas_price_strategy)
    assert w3.eth.generate_gas_price() == 5


def test_setGasPriceStrategy_deprecated(w3):
    my_gas_price_strategy = Mock(return_value=5)
    with pytest.warns(DeprecationWarning,
                      match="setGasPriceStrategy is deprecated in favor of "
                            "set_gas_price_strategy"):
        w3.eth.setGasPriceStrategy(my_gas_price_strategy)
    assert w3.eth.generate_gas_price() == 5


def test_gas_price_strategy_calls(w3):
    transaction = {
        'to': '0x0',
        'value': 1000000000
    }
    my_gas_price_strategy = Mock(return_value=5)
    w3.eth.set_gas_price_strategy(my_gas_price_strategy)
    assert w3.eth.generate_gas_price(transaction) == 5
    my_gas_price_strategy.assert_called_once_with(w3, transaction)
