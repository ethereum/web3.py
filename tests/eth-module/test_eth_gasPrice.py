def test_eth_gasPrice_property(web3):
    gas_price = web3.eth.gasPrice
    assert gas_price >= 1
