def test_admin_peers(w3, skip_if_testrpc):
    skip_if_testrpc(w3)

    assert w3.geth.admin.peers == []
