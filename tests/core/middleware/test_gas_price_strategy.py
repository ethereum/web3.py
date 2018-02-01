import pytest
from unittest.mock import (
    Mock,
)

from web3.middleware import (
    gas_price_strategy_middleware,
)


@pytest.fixture
def the_gas_price_strategy_middleware(web3):
    make_request, web3 = Mock(), Mock()
    initialized = gas_price_strategy_middleware(make_request, web3)
    initialized.web3 = web3
    initialized.make_request = make_request
    return initialized


def test_gas_price_generated(the_gas_price_strategy_middleware):
    the_gas_price_strategy_middleware.web3.eth.generateGasPrice.return_value = 5
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
    }]
    the_gas_price_strategy_middleware(method, params)
    the_gas_price_strategy_middleware.web3.eth.generateGasPrice.assert_called_once_with({
        'to': '0x0',
        'value': 1,
    })
    the_gas_price_strategy_middleware.make_request.assert_called_once_with(method, [{
        'to': '0x0',
        'value': 1,
        'gasPrice': 5,
    }])


def test_gas_price_not_overridden(the_gas_price_strategy_middleware):
    the_gas_price_strategy_middleware.web3.eth.generateGasPrice.return_value = 5
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
        'gasPrice': 10,
    }]
    the_gas_price_strategy_middleware(method, params)
    the_gas_price_strategy_middleware.make_request.assert_called_once_with(method, [{
        'to': '0x0',
        'value': 1,
        'gasPrice': 10,
    }])


def test_gas_price_not_set_without_gas_price_strategy(the_gas_price_strategy_middleware):
    the_gas_price_strategy_middleware.web3.eth.generateGasPrice.return_value = None
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
    }]
    the_gas_price_strategy_middleware(method, params)
    the_gas_price_strategy_middleware.make_request.assert_called_once_with(method, params)


def test_not_generate_gas_price_when_not_send_transaction_rpc(the_gas_price_strategy_middleware):
    the_gas_price_strategy_middleware.web3.getGasPriceStrategy = Mock()
    the_gas_price_strategy_middleware('eth_getBalance', [])
    the_gas_price_strategy_middleware.web3.getGasPriceStrategy.assert_not_called()
