from eth_utils import (
    is_integer,
)


def test_eth_blockNumber(web3):
    block_number = web3.eth.blockNumber
    assert is_integer(block_number)
