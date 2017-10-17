
from unittest.mock import patch, MagicMock
import pytest

from web3 import Web3
from web3.exceptions import StaleBlockchain

from ens import ENS


@pytest.mark.parametrize(
    'name, expected',
    [
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
    ],
)
def test_namehash_result(name, expected):
    namehash = ENS.namehash(name)
    assert isinstance(namehash, bytes)
    assert namehash.hex() == expected


def test_resolver(ens, mocker, hash1, addr1):
    mocker.patch.object(ens, 'namehash', return_value=hash1)
    mocker.patch.object(ens.ens, 'resolver', return_value=addr1)
    assert ens.resolver('')._classic_contract.address == addr1
    ens.ens.resolver.assert_called_once_with(hash1)


def test_resolver_empty(ens):
    with patch.object(ens.ens, 'resolver', return_value=None):
        assert ens.resolver('') is None


@pytest.mark.parametrize("address_content", [1, 'a'])
def test_address(ens, mocker, hash1, address_content, hash_maker):
    '''
    Using namehash is required, to expand from label to full name
    '''
    address = hash_maker(address_content)
    mocker.patch.object(ens, 'namehash', return_value=hash1)
    resolver = MagicMock()
    resolver.addr.return_value = address
    mocker.patch.object(ens, 'resolver', return_value=resolver)
    assert ens.address('eth') == Web3.toChecksumAddress(address)
    ens.namehash.assert_called_once_with('eth')
    resolver.addr.assert_called_once_with(hash1)


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
    mocker.patch.object(ens, 'reverse_domain', return_value=name1)
    mocker.patch.object(ens, 'resolve', return_value=name2)
    assert ens.name('') == name2
    assert ens.reverse == ens.name
    ens.resolve.assert_called_once_with(name1, get='name')


def test_owner_expand_name_with_namehash(ens, mocker):
    mocker.patch.object(ens, 'namehash')
    mocker.patch.object(ens.ens, 'owner')
    ens.owner('different')
    ens.namehash.assert_called_once_with('different')


def test_owner_passthrough_namehash_result(ens, mocker, hash1):
    mocker.patch.object(ens, 'namehash', return_value=hash1)
    mocker.patch.object(ens.ens, 'owner')
    ens.owner('')
    ens.ens.owner.assert_called_once_with(hash1)


def test_owner_stale(ens, mocker):
    mocker.patch('web3.middleware.stalecheck._isfresh', return_value=False)
    with pytest.raises(StaleBlockchain):
        ens.owner('')


def test_labelhash(ens):
    labelhash = ens.labelhash('eth')
    assert type(labelhash) == bytes
    hash_hex = Web3.toHex(labelhash)
    assert hash_hex == '0x4f5b812789fc606be1b3b16908db13fc7a9adf7ca72641f84d75b47069d3d7f0'
