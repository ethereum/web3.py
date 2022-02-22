def test_web3_clientVersion(w3):
    assert w3.clientVersion.startswith("EthereumTester/")
