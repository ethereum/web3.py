import pytest

from eth_tester.exceptions import (
    TransactionFailed,
)

from ens.exceptions import (
    ResolverNotFound,
    UnsupportedFunction,
)
from web3 import Web3


@pytest.mark.parametrize(
    "key,expected",
    (
        ("avatar", "tester.jpeg"),
        ("email", "user@example.com"),
        ("url", "http://example.com"),
        ("description", "a test"),
        ("notice", "this contract is a test contract"),
    ),
)
def test_set_text_resolver_not_found(ens, key, expected):
    with pytest.raises(ResolverNotFound):
        ens.set_text("tld", key, expected)


def test_set_text_fails_with_bad_address(ens):
    address = ens.w3.eth.accounts[2]
    ens.setup_address("tester.eth", address)
    zero_address = "0x" + "00" * 20
    with pytest.raises(TransactionFailed):
        ens.set_text(
            "tester.eth", "url", "http://example.com", transact={"from": zero_address}
        )


def test_set_text_pass_in_transaction_dict(ens):
    address = ens.w3.eth.accounts[2]
    ens.setup_address("tester.eth", address)
    ens.set_text("tester.eth", "url", "http://example.com", transact={"from": address})
    ens.set_text(
        "tester.eth",
        "avatar",
        "example.jpeg",
        transact={
            "maxFeePerGas": Web3.toWei(100, "gwei"),
            "maxPriorityFeePerGas": Web3.toWei(100, "gwei"),
        },
    )
    assert ens.get_text("tester.eth", "url") == "http://example.com"
    assert ens.get_text("tester.eth", "avatar") == "example.jpeg"

    # teardown
    ens.setup_address("tester.eth", None)


@pytest.mark.parametrize(
    "key,expected",
    (
        ("avatar", "tester.jpeg"),
        ("email", "user@example.com"),
        ("url", "http://example.com"),
        ("description", "a test"),
        ("notice", "this contract is a test contract"),
    ),
)
def test_get_text(ens, key, expected):
    address = ens.w3.eth.accounts[2]
    ens.setup_address("tester.eth", address)
    owner = ens.owner("tester.eth")
    assert address == owner
    ens.set_text("tester.eth", key, expected)
    assert ens.get_text("tester.eth", key) == expected

    # teardown
    ens.setup_address("tester.eth", None)


def test_get_text_resolver_not_found(ens):
    with pytest.raises(ResolverNotFound):
        ens.get_text("tld", "any_key")


def test_get_text_for_resolver_with_unsupported_function(ens):
    with pytest.raises(UnsupportedFunction, match="does not support `text` function"):
        ens.get_text("simple-resolver.eth", "any_key")


@pytest.mark.asyncio
async def test_async_get_text(async_ens):
    acoounts = await async_ens.w3.eth.accounts
    address = acoounts[2]
    await async_ens.setup_address("tester.eth", address)
    await async_ens.set_text("tester.eth", "test", "123")
    text = await async_ens.get_text("tester.eth", "test")
    assert text == "123"
