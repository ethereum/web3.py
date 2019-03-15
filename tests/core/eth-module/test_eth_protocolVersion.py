def test_eth_protocolVersion(web3):
    assert web3.eth.protocolVersion == '63'
