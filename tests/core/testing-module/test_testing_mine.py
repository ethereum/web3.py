def test_testing_mine_single_block(w3):
    w3.testing.mine()

    before_mining_block = w3.eth.get_block("latest")

    w3.testing.mine()

    after_mining_block = w3.eth.get_block("latest")

    assert after_mining_block["number"] - before_mining_block["number"] == 1


def test_testing_mine_multiple_blocks(w3):
    w3.testing.mine()

    before_mining_block = w3.eth.get_block("latest")

    w3.testing.mine(5)

    after_mining_block = w3.eth.get_block("latest")

    assert after_mining_block["number"] - before_mining_block["number"] == 5
