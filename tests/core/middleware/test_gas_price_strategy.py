import pytest
from unittest.mock import (
    Mock,
)

from toolz import (
    merge,
)

from web3.middleware import (
    GasPriceStrategyMiddleware,
)


@pytest.fixture
def the_GasPriceStrategyMiddleware():
    w3 = Mock()
    initialized = GasPriceStrategyMiddleware(w3)
    return initialized


def test_gas_price_generated(the_GasPriceStrategyMiddleware):
    w3 = the_GasPriceStrategyMiddleware._w3
    w3.eth.generate_gas_price.return_value = 5

    make_request = Mock()
    inner = the_GasPriceStrategyMiddleware.wrap_make_request(make_request)
    method, dict_param = "eth_sendTransaction", {"to": "0x0", "value": 1}
    inner(method, (dict_param,))

    w3.eth.generate_gas_price.assert_called_once_with(dict_param)
    make_request.assert_called_once_with(
        method, (merge(dict_param, {"gasPrice": "0x5"}),)
    )


def test_gas_price_not_overridden(the_GasPriceStrategyMiddleware):
    the_GasPriceStrategyMiddleware._w3.eth.generate_gas_price.return_value = 5

    make_request = Mock()
    inner = the_GasPriceStrategyMiddleware.wrap_make_request(make_request)
    method, params = "eth_sendTransaction", ({"to": "0x0", "value": 1, "gasPrice": 10},)
    inner(method, params)

    make_request.assert_called_once_with(method, params)


def test_gas_price_not_set_without_gas_price_strategy(
    the_GasPriceStrategyMiddleware,
):
    the_GasPriceStrategyMiddleware._w3.eth.generate_gas_price.return_value = None

    make_request = Mock()
    inner = the_GasPriceStrategyMiddleware.wrap_make_request(make_request)
    method, params = "eth_sendTransaction", ({"to": "0x0", "value": 1},)
    inner(method, params)

    make_request.assert_called_once_with(method, params)


def test_not_generate_gas_price_when_not_send_transaction_rpc(
    the_GasPriceStrategyMiddleware,
):
    the_GasPriceStrategyMiddleware._w3.get_gas_price_strategy = Mock()

    inner = the_GasPriceStrategyMiddleware.wrap_make_request(Mock())
    inner("eth_getBalance", [])

    the_GasPriceStrategyMiddleware._w3.get_gas_price_strategy.assert_not_called()
