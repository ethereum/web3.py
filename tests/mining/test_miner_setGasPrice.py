import random
import gevent


def test_miner_setGasPrice(web3_ipc_empty, wait_for_block):
    web3 = web3_ipc_empty

    initial_gas_price = web3.eth.gasPrice

    # sanity check
    assert web3.eth.gasPrice > 1000

    web3.miner.setGasPrice(initial_gas_price // 2)

    with gevent.Timeout(30):
        while web3.eth.gasPrice == initial_gas_price:
            gevent.sleep(random.random())

    after_gas_price = web3.eth.gasPrice
    assert after_gas_price < initial_gas_price
