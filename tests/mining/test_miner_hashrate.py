from web3.providers.rpc import TestRPCProvider


def test_miner_hashrate(web3, wait_for_miner_start):
    hashrate = web3.miner.hashrate
    assert hashrate > 0
