import pytest

from web3._utils.abi import (
    is_address_type,
    is_array_type,
    is_bool_type,
    is_bytes_type,
    is_int_type,
    is_recognized_type,
    is_string_type,
    is_uint_type,
)


@pytest.mark.parametrize(
    "abi_type,should_match",
    (
        ("bool", True),
        ("uint", False),
        ("uint256", True),
        ("uint8", True),
        ("uint7", False),
        ("int", False),
        ("int256", True),
        ("int8", True),
        ("int7", False),
        ("byte", False),
        ("bytes1", True),
        ("bytes7", True),
        ("bytes32", True),
        ("bytes32.byte", True),
        ("bytes", True),
        ("string", True),
        ("address", True),
        ("uint256[]", True),
        ("uint256[][]", True),
        ("uint256[][][]", True),
        ("uint256[1][][3]", True),
        ("uint256[1][20000][3]", True),
        ("uint256[][20000][]", True),
        ("bytes20[]", True),
        ("bytes20[][]", True),
        ("bytes20[][][]", True),
        ("bytes20[1][][3]", True),
        ("bytes20[1][20000][3]", True),
        ("bytes20[][20000][]", True),
        ("address[]", True),
        ("address[][]", True),
        ("address[][][]", True),
        ("address[1][][3]", True),
        ("address[1][20000][3]", True),
        ("address[][20000][]", True),
        ("SomeEnum.SomeValue", False),
    ),
)
def test_is_recognized_type(abi_type, should_match):
    is_match = is_recognized_type(abi_type)
    assert is_match is should_match


@pytest.mark.parametrize(
    "abi_type,should_match",
    (
        ("bool", True),
        ("uint", False),
        ("sbool", False),
        ("bools", False),
    ),
)
def test_is_bool_type(abi_type, should_match):
    is_match = is_bool_type(abi_type)
    assert is_match is should_match


@pytest.mark.parametrize(
    "abi_type,should_match",
    (
        ("uint", False),
        ("uint32", True),
        ("uint255", False),
        ("uint256", True),
        ("uint0", False),
        ("int", False),
        ("int16", False),
        ("suint", False),
        ("uints", False),
    ),
)
def test_is_uint_type(abi_type, should_match):
    is_match = is_uint_type(abi_type)
    assert is_match is should_match


@pytest.mark.parametrize(
    "abi_type,should_match",
    (
        ("int", False),
        ("int32", True),
        ("int255", False),
        ("int256", True),
        ("int0", False),
        ("uint", False),
        ("uint16", False),
        ("sint", False),
        ("ints", False),
    ),
)
def test_is_int_type(abi_type, should_match):
    is_match = is_int_type(abi_type)
    assert is_match is should_match


@pytest.mark.parametrize(
    "abi_type,should_match",
    (
        ("address", True),
        ("uint", False),
        ("saddress", False),
        ("addresss", False),
    ),
)
def test_is_address_type(abi_type, should_match):
    is_match = is_address_type(abi_type)
    assert is_match is should_match


@pytest.mark.parametrize(
    "abi_type,should_match",
    (
        ("bytes", True),
        ("bytes4", True),
        ("bytes32.byte", True),
        ("sbyte", False),
        ("bytess", False),
        ("byte", False),
        ("byte0", False),
        ("bytes33", False),
        ("bytes32..byte", False),
        ("bytes32mbyte", False),
        ("bytes32byte", False),
    ),
)
def test_is_bytes_type(abi_type, should_match):
    is_match = is_bytes_type(abi_type)
    assert is_match is should_match


@pytest.mark.parametrize(
    "abi_type,should_match",
    (
        ("string", True),
        ("uint", False),
        ("sstring", False),
        ("strings", False),
    ),
)
def test_is_string_type(abi_type, should_match):
    is_match = is_string_type(abi_type)
    assert is_match is should_match


@pytest.mark.parametrize(
    "abi_type,should_match",
    (
        ("bool[]", True),
        ("uint[]", True),
        ("uint[][]", True),
        ("uint[5][]", True),
        ("uint[][5]", True),
        ("int[]", True),
        ("string[]", True),
        ("address[]", True),
        ("bytes[]", True),
        ("string", False),
        ("bytes", False),
        ("uint[", False),
        ("uint]", False),
    ),
)
def test_is_array_type(abi_type, should_match):
    is_match = is_array_type(abi_type)
    assert is_match is should_match
