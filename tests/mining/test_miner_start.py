import random

import gevent


reset_chain = True


def test_miner_start(web3, wait_for_miner_start):
    # sanity
    assert web3.eth.mining
    assert web3.miner.hashrate

    web3.miner.stop()

    with gevent.Timeout(30):
        while web3.eth.mining or web3.eth.hashrate:
            gevent.sleep(random.random())

    assert not web3.eth.mining
    assert not web3.miner.hashrate

    web3.miner.start(1)

    wait_for_miner_start(web3)

    assert web3.eth.mining
    assert web3.miner.hashrate
