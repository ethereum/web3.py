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


def test_eth_protocol_version(web3):
    with pytest.warns(DeprecationWarning):
        assert web3.eth.protocol_version == '63'


def test_eth_protocolVersion(web3):
    with pytest.warns(DeprecationWarning):
        assert web3.eth.protocolVersion == '63'


def test_eth_chain_id(web3):
    assert web3.eth.chain_id == 61


def test_eth_chainId(web3):
    with pytest.warns(DeprecationWarning):
        assert web3.eth.chainId == 61


def test_set_chain_id(web3):
    assert web3.eth.chain_id == 61

    web3.eth.chain_id = 72
    assert web3.eth.chain_id == 72

    web3.eth.chain_id = None
    assert web3.eth.chain_id == 61


@pytest.mark.asyncio
async def test_async_set_chain_id(async_w3):
    assert await async_w3.eth.chain_id == 61

    async_w3.eth.chain_id = 72
    assert await async_w3.eth.chain_id == 72

    async_w3.eth.chain_id = None
    assert await async_w3.eth.chain_id == 61
