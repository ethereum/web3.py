def test_admin_peers(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    assert web3.admin.peers == []
