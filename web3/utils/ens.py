from contextlib import contextmanager

from cytoolz import (
    curry,
)

from unittest.mock import patch

from web3.exceptions import (
    NameNotFound,
)


def is_ens_name(value):
    if not isinstance(value, str):
        return False
    return value.endswith('.eth')


def validate_name_has_address(ens, name):
    addr = ens.address(name)
    if addr:
        return addr
    else:
        raise NameNotFound("Could not find address for name %r" % name)


@curry
def abi_ens_resolver(ens, abi_type, val):
    if abi_type == 'address' and is_ens_name(val):
        return (abi_type, validate_name_has_address(ens, val))
    else:
        return (abi_type, val)


@contextmanager
def ens_addresses(name_addr_pairs):
    '''
    Use this context manager to temporarily resolve name/address pairs
    supplied as the argument. For example:

    with ens_addresses([('resolve-as-0s.eth', '0x000...000')]):
        # any contract call in here would only resolve the above ENS pair
    '''
    registry = dict(name_addr_pairs)

    def resolver(name):
        return registry.get(name, None)
    with patch('web3.contract.ENS.fromWeb3') as MockENS_contract, \
            patch('web3.middleware.names.ENS.fromWeb3') as MockENS_middleware:
        for mocked in (MockENS_contract, MockENS_middleware):
            ens = mocked.return_value
            ens.address.side_effect = resolver
        yield
