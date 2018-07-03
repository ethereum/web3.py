
import pytest

from ens.main import (
    AddressMismatch,
    UnauthorizedError,
    UnownedName,
)
from web3 import Web3


'''
API at: https://github.com/carver/ens.py/issues/2
'''


@pytest.fixture()
def TEST_ADDRESS(address_conversion_func):
    return address_conversion_func("0x000000000000000000000000000000000000dEaD")


@pytest.mark.parametrize(
    'name, normalized_name, namehash_hex',
    [
        (
            'tester.eth',
            'tester.eth',
            '2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        (
            'tester',
            'tester.eth',
            '2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        (
            'TESTER',
            'tester.eth',
            '2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        (
            'tester．eth',
            'tester.eth',
            '2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        (
            'tester。eth',
            'tester.eth',
            '2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        (
            'tester｡eth',
            'tester.eth',
            '2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        # confirm that set-owner works
        (
            'lots.of.subdomains.tester.eth',
            'lots.of.subdomains.tester.eth',
            '0d62a759aa1f1c9680de8603a12a5eb175cd1bfa79426229868eba99f4dce692',
        ),
        (
            'lots.of.subdomains.tester',
            'lots.of.subdomains.tester.eth',
            '0d62a759aa1f1c9680de8603a12a5eb175cd1bfa79426229868eba99f4dce692',
        ),
    ],
)
def test_setup_name(ens, name, normalized_name, namehash_hex):
    address = ens.web3.eth.accounts[3]
    assert not ens.name(address)
    owner = ens.owner('tester')

    ens.setup_name(name, address)
    assert ens.name(address) == normalized_name

    # check that .eth is only appended if guess_tld is True
    if ens.nameprep(name) != normalized_name:
        assert ens.address(name, guess_tld=False) is None

    # check that the correct namehash is set:
    node = Web3.toBytes(hexstr=namehash_hex)
    assert ens.resolver(normalized_name).addr(node) == address

    # check that the correct owner is set:
    assert ens.owner(name) == owner

    ens.setup_name(None, address)
    ens.setup_address(name, None)
    assert not ens.name(address)
    assert not ens.address(name)


def test_cannot_set_name_on_mismatch_address(ens, TEST_ADDRESS):
    ens.setup_address('mismatch-reverse.tester.eth', TEST_ADDRESS)
    with pytest.raises(AddressMismatch):
        ens.setup_name('mismatch-reverse.tester.eth', '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413')


def test_setup_name_default_address(ens):
    name = 'reverse-defaults-to-forward.tester.eth'
    owner = ens.owner('tester.eth')
    new_resolution = ens.web3.eth.accounts[-1]
    ens.setup_address(name, new_resolution)
    assert not ens.name(new_resolution)
    assert ens.owner(name) == owner
    assert ens.address(name) == new_resolution
    ens.setup_name(name)
    assert ens.name(new_resolution) == name
    ens.setup_name(None, new_resolution)


def test_setup_name_default_to_owner(ens):
    name = 'reverse-defaults-to-owner.tester.eth'
    new_owner = ens.web3.eth.accounts[-1]
    ens.setup_owner(name, new_owner)
    assert not ens.name(new_owner)
    assert ens.owner(name) == new_owner
    assert not ens.address(name)
    ens.setup_name(name)
    assert ens.name(new_owner) == name


def test_setup_name_unowned_exception(ens):
    with pytest.raises(UnownedName):
        ens.setup_name('unowned-name.tester.eth')


def test_setup_name_unauthorized(ens, TEST_ADDRESS):
    with pytest.raises(UnauthorizedError):
        ens.setup_name('root-owned-tld', TEST_ADDRESS)


def test_setup_reverse_dict_unmodified(ens):
    # setup
    owner = ens.owner('tester.eth')
    eth = ens.web3.eth
    start_count = eth.getTransactionCount(owner)

    address = ens.web3.eth.accounts[3]
    transact = {}
    ens.setup_name('tester.eth', address, transact=transact)

    # even though a transaction was issued, the dict argument was not modified
    assert eth.getTransactionCount(owner) > start_count
    assert transact == {}

    # teardown
    ens.setup_name(None, address, transact=transact)
