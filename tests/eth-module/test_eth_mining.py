reset_chain = True


def test_mining_property(web3_tester):
    web3 = web3_tester

    assert web3.eth.mining is False


def test_mining_property_ipc(web3_ipc_empty, wait_for_miner_start):
    web3 = web3_ipc_empty

    wait_for_miner_start(web3)
    assert web3.eth.mining is True


def test_mining_property_rpc(web3_rpc_empty, wait_for_miner_start):
    web3 = web3_rpc_empty

    wait_for_miner_start(web3)
    assert web3.eth.mining is True
