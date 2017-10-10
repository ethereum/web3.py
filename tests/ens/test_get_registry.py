
from unittest.mock import patch, MagicMock
import pytest

from web3 import Web3
from web3.exceptions import StaleBlockchain

from ens.constants import EMPTY_SHA3_BYTES


def test_namehash_three_labels(ens, mocker, fake_hash, fake_hash_hexout):
    mocker.patch('web3.Web3.sha3', side_effect=fake_hash_hexout)
    namehash = ens.namehash('grail.seeker.eth')
    assert namehash == fake_hash(
        fake_hash(
            fake_hash(
                EMPTY_SHA3_BYTES +
                fake_hash(b'eth')
            ) +
            fake_hash(b'seeker')
        ) +
        fake_hash(b'grail')
    )


def test_namehash_nameprep(ens, mocker, fake_hash, fake_hash_hexout):
    mocker.patch('web3.Web3.sha3', side_effect=fake_hash_hexout)
    uhash = ens.namehash('Öbb.eth')
    assert uhash == fake_hash(
        fake_hash(
            EMPTY_SHA3_BYTES +
            fake_hash(b'eth')
        ) +
        fake_hash("öbb".encode('utf8'))
    )


def test_namehash_expand(ens, mocker, fake_hash, fake_hash_hexout):
    mocker.patch('web3.Web3.sha3', side_effect=fake_hash_hexout)
    uhash = ens.namehash('circus')
    assert uhash == fake_hash(
        fake_hash(
            EMPTY_SHA3_BYTES +
            fake_hash(b'eth')
        ) +
        fake_hash(b'circus')
    )


def test_namehash_expand_equivalence(ens):
    assert ens.namehash('spamalot.eth') == ens.namehash('spamalot')


def test_namehash_result(ens):
    namehash = ens.namehash('flying.circus.eth')
    assert type(namehash) == bytes
    hash_hex = Web3.toHex(namehash)
    assert hash_hex == '0xf55bac2e53e0b47ee3a29324e114fc0996e651542abff256fa1daab5a68f1ff6'


@pytest.mark.parametrize("alternate_dot", ['．', '。', '｡'])
def test_namehash_alternate_dots(ens, alternate_dot):
    assert ens.namehash('gallahad' + alternate_dot + 'eth') == ens.namehash('gallahad.eth')


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


def test_reverse_domain(ens, addr1):
    assert ens.reverse_domain(addr1) == addr1[2:] + '.addr.reverse'


def test_reverse_domain_from_bytes(ens, addr1, addrbytes1):
    assert ens.reverse_domain(addrbytes1) == addr1[2:] + '.addr.reverse'


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
