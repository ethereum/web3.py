# Address utilities
from __future__ import absolute_import

import re

from .crypto import (
    sha3,
)
from .encoding import (
    encode_hex,
)
from .types import (
    is_string,
)
from .formatting import (
    add_0x_prefix,
    remove_0x_prefix,
)


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


def is_checksum_address(address):
    """
    Checks if the given string is a checksummed address
    """

    if not is_string(address):
        return False

    address = remove_0x_prefix(address)
    checksum_address = to_checksum_address(address)

    return address == checksum_address


def is_strict_address(address):
    """
    Checks if the given string is strictly an address
    """

    if not is_string(address):
        return False

    return re.match(r"^0x[0-9a-fA-F]{40}$", address) is not None


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
            checksumAddress += addressHash[i].upper()
        else:
            checksumAddress += addressHash[i]

    return checksumAddress


def to_address(address):
    """
    Transforms given string to valid 20 bytes-length addres with 0x prefix
    """

    if is_string(address):
        if len(address) == 42:
            return address
        elif len(address) == 40:
            return add_0x_prefix(address)
        elif len(address) == 20:
            return encode_hex(address)

    raise ValueError("Unknown address format")
