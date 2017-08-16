# String encodings and numeric representations
import sys
import json
import re
import codecs

from rlp.sedes import big_endian_int

from eth_utils import (
    is_bytes,
    is_string,
    is_boolean,
    is_dict,
    is_integer,
    coerce_args_to_text,
    coerce_args_to_bytes,
    add_0x_prefix,
    is_0x_prefixed,
    encode_hex,
    remove_0x_prefix,
)

from .formatting import (
    is_prefixed,
)

from web3.utils.abi import (
    is_address_type,
    is_array_type,
    is_bool_type,
    is_bytes_type,
    is_int_type,
    is_uint_type,
    is_string_type,
    size_of_type,
)


def hex_encode_abi_type(abi_type, value, force_size=None):
    data_size = force_size or size_of_type(abi_type)
    if is_array_type(abi_type):
        sub_type = re.sub(r"\[[^]]*\]$", "", abi_type, 1)
        return "".join([remove_0x_prefix(hex_encode_abi_type(sub_type, v, 256)) for v in value])
    elif is_bool_type(abi_type):
        return to_hex_with_size(value, data_size)
    elif is_uint_type(abi_type):
        return to_hex_with_size(value, data_size)
    elif is_int_type(abi_type):
        return to_hex_twos_compliment(value, data_size)
    elif is_address_type(abi_type):
        return pad_hex(value, data_size)
    elif is_bytes_type(abi_type):
        if sys.version_info[0] >= 3:
            if is_bytes(value):
                return to_hex(value)
            return value
        else:
            return to_hex(value)
    elif is_string_type(abi_type):
        return bytes_to_hex(value)


def bytes_to_hex(byte_string):
    if type(byte_string) == str:
        byte_string = byte_string.encode('utf-8')
    return add_0x_prefix(codecs.getencoder('hex')(byte_string)[0].decode("utf-8"))


def to_hex_twos_compliment(value, bit_size):
    if value >= 0:
        return to_hex_with_size(value, bit_size)

    value = (1 << bit_size) + value
    hex_value = hex(value)
    hex_value = hex_value.rstrip("L")
    return hex_value


def to_hex_with_size(value, bit_size):
    return pad_hex(to_hex(value), bit_size)


def pad_hex(value, bit_size):
    value = remove_0x_prefix(value)
    return "0x{hex_string}".format(hex_string=value.zfill(int(bit_size / 4)))


@coerce_args_to_text
def to_hex(value):
    """
    Auto converts any supported value into it's hex representation.
    """
    if is_boolean(value):
        return "0x1" if value else "0x0"

    if is_dict(value):
        return encode_hex(json.dumps(value, sort_keys=True))

    if is_string(value):
        return encode_hex(value)

    if is_integer(value):
        return from_decimal(value)

    raise TypeError(
        "Unsupported type: '{0}'.  Must be one of Boolean, Dictionary, String, "
        "or Integer.".format(repr(type(value)))
    )


def to_decimal(value):
    """
    Converts value to it's decimal representation in string
    """
    if is_string(value):
        if is_0x_prefixed(value) or is_prefixed(value, '-0x'):
            value = int(value, 16)
        else:
            value = int(value)
    else:
        value = int(value)

    return value


def from_decimal(value):
    """
    Converts numeric value to it's hex representation
    """
    if is_string(value):
        if is_0x_prefixed(value) or is_prefixed(value, '-0x'):
            value = int(value, 16)
        else:
            value = int(value)

    # python2 longs end up with an `L` hanging off the end of their hexidecimal
    # representation.
    result = hex(value).rstrip('L')
    return result


@coerce_args_to_bytes
def decode_big_endian_int(value):
    return big_endian_int.deserialize(value.lstrip(b'\x00'))
