
from cytoolz import (
    curry,
)

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
