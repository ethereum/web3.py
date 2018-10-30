from asynctest import (
    CoroutineMock,
)
import asyncio
import pytest
from web3.middleware import (
    gas_price_strategy_middleware,
)


def async_return(result):
    f = asyncio.Future()
    f.set_result(result)
    return f


@pytest.fixture
def the_gas_price_strategy_middleware(web3):
    make_request = CoroutineMock(return_value=None)
    web3 = CoroutineMock(return_value=None)
    initialized = gas_price_strategy_middleware(make_request, web3)
    initialized.web3 = web3
    initialized.make_request = make_request
    return initialized


@pytest.mark.asyncio
async def test_gas_price_generated(the_gas_price_strategy_middleware):
    the_gas_price_strategy_middleware.web3.eth.coro_generateGasPrice = CoroutineMock(return_value=5)
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
    }]
    await the_gas_price_strategy_middleware(method, params)
    the_gas_price_strategy_middleware.web3.eth.coro_generateGasPrice.assert_called_once_with({
        'to': '0x0',
        'value': 1,
    })
    the_gas_price_strategy_middleware.make_request.assert_called_once_with(method, [{
        'to': '0x0',
        'value': 1,
        'gasPrice': 5,
    }])


@pytest.mark.asyncio
async def test_gas_price_not_overridden(the_gas_price_strategy_middleware):
    the_gas_price_strategy_middleware.web3.eth.coro_generateGasPrice = CoroutineMock(return_value=5)
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
        'gasPrice': 10,
    }]
    await the_gas_price_strategy_middleware(method, params)
    the_gas_price_strategy_middleware.make_request.assert_called_once_with(method, [{
        'to': '0x0',
        'value': 1,
        'gasPrice': 10,
    }])


@pytest.mark.asyncio
async def test_gas_price_not_set_without_gas_price_strategy(the_gas_price_strategy_middleware):
    the_gas_price_strategy_middleware.web3.eth.coro_generateGasPrice = CoroutineMock(return_value=None)
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
    }]
    await the_gas_price_strategy_middleware(method, params)
    the_gas_price_strategy_middleware.make_request.assert_called_once_with(method, params)


@pytest.mark.asyncio
async def test_not_generate_gas_price_when_not_send_transaction_rpc(
        the_gas_price_strategy_middleware):
    the_gas_price_strategy_middleware.web3.coro_getGasPriceStrategy = CoroutineMock()
    await the_gas_price_strategy_middleware('eth_getBalance', [])
    the_gas_price_strategy_middleware.web3.getGasPriceStrategy.assert_not_called()
