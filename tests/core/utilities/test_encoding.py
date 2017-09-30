# encoding: utf-8

from __future__ import unicode_literals

import pytest
import string
import sys

from hypothesis import (
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


@pytest.mark.skipif(sys.version_info.major < 3, reason="these test values only valid for py3")
@pytest.mark.parametrize(
    "val, expected",
    (
        (
            0,
            ((0, ), {'hexstr': None}),
        ),
        (
            'g',
            TypeError,
        ),
        (
            string.hexdigits,
            ((None, ), {'hexstr': string.hexdigits}),
        ),
        (
            '0x' + string.hexdigits,
            ((None, ), {'hexstr': '0x' + string.hexdigits}),
        ),
        (
            b'',
            ((b'', ), {'hexstr': None}),
        ),
        (
            'mö'.encode('utf8'),
            (('mö'.encode('utf8'), ), {'hexstr': None}),
        ),
        (
            0x123,
            ((0x123, ), {'hexstr': None}),
        ),
        (
            True,
            ((True, ), {'hexstr': None}),
        ),
        (
            False,
            ((False, ), {'hexstr': None}),
        ),
    ),
)
def test_hexstr_if_str_conversion(val, expected):
    from unittest.mock import Mock
    to_type = Mock(return_value='zoot')
    if type(expected) == type and issubclass(expected, BaseException):
        with pytest.raises(expected):
            hexstr_if_str(to_type, val)
    else:
        assert hexstr_if_str(to_type, val) == 'zoot'
        assert to_type.call_args == expected


@pytest.mark.skipif(sys.version_info.major >= 3, reason="these test values only valid for py2")
@pytest.mark.parametrize(
    "val, expected",
    (
        (
            0,
            b'\x00',
        ),
        (
            'g',
            TypeError,
        ),
        (
            string.hexdigits,
            b'\x01#Eg\x89\xab\xcd\xef\xab\xcd\xef',
        ),
        (
            # unicode
            '0x0123456789abcdefABCDEF',
            b'\x01#Eg\x89\xab\xcd\xef\xab\xcd\xef',
        ),
        (
            # bytes, aka str
            b'0x0123456789abcdefABCDEF',
            b'\x01#Eg\x89\xab\xcd\xef\xab\xcd\xef',
        ),
        (
            # bytes with invalid hex characters
            b'\x01#Eg\x89\xab\xcd\xef\xab\xcd\xef',
            TypeError,
        ),
        (
            b'',
            b'',
        ),
        (
            'mö'.encode('utf8'),
            TypeError,
        ),
        (
            0x123,
            b'\x01\x23',
        ),
        (
            True,
            b'\x01',
        ),
        (
            False,
            b'\x00',
        ),
    ),
)
def test_hexstr_if_str_conversion_py2(val, expected):
    if type(expected) == type and issubclass(expected, BaseException):
        with pytest.raises(expected):
            hexstr_if_str(to_bytes, val)
    else:
        assert hexstr_if_str(to_bytes, val) == expected


@pytest.mark.skipif(sys.version_info.major < 3, reason="these test values only valid for py3")
@pytest.mark.parametrize(
    "val, expected",
    (
        (
            0,
            ((0, ), {'text': None}),
        ),
        (
            string.hexdigits,
            ((None, ), {'text': string.hexdigits}),
        ),
        (
            '0x' + string.hexdigits,
            ((None, ), {'text': '0x' + string.hexdigits}),
        ),
        (
            b'',
            ((b'', ), {'text': None}),
        ),
        (
            'mö',
            ((None, ), {'text': 'mö'}),
        ),
        (
            'mö'.encode('utf8'),
            (('mö'.encode('utf8'), ), {'text': None}),
        ),
        (
            0x123,
            ((0x123, ), {'text': None}),
        ),
        (
            True,
            ((True, ), {'text': None}),
        ),
        (
            False,
            ((False, ), {'text': None}),
        ),
    ),
)
def test_text_if_str_conversion(val, expected):
    from unittest.mock import Mock
    to_type = Mock(return_value='zoot')
    assert text_if_str(to_type, val) == 'zoot'
    assert to_type.call_args == expected


@pytest.mark.skipif(sys.version_info.major >= 3, reason="these test values only valid for py2")
@pytest.mark.parametrize(
    "val, expected",
    (
        (
            0,
            b'\x00',
        ),
        (
            string.hexdigits,
            string.hexdigits,
        ),
        (
            b'0x0123456789abcdefABCDEF',
            b'0x0123456789abcdefABCDEF',
        ),
        (
            b'',
            b'',
        ),
        (
            # unicode point of ascii \xff char
            # just... don't. But in case you do, here's what happens:
            u'\xff',
            # utf-8 encoding of char decoded by ascii \xff
            b'\xc3\xbf',
        ),
        (
            # unicode
            'mö',
            b'm\xc3\xb6',
        ),
        (
            # bytes
            'mö'.encode('utf8'),
            b'm\xc3\xb6',
        ),
        (
            0x123,
            b'\x01\x23',
        ),
        (
            True,
            b'\x01',
        ),
        (
            False,
            b'\x00',
        ),
    ),
)
def test_text_if_str_conversion_py2(val, expected):
    assert text_if_str(to_bytes, val) == expected
