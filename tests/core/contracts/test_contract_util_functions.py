from web3.contract import (
    parse_block_identifier_int,
)


def test_parse_block_identifier_int(web3):
    last_num = web3.eth.getBlock('latest').number
    assert 0 == parse_block_identifier_int(web3, -1 - last_num)
