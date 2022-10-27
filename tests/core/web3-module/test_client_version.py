def test_web3_client_version(w3):
    assert w3.client_version.startswith("EthereumTester/")
