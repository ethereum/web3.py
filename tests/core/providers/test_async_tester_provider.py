import pytest

from web3.providers.eth_tester.main import (
    AsyncEthereumTesterProvider,
)


@pytest.mark.asyncio
async def test_async_tester_provider_is_connected() -> None:
    provider = AsyncEthereumTesterProvider()
    connected = await provider.isConnected()
    assert connected


@pytest.mark.asyncio
async def test_async_tester_provider_creates_a_block() -> None:
    provider = AsyncEthereumTesterProvider()
    accounts = await provider.make_request("eth_accounts", [])
    a, b = accounts["result"][:2]
    current_block = await provider.make_request("eth_blockNumber", [])
    assert current_block["result"] == 0
    tx = await provider.make_request(
        "eth_sendTransaction", [{"from": a, "to": b, "gas": 21000}]
    )
    assert tx
    current_block = await provider.make_request("eth_blockNumber", [])
    assert current_block["result"] == 1
