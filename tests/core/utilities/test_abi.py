
import pytest

from eth_abi.abi import (
    process_type,
)

from web3.utils.abi import (
    collapse_type,
)


@pytest.mark.parametrize(
    'original, expected',
    [
        ('address', 'address'),
        # ('uint[2][]', 'uint256[2][]'),  # pending an eth_abi pull request
        ('uint256[2][]', 'uint256[2][]'),
        ('function', 'bytes24'),
        ('bool', 'bool'),
        ('bytes32', 'bytes32'),
        ('bytes', 'bytes'),
        ('string', 'string'),
    ],
)
def test_collapse_type(original, expected):
    assert collapse_type(*process_type(original)) == expected
