import pytest


def test_admin_nodeInfo(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    with pytest.warns(DeprecationWarning):
        node_info = web3.geth.admin.nodeInfo

        assert 'enode' in node_info
        assert 'id' in node_info


def test_admin_node_info(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    node_info = web3.geth.admin.node_info

    assert 'enode' in node_info
    assert 'id' in node_info
