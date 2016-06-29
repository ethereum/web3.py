def test_coinbase_property(web3):
    cb = web3.eth.coinbase
    assert len(cb) == 42
