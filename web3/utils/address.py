# Address utilities
from __future__ import absolute_import
from . import encoding, utils
from web3.utils.crypto import sha3
import re


def is_address(address):
    """
    Checks if the given string is an address
    """

    if not utils.isString(address):
        return False

    if not re.match(r"^(0x)?[0-9a-fA-F]{40}$", address):
        return False
    elif re.match(r"^(0x)?[0-9a-f]{40}", address) or re.match(r"(0x)?[0-9A-F]{40}$", address):
        return True
    else:
        return isChecksumAddress(address)


isAddress = is_address


def isChecksumAddress(address):
    """
    Checks if the given string is a checksummed address
    """

    if not utils.isString(address):
        return False

    address = address.replace("0x", "")
    addressHash = sha3(address.lower())

    for i in range(40):
        if (int(addressHash[i], 16) > 7 and address[i].upper() != address[i]) or \
                (int(addressHash[i], 16) <= 7 and address[i].lower() != address[i]):
            return False

    return True


def isStrictAddress(address):
    """
    Checks if the given string is strictly an address
    """

    if not utils.isString(address):
        return False

    return re.match(r"^0x[0-9a-fA-F]{40}$", address) is not None


def toChecksumAddress(address):
    """
    Makes a checksum address
    """

    if not utils.isString(address):
        return False

    address = address.lower().replace("0x", "")
    addressHash = sha3(address)
    checksumAddress = "0x"

    for i in range(len(address)):
        if int(addressHash[i], 16) > 7:
            checksumAddress += addressHash[i].upper()
        else:
            checksumAddress += addressHash[i]

    return checksumAddress


def toAddress(address):
    """
    Transforms given string to valid 20 bytes-length addres with 0x prefix
    """

    if not utils.isString(address):
        return False

    if isStrictAddress(address):
        return address

    if re.match(r"^[0-9a-f]{3}$", address):
        return "0x"+address

    return "0x" + utils.padLeft(encoding.toHex(address)[2:], 40)
