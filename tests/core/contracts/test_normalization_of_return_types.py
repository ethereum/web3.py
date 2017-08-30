import pytest
import sys

from web3.utils.abi import normalize_return_type

if sys.version_info.major >= 3:
    from unittest.mock import Mock

EMPTY_ADDR = '00' * 20


def empty_to_none(val, base, sub, arr):
    if base == 'address' and not arr and int(val, base=16) == 0:
        return None
    else:
        return val


@pytest.mark.parametrize(
    'data_type,data_value,expected_value',
    (
        (
            'bytes32',
            'arst\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',  # noqa: E501
            'arst\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',  # noqa: E501
        ),
        (
            'address',
            'd3cda913deb6f67967b99d67acdfa1712c293601',
            '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        ),
        (
            'address[]',
            [
                'd3cda913deb6f67967b99d67acdfa1712c293601',
                'bb9bc244d798123fde783fcc1c72d3bb8c189413',
            ],
            [
                '0xd3cda913deb6f67967b99d67acdfa1712c293601',
                '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
            ],
        ),
    ),
    ids=['nullbyte', 'soloaddr', 'addrlist']

)
def test_normalizing_return_values(data_type, data_value, expected_value):
    actual_value = normalize_return_type(data_type, data_value)
    assert actual_value == expected_value


@pytest.mark.skipif(sys.version_info.major < 3, reason="mock requires py3")
@pytest.mark.parametrize(
    'addr, customizer, expected',
    [
        (EMPTY_ADDR, None, '0x' + EMPTY_ADDR),
        (EMPTY_ADDR, lambda val, base, sub, lst: val, '0x' + EMPTY_ADDR),
        (EMPTY_ADDR, lambda val, base, sub, lst: None, None),
    ]
)
def test_normalize_custom(addr, customizer, expected):
    if customizer:
        customizer = Mock(wraps=customizer)
    assert normalize_return_type('address', addr, custom_normalizer=customizer) == expected
    if customizer:
        customizer.assert_called_once_with('0x' + addr, 'address', '', [])


@pytest.mark.parametrize(
    'addr, customizer, expected',
    [
        (
            [
                'bb9bc244d798123fde783fcc1c72d3bb8c189413',
                EMPTY_ADDR,
            ],
            empty_to_none,
            [
                '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
                None,
            ],
        ),
        (
            [
                EMPTY_ADDR,
                EMPTY_ADDR,
            ],
            empty_to_none,
            [
                None,
                None,
            ],
        ),
    ]
)
def test_normalize_custom_array(addr, customizer, expected):
    assert normalize_return_type('address[]', addr, custom_normalizer=customizer) == expected
