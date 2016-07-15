import pytest

from hypothesis import (
    given,
    strategies as st,
)

from web3.utils.encoding import (
    encode_hex,
    from_decimal,
    to_decimal,
)


@pytest.mark.parametrize(
    "value,expected",
    [
        ('myString', b'0x6d79537472696e67'),
        ('myString\x00', b'0x6d79537472696e6700'),
    ]
)
def test_encode_hex(value, expected):
    assert encode_hex(value) == expected


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
    assert result_value == value
