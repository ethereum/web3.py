
from unittest.mock import patch
import pytest

from web3 import Web3
from web3.exceptions import StaleBlockchain

from ens import ENS

NAME_HASHES = [
    ('öbb.eth', '2774094517aaa884fc7183cf681150529b9acc7c9e7b71cf3a470200135a20b4'),
    # handles alternative dot separators
    ('öbb．eth', '2774094517aaa884fc7183cf681150529b9acc7c9e7b71cf3a470200135a20b4'),
    ('öbb。eth', '2774094517aaa884fc7183cf681150529b9acc7c9e7b71cf3a470200135a20b4'),
    ('öbb｡eth', '2774094517aaa884fc7183cf681150529b9acc7c9e7b71cf3a470200135a20b4'),
    # presumes a .eth ending if tld is not recognized
    ('öbb', '2774094517aaa884fc7183cf681150529b9acc7c9e7b71cf3a470200135a20b4'),
    # namehash prepares name (to lower case, etc)
    ('Öbb', '2774094517aaa884fc7183cf681150529b9acc7c9e7b71cf3a470200135a20b4'),
    # handles subdomains correctly
    ('flying.circus.eth', 'f55bac2e53e0b47ee3a29324e114fc0996e651542abff256fa1daab5a68f1ff6'),
]


@pytest.mark.parametrize(
    'name, expected_hash',
    NAME_HASHES,
)
def test_namehash_result(name, expected_hash):
    namehash = ENS.namehash(name)
    assert isinstance(namehash, bytes)
    assert namehash.hex() == expected_hash


@pytest.mark.parametrize(
    'name, expected_hash',
    NAME_HASHES,
)
def test_resolver(ens, mocker, name, expected_hash, addr1):
    mocker.patch.object(ens.ens, 'resolver', return_value=addr1)
    ens.resolver(name)
    ens.ens.resolver.assert_called_once_with(Web3.toBytes(hexstr=expected_hash))


def test_resolver_empty(ens):
    with patch.object(ens.ens, 'resolver', return_value=None):
        assert ens.resolver('') is None


@pytest.mark.parametrize(
    "name, expected_hash",
    NAME_HASHES,
)
def test_address_uses_correct_namehash(ens, mocker, name, expected_hash):
    '''
    Using namehash is required, to expand from label to full name
    '''
    resolver = mocker.patch.object(ens.ens, 'resolver')
    mocker.patch.object(ens, '_resolverContract')
    ens.address(name)
    assert resolver.call_count == 1
    resolver.assert_called_once_with(Web3.toBytes(hexstr=expected_hash))


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
    "name, expected_hash",
    NAME_HASHES,
)
def test_owner_passthrough_namehash_result(ens, mocker, name, expected_hash):
    owner = mocker.patch.object(ens.ens, 'owner')
    ens.owner(name)
    owner.assert_called_once_with(Web3.toBytes(hexstr=expected_hash))


def test_owner_stale(ens, mocker):
    mocker.patch('web3.middleware.stalecheck._isfresh', return_value=False)
    with pytest.raises(StaleBlockchain):
        ens.owner('')


def test_labelhash(ens):
    labelhash = ens.labelhash('eth')
    assert type(labelhash) == bytes
    hash_hex = Web3.toHex(labelhash)
    assert hash_hex == '0x4f5b812789fc606be1b3b16908db13fc7a9adf7ca72641f84d75b47069d3d7f0'
