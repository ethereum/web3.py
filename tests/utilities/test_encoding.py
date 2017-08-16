import pytest
import sys

from hypothesis import (
    given,
    strategies as st,
)

from web3.utils.encoding import (
    from_decimal,
    hex_encode_abi_type,
    to_decimal,
    to_hex,
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


def test_bytes_that_start_with_0x():
    sneaky_bytes = b'0x\xde\xad'
    assert to_hex(sneaky_bytes) == '0x3078dead'


@pytest.mark.parametrize(
    "abi_type,value,expected",
    [
        ('bool', True, "0x01"),
        ('bool', False, "0x00"),
        ('uint16', 8, "0x0008"),
        ('int16', 8, "0x0008"),
        ('int16', -8, "0xfff8"),
        (
            'address',
            "0x00360d2b7D240Ec0643B6D819ba81A09e40E5bCd",
            "0x00360d2b7D240Ec0643B6D819ba81A09e40E5bCd"
        ),
        ("bytes2", b"T\x02", "0x5402"),
        ("bytes3", b"T\x02", "0x5402"),
        ("bytes", '0x5402' if sys.version_info[0] >= 3 else b'T\x02', "0x5402"),
        ("string", "testing a string!", "0x74657374696e67206120737472696e6721"),
    ]
)
def test_hex_encode_abi_type(abi_type, value, expected):
    actual = hex_encode_abi_type(abi_type, value)
    assert actual == expected
