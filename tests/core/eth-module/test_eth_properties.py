def test_eth_protocolVersion(web3):
    assert web3.eth.protocolVersion == '65'


def test_eth_chainId(web3):
    assert web3.eth.chainId == 61
