# encoding: utf-8

from __future__ import unicode_literals

import pytest
import re
import sys

from eth_utils import (
    is_hex,
)

from hypothesis import (
    example,
    given,
    strategies as st,
)

from web3.utils.encoding import (
    hex_encode_abi_type,
    text_if_str,
    hexstr_if_str,
    to_bytes,
    to_decimal,
    to_hex,
)

# Several tests are split into py2 & py3 tests below, with py3 tests using Mock
if sys.version_info.major > 2:
    from unittest.mock import Mock

only_python2 = pytest.mark.skipif(
    sys.version_info.major > 2,
    reason="these test values only valid for py2"
)
only_python3 = pytest.mark.skipif(
    sys.version_info.major < 3,
    reason="these test values only valid for py3"
)

HEX_REGEX = re.compile('\A(0[xX])?[0-9a-fA-F]*\Z')


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, '0x1'),
        (15, '0xf'),
        (-1, '-0x1'),
        (-15, '-0xf'),
        (0, '0x0'),
        (-0, '0x0'),
    ]
)
def test_to_hex(value, expected):
    assert to_hex(value) == expected


@given(value=st.integers(min_value=-1 * 2**255 + 1, max_value=2**256 - 1))
def test_conversion_round_trip(value):
    intermediate_value = to_hex(value)
    result_value = to_decimal(hexstr=intermediate_value)
    error_msg = "Expected: {0!r}, Result: {1!r}, Intermediate: {2!r}".format(
        value,
        result_value,
        intermediate_value,
    )
    assert result_value == value, error_msg


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
        ("bytes2", b"T\x02", "0x5402" if sys.version_info[0] >= 3 else TypeError),
        ("bytes3", b"T\x02", "0x5402" if sys.version_info[0] >= 3 else TypeError),
        ("bytes", '0x5402', "0x5402"),
        ("bytes", '5402', TypeError),
        ("string", "testing a string!", "0x74657374696e67206120737472696e6721"),
        ("strings", "bad abi!", ValueError),
        ("bool[", True, ValueError),
        ("bool", "string", TypeError),
        ("uint24", -20, TypeError),
    ]
)
def test_hex_encode_abi_type(abi_type, value, expected):

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            hex_encode_abi_type(abi_type, value)
        return

    actual = hex_encode_abi_type(abi_type, value)
    assert actual == expected


@only_python2
@given(
    st.one_of(st.integers(min_value=0), st.booleans()),
    st.sampled_from((to_bytes, to_hex, to_decimal)),
)
def test_hexstr_if_str_passthrough_py2(val, converter):
    assert hexstr_if_str(converter, val) == converter(val)


@only_python2
@given(
    st.from_regex(HEX_REGEX),
    st.sampled_from((to_bytes, to_hex, to_decimal)),
)
def test_hexstr_if_str_valid_hex_py2(val, converter):
    if converter is to_decimal and to_bytes(hexstr=val) == b'':
        with pytest.raises(ValueError):
            hexstr_if_str(converter, val)
    else:
        assert hexstr_if_str(converter, val) == converter(hexstr=val)


@only_python2
@given(
    st.one_of(st.text(), st.binary()),
    st.sampled_from((to_bytes, to_hex, to_decimal)),
)
def test_hexstr_if_str_invalid_hex_py2(val, converter):
    try:
        is_hexstr = (is_hex(val) or val == '')
    except ValueError:
        is_hexstr = False

    if not is_hexstr:
        with pytest.raises(ValueError):
            hexstr_if_str(converter, val)


@only_python3
@given(st.one_of(st.integers(), st.booleans(), st.binary()))
@example(b'')
def test_hexstr_if_str_passthrough(val):
    to_type = Mock(return_value='zoot')
    assert hexstr_if_str(to_type, val) == 'zoot'
    assert to_type.call_args == ((val, ), {'hexstr': None})


@only_python3
@given(st.from_regex(HEX_REGEX))
@example('0x')
@example('0')
def test_hexstr_if_str_on_valid_hex(val):
    to_type = Mock(return_value='zoot')
    assert hexstr_if_str(to_type, val) == 'zoot'
    assert to_type.call_args == ((None, ), {'hexstr': val})


@only_python3
@given(st.text())
def test_hexstr_if_str_on_invalid_hex(val):
    try:
        is_hexstr = (is_hex(val) or val == '')
    except ValueError:
        is_hexstr = False

    if not is_hexstr:
        with pytest.raises(ValueError):
            hexstr_if_str(Mock(), val)


@only_python3
@given(st.one_of(st.integers(), st.booleans(), st.binary()))
@example(b'')
def test_text_if_str_passthrough(val):
    to_type = Mock(return_value='zoot')
    assert text_if_str(to_type, val) == 'zoot'
    assert to_type.call_args == ((val, ), {'text': None})


@only_python3
@given(st.text())
@example('0xa1')  # valid hexadecimal is still interpreted as unicode characters
def test_text_if_str_on_text(val):
    to_type = Mock(return_value='zoot')
    assert text_if_str(to_type, val) == 'zoot'
    assert to_type.call_args == ((None, ), {'text': val})


@only_python2
@given(
    st.one_of(st.integers(min_value=0), st.booleans(), st.binary()),
    st.sampled_from((to_bytes, to_hex)),
)
@example(b'', to_hex)
@example(b'\xff', to_bytes)  # bytes are passed through, no matter the text
def test_text_if_str_passthrough_py2(val, converter):
    if converter is to_decimal and to_bytes(val) == b'':
        with pytest.raises(ValueError):
            text_if_str(converter, val)
    else:
        assert text_if_str(converter, val) == converter(val)


@only_python2
@given(
    st.text(),
    st.sampled_from((to_bytes, to_hex)),
)
@example('0xa1', to_bytes)  # valid hexadecimal is still interpreted as unicode characters
def test_text_if_str_on_text_py2(val, converter):
    assert text_if_str(converter, val) == converter(text=val)


@only_python2
@given(st.from_regex('\A[0-9]+\Z'))
def test_text_if_str_on_text_to_decimal_py2(val):
    assert text_if_str(to_decimal, val) == to_decimal(text=val)
