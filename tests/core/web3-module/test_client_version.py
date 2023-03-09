def test_web3_client_version(web3):
    assert web3.client_version.startswith("EthereumTester/")
