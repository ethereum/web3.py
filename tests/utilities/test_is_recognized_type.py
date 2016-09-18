import pytest

from web3.utils.abi import is_recognized_type


@pytest.mark.parametrize(
    'abi_type,should_match',
    (
        ('uint', False),
        ('uint256', True),
        ('uint8', True),
        ('uint7', False),
        ('int', False),
        ('int256', True),
        ('int8', True),
        ('int7', False),
        ('byte', False),
        ('bytes1', True),
        ('bytes7', True),
        ('bytes32', True),
        ('bytes', True),
        ('string', True),
        ('address', True),
        ('uint256[]', True),
        ('uint256[][]', True),
        ('uint256[][][]', True),
        ('uint256[1][][3]', True),
        ('uint256[1][20000][3]', True),
        ('uint256[][20000][]', True),
        ('bytes20[]', True),
        ('bytes20[][]', True),
        ('bytes20[][][]', True),
        ('bytes20[1][][3]', True),
        ('bytes20[1][20000][3]', True),
        ('bytes20[][20000][]', True),
        ('address[]', True),
        ('address[][]', True),
        ('address[][][]', True),
        ('address[1][][3]', True),
        ('address[1][20000][3]', True),
        ('address[][20000][]', True),
        ('SomeEnum.SomeValue', False),
    ),
)
def test_is_recognized_type(abi_type, should_match):
    is_match = is_recognized_type(abi_type)
    assert is_match is should_match
