from ast import (
    literal_eval,
)
import datetime
import pytest
from unittest.mock import (
    Mock,
)

from eth_utils import (
    is_hex,
)
from hypothesis import (
    example,
    given,
    strategies as st,
)

from web3.providers import (
    JSONBaseProvider,
)
from web3.utils.encoding import (
    FriendlyJsonSerde as FriendlyJson,
    hex_encode_abi_type,
    hexstr_if_str,
    text_if_str,
    to_hex,
    to_int,
)
from web3.utils.hypothesis import (
    hexstr_strategy,
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


@pytest.mark.parametrize(
    "py_obj, exc_type, expected",
    (
        (
            {
                'date': [
                    datetime.datetime(2018, 5, 10, 1, 5, 10).isoformat(),
                    datetime.datetime(2018, 5, 10, 1, 5, 10).isoformat(),
                ],
                'other_date': datetime.datetime(2018, 5, 10, 1, 5, 10).date().isoformat(),
            },
            None,
            '{"date": ["2018-05-10T01:05:10", "2018-05-10T01:05:10"], "other_date": "2018-05-10"}',
        ),
        (
            {
                'date': [datetime.datetime.utcnow(), datetime.datetime.now()],
                'other_date': datetime.datetime.utcnow().date(),
            },
            TypeError,
            "Could not encode to JSON: .*'other_date'.*is not JSON serializable",
        ),
    ),
)
def test_friendly_json_encode(py_obj, exc_type, expected):
    if exc_type is None:
        assert literal_eval(FriendlyJson().json_encode(py_obj)) == literal_eval(expected)
    else:
        with pytest.raises(exc_type, match=expected):
            FriendlyJson().json_encode(py_obj)


@pytest.mark.parametrize(
    "json_str, expected",
    (
        (
            '{"date": ["2018-05-10T01:05:10", "2018-05-10T01:05:10"],"other_date": "2018-05-10"}',
            dict,
        ),
    ),
)
def test_friendly_json_decode(json_str, expected):
    assert isinstance(FriendlyJson().json_decode(json_str), expected)


@pytest.mark.parametrize(
    "rpc_response, expected",
    (
        (
            '{"jsonrpc": "2.0", "method": "test_method", "params": [], "id": 1}',
            {"jsonrpc": "2.0", "method": "test_method", "params": [], "id": 1},
        ),
    ),
)
def test_decode_rpc_response(rpc_response, expected):
    assert JSONBaseProvider().decode_rpc_response(rpc_response.encode('utf8')) == expected


@pytest.mark.parametrize(
    "rpc_kwargs, exc_type, expected",
    (
        (
            {'id': 1, 'method': 'test', 'params': [], "jsonrpc": "2.0"},
            None,
            '{"id": 0, "method": "test", "params": [], "jsonrpc": "2.0",}',
        ),
        (
            {'id': 0, 'method': 'test', 'params': [datetime.datetime(2018, 5, 10, 1, 5, 10)]},
            TypeError,
            r"Could not encode to JSON: .*'params'.* is not JSON serializable",
        ),
    ),
)
def test_encode_rpc_request(rpc_kwargs, exc_type, expected):
    if exc_type is None:
        res = JSONBaseProvider().encode_rpc_request(
            rpc_kwargs['method'],
            rpc_kwargs['params']
        )
        assert literal_eval(res.decode('utf8')) == literal_eval(expected)
    else:
        with pytest.raises(exc_type, match=expected):
            JSONBaseProvider().encode_rpc_request(
                rpc_kwargs['method'],
                rpc_kwargs['params'],
            )
