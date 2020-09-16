import pytest

from ethpm._utils.chains import (
    is_BIP122_block_uri,
    is_supported_chain_id,
    parse_BIP122_uri,
)

HASH_A = "0x1234567890123456789012345678901234567890123456789012345678901234"
HASH_A_NO_PREFIX = "1234567890123456789012345678901234567890123456789012345678901234"
HASH_B = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
HASH_B_NO_PREFIX = "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
BLOCK_URI = f"blockchain://{HASH_A_NO_PREFIX}/block/{HASH_B_NO_PREFIX}"
TRANSACTION_URI = f"blockchain://{HASH_A_NO_PREFIX}/transaction/{HASH_B_NO_PREFIX}"


@pytest.mark.parametrize(
    "value,expected",
    (
        (BLOCK_URI, True),
        (TRANSACTION_URI, False),
        (f"blockchain://{HASH_A}/block/{HASH_B_NO_PREFIX}", False),
        (f"blockchain://{HASH_A_NO_PREFIX}/block/{HASH_B}", False),
        (f"blockchain://{HASH_A}/block/{HASH_B_NO_PREFIX}", False),
        (f"blockchain://{HASH_A_NO_PREFIX[:-1]}/block/{HASH_B_NO_PREFIX}", False),
        (f"blockchain://{HASH_A_NO_PREFIX}/block/{HASH_B_NO_PREFIX[:-1]}", False),
    ),
)
def test_is_BIP122_block_uri(value, expected):
    actual = is_BIP122_block_uri(value)
    assert actual is expected


@pytest.mark.parametrize(
    "value, expected_resource_type",
    ((TRANSACTION_URI, "transaction"), (BLOCK_URI, "block")),
)
def test_parse_BIP122_uri(value, expected_resource_type):
    chain_id, resource_type, resource_identifier = parse_BIP122_uri(value)
    assert chain_id == HASH_A
    assert resource_type == expected_resource_type
    assert resource_identifier == HASH_B


@pytest.mark.parametrize(
    "chain_id,expected",
    (
        (1, True),
        (3, True),
        (4, True),
        (5, True),
        (42, True),
        (2, False),
        ("1", False),
        ({}, False),
        (None, False),
        (False, False),
    )
)
def test_is_supported_chain_id(chain_id, expected):
    actual = is_supported_chain_id(chain_id)
    assert actual is expected
