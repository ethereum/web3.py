

def test_eth_syncing(web3):
    syncing = web3.eth.syncing
    assert syncing is False
