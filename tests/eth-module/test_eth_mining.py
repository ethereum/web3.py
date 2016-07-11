def test_mining_property(web3):
    is_mining = web3.eth.mining
    assert is_mining is False
