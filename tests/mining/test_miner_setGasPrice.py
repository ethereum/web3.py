def test_miner_setGasPrice(web3_ipc_empty, wait_for_block):
    web3 = web3_ipc_empty

    initial_gas_price = web3.eth.gasPrice

    # sanity check
    assert web3.eth.gasPrice > 1000

    web3.miner.setGasPrice(initial_gas_price // 2)

    wait_for_block(web3, web3.eth.blockNumber + 2, timeout=60)

    after_gas_price = web3.eth.gasPrice
    assert after_gas_price < initial_gas_price
