def test_parse_block_identifier_int(web3):
    last_num = web3.eth.getBlock('latest').number
    assert web3.eth.getBlock(0) == web3.eth.getBlock(-1 - last_num)
