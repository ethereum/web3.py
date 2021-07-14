import pytest
from typing import (
    TYPE_CHECKING,
)

from eth_utils import (
    is_boolean,
    is_integer,
    is_string,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


class NetModuleTest:
    def test_net_version(self, web3: "Web3") -> None:
        version = web3.net.version

        assert is_string(version)
        assert version.isdigit()

    def test_net_listening(self, web3: "Web3") -> None:
        listening = web3.net.listening

        assert is_boolean(listening)

    def test_net_peer_count(self, web3: "Web3") -> None:
        peer_count = web3.net.peer_count

        assert is_integer(peer_count)

    def test_net_peerCount(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            peer_count = web3.net.peerCount

        assert is_integer(peer_count)

    def test_net_chainId_deprecation(self, web3: "Web3") -> None:
        with pytest.raises(DeprecationWarning):
            web3.net.chainId


class AsyncNetModuleTest:
    @pytest.mark.asyncio
    async def test_net_version(self, async_w3: "Web3") -> None:
        version = await async_w3.async_net.version

        assert is_string(version)
        assert version.isdigit()

    @pytest.mark.asyncio
    async def test_net_listening(self, async_w3: "Web3") -> None:
        listening = await async_w3.async_net.listening

        assert is_boolean(listening)

    @pytest.mark.asyncio
    async def test_net_peer_count(self, async_w3: "Web3") -> None:
        peer_count = await async_w3.async_net.peer_count

        assert is_integer(peer_count)
