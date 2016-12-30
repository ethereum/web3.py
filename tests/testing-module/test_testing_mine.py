def test_testing_mine_single_block(web3):
    web3.testing.mine()

    before_mining_block = web3.eth.getBlock("latest")

    web3.testing.mine()

    after_mining_block = web3.eth.getBlock("latest")

    assert after_mining_block['number'] - before_mining_block['number'] == 1


def test_testing_mine_multiple_blocks(web3):
    web3.testing.mine()

    before_mining_block = web3.eth.getBlock("latest")

    web3.testing.mine(5)

    after_mining_block = web3.eth.getBlock("latest")

    assert after_mining_block['number'] - before_mining_block['number'] == 5
