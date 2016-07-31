import pytest

from web3.providers.rpc import TestRPCProvider


@pytest.fixture(autouse=True)
def skip_testrpc_and_wait_for_mining_start(web3, wait_for_miner_start):
    if isinstance(web3.currentProvider, TestRPCProvider):
        pytest.skip("No miner interface on eth-testrpc")

    wait_for_miner_start(web3)

    assert web3.eth.mining
    assert web3.miner.hashrate
