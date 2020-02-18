import pytest
import random

from flaky import (
    flaky,
)

from web3._utils.threads import (
    Timeout,
)


@flaky(max_runs=3)
def test_miner_set_gas_price(web3_empty, wait_for_block):
    web3 = web3_empty

    initial_gas_price = web3.eth.gasPrice

    # sanity check
    assert web3.eth.gasPrice > 1000

    web3.geth.miner.set_gas_price(initial_gas_price // 2)

    with Timeout(60) as timeout:
        while web3.eth.gasPrice == initial_gas_price:
            timeout.sleep(random.random())

    after_gas_price = web3.eth.gasPrice
    assert after_gas_price < initial_gas_price


@flaky(max_runs=3)
def test_miner_setGasPrice(web3_empty, wait_for_block):
    web3 = web3_empty

    initial_gas_price = web3.eth.gasPrice
    assert web3.eth.gasPrice > 1000

    # sanity check

    with pytest.warns(DeprecationWarning):
        web3.geth.miner.setGasPrice(initial_gas_price // 2)

    with Timeout(60) as timeout:
        while web3.eth.gasPrice == initial_gas_price:
            timeout.sleep(random.random())

    after_gas_price = web3.eth.gasPrice
    assert after_gas_price < initial_gas_price
