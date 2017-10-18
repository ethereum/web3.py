
from unittest.mock import patch
import pytest

from web3 import Web3
from web3.exceptions import StaleBlockchain

from ens import ENS


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
            '1111111111111111111111111111111111111111',
            '1111111111111111111111111111111111111111.addr.reverse',
        ),
        (
            0x1111111111111111111111111111111111111111,
            '1111111111111111111111111111111111111111.addr.reverse',
        ),
        (
            b'\x11' * 20,
            '1111111111111111111111111111111111111111.addr.reverse',
        ),
        (
            '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413',
            'bb9bc244d798123fde783fcc1c72d3bb8c189413.addr.reverse',
        ),
    ],
)
def test_reverse_domain(address, expected_reverse):
    assert ENS.reverse_domain(address) == expected_reverse


def test_reverser_lookup(ens, addr1, hash1):
    with patch.object(ens, 'resolver', return_value=hash1):
        assert ens.reverser(addr1) == hash1
        ens.resolver.assert_called_once_with(ens.reverse_domain(addr1))


def test_reverse(ens, mocker, name1, name2):
    # TODO test set and get reverse resolution
    pass


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
        assert type(labelhash) == bytes
        hash_hex = Web3.toHex(labelhash)
        assert hash_hex == expected_hash
