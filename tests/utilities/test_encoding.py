import pytest

from hypothesis import (
    given,
    strategies as st,
)

from web3.utils.encoding import (
    from_decimal,
    to_decimal,
)


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, '0x1'),
        ('1', '0x1'),
        (15, '0xf'),
        ('15', '0xf'),
        (-1, '-0x1'),
        ('-1', '-0x1'),
        (-15, '-0xf'),
        ('-15', '-0xf'),
        (0, '0x0'),
        ('0', '0x0'),
        (-0, '0x0'),
        ('-0', '0x0'),
        ("0x0", "0x0"),
        ("-0x0", "0x0"),
        ("0x5", "0x5"),
    ]
)
def test_from_decimal(value, expected):
    assert from_decimal(value) == expected


@given(value=st.integers(min_value=-1 * 2**255 + 1, max_value=2**256 - 1))
def test_conversion_rount_trip(value):
    intermediate_value = from_decimal(value)
    result_value = to_decimal(intermediate_value)
    assert result_value == value, "Expected: {0!r}, Result: {1!r}, Intermediate: {2!r}".format(value, result_value, intermediate_value)
