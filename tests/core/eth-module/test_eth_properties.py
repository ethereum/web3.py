import pytest

from web3 import (
    Web3,
)
from web3.eth import (
    AsyncEth,
)
from web3.providers.eth_tester.main import (
    AsyncEthereumTesterProvider,
)


@pytest.fixture
def async_w3():
    return Web3(
        AsyncEthereumTesterProvider(),
        middlewares=[],
    )


def test_eth_chain_id(w3):
    assert w3.eth.chain_id == 131277322940537  # from fixture generation file


@pytest.mark.asyncio
async def test_async_eth_chain_id(async_w3):
    assert (
        await async_w3.eth.chain_id == 131277322940537
    )  # from fixture generation file
