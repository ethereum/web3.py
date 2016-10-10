# Address utilities
from __future__ import absolute_import

import re

from .crypto import (
    sha3,
)
from .encoding import (
    encode_hex,
)
from .string import (
    force_text,
    coerce_args_to_text,
    coerce_return_to_text,
)
from .types import (
    is_string,
)
from .formatting import (
    add_0x_prefix,
    remove_0x_prefix,
    is_prefixed,
)


@coerce_args_to_text
def is_address(address):
    """
    Checks if the given string is an address
    """

    if not is_string(address):
        return False

    if not re.match(r"^(0x)?[0-9a-fA-F]{40}$", address):
        return False
    elif re.match(r"^(0x)?[0-9a-f]{40}", address) or re.match(r"(0x)?[0-9A-F]{40}$", address):
        return True
    else:
        return is_checksum_address(address)


@coerce_args_to_text
def is_checksum_address(address):
    """
    Checks if the given string is a checksummed address
    """

    if not is_string(address):
        return False

    checksum_address = to_checksum_address(address)

    return force_text(address) == force_text(checksum_address)


@coerce_args_to_text
def is_strict_address(address):
    """
    Checks if the given string is strictly an address
    """

    if not is_string(address):
        return False

    return re.match(r"^0x[0-9a-fA-F]{40}$", address) is not None


@coerce_args_to_text
@coerce_return_to_text
def to_checksum_address(address):
    """
    Makes a checksum address
    """
    if not is_string(address):
        return False

    address = remove_0x_prefix(address.lower())
    addressHash = sha3(address)
    checksumAddress = "0x"

    for i in range(len(address)):
        if int(addressHash[i], 16) > 7:
            checksumAddress += address[i].upper()
        else:
            checksumAddress += address[i]

    return checksumAddress


@coerce_args_to_text
@coerce_return_to_text
def to_address(address):
    """
    Transforms given string to valid 20 bytes-length addres with 0x prefix
    """

    if is_string(address):
        if len(address) == 42:
            return address.lower()
        elif len(address) == 40:
            return add_0x_prefix(address.lower())
        elif len(address) == 20:
            return encode_hex(address)
        elif len(address) in {66, 64}:
            long_address = remove_0x_prefix(address.lower())
            if is_prefixed(long_address, '000000000000000000000000'):
                return add_0x_prefix(address[-40:])

    raise ValueError("Unknown address format")
