import pytest
from typing import (
    TYPE_CHECKING,
    List,
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
    def test_add_peer(self, w3: "Web3") -> None:
        result = w3.geth.admin.add_peer(
            EnodeURI(
                "enode://f1a6b0bdbf014355587c3018454d070ac57801f05d3b39fe85da574f002a32e929f683d72aa5a8318382e4d3c7a05c9b91687b0d997a39619fb8a6e7ad88e512@1.1.1.1:30303"  # noqa: E501
            ),
        )
        assert result is True

    def test_admin_datadir(self, w3: "Web3", datadir: str) -> None:
        result = w3.geth.admin.datadir()
        assert result == datadir

    def test_admin_node_info(self, w3: "Web3") -> None:
        result = w3.geth.admin.node_info()
        expected = AttributeDict(
            {
                "id": "",
                "name": "",
                "enode": "",
                "ip": "",
                "ports": AttributeDict({}),
                "listenAddr": "",
                "protocols": AttributeDict({}),
            }
        )
        # Test that result gives at least the keys that are listed in `expected`
        assert not set(expected.keys()).difference(result.keys())

    def test_admin_peers(self, w3: "Web3") -> None:
        enode = w3.geth.admin.node_info()["enode"]
        w3.geth.admin.add_peer(enode)
        result = w3.geth.admin.peers()
        assert len(result) == 1

    def test_admin_start_stop_http(self, w3: "Web3") -> None:
        stop = w3.geth.admin.stop_http()
        assert stop is True

        start = w3.geth.admin.start_http()
        assert start is True

    def test_admin_start_stop_rpc(self, w3: "Web3") -> None:
        with pytest.warns(DeprecationWarning, match="deprecated in favor of stop_http"):
            stop = w3.geth.admin.stop_rpc()
            assert stop is True

        with pytest.warns(
            DeprecationWarning, match="deprecated in favor of start_http"
        ):
            start = w3.geth.admin.start_rpc()
            assert start is True

    def test_admin_start_stop_ws(self, w3: "Web3") -> None:
        stop = w3.geth.admin.stop_ws()
        assert stop is True

        start = w3.geth.admin.start_ws()
        assert start is True


class GoEthereumAsyncAdminModuleTest:
    @pytest.mark.asyncio
    async def test_async_datadir(self, async_w3: "Web3") -> None:
        datadir = await async_w3.geth.admin.datadir()  # type: ignore
        assert isinstance(datadir, str)

    @pytest.mark.asyncio
    async def test_async_nodeinfo(self, async_w3: "Web3") -> None:
        node_info = await async_w3.geth.admin.node_info()  # type: ignore
        assert "Geth" in node_info["name"]

    @pytest.mark.asyncio
    async def test_async_nodes(self, async_w3: "Web3") -> None:
        nodes = await async_w3.geth.admin.peers()  # type: ignore
        assert isinstance(nodes, List)

    @pytest.mark.asyncio
    async def test_admin_peers(self, w3: "Web3") -> None:
        enode = await w3.geth.admin.node_info()["enode"]  # type: ignore
        w3.geth.admin.add_peer(enode)
        result = await w3.geth.admin.peers()  # type: ignore
        assert len(result) == 1

    @pytest.mark.asyncio
    async def test_admin_start_stop_http(self, w3: "Web3") -> None:
        stop = await w3.geth.admin.stop_http()  # type: ignore
        assert stop is True

        start = await w3.geth.admin.start_http()  # type: ignore
        assert start is True

    @pytest.mark.asyncio
    async def test_admin_start_stop_rpc(self, w3: "Web3") -> None:
        with pytest.warns(DeprecationWarning, match="deprecated in favor of stop_http"):
            stop = await w3.geth.admin.stop_rpc()
            assert stop is True

        with pytest.warns(
            DeprecationWarning, match="deprecated in favor of start_http"
        ):
            start = await w3.geth.admin.start_rpc()
            assert start is True

    @pytest.mark.asyncio
    async def test_admin_start_stop_ws(self, w3: "Web3") -> None:
        stop = await w3.geth.admin.stop_ws()  # type: ignore
        assert stop is True

        start = await w3.geth.admin.start_ws()  # type: ignore
        assert start is True
