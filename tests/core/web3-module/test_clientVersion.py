def test_w3_clientVersion(web3):
    assert web3.clientVersion.startswith("EthereumTester/")
