import pytest

import pytest_asyncio

from web3 import (
    AsyncWeb3,
    Web3,
)
from web3.exceptions import (
    InvalidAddress,
)
from web3.middleware import (  # noqa: F401
    construct_fixture_middleware,
    name_to_address_middleware,
)
from web3.middleware.names import async_name_to_address_middleware
from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
    EthereumTesterProvider,
)


NAME = "tester.eth"


class TempENS:
    def __init__(self, name_addr_pairs):
        self.registry = dict(name_addr_pairs)

    def address(self, name):
        return self.registry.get(name, None)


@pytest.fixture
def _w3_setup():
    return Web3(provider=EthereumTesterProvider(), middlewares=[])


@pytest.fixture
def ens_mapped_address(_w3_setup):
    return _w3_setup.eth.accounts[0]


@pytest.fixture
def w3(_w3_setup, ens_mapped_address):
    _w3_setup.ens = TempENS({NAME: ens_mapped_address})
    _w3_setup.middleware_onion.add(name_to_address_middleware(_w3_setup))
    return _w3_setup


def test_pass_name_resolver(w3, ens_mapped_address):
    return_chain_on_mainnet = construct_fixture_middleware(
        {
            "net_version": "1",
        }
    )
    known_account_balance = w3.eth.get_balance(ens_mapped_address)
    w3.middleware_onion.inject(return_chain_on_mainnet, layer=0)
    assert w3.eth.get_balance(NAME) == known_account_balance


def test_fail_name_resolver(w3):
    return_chain_on_mainnet = construct_fixture_middleware(
        {
            "net_version": "2",
        }
    )
    w3.middleware_onion.inject(return_chain_on_mainnet, layer=0)
    with pytest.raises(InvalidAddress, match=r".*ethereum\.eth.*"):
        w3.eth.get_balance("ethereum.eth")


# --- async --- #


class AsyncTempENS(TempENS):
    async def address(self, name):
        return self.registry.get(name, None)


@pytest_asyncio.fixture
async def _async_w3_setup():
    return AsyncWeb3(provider=AsyncEthereumTesterProvider(), middlewares=[])


@pytest_asyncio.fixture
async def async_ens_mapped_address(_async_w3_setup):
    accts = await _async_w3_setup.eth.accounts
    return accts[0]


@pytest_asyncio.fixture
async def async_w3(_async_w3_setup, async_ens_mapped_address):
    _async_w3_setup.ens = AsyncTempENS({NAME: async_ens_mapped_address})
    _async_w3_setup.middleware_onion.add(async_name_to_address_middleware)
    return _async_w3_setup


@pytest.mark.asyncio
async def test_async_pass_name_resolver(async_w3, async_ens_mapped_address):
    known_account_balance = await async_w3.eth.get_balance(async_ens_mapped_address)
    assert await async_w3.eth.get_balance(NAME) == known_account_balance


@pytest.mark.asyncio
async def test_async_fail_name_resolver(async_w3):
    with pytest.raises(InvalidAddress, match=r".*ethereum\.eth.*"):
        await async_w3.eth.get_balance("ethereum.eth")
