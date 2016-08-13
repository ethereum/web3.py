def test_admin_nodeInfo(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    node_info = web3.admin.nodeInfo

    assert 'enode' in node_info
    assert 'id' in node_info
