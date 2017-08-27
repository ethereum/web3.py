import pytest

from web3.utils.blocks import (
    is_predefined_block_number,
)


@pytest.mark.parametrize(
    'block_identifier,expected',
    (
        ('earliest', True),
        ('latest', True),
        ('pending', True),
        (1, False),
        ('0x1', False),
    ),
)
def test_is_predefined_block_number(block_identifier, expected):
    actual = is_predefined_block_number(block_identifier)
    assert actual is expected
