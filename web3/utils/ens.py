from contextlib import (
    contextmanager,
)

from eth_utils import (
    is_0x_prefixed,
    is_hex,
    is_hex_address,
)

from ens import ENS
from web3.exceptions import (
    NameNotFound,
)


def is_ens_name(value):
    if not isinstance(value, str):
        return False
    elif is_hex_address(value):
        return False
    elif is_0x_prefixed(value) and is_hex(value):
        return False
    else:
        return ENS.is_valid_name(value)


def validate_name_has_address(ens, name):
    addr = ens.address(name, guess_tld=False)
    if addr:
        return addr
    else:
        raise NameNotFound("Could not find address for name %r" % name)


class StaticENS:
    def __init__(self, name_addr_pairs):
        self.registry = dict(name_addr_pairs)

    def address(self, name, guess_tld=True):
        # no automated web3 usages should be guessing the TLD
        assert not guess_tld
        return self.registry.get(name, None)


@contextmanager
def ens_addresses(w3, name_addr_pairs):
    original_ens = w3.ens
    w3.ens = StaticENS(name_addr_pairs)
    yield
    w3.ens = original_ens


@contextmanager
def contract_ens_addresses(contract, name_addr_pairs):
    '''
    Use this context manager to temporarily resolve name/address pairs
    supplied as the argument. For example:

    with contract_ens_addresses(mycontract, [('resolve-as-1s.eth', '0x111...111')]):
        # any contract call or transaction in here would only resolve the above ENS pair
    '''
    with ens_addresses(contract.web3, name_addr_pairs):
        yield
