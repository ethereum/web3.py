import pytest

import pytest_asyncio

from web3 import (
    Web3,
    constants,
)
from web3.exceptions import (
    InvalidAddress,
)
from web3.middleware import (  # noqa: F401
    async_construct_fixture_middleware,
    async_name_to_address_middleware,
    construct_fixture_middleware,
    name_to_address_middleware,
)
from web3.providers.async_base import (
    AsyncBaseProvider,
)
from web3.providers.base import (
    BaseProvider,
)

NAME = "dump.eth"
ADDRESS = constants.ADDRESS_ZERO
BALANCE = 0


class TempENS:
    def __init__(self, name_addr_pairs):
        self.registry = dict(name_addr_pairs)

    def address(self, name):
        return self.registry.get(name, None)


@pytest.fixture
def w3():
    w3 = Web3(provider=BaseProvider(), middlewares=[])
    w3.ens = TempENS({NAME: ADDRESS})
    w3.middleware_onion.add(name_to_address_middleware(w3))
    return w3


def test_pass_name_resolver(w3):
    return_chain_on_mainnet = construct_fixture_middleware(
        {
            "net_version": "1",
        }
    )
    return_balance = construct_fixture_middleware({"eth_getBalance": BALANCE})
    w3.middleware_onion.inject(return_chain_on_mainnet, layer=0)
    w3.middleware_onion.inject(return_balance, layer=0)
    assert w3.eth.get_balance(NAME) == BALANCE


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


@pytest_asyncio.fixture
async def async_w3():
    async_w3 = Web3(provider=AsyncBaseProvider(), middlewares=[])
    async_w3.ens = TempENS({NAME: ADDRESS})
    _middleware = await async_name_to_address_middleware(async_w3)
    async_w3.middleware_onion.add(_middleware, "name_to_address")
    return async_w3


@pytest.mark.asyncio
async def test_async_pass_name_resolver(async_w3):
    return_chain_on_mainnet = await async_construct_fixture_middleware(
        {
            "net_version": "1",
        }
    )
    return_balance = await async_construct_fixture_middleware(
        {"eth_getBalance": BALANCE}
    )
    async_w3.middleware_onion.inject(return_chain_on_mainnet, layer=0)
    async_w3.middleware_onion.inject(return_balance, layer=0)

    # breakpoint()
    assert await async_w3.eth.get_balance(NAME) == BALANCE


@pytest.mark.asyncio
async def test_async_fail_name_resolver(async_w3):
    return_chain_on_mainnet = await async_construct_fixture_middleware(
        {
            "net_version": "2",
        }
    )
    async_w3.middleware_onion.inject(return_chain_on_mainnet, layer=0)
    with pytest.raises(InvalidAddress, match=r".*ethereum\.eth.*"):
        await async_w3.eth.get_balance("ethereum.eth")
