import pytest


@pytest.fixture(autouse=True)
def always_wait_for_mining_start(w3,
                                 wait_for_miner_start,
                                 skip_if_testrpc):
    skip_if_testrpc(w3)

    wait_for_miner_start(w3)

    assert w3.eth.mining
    assert w3.eth.hashrate
