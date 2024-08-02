import pytest

from web3 import (
    AsyncWeb3,
)
from web3.providers.eth_tester.main import (
    AsyncEthereumTesterProvider,
)


@pytest.fixture
def async_w3():
    return AsyncWeb3(
        AsyncEthereumTesterProvider(),
    )


def test_eth_chain_id(w3):
    assert w3.eth.chain_id == w3.provider.eth_tester.chain_id


@pytest.mark.asyncio
async def test_async_eth_chain_id(async_w3):
    assert await async_w3.eth.chain_id == async_w3.provider.eth_tester.chain_id
