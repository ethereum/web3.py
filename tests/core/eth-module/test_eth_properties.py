import pytest

from web3 import Web3
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
        modules={
            'eth': (AsyncEth,),
        })


def test_eth_protocol_version(w3):
    with pytest.warns(DeprecationWarning):
        assert w3.eth.protocol_version == '63'


def test_eth_protocolVersion(w3):
    with pytest.warns(DeprecationWarning):
        assert w3.eth.protocolVersion == '63'


def test_eth_chain_id(w3):
    assert w3.eth.chain_id == 61


def test_eth_chainId(w3):
    with pytest.warns(DeprecationWarning):
        assert w3.eth.chainId == 61


def test_set_chain_id(w3):
    assert w3.eth.chain_id == 61

    w3.eth.chain_id = 72
    assert w3.eth.chain_id == 72

    w3.eth.chain_id = None
    assert w3.eth.chain_id == 61


@pytest.mark.asyncio
async def test_async_set_chain_id(async_w3):
    assert await async_w3.eth.chain_id == 61

    async_w3.eth.chain_id = 72
    assert await async_w3.eth.chain_id == 72

    async_w3.eth.chain_id = None
    assert await async_w3.eth.chain_id == 61
