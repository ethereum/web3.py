import pytest

from web3.utils.abi import (
    is_encodable,
)


@pytest.mark.parametrize(
    'value,_type,expected',
    (
        # bytes
        (0, 'bytes32', False),
        ('123', 'bytes2', False),
        (True, 'bytes32', False),
        # int
        (-1 * 2**255, 'int256', False),
        (-1 * 2**255 + 1, 'int256', True),
        (-1, 'int256', True),
        (0, 'int256', True),
        (1, 'int256', True),
        (2**255 - 1, 'int256', True),
        (2**255, 'int256', False),
        ('abc', 'int256', False),
        (True, 'int256', False),
        # uint
        (-1, 'uint256', False),
        (0, 'uint256', True),
        (1, 'uint256', True),
        (2**256 - 1, 'uint256', True),
        (2**256, 'uint256', False),
        ('abc', 'uint256', False),
        (True, 'uint256', False),
    ),
)
def test_is_encodable(value, _type, expected):
    actual = is_encodable(_type, value)
    assert actual is expected
