def test_snapshot_revert_to_latest_snapshot(w3):
    w3.testing.mine(5)

    block_before_snapshot = w3.eth.get_block("latest")

    w3.testing.snapshot()

    block_after_snapshot = w3.eth.get_block("latest")

    w3.testing.mine(3)

    block_after_mining = w3.eth.get_block("latest")

    w3.testing.revert()

    block_after_revert = w3.eth.get_block("latest")

    assert block_after_mining["number"] > block_before_snapshot["number"]
    assert block_before_snapshot["hash"] == block_after_snapshot["hash"]
    assert block_after_snapshot["hash"] == block_after_revert["hash"]


def test_snapshot_revert_to_specific(w3):
    w3.testing.mine(5)

    block_before_snapshot = w3.eth.get_block("latest")

    snapshot_idx = w3.testing.snapshot()

    block_after_snapshot = w3.eth.get_block("latest")

    w3.testing.mine()
    w3.testing.snapshot()
    w3.testing.mine()
    w3.testing.snapshot()
    w3.testing.mine()
    w3.testing.snapshot()

    block_after_mining = w3.eth.get_block("latest")

    w3.testing.revert(snapshot_idx)

    block_after_revert = w3.eth.get_block("latest")

    assert block_after_mining["number"] > block_before_snapshot["number"]
    assert block_before_snapshot["hash"] == block_after_snapshot["hash"]
    assert block_after_snapshot["hash"] == block_after_revert["hash"]
