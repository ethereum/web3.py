from eth_utils import (
    is_integer,
)


def test_eth_gasPrice_property(web3):
    gas_price = web3.eth.gasPrice
    assert is_integer(gas_price)
    assert gas_price >= 1
