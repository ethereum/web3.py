
import codecs
from distutils.version import (
    LooseVersion,
)
import functools
import json

import eth_abi
from eth_abi.abi import (
    process_type,
)
from eth_utils import (
    to_checksum_address,
)
from eth_utils.address import (
    is_binary_address,
)
from hexbytes import (
    HexBytes,
)

from web3.exceptions import (
    InvalidAddress,
)
from web3.utils.encoding import (
    hexstr_if_str,
    text_if_str,
    to_bytes,
    to_hex,
    to_text,
)
from web3.utils.ens import (
    StaticENS,
    is_ens_name,
    validate_name_has_address,
)
from web3.utils.toolz import (
    curry,
)
from web3.utils.validation import (
    validate_abi,
    validate_address,
)


def implicitly_identity(to_wrap):
    @functools.wraps(to_wrap)
    def wrapper(abi_type, data):
        modified = to_wrap(abi_type, data)
        if modified is None:
            return abi_type, data
        else:
            return modified
    return wrapper


#
# Return Normalizers
#


@implicitly_identity
def addresses_checksummed(abi_type, data):
    if abi_type == 'address':
        return abi_type, to_checksum_address(data)


@implicitly_identity
def decode_abi_strings(abi_type, data):
    if abi_type == 'string':
        return abi_type, codecs.decode(data, 'utf8', 'backslashreplace')


#
# Argument Normalizers
#


@implicitly_identity
def abi_bytes_to_hex(abi_type, data):
    base, sub, arrlist = process_type(abi_type)
    if base == 'bytes' and not arrlist:
        bytes_data = hexstr_if_str(to_bytes, data)
        if not sub:
            return abi_type, to_hex(bytes_data)
        else:
            num_bytes = int(sub)
            if len(bytes_data) <= num_bytes:
                padded = bytes_data.ljust(num_bytes, b'\0')
                return abi_type, to_hex(padded)
            else:
                raise ValueError(
                    "This value was expected to be at most %d bytes, but instead was %d: %r" % (
                        (num_bytes, len(bytes_data), data)
                    )
                )


@implicitly_identity
def abi_int_to_hex(abi_type, data):
    base, _sub, arrlist = process_type(abi_type)
    if base == 'uint' and not arrlist:
        return abi_type, hexstr_if_str(to_hex, data)


@implicitly_identity
def abi_string_to_hex(abi_type, data):
    if abi_type == 'string':
        return abi_type, text_if_str(to_hex, data)


@implicitly_identity
def abi_string_to_text(abi_type, data):
    if abi_type == 'string':
        return abi_type, text_if_str(to_text, data)


@implicitly_identity
def abi_bytes_to_bytes(abi_type, data):
    base, sub, arrlist = process_type(abi_type)
    if base == 'bytes' and not arrlist:
        return abi_type, hexstr_if_str(to_bytes, data)


@implicitly_identity
def abi_address_to_hex(abi_type, data):
    if abi_type == 'address':
        validate_address(data)
        if is_binary_address(data):
            return abi_type, to_checksum_address(data)


@curry
def abi_ens_resolver(w3, abi_type, val):
    if abi_type == 'address' and is_ens_name(val):
        if w3 is None:
            raise InvalidAddress(
                "Could not look up name %r because no web3"
                " connection available" % (val)
            )
        elif w3.ens is None:
            raise InvalidAddress(
                "Could not look up name %r because ENS is"
                " set to None" % (val)
            )
        elif int(w3.net.version) is not 1 and not isinstance(w3.ens, StaticENS):
            raise InvalidAddress(
                "Could not look up name %r because web3 is"
                " not connected to mainnet" % (val)
            )
        else:
            return (abi_type, validate_name_has_address(w3.ens, val))
    else:
        return (abi_type, val)


BASE_RETURN_NORMALIZERS = [
    addresses_checksummed,
]


if LooseVersion(eth_abi.__version__) < LooseVersion("2"):
    BASE_RETURN_NORMALIZERS.append(decode_abi_strings)


#
# Property Normalizers
#


def normalize_abi(abi):
    if isinstance(abi, str):
        abi = json.loads(abi)
    validate_abi(abi)
    return abi


def normalize_address(ens, address):
    if address:
        if is_ens_name(address):
            validate_name_has_address(ens, address)
        else:
            validate_address(address)
    return address


def normalize_bytecode(bytecode):
    if bytecode:
        bytecode = HexBytes(bytecode)
    return bytecode
