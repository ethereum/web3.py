import random

from flaky import (
    flaky,
)

from web3._utils.threads import (
    Timeout,
)


@flaky(max_runs=3)
def test_miner_stop(web3_empty):
    web3 = web3_empty

    assert web3.eth.mining
    assert web3.eth.hashrate

    web3.geth.miner.stop()

    with Timeout(60) as timeout:
        while web3.eth.mining or web3.eth.hashrate:
            timeout.sleep(random.random())
            timeout.check()

    assert not web3.eth.mining
    assert not web3.eth.hashrate
