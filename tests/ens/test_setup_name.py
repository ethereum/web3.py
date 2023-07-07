import pytest

from eth_typing import (
    HexStr,
)

from ens import (
    AddressMismatch,
    UnauthorizedError,
    UnownedName,
)
from web3 import (
    Web3,
)

"""
API at: https://github.com/carver/ens.py/issues/2
"""

SETUP_NAME_TEST_CASES = (
    (
        "tester.eth",
        "tester.eth",
        "2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe",
    ),
    (
        "TESTER.eth",
        "tester.eth",
        "2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe",
    ),
    # confirm that set-owner works
    (
        "lots.of.subdomains.tester.eth",
        "lots.of.subdomains.tester.eth",
        "0d62a759aa1f1c9680de8603a12a5eb175cd1bfa79426229868eba99f4dce692",
    ),
)


@pytest.fixture
def TEST_ADDRESS(address_conversion_func):
    return address_conversion_func("0x000000000000000000000000000000000000dEaD")


@pytest.mark.parametrize("name, normalized_name, namehash_hex", SETUP_NAME_TEST_CASES)
def test_setup_name(ens, name, normalized_name, namehash_hex):
    address = ens.w3.eth.accounts[3]
    assert not ens.name(address)
    owner = ens.owner("tester.eth")

    ens.setup_name(name, address)
    assert ens.name(address) == normalized_name

    # check that the correct namehash is set:
    node = Web3.to_bytes(hexstr=HexStr(namehash_hex))
    assert ens.resolver(normalized_name).caller.addr(node) == address

    # check that the correct owner is set:
    assert ens.owner(name) == owner

    # setup name to point to new address
    new_address = ens.w3.eth.accounts[4]
    ens.setup_address(name, None)
    ens.setup_name(name, new_address)

    # validate that ens.name() only returns a name if the
    # forward resolution also returns the address
    assert ens.name(new_address) == normalized_name  # reverse resolution
    assert ens.address(name) == new_address  # forward resolution
    assert not ens.name(address)

    # teardown
    ens.setup_name(None, address)
    ens.setup_address(name, None)
    assert not ens.name(address)
    assert not ens.address(name)


def test_cannot_set_name_on_mismatch_address(ens, TEST_ADDRESS):
    ens.setup_address("mismatch-reverse.tester.eth", TEST_ADDRESS)
    with pytest.raises(AddressMismatch):
        ens.setup_name(
            "mismatch-reverse.tester.eth", "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"
        )


def test_setup_name_default_address(ens):
    name = "reverse-defaults-to-forward.tester.eth"
    owner = ens.owner("tester.eth")
    new_resolution = ens.w3.eth.accounts[-1]
    ens.setup_address(name, new_resolution)
    assert not ens.name(new_resolution)
    assert ens.owner(name) == owner
    assert ens.address(name) == new_resolution
    ens.setup_name(name)
    assert ens.name(new_resolution) == name
    ens.setup_name(None, new_resolution)


def test_setup_name_default_to_owner(ens):
    name = "reverse-defaults-to-owner.tester.eth"
    new_owner = ens.w3.eth.accounts[-1]
    ens.setup_owner(name, new_owner)
    assert not ens.name(new_owner)
    assert ens.owner(name) == new_owner
    assert not ens.address(name)
    ens.setup_name(name)
    assert ens.name(new_owner) == name
    ens.setup_name(None, new_owner)


def test_setup_name_unowned_exception(ens):
    with pytest.raises(UnownedName):
        ens.setup_name("unowned-name.tester.eth")


def test_setup_name_unauthorized(ens, TEST_ADDRESS):
    with pytest.raises(UnauthorizedError):
        ens.setup_name("root-owned-tld", TEST_ADDRESS)


def test_setup_reverse_dict_unmodified(ens):
    # setup
    owner = ens.owner("tester.eth")
    eth = ens.w3.eth
    start_count = eth.get_transaction_count(owner)

    address = ens.w3.eth.accounts[3]
    transact = {}
    ens.setup_name("tester.eth", address, transact=transact)

    # even though a transaction was issued, the dict argument was not modified
    assert eth.get_transaction_count(owner) > start_count
    assert transact == {}

    # teardown
    ens.setup_name(None, address, transact=transact)


