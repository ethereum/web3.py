def test_snapshot_revert_to_latest_snapshot(web3):
    web3.testing.mine(5)

    block_before_snapshot = web3.eth.getBlock("latest")

    web3.testing.snapshot()

    block_after_snapshot = web3.eth.getBlock("latest")

    web3.testing.mine(3)

    block_after_mining = web3.eth.getBlock("latest")

    web3.testing.revert()

    block_after_revert = web3.eth.getBlock("latest")

    assert block_after_mining['number'] > block_before_snapshot['number']
    assert block_before_snapshot['hash'] == block_after_snapshot['hash']
    assert block_after_snapshot['hash'] == block_after_revert['hash']


def test_snapshot_revert_to_specific(web3):
    web3.testing.mine(5)

    block_before_snapshot = web3.eth.getBlock("latest")

    snapshot_idx = web3.testing.snapshot()

    block_after_snapshot = web3.eth.getBlock("latest")

    web3.testing.mine()
    web3.testing.snapshot()
    web3.testing.mine()
    web3.testing.snapshot()
    web3.testing.mine()
    web3.testing.snapshot()

    block_after_mining = web3.eth.getBlock("latest")

    web3.testing.revert(snapshot_idx)

    block_after_revert = web3.eth.getBlock("latest")

    assert block_after_mining['number'] > block_before_snapshot['number']
    assert block_before_snapshot['hash'] == block_after_snapshot['hash']
    assert block_after_snapshot['hash'] == block_after_revert['hash']
