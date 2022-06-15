import pytest

from web3 import Web3


class GoEthereumAsyncTxPoolModuleTest:
    @pytest.mark.asyncio
    async def test_async_geth_txpool_inspect(self, async_w3: "Web3") -> None:
        test_data = await async_w3.geth.txpool.inspect()  # type: ignore
        assert "pending" in test_data

    @pytest.mark.asyncio
    async def test_async_geth_txpool_content(self, async_w3: "Web3") -> None:
        test_data = await async_w3.geth.txpool.content()  # type: ignore
        assert "pending" in test_data

    @pytest.mark.asyncio
    async def test_async_geth_txpool_status(self, async_w3: "Web3") -> None:
        test_data = await async_w3.geth.txpool.status()  # type: ignore
        assert "pending" in test_data


class GoEthereumTxPoolModuleTest:
    def test_geth_txpool_inspect(self, w3: "Web3") -> None:
        test_data = w3.geth.txpool.inspect()  # type: ignore
        assert "pending" in test_data

    def test_geth_txpool_content(self, w3: "Web3") -> None:
        test_data = w3.geth.txpool.content()  # type: ignore
        assert "pending" in test_data

    def test_geth_txpool_status(self, w3: "Web3") -> None:
        test_data = w3.geth.txpool.status()  # type: ignore
        assert "pending" in test_data
