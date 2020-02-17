import pytest


def test_miner_makeDag(web3_empty):
    web3 = web3_empty

    with pytest.warns(DeprecationWarning):
        web3.geth.miner.makeDag(0)

def test_miner_make_dag(web3_empty, wait_for_block):
    web3 = web3_empty
    
    web3.geth.miner.make_dag(0)
