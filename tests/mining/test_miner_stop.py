import random

import gevent


def test_miner_stop(web3):
    # sanity
    assert web3.eth.mining
    assert web3.miner.hashrate

    web3.miner.stop()

    with gevent.Timeout(30):
        while web3.eth.mining or web3.eth.hashrate:
            gevent.sleep(random.random())

    assert not web3.eth.mining
    assert not web3.miner.hashrate
