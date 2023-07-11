import pytest
from unittest.mock import (
    patch,
)

from eth_typing import (
    HexStr,
)
from eth_utils import (
    is_same_address,
    to_bytes,
)

from ens import (
    UnauthorizedError,
)
from ens.constants import (
    EMPTY_ADDR_HEX,
)
from web3 import (
    Web3,
)

"""
API at: https://github.com/carver/ens.py/issues/2
"""

SETUP_ADDRESS_TEST_CASES = (
    (
        "tester.eth",
        "0x2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe",
    ),
    (
        "TESTER.eth",
        "0x2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe",
    ),
    # confirm that set-owner works
    (
        "lots.of.subdomains.tester.eth",
        "0x0d62a759aa1f1c9680de8603a12a5eb175cd1bfa79426229868eba99f4dce692",
    ),
)
SETUP_ADDRESS_EQUIVALENCE_TEST_CASES = (
    ("TESTER.eth", "tester.eth"),
    ("unicÖde.tester.eth", "unicöde.tester.eth"),
)
SETUP_ADDRESS_NOOP_TEST_CASES = (
    # since the test uses get_transaction_count,
    # using a same address converted to bytes and hex will error with same count,
    # use two different addresses of each type (hex, bytes)
    "0x000000000000000000000000000000000000dEaD",
    to_bytes(hexstr="0x5B2063246F2191f18F2675ceDB8b28102e957458"),
    EMPTY_ADDR_HEX,
    None,
    "",
)


@pytest.mark.parametrize("name, namehash_hex", SETUP_ADDRESS_TEST_CASES)
def test_setup_address(ens, name, namehash_hex, TEST_ADDRESS):
    assert ens.address(name) is None
    owner = ens.owner("tester.eth")

    ens.setup_address(name, TEST_ADDRESS)
    assert is_same_address(ens.address(name), TEST_ADDRESS)

    namehash = Web3.to_bytes(hexstr=HexStr(namehash_hex))
    normal_name = ens.nameprep(name)
    # check that the correct namehash is set:
    assert is_same_address(
        ens.resolver(normal_name).caller.addr(namehash), TEST_ADDRESS
    )

    # check that the correct owner is set:
    assert ens.owner(name) == owner

    ens.setup_address(name, None)
    assert ens.address(name) is None


@pytest.mark.parametrize(
    "name, equivalent",
    SETUP_ADDRESS_EQUIVALENCE_TEST_CASES,
)
def test_setup_address_equivalence(ens, name, equivalent, TEST_ADDRESS):
    assert ens.address(name) is None

    ens.setup_address(name, TEST_ADDRESS)
    assert is_same_address(ens.address(name), TEST_ADDRESS)
    assert is_same_address(ens.address(equivalent), TEST_ADDRESS)

    ens.setup_address(name, None)
    assert ens.address(name) is None


@pytest.mark.parametrize(
    "setup_address",
    SETUP_ADDRESS_NOOP_TEST_CASES,
)
def test_setup_address_noop(ens, setup_address):
    eth = ens.w3.eth
    owner = ens.owner("tester.eth")
    ens.setup_address("noop.tester.eth", setup_address)
    starting_transactions = eth.get_transaction_count(owner)

    # do not issue transaction if address is already set
    ens.setup_address("noop.tester.eth", setup_address)
    assert eth.get_transaction_count(owner) == starting_transactions


def test_setup_address_unauthorized(ens, TEST_ADDRESS):
    with pytest.raises(UnauthorizedError):
        ens.setup_address("eth", TEST_ADDRESS)


def test_setup_address_default_address_to_owner(ens):
    assert ens.address("default.tester.eth") is None
    owner = ens.owner("tester.eth")

    ens.setup_address("default.tester.eth")
    assert ens.address("default.tester.eth") == owner


def test_setup_address_default_to_owner_for_multichain_address_resolution(ens):
    ens.setup_address("leet.tester.eth", coin_type=1337)

    # was never set up for ETH, so no address resolution expected
    assert ens.address("leet.tester.eth") is None

    # assert resolves for ``coin_type == 1337``
    owner = ens.owner("tester.eth")
    assert ens.address("leet.tester.eth", coin_type=1337) == owner


def test_first_owner_upchain_identify(ens):
    # _first_owner should auto-select the name owner to send the transaction from
    addr = "0x5B2063246F2191f18F2675ceDB8b28102e957458"

    def getowner(name):
        if name == "cdefghi.eth":
            return addr
        else:
            return None

    with patch.object(ens, "owner", side_effect=getowner):
        assert ens._first_owner("abcdefg.bcdefgh.cdefghi.eth") == (
            addr,
            ["abcdefg", "bcdefgh"],
            "cdefghi.eth",
        )


