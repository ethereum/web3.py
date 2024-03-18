import pytest

from eth_utils.toolz import (
    partial,
)

from web3._utils.blocks import (
    select_method_for_block_identifier,
)
from web3.exceptions import (
    Web3ValueError,
)

selector_fn = partial(
    select_method_for_block_identifier,
    if_hash="test_hash",
    if_number="test_number",
    if_predefined="test_predefined",
)


@pytest.mark.parametrize(
    "input,expected",
    (
        ("latest", "test_predefined"),
        ("pending", "test_predefined"),
        ("earliest", "test_predefined"),
        ("safe", "test_predefined"),
        ("finalized", "test_predefined"),
        (-1, Web3ValueError),
        (0, "test_number"),
        (1, "test_number"),
        (4000000, "test_number"),
        ("0x0", "test_number"),
        ("0x00", "test_number"),
        ("0x1", "test_number"),
        ("0x01", "test_number"),
        (hex(4000000), "test_number"),
        ("0x" + "".zfill(64), "test_hash"),
    ),
)
def test_select_method_for_block_identifier(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            selector_fn(input)
    else:
        actual = selector_fn(input)
        assert actual == expected
