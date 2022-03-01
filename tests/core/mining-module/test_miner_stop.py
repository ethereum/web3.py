import random

from flaky import (
    flaky,
)

from web3._utils.threads import (
    Timeout,
)


@flaky(max_runs=3)
def test_miner_stop(w3_empty):
    w3 = w3_empty

    assert w3.eth.mining
    assert w3.eth.hashrate

    w3.geth.miner.stop()

    with Timeout(60) as timeout:
        while w3.eth.mining or w3.eth.hashrate:
            timeout.sleep(random.random())
            timeout.check()

    assert not w3.eth.mining
    assert not w3.eth.hashrate