def test_setup_resolver_leave_default(ens, TEST_ADDRESS):
    owner = ens.owner("tester.eth")
    ens.setup_address("leave-default-resolver.tester.eth", TEST_ADDRESS)
    eth = ens.w3.eth
    num_transactions = eth.get_transaction_count(owner)

    ens.setup_address(
        "leave-default-resolver.tester.eth",
        "0x5B2063246F2191f18F2675ceDB8b28102e957458",
    )

    # should skip setting the owner and setting the default resolver, and only
    #   set the name in the default resolver to point to the new address
    assert eth.get_transaction_count(owner) == num_transactions + 1


# -- async -- #


@pytest.mark.asyncio
@pytest.mark.parametrize("name, namehash_hex", SETUP_ADDRESS_TEST_CASES)
async def test_async_setup_address(async_ens, name, namehash_hex, TEST_ADDRESS):
    assert await async_ens.address(name) is None
    owner = await async_ens.owner("tester.eth")

    await async_ens.setup_address(name, TEST_ADDRESS)
    assert is_same_address(await async_ens.address(name), TEST_ADDRESS)

    namehash = Web3.to_bytes(hexstr=HexStr(namehash_hex))
    normal_name = async_ens.nameprep(name)

    # check that the correct namehash is set:
    resolver = await async_ens.resolver(normal_name)
    assert is_same_address(await resolver.caller.addr(namehash), TEST_ADDRESS)

    # check that the correct owner is set:
    assert await async_ens.owner(name) == owner

    # teardown
    await async_ens.setup_address(name, None)
    assert await async_ens.address(name) is None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name, equivalent",
    SETUP_ADDRESS_EQUIVALENCE_TEST_CASES,
)
async def test_async_setup_address_equivalence(
    async_ens, name, equivalent, TEST_ADDRESS
):
    assert await async_ens.address(name) is None

    await async_ens.setup_address(name, TEST_ADDRESS)
    assert is_same_address(await async_ens.address(name), TEST_ADDRESS)
    assert is_same_address(await async_ens.address(equivalent), TEST_ADDRESS)

    # teardown
    await async_ens.setup_address(name, None)
    assert await async_ens.address(name) is None


@pytest.mark.asyncio
@pytest.mark.parametrize("setup_address", SETUP_ADDRESS_NOOP_TEST_CASES)
async def test_async_setup_address_noop(async_ens, setup_address):
    eth = async_ens.w3.eth
    owner = await async_ens.owner("tester.eth")
    await async_ens.setup_address("noop.tester.eth", setup_address)
    starting_transactions = await eth.get_transaction_count(owner)

    # do not issue transaction if address is already set
    await async_ens.setup_address("noop.tester.eth", setup_address)
    assert await eth.get_transaction_count(owner) == starting_transactions


@pytest.mark.asyncio
async def test_async_setup_address_unauthorized(async_ens, TEST_ADDRESS):
    with pytest.raises(UnauthorizedError):
        await async_ens.setup_address("eth", TEST_ADDRESS)


@pytest.mark.asyncio
async def test_async_setup_address_default_address_to_owner(async_ens):
    assert await async_ens.address("default.tester.eth") is None
    owner = await async_ens.owner("tester.eth")

    await async_ens.setup_address("default.tester.eth")
    assert await async_ens.address("default.tester.eth") == owner


@pytest.mark.asyncio
async def test_async_setup_address_default_to_owner_for_multichain_address_resolution(
    async_ens,
):
    await async_ens.setup_address("leet.tester.eth", coin_type=1337)

    # was never set up for ETH, so no address resolution expected
    assert await async_ens.address("leet.tester.eth") is None

    # assert resolves for ``coin_type == 1337``
    owner = await async_ens.owner("tester.eth")
    assert await async_ens.address("leet.tester.eth", coin_type=1337) == owner


@pytest.mark.asyncio
async def test_async_first_owner_upchain_identify(async_ens):
    # _first_owner should auto-select the name owner to send the transaction
    # from
    addr = "0x5B2063246F2191f18F2675ceDB8b28102e957458"

    async def mock_async_get_owner(name):
        return addr if name == "cdefghi.eth" else None

    with patch.object(async_ens, "owner", side_effect=mock_async_get_owner):
        assert await async_ens._first_owner("abcdefg.bcdefgh.cdefghi.eth") == (
            addr,
            ["abcdefg", "bcdefgh"],
            "cdefghi.eth",
        )


@pytest.mark.asyncio
async def test_async_setup_resolver_leave_default(async_ens, TEST_ADDRESS):
    owner = await async_ens.owner("tester.eth")
    await async_ens.setup_address("leave-default-resolver.tester.eth", TEST_ADDRESS)
    eth = async_ens.w3.eth
    num_transactions = await eth.get_transaction_count(owner)

    await async_ens.setup_address(
        "leave-default-resolver.tester.eth",
        "0x5B2063246F2191f18F2675ceDB8b28102e957458",
    )

    # should skip setting the owner and setting the default resolver, and only
    #   set the name in the default resolver to point to the new address
    assert await eth.get_transaction_count(owner) == num_transactions + 1
