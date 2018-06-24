
import pytest
from unittest.mock import (
    patch,
)

from eth_utils import (
    is_same_address,
    to_bytes,
)

from ens.constants import (
    EMPTY_ADDR_HEX,
)
from ens.main import (
    UnauthorizedError,
)
from web3 import Web3


'''
API at: https://github.com/carver/ens.py/issues/2
'''


@pytest.mark.parametrize(
    'name, full_name, namehash_hex',
    [
        (
            'tester.eth',
            'tester.eth',
            '0x2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        (
            'tester',
            'tester.eth',
            '0x2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        (
            'TESTER',
            'TESTER.eth',
            '0x2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        # handles alternative dot separators
        (
            'tester．eth',
            'tester．eth',
            '0x2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        (
            'tester。eth',
            'tester。eth',
            '0x2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        (
            'tester｡eth',
            'tester｡eth',
            '0x2a7ac1c833d35677c2ff34a908951de142cc1653de6080ad4e38f4c9cc00aafe',
        ),
        # confirm that set-owner works
        (
            'lots.of.subdomains.tester.eth',
            'lots.of.subdomains.tester.eth',
            '0x0d62a759aa1f1c9680de8603a12a5eb175cd1bfa79426229868eba99f4dce692',
        ),
        (
            'lots.of.subdomains.tester',
            'lots.of.subdomains.tester.eth',
            '0x0d62a759aa1f1c9680de8603a12a5eb175cd1bfa79426229868eba99f4dce692',
        ),
    ],
)
def test_set_address(ens, name, full_name, namehash_hex, TEST_ADDRESS):
    assert ens.address(name) is None
    owner = ens.owner('tester')

    ens.setup_address(name, TEST_ADDRESS)
    assert is_same_address(ens.address(name), TEST_ADDRESS)

    # check that .eth is only appended if guess_tld is True
    namehash = Web3.toBytes(hexstr=namehash_hex)
    normal_name = ens.nameprep(full_name)
    if ens.nameprep(name) == normal_name:
        assert is_same_address(ens.address(name, guess_tld=False), TEST_ADDRESS)
    else:
        assert ens.address(name, guess_tld=False) is None

    # check that the correct namehash is set:
    assert is_same_address(ens.resolver(normal_name).addr(namehash), TEST_ADDRESS)

    # check that the correct owner is set:
    assert ens.owner(name) == owner

    ens.setup_address(name, None)
    assert ens.address(name) is None


@pytest.mark.parametrize(
    'name, equivalent',
    [
        ('TESTER', 'tester.eth'),
        ('unicÖde.tester.eth', 'unicöde.tester.eth'),
    ],
)
def test_set_address_equivalence(ens, name, equivalent, TEST_ADDRESS):
    assert ens.address(name) is None

    ens.setup_address(name, TEST_ADDRESS)
    assert is_same_address(ens.address(name), TEST_ADDRESS)
    assert is_same_address(ens.address(equivalent), TEST_ADDRESS)

    ens.setup_address(name, None)
    assert ens.address(name) is None


@pytest.mark.parametrize(
    'set_address',
    [
        # since the test uses getTransactionCount,
        # using a same address converted to bytes and hex will error with same count,
        # use two different addresses of each type (hex, bytes)
        "0x000000000000000000000000000000000000dEaD",
        to_bytes(hexstr="0x5B2063246F2191f18F2675ceDB8b28102e957458"),
        EMPTY_ADDR_HEX,
        None,
        '',
    ],
)
def test_set_address_noop(ens, set_address):
    eth = ens.web3.eth
    owner = ens.owner('tester.eth')
    ens.setup_address('noop.tester.eth', set_address)
    starting_transactions = eth.getTransactionCount(owner)

    # do not issue transaction if address is already set
    ens.setup_address('noop.tester.eth', set_address)
    assert eth.getTransactionCount(owner) == starting_transactions


def test_set_address_unauthorized(ens, TEST_ADDRESS):
    with pytest.raises(UnauthorizedError):
        ens.setup_address('eth', TEST_ADDRESS)


def test_setup_address_default_address_to_owner(ens):
    assert ens.address('default.tester.eth') is None
    owner = ens.owner('tester.eth')

    ens.setup_address('default.tester.eth')
    assert ens.address('default.tester.eth') == owner


def test_first_owner_upchain_identify(ens):
    # _first_owner should auto-select the name owner to send the transaction from
    addr = '0x5B2063246F2191f18F2675ceDB8b28102e957458'

    def getowner(name):
        if name == "cdefghi.eth":
            return addr
        else:
            return None
    with patch.object(ens, 'owner', side_effect=getowner):
        assert ens._first_owner('abcdefg.bcdefgh.cdefghi.eth') == \
            (addr, ['abcdefg', 'bcdefgh'], 'cdefghi.eth')


def test_set_resolver_leave_default(ens, TEST_ADDRESS):
    owner = ens.owner('tester')
    ens.setup_address('leave-default-resolver.tester.eth', TEST_ADDRESS)
    eth = ens.web3.eth
    num_transactions = eth.getTransactionCount(owner)

    ens.setup_address('leave-default-resolver.tester', '0x5B2063246F2191f18F2675ceDB8b28102e957458')

    # should skip setting the owner and setting the default resolver, and only
    #   set the name in the default resolver to point to the new address
    assert eth.getTransactionCount(owner) == num_transactions + 1
