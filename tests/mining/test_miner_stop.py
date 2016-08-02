import random

import gevent

from flaky import flaky


reset_chain = True


@flaky(max_runs=3)
def test_miner_stop(web3):
    assert web3.eth.mining
    assert web3.miner.hashrate

    web3.miner.stop()

    with gevent.Timeout(30):
        while web3.eth.mining or web3.eth.hashrate:
            gevent.sleep(random.random())

    assert not web3.eth.mining
    assert not web3.miner.hashrate
