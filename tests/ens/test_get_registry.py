
import pytest
from unittest.mock import (
    patch,
)

from ens import ENS
from web3 import Web3


def test_resolver_empty(ens):
    with patch.object(ens.ens, 'resolver', return_value=None):
        assert ens.resolver('') is None


@pytest.mark.parametrize(
    'address, expected_reverse',
    [
        (
            '0x1111111111111111111111111111111111111111',
            '1111111111111111111111111111111111111111.addr.reverse',
        ),
        (
            '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413',
            'bb9bc244d798123fde783fcc1c72d3bb8c189413.addr.reverse',
        ),
    ],
)
def test_reverse_domain(address, expected_reverse, address_conversion_func):
    address = address_conversion_func(address)
    assert ENS.reverse_domain(address) == expected_reverse


@pytest.mark.parametrize(
    'label, expected_hash',
    [
        ('eth', '0x4f5b812789fc606be1b3b16908db13fc7a9adf7ca72641f84d75b47069d3d7f0'),
        ('ETH', '0x4f5b812789fc606be1b3b16908db13fc7a9adf7ca72641f84d75b47069d3d7f0'),
        ('a.b', ValueError),
    ],
)
def test_labelhash(ens, label, expected_hash):
    if isinstance(expected_hash, type):
        with pytest.raises(expected_hash):
            ens.labelhash(label)
    else:
        labelhash = ens.labelhash(label)
        assert isinstance(labelhash, bytes)
        hash_hex = Web3.toHex(labelhash)
        assert hash_hex == expected_hash
