
import pytest
from unittest.mock import Mock

from ens.main import UnauthorizedError, AddressMismatch, UnownedName

'''
API at: https://github.com/carver/ens.py/issues/2
'''


@pytest.fixture
def ens2(ens, mocker, addr1, addr9, hash9):
    mocker.patch.object(ens, '_setup_reverse')
    mocker.patch.object(ens, 'address', return_value=None)
    mocker.patch.object(ens, 'owner', return_value=None)
    mocker.patch.object(ens.web3, 'eth', wraps=ens.web3.eth, accounts=[addr1, addr9])
    mocker.patch.object(ens, 'setup_address')
    '''
    mocker.patch.object(ens, '_resolverContract', return_value=Mock())
    mocker.patch.object(ens, '_first_owner', wraps=ens._first_owner)
    mocker.patch.object(ens, '_claim_ownership', wraps=ens._claim_ownership)
    mocker.patch.object(ens, '_set_resolver', wraps=ens._set_resolver)
    mocker.patch.object(ens.ens, 'resolver', return_value=None)
    mocker.patch.object(ens.ens, 'setAddr', return_value=hash9)
    mocker.patch.object(ens.ens, 'setResolver')
    mocker.patch.object(ens.ens, 'setSubnodeOwner')
    '''
    return ens


def test_cannot_set_name_on_mismatch_address(ens2, mocker, name1, addr1, addr2):
    mocker.patch.object(ens2, 'address', return_value=addr2)
    with pytest.raises(AddressMismatch):
        ens2.setup_name(name1, addr1)


def test_setup_name_default_address(ens2, mocker, name1, addr1):
    mocker.patch.object(ens2, 'address', return_value=addr1)
    ens2.setup_name(name1)
    ens2._setup_reverse.assert_called_once_with(name1, addr1, transact={})


def test_setup_name_default_to_owner(ens2, mocker, name1, addr1):
    mocker.patch.object(ens2, 'owner', return_value=addr1)
    ens2.setup_name(name1)
    ens2._setup_reverse.assert_called_once_with(name1, addr1, transact={})


def test_setup_name_unowned_exception(ens2, name1):
    with pytest.raises(UnownedName):
        ens2.setup_name(name1)


def test_setup_name_unauthorized(ens2, mocker, name1, addr1):
    mocker.patch.object(ens2, 'address', return_value=addr1)
    mocker.patch.object(ens2.web3, 'eth', wraps=ens2.web3.eth, accounts=[])
    with pytest.raises(UnauthorizedError):
        ens2.setup_name(name1, addr1)


def test_setup_name_no_resolution(ens2, name1, addr1):
    ens2.setup_name(name1, addr1)
    ens2._setup_reverse.assert_called_once_with(name1, addr1, transact={})


def test_setup_name_transact_passthrough(ens2, name1, addr1):
    transact = {'gasPrice': 1}
    ens2.setup_name(name1, addr1, transact=transact)
    ens2._setup_reverse.assert_called_once_with(name1, addr1, transact=transact)


def test_setup_name_resolver_setup(ens2, name1, addr1):
    # if the name doesn't currently resolve to anything, set it up
    transact = {'gasPrice': 1}
    ens2.setup_name(name1, addr1, transact=transact)
    ens2.setup_address.assert_called_once_with(name1, addr1, transact=transact)


def test_setup_reverse_label_to_fullname(ens, mocker, addr1):
    registrar = mocker.patch.object(ens, '_reverse_registrar', return_value=Mock())
    ens._setup_reverse('castleanthrax', addr1)
    registrar().setName.assert_called_once_with('castleanthrax.eth', transact={'from': addr1})


def test_setup_reverse_dict_unmodified(ens, mocker, addr1):
    mocker.patch.object(ens, '_reverse_registrar', return_value=Mock())
    transact = {}
    ens._setup_reverse('castleanthrax', addr1, transact=transact)
    assert transact == {}
