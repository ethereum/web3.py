import pytest

from web3.utils.filters import (
    construct_data_filter_regex,
)


def hex_and_pad(*i):
    return '0x' + ''.join(
        hex(v).rstrip('L')[2:].zfill(64)
        for v in i
    )


SINGLE_VALUE = [
    [hex_and_pad(1)],
]
TWO_VALUES = [
    [hex_and_pad(12345), hex_and_pad(54321)],
]
TWO_VALUES_WITH_WILDCARD = [
    [hex_and_pad(12345), None],
]
THREE_VALUES_WITH_WILDCARD = [
    [hex_and_pad(12345), None, hex_and_pad(54321)],
]
MULTI_VALUE = [
    [hex_and_pad(1)],
    [hex_and_pad(2)],
]
MULTI_NESTED_VALUE = [
    [hex_and_pad(1, 2)],
    [hex_and_pad(2, 1)],
]
MULTI_NESTED_VALUE_WITH_WILDCARD = [
    [hex_and_pad(1), None],
    [hex_and_pad(2, 1)],
]


@pytest.mark.parametrize(
    "filter_set,data_value,should_match",
    (
        (SINGLE_VALUE, hex_and_pad(1), True),
        (SINGLE_VALUE, hex_and_pad(0), False),
        (SINGLE_VALUE, hex_and_pad(2), False),
        (TWO_VALUES, hex_and_pad(12345, 54321), True),
        (TWO_VALUES_WITH_WILDCARD, hex_and_pad(12345, 54321), True),
        (TWO_VALUES_WITH_WILDCARD, hex_and_pad(12345, 1), True),
        (TWO_VALUES_WITH_WILDCARD, hex_and_pad(1, 1), False),
        (THREE_VALUES_WITH_WILDCARD, hex_and_pad(12345, 0, 54321), True),
        (THREE_VALUES_WITH_WILDCARD, hex_and_pad(12345, 1, 54321), True),
        (THREE_VALUES_WITH_WILDCARD, hex_and_pad(12345, 2**256 - 1, 54321), True),
        (THREE_VALUES_WITH_WILDCARD, hex_and_pad(12344, 0, 54321), False),
        (MULTI_VALUE, hex_and_pad(1), True),
        (MULTI_VALUE, hex_and_pad(2), True),
        (MULTI_VALUE, hex_and_pad(3), False),
        (MULTI_VALUE, hex_and_pad(1, 2), True),
        (MULTI_VALUE, hex_and_pad(2, 1), False),
        (MULTI_NESTED_VALUE_WITH_WILDCARD, hex_and_pad(1, 1), True),
        (MULTI_NESTED_VALUE_WITH_WILDCARD, hex_and_pad(1, 12345), True),
        (MULTI_NESTED_VALUE_WITH_WILDCARD, hex_and_pad(2, 1), True),
        (MULTI_NESTED_VALUE_WITH_WILDCARD, hex_and_pad(2, 12345), False),
    )
)
def test_construct_data_filter_regex(filter_set, data_value, should_match):
    data_filter_regex = construct_data_filter_regex(filter_set)
    is_match = bool(data_filter_regex.match(data_value))
    assert is_match is should_match, data_filter_regex
