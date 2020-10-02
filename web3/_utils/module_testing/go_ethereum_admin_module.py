import pytest
from typing import (
    TYPE_CHECKING,
)

from web3.datastructures import (
    AttributeDict,
)
from web3.types import (
    EnodeURI,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


class GoEthereumAdminModuleTest:
    def test_add_peer(self, web3: "Web3") -> None:
        result = web3.geth.admin.add_peer(
            EnodeURI('enode://f1a6b0bdbf014355587c3018454d070ac57801f05d3b39fe85da574f002a32e929f683d72aa5a8318382e4d3c7a05c9b91687b0d997a39619fb8a6e7ad88e512@1.1.1.1:30303'),)  # noqa: E501
        assert result is True

    def test_admin_datadir(self, web3: "Web3", datadir: str) -> None:
        result = web3.geth.admin.datadir()
        assert result == datadir

    def test_admin_node_info(self, web3: "Web3") -> None:
        result = web3.geth.admin.node_info()
        expected = AttributeDict({
            'id': '',
            'name': '',
            'enode': '',
            'ip': '',
            'ports': AttributeDict({}),
            'listenAddr': '',
            'protocols': AttributeDict({})
        })
        # Test that result gives at least the keys that are listed in `expected`
        assert not set(expected.keys()).difference(result.keys())

    def test_admin_peers(self, web3: "Web3") -> None:
        enode = web3.geth.admin.node_info()['enode']
        web3.geth.admin.add_peer(enode)
        result = web3.geth.admin.peers()
        assert len(result) == 1

    def test_admin_start_stop_rpc(self, web3: "Web3") -> None:
        stop = web3.geth.admin.stop_rpc()
        assert stop is True

        start = web3.geth.admin.start_rpc()
        assert start is True

        with pytest.warns(DeprecationWarning):
            stop = web3.geth.admin.stopRPC()
            assert stop is True

        with pytest.warns(DeprecationWarning):
            start = web3.geth.admin.startRPC()
            assert start is True

    def test_admin_start_stop_ws(self, web3: "Web3") -> None:
        stop = web3.geth.admin.stop_ws()
        assert stop is True

        start = web3.geth.admin.start_ws()
        assert start is True

        with pytest.warns(DeprecationWarning):
            stop = web3.geth.admin.stopWS()
            assert stop is True

        with pytest.warns(DeprecationWarning):
            start = web3.geth.admin.startWS()
            assert start is True

    #
    # Deprecated
    #
    def test_admin_addPeer(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            result = web3.geth.admin.addPeer(
                'enode://f1a6b0bdbf014355587c3018454d070ac57801f05d3b39fe85da574f002a32e929f683d72aa5a8318382e4d3c7a05c9b91687b0d997a39619fb8a6e7ad88e512@1.1.1.1:30303',  # noqa: E501
            )
            assert result is True

    def test_admin_nodeInfo(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            result = web3.geth.admin.nodeInfo()
            expected = AttributeDict({
                'id': '',
                'name': '',
                'enode': '',
                'ip': '',
                'ports': AttributeDict({}),
                'listenAddr': '',
                'protocols': AttributeDict({})
            })
            # Test that result gives at least the keys that are listed in `expected`
            assert not set(expected.keys()).difference(result.keys())
