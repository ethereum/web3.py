import pytest

from eth_abi import encode_single
from web3.utils.abi import normalize_return_type


@pytest.mark.parametrize(
    'data_type,data_value,expected_value',
    (
        (
            'bytes32',
            'arst\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            'arst\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
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
    )
)
def test_normalizing_return_values(data_type, data_value, expected_value):
    actual_value = normalize_return_type(data_type, data_value)
    assert actual_value == expected_value
