def test_eth_chain_id(w3):
    assert w3.eth.chain_id == 61
