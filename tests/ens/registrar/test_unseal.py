
import pytest

from ens.registrar import InvalidBidHash


@pytest.fixture
def unseal_registrar(registrar, mocker, hashbytes9, addr9):
    mocker.patch.object(registrar.core, 'shaBid', return_value=hashbytes9)
    mocker.patch.object(registrar.core, 'sealedBids', return_value=addr9)
    mocker.patch.object(registrar.core, 'unsealBid')
    return registrar


def test_alias_reveal(unseal_registrar):
    assert unseal_registrar.unseal == unseal_registrar.reveal


def test_reveal_requires_from(unseal_registrar, label1, value1, secret1):
    with pytest.raises(TypeError):
        unseal_registrar.reveal(label1, value1, secret1)


def test_reveal_confirms_sealed_bid(unseal_registrar, mocker, label1, hashbytes9, value1, addr1):
    unseal_registrar.reveal(label1, value1, '', transact={'from': addr1})
    unseal_registrar.core.sealedBids.assert_called_once_with(addr1, hashbytes9)


def test_reveal_fails_on_seal_mismatch(unseal_registrar, mocker, label1, value1, addr1):
    mocker.patch.object(unseal_registrar.core, 'sealedBids', return_value=None)
    with pytest.raises(InvalidBidHash):
        unseal_registrar.reveal(label1, value1, '', transact={'from': addr1})


def test_reveal_nameprep(
        unseal_registrar, mocker, fake_hash, fake_hash_hexout, value1, secret1, addr1):
    '''
    Must convert unicode letters to lowercase, and convert from full name to label
    '''
    mocker.patch('web3.Web3.sha3', side_effect=fake_hash_hexout)
    unseal_registrar.reveal("ÖÖÖÖÖÖÖ.eth", value1, secret1, transact={'from': addr1})
    unseal_registrar.core.shaBid.assert_called_once_with(
        fake_hash("ööööööö".encode()),
        addr1,
        value1,
        fake_hash(secret1.encode()),
    )


def test_unseal_bid(
        unseal_registrar, mocker, fake_hash, fake_hash_hexout, label1, value1, secret1, addr1):
    mocker.patch('web3.Web3.sha3', side_effect=fake_hash_hexout)
    unseal_registrar.reveal(label1, value1, secret1, transact={'from': addr1})
    unseal_registrar.core.unsealBid.assert_called_once_with(
        fake_hash(label1.encode()),
        value1,
        fake_hash(secret1.encode()),
        transact={'from': addr1, 'gas': 150000})
