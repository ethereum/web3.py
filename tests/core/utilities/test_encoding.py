# encoding: utf-8

import pytest
from unittest.mock import Mock

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
    to_int,
    to_hex,
)

from web3.utils.hypothesis import (
    hexstr_strategy,
)

from web3.utils.encoding import (
    _encode_for_json,
    to_serial,
    to_json,
)

from web3.utils.datastructures import (
    HexBytes,
    AttributeDict,
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
    result_value = to_int(hexstr=intermediate_value)
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
        ("bytes2", b"T\x02", "0x5402"),
        ("bytes3", b"T\x02", "0x5402"),
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


@given(st.one_of(st.integers(), st.booleans(), st.binary()))
@example(b'')
def test_hexstr_if_str_passthrough(val):
    to_type = Mock(return_value='zoot')
    assert hexstr_if_str(to_type, val) == 'zoot'
    assert to_type.call_args == ((val, ), {'hexstr': None})


def test_hexstr_if_str_curried():
    converter = hexstr_if_str(to_hex)
    assert converter(255) == '0xff'


@given(hexstr_strategy())
@example('0x')
@example('0')
def test_hexstr_if_str_on_valid_hex(val):
    to_type = Mock(return_value='zoot')
    assert hexstr_if_str(to_type, val) == 'zoot'
    assert to_type.call_args == ((None, ), {'hexstr': val})


@given(st.text())
def test_hexstr_if_str_on_invalid_hex(val):
    try:
        is_hexstr = (is_hex(val) or val == '')
    except ValueError:
        is_hexstr = False

    if not is_hexstr:
        with pytest.raises(ValueError):
            hexstr_if_str(Mock(), val)


@given(st.one_of(st.integers(), st.booleans(), st.binary()))
@example(b'')
def test_text_if_str_passthrough(val):
    to_type = Mock(return_value='zoot')
    assert text_if_str(to_type, val) == 'zoot'
    assert to_type.call_args == ((val, ), {'text': None})


@given(st.text())
@example('0xa1')  # valid hexadecimal is still interpreted as unicode characters
def test_text_if_str_on_text(val):
    to_type = Mock(return_value='zoot')
    assert text_if_str(to_type, val) == 'zoot'
    assert to_type.call_args == ((None, ), {'text': val})


def test_encode_for_json():
    value = HexBytes(b'\x11')
    expected_output = value.hex()
    output = _encode_for_json(value)
    assert output == expected_output


def test_to_serialized():
    data = AttributeDict({'b': HexBytes(b'\x11')})
    expected_output = {"b": "0x11"}
    output = to_serial(data)
    assert output == expected_output


def test_recursive_serialized():
    data = AttributeDict({'a': {'b': HexBytes(b'\x11')}})
    expected_output = {"a": {"b": "0x11"}}
    output = to_serial(data)
    assert output == expected_output


def test_recursive_serialized_array():
    data = AttributeDict({'a': [{'b': HexBytes(b'\x11')}]})
    expected_output = {"a": [{"b": "0x11"}]}
    output = to_serial(data)
    assert output == expected_output


def test_to_json():
    data = AttributeDict({'b': HexBytes(b'\x11')})
    expected_output = '{"b": "0x11"}'
    output = to_json(data)
    assert output == expected_output


def test_recursive_json():
    data = AttributeDict({'a': {'b': HexBytes(b'\x11')}})
    expected_output = '{"a": {"b": "0x11"}}'
    output = to_json(data)
    assert output == expected_output


def test_recursive_json_array():
    data = AttributeDict({'a': [{'b': HexBytes(b'\x11')}]})
    expected_output = '{"a": [{"b": "0x11"}]}'
    output = to_json(data)
    assert output == expected_output
