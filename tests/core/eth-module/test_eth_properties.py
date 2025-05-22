import pytest

from eth_tester import (
    EthereumTester,
)

from web3 import (
    AsyncWeb3,
)
from web3.providers.eth_tester.main import (
    AsyncEthereumTesterProvider,
)


@pytest.fixture
def async_w3(backend_class):
    return AsyncWeb3(
        AsyncEthereumTesterProvider(EthereumTester(backend=backend_class())),
    )


def test_eth_chain_id(w3):
    assert w3.eth.chain_id == w3.provider.ethereum_tester.backend.chain.chain_id


@pytest.mark.asyncio
async def test_async_eth_chain_id(async_w3):
    assert (
        await async_w3.eth.chain_id
        == async_w3.provider.ethereum_tester.backend.chain.chain_id
    )
