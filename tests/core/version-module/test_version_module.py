import pytest

from web3 import (
    EthereumTesterProvider,
    Web3,
)
from web3.providers.eth_tester.main import (
    AsyncEthereumTesterProvider,
)
from web3.version import (
    AsyncVersion,
    BlockingVersion,
    Version,
)


@pytest.fixture
def blocking_w3():
    return Web3(
        EthereumTesterProvider(),
        modules={
            "blocking_version": (BlockingVersion,),
            "legacy_version": (Version,),
        })


@pytest.fixture
def async_w3():
    return Web3(
        AsyncEthereumTesterProvider(),
        middlewares=[],
        modules={
            'async_version': (AsyncVersion,),
        })


def test_blocking_version(blocking_w3):
    assert blocking_w3.blocking_version.api == blocking_w3.legacy_version.api


def test_legacy_version_deprecation(blocking_w3):
    with pytest.raises(DeprecationWarning):
        blocking_w3.legacy_version.node
    with pytest.raises(DeprecationWarning):
        blocking_w3.legacy_version.ethereum


@pytest.mark.asyncio
async def test_async_blocking_version(async_w3, blocking_w3):
    assert async_w3.async_version.api == blocking_w3.legacy_version.api

    assert await async_w3.async_version.node == blocking_w3.legacy_version.node
    with pytest.raises(
        ValueError,
        message="RPC Endpoint has not been implemented: eth_protocolVersion"
    ):
        assert await async_w3.async_version.ethereum == blocking_w3.legacy_version.ethereum
