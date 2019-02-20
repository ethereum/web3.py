
import codecs
from distutils.version import (
    LooseVersion,
)
import functools
import json

import eth_abi
from eth_abi.exceptions import (
    ParseError,
)
from eth_abi.grammar import (
    BasicType,
    parse,
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

from web3._utils.encoding import (
    hexstr_if_str,
    text_if_str,
    to_bytes,
    to_hex,
    to_text,
)
from web3._utils.ens import (
    StaticENS,
    is_ens_name,
    validate_name_has_address,
)
from web3._utils.toolz import (
    curry,
)
from web3._utils.validation import (
    validate_abi,
    validate_address,
)
from web3.exceptions import (
    InvalidAddress,
)


def implicitly_identity(to_wrap):
    @functools.wraps(to_wrap)
    def wrapper(type_str, data):
        modified = to_wrap(type_str, data)
        if modified is None:
            return type_str, data
        else:
            return modified
    return wrapper


#
# Return Normalizers
#


@implicitly_identity
def addresses_checksummed(type_str, data):
    if type_str == 'address':
        return type_str, to_checksum_address(data)


@implicitly_identity
def decode_abi_strings(type_str, data):
    if type_str == 'string':
        return type_str, codecs.decode(data, 'utf8', 'backslashreplace')


#
# Argument Normalizers
#


def parse_basic_type_str(old_normalizer):
    """
    Modifies a normalizer to automatically parse the incoming type string.  If
    that type string does not represent a basic type (i.e. non-tuple type) or is
    not parsable, the normalizer does nothing.
    """
    @functools.wraps(old_normalizer)
    def new_normalizer(type_str, data):
        try:
            abi_type = parse(type_str)
        except ParseError:
            # If type string is not parsable, do nothing
            return type_str, data

        if not isinstance(abi_type, BasicType):
            return type_str, data

        return old_normalizer(abi_type, type_str, data)

    return new_normalizer


@implicitly_identity
@parse_basic_type_str
def abi_bytes_to_hex(abi_type, type_str, data):
    if abi_type.base != 'bytes' or abi_type.is_array:
        return

    bytes_data = hexstr_if_str(to_bytes, data)
    if abi_type.sub is None:
        return type_str, to_hex(bytes_data)

    num_bytes = abi_type.sub
    if len(bytes_data) > num_bytes:
        raise ValueError(
            "This value was expected to be at most %d bytes, but instead was %d: %r" % (
                (num_bytes, len(bytes_data), data)
            )
        )

    padded = bytes_data.ljust(num_bytes, b'\0')
    return type_str, to_hex(padded)


@implicitly_identity
@parse_basic_type_str
def abi_int_to_hex(abi_type, type_str, data):
    if abi_type.base == 'uint' and not abi_type.is_array:
        return abi_type, hexstr_if_str(to_hex, data)


@implicitly_identity
def abi_string_to_hex(type_str, data):
    if type_str == 'string':
        return type_str, text_if_str(to_hex, data)


@implicitly_identity
def abi_string_to_text(type_str, data):
    if type_str == 'string':
        return type_str, text_if_str(to_text, data)


@implicitly_identity
@parse_basic_type_str
def abi_bytes_to_bytes(abi_type, type_str, data):
    if abi_type.base == 'bytes' and not abi_type.is_array:
        return type_str, hexstr_if_str(to_bytes, data)


@implicitly_identity
def abi_address_to_hex(type_str, data):
    if type_str == 'address':
        validate_address(data)
        if is_binary_address(data):
            return type_str, to_checksum_address(data)


@curry
def abi_ens_resolver(w3, type_str, val):
    if type_str == 'address' and is_ens_name(val):
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
            return type_str, validate_name_has_address(w3.ens, val)
    else:
        return type_str, val


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
