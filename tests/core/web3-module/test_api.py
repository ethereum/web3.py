def test_web3_api(web3):
    assert web3.api.startswith("5")
