import pytest

from web3._utils.abi import (
    is_probably_enum,
)


@pytest.mark.parametrize(
    "abi_type,should_match",
    (
        ("SomeEnum.SomeValue", True),
        ("Some_Enum.Some_Value", True),
        ("SomeEnum.someValue", True),
        ("SomeEnum.some_value", True),
        ("__SomeEnum__.some_value", True),
        ("__SomeEnum__.__some_value__", True),
        ("SomeEnum.__some_value__", True),
        ("uint256", False),
    ),
)
def test_is_probably_enum(abi_type, should_match):
    is_match = is_probably_enum(abi_type)
    assert is_match is should_match
