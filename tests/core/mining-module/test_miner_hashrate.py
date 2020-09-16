from flaky import (
    flaky,
)


@flaky(max_runs=3)
def test_miner_hashrate(web3_empty, wait_for_miner_start):
    web3 = web3_empty

    hashrate = web3.eth.hashrate
    assert hashrate > 0
