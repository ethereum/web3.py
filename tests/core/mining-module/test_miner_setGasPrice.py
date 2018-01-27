import random

from flaky import (
    flaky,
)

from web3.utils.threads import (
    Timeout,
)


@flaky(max_runs=3)
def test_miner_setGasPrice(web3_empty, wait_for_block):
    web3 = web3_empty

    initial_gas_price = web3.eth.gasPrice

    # sanity check
    assert web3.eth.gasPrice > 1000

    web3.miner.setGasPrice(initial_gas_price // 2)

    with Timeout(60) as timeout:
        while web3.eth.gasPrice == initial_gas_price:
            timeout.sleep(random.random())

    after_gas_price = web3.eth.gasPrice
    assert after_gas_price < initial_gas_price
