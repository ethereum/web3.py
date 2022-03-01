from flaky import (
    flaky,
)


@flaky(max_runs=3)
def test_miner_hashrate(w3_empty, wait_for_miner_start):
    w3 = w3_empty

    hashrate = w3.eth.hashrate
    assert hashrate > 0
