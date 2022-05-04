def test_mining_property_tester(w3):
    assert w3.eth.mining is False


def test_mining_property_ipc_and_rpc(w3, wait_for_miner_start, skip_if_testrpc):
    skip_if_testrpc(w3)

    wait_for_miner_start(w3)
    assert w3.eth.mining is True