# -- async -- #


@pytest.mark.asyncio
@pytest.mark.parametrize("name, normalized_name, namehash_hex", SETUP_NAME_TEST_CASES)
async def test_async_setup_name(async_ens, name, normalized_name, namehash_hex):
    accounts = await async_ens.w3.eth.accounts
    address = accounts[3]

    assert not await async_ens.name(address)
    owner = await async_ens.owner("tester.eth")

    await async_ens.setup_name(name, address)
    assert await async_ens.name(address) == normalized_name

    # check that the correct namehash is set:
    node = Web3.to_bytes(hexstr=HexStr(namehash_hex))
    resolver = await async_ens.resolver(normalized_name)
    assert await resolver.caller.addr(node) == address

    # check that the correct owner is set:
    assert await async_ens.owner(name) == owner

    # setup name to point to new address
    new_address = accounts[4]
    await async_ens.setup_address(name, None)
    await async_ens.setup_name(name, new_address)

    # validate that ens.name() only returns a name if the
    # forward resolution also returns the address
    assert await async_ens.name(new_address) == normalized_name  # reverse resolution
    assert await async_ens.address(name) == new_address  # forward resolution
    assert not await async_ens.name(address)

    # teardown
    await async_ens.setup_name(None, address)
    await async_ens.setup_address(name, None)
    assert not await async_ens.name(address)
    assert not await async_ens.address(name)


@pytest.mark.asyncio
async def test_async_setup_name_default_address(async_ens):
    name = "reverse-defaults-to-forward.tester.eth"
    owner = await async_ens.owner("tester.eth")

    accounts = await async_ens.w3.eth.accounts
    new_resolution = accounts[-1]

    await async_ens.setup_address(name, new_resolution)
    assert not await async_ens.name(new_resolution)
    assert await async_ens.owner(name) == owner
    assert await async_ens.address(name) == new_resolution
    await async_ens.setup_name(name)
    assert await async_ens.name(new_resolution) == name
    await async_ens.setup_name(None, new_resolution)


@pytest.mark.asyncio
async def test_async_setup_name_default_to_owner(async_ens):
    name = "reverse-defaults-to-owner.tester.eth"
    accounts = await async_ens.w3.eth.accounts
    new_owner = accounts[-1]

    await async_ens.setup_owner(name, new_owner)
    assert not await async_ens.name(new_owner)
    assert await async_ens.owner(name) == new_owner
    assert not await async_ens.address(name)
    await async_ens.setup_name(name)
    assert await async_ens.name(new_owner) == name


@pytest.mark.asyncio
async def test_async_setup_reverse_dict_unmodified(async_ens):
    # setup
    owner = await async_ens.owner("tester.eth")
    eth = async_ens.w3.eth
    start_count = await eth.get_transaction_count(owner)

    accounts = await eth.accounts
    address = accounts[3]
    transact = {}
    await async_ens.setup_name("tester.eth", address, transact=transact)

    # even though a transaction was issued, the dict argument was not modified
    assert await eth.get_transaction_count(owner) > start_count
    assert transact == {}

    # teardown
    await async_ens.setup_name(None, address, transact=transact)


@pytest.mark.asyncio
async def test_async_setup_name_unowned_exception(async_ens):
    with pytest.raises(UnownedName):
        await async_ens.setup_name("unowned-name.tester.eth")


@pytest.mark.asyncio
async def test_async_setup_name_unauthorized(async_ens, TEST_ADDRESS):
    with pytest.raises(UnauthorizedError):
        await async_ens.setup_name("root-owned-tld", TEST_ADDRESS)


@pytest.mark.asyncio
async def test_async_cannot_set_name_on_mismatch_address(async_ens, TEST_ADDRESS):
    await async_ens.setup_address("mismatch-reverse.tester.eth", TEST_ADDRESS)
    with pytest.raises(AddressMismatch):
        await async_ens.setup_name(
            "mismatch-reverse.tester.eth", "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"
        )
