def test_mining_property_tester(web3_tester):
    web3 = web3_tester

    assert web3.eth.mining is False


def test_mining_property_ipc_and_rpc(web3_empty, wait_for_miner_start,
                                     skip_if_testrpc):
    web3 = web3_empty

    skip_if_testrpc(web3)

    wait_for_miner_start(web3)
    assert web3.eth.mining is True
