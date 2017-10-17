
import pytest
from unittest.mock import Mock

from web3 import Web3

from ens.main import UnauthorizedError

'''
API at: https://github.com/carver/ens.py/issues/2
'''


@pytest.fixture
def enssetter(ens, mocker, addr1, addr2, hash9):
    mocker.patch.object(ens.web3, 'eth', wraps=ens.web3.eth, accounts=[addr1, addr2])
    mocker.patch.object(ens, 'owner', return_value=addr1)
    mocker.patch.object(ens, 'address', return_value=None)
    mocker.patch.object(ens, '_resolverContract', return_value=Mock())
    mocker.patch.object(ens, '_first_owner', wraps=ens._first_owner)
    mocker.patch.object(ens, '_claim_ownership', wraps=ens._claim_ownership)
    mocker.patch.object(ens, '_set_resolver', wraps=ens._set_resolver)
    mocker.patch.object(ens.ens, 'resolver', return_value=None)
    mocker.patch.object(ens.ens, 'setAddr', return_value=hash9)
    mocker.patch.object(ens.ens, 'setResolver')
    mocker.patch.object(ens.ens, 'setSubnodeOwner')
    return ens


def test_set_address_noop(enssetter, mocker, name1, addr1):
    # show the name as already set up correctly
    mocker.patch.object(enssetter, 'address', return_value=addr1)
    # in case of bug where ens.py tries to set the address up, show resolver as not set
    assert enssetter.setup_address(name1, addr1) is None
    enssetter.address.assert_called_once_with(name1)
    assert not enssetter._claim_ownership.called
    assert not enssetter._set_resolver.called


def test_set_address_noop_with_bytes(enssetter, mocker, name1, addr1, addrbytes1):
    # show the name as already set up correctly
    mocker.patch.object(enssetter, 'address', return_value=addr1)
    # in case of bug where ens.py tries to set the address up, show resolver as not set
    assert enssetter.setup_address(name1, addrbytes1) is None
    enssetter.address.assert_called_once_with(name1)
    assert not enssetter._claim_ownership.called
    assert not enssetter._set_resolver.called


def test_set_address_unauthorized(enssetter, mocker, name1, addr1):
    # show the name as not set up
    # pretend there are no available accounts to send from
    mocker.patch.object(enssetter.web3, 'eth', wraps=enssetter.web3.eth, accounts=[])
    with pytest.raises(UnauthorizedError):
        enssetter.setup_address(name1, addr1)


def test_setup_address_default_address_to_owner(enssetter, mocker, name1, addr1, addrbytes1):
    mocker.patch.object(enssetter, 'owner', return_value=addr1)
    enssetter.setup_address(name1)
    resolver = enssetter._resolverContract()
    assert resolver.setAddr.called
    assert resolver.setAddr.call_args[0][1] == addrbytes1


def test_set_address_autoselect_first_owner(enssetter, mocker, name1, addr1, addr2):
    mocker.patch.object(enssetter.web3, 'eth', wraps=enssetter.web3.eth, accounts=[addr1, addr2])
    # set_address should auto-select the name owner to send the transaction from
    mocker.patch.object(enssetter, '_first_owner', return_value=(addr2, None, None))
    enssetter.setup_address(name1, addr1)
    resolver = enssetter._resolverContract()
    assert resolver.setAddr.called
    assert resolver.setAddr.call_args[1]['transact']['from'] == addr2


def test_first_owner_label_to_name(enssetter, addr1):
    # show the name as not set up
    # set_address should auto-select the name owner to send the transaction from
    assert enssetter._first_owner('labelonly') == (addr1, [], 'labelonly.eth')


def test_first_owner_upchain_identify(enssetter, mocker, name1, addr1, addr2):
    # show the name as not set up
    # set_address should auto-select the name owner to send the transaction from
    mocker.patch.object(
        enssetter,
        'owner',
        side_effect=lambda name: None if len(name.split('.')) >= 3 else addr2
    )
    assert enssetter._first_owner('abcdefg.bcdefgh.cdefghi.eth') == \
        (addr2, ['abcdefg', 'bcdefgh'], 'cdefghi.eth')


def test_claim_ownership_takeover_subdomains(enssetter, mocker, name1, addr1, addr2):
    # show the name as not set up
    # set_address should auto-select the name owner to send the transaction from
    enssetter._claim_ownership(addr2, ['abcdefg', 'bcdefgh'], 'cdefghi.eth')
    assert enssetter.ens.setSubnodeOwner.call_count == 2
    assert enssetter.ens.setSubnodeOwner.call_args_list[0][0] == (
        enssetter.namehash('cdefghi.eth'),
        enssetter.labelhash('bcdefgh'),
        addr2,
    )
    assert enssetter.ens.setSubnodeOwner.call_args_list[1][0] == (
        enssetter.namehash('bcdefgh.cdefghi.eth'),
        enssetter.labelhash('abcdefg'),
        addr2,
    )


def test_set_address_skip_claim_if_owned(enssetter, mocker, addr1, addr2, name1):
    mocker.patch.object(
        enssetter,
        '_first_owner',
        return_value=(addr2, [], 'ab.cdefghi.eth')
    )
    enssetter.setup_address(name1, addr1)
    assert not enssetter._claim_ownership.called


def test_set_address_claim_if_unowned(enssetter, mocker, addr1, addr2, name1):
    mocker.patch.object(
        enssetter,
        '_first_owner',
        return_value=(addr2, ['abcdefg', 'bcdefgh'], 'cdefghi.eth')
    )
    enssetter.setup_address(name1, addr1)
    assert enssetter._claim_ownership.call_args[0] == enssetter._first_owner()


def test_set_resolver_leave_default(enssetter, mocker, name1, addr1, addr2, fake_hash_utf8):
    # TODO write a test interacting with a copy of the real ENS contract
    # assert not enssetter.ens.setResolver.called
    pass


def test_set_resolver_set_default_resolver(enssetter, mocker, name1, addr1, addr2, fake_hash_utf8):
    def addr_of_name(name):
        return Web3.toHex(text=name)[:42]
    mocker.patch.object(enssetter, 'address', side_effect=addr_of_name)
    enssetter._set_resolver(name1)
    assert enssetter.ens.setResolver.called
    assert enssetter.ens.setResolver.call_args[0] == (
        enssetter.namehash(name1),
        b'resolver.eth',
    )


def test_set_address_set_resolver(enssetter, mocker, name1, addr1, addr2, fake_hash_utf8):
    enssetter.setup_address(name1, addr1)
    assert not enssetter.ens.setResolver.called
    assert enssetter._set_resolver.call_args[0] == (name1,)


def test_set_address_in_default_resolver(enssetter, mocker, name1, addr1, addrbytes1, hash1):
    resolver = enssetter._resolverContract()
    resolver.setAddr.return_value = hash1
    txid = enssetter.setup_address(name1, addr1)
    assert resolver.setAddr.called
    assert resolver.setAddr.call_args_list[0][0] == (
        enssetter.namehash(name1),
        addrbytes1,
    )
    assert txid is not None
