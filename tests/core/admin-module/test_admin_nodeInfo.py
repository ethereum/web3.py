import pytest


def test_admin_nodeInfo(w3, skip_if_testrpc):
    skip_if_testrpc(w3)

    with pytest.warns(DeprecationWarning):
        node_info = w3.geth.admin.nodeInfo

        assert 'enode' in node_info
        assert 'id' in node_info


def test_admin_node_info(w3, skip_if_testrpc):
    skip_if_testrpc(w3)

    node_info = w3.geth.admin.node_info

    assert 'enode' in node_info
    assert 'id' in node_info
