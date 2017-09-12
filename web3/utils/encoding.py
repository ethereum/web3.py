# String encodings and numeric representations
import sys
import json

from rlp.sedes import big_endian_int

from eth_utils import (
    is_bytes,
    is_string,
    is_boolean,
    is_dict,
    is_integer,
    coerce_args_to_bytes,
    add_0x_prefix,
    is_0x_prefixed,
    encode_hex,
    remove_0x_prefix,
    force_text,
    force_bytes,
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
    sub_type_of_array_type,
)

from web3.utils.validation import (
    validate_abi_type,
    validate_abi_value,
)


def _is_prefixed(value, prefix):
    return value.startswith(
        force_bytes(prefix) if is_bytes(value) else force_text(prefix)
    )


def hex_encode_abi_type(abi_type, value, force_size=None):
    """
    Encodes value into a hex string in format of abi_type
    """
    validate_abi_type(abi_type)
    validate_abi_value(abi_type, value)

    data_size = force_size or size_of_type(abi_type)
    if is_array_type(abi_type):
        sub_type = sub_type_of_array_type(abi_type)
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
        if sys.version_info.major >= 3 and is_bytes(value):
            return encode_hex(value)
        else:
            return value
    elif is_string_type(abi_type):
        return encode_hex(value)
    else:
        raise ValueError(
            "Unsupported ABI type: {0}".format(abi_type)
        )


def to_hex_twos_compliment(value, bit_size):
    """
    Converts integer value to twos compliment hex representation with given bit_size
    """
    if value >= 0:
        return to_hex_with_size(value, bit_size)

    value = (1 << bit_size) + value
    hex_value = hex(value)
    hex_value = hex_value.rstrip("L")
    return hex_value


def to_hex_with_size(value, bit_size):
    """
    Converts a value to hex with given bit_size:
    """
    return pad_hex(to_hex(value), bit_size)


def pad_hex(value, bit_size):
    """
    Pads a hex string up to the given bit_size
    """
    value = remove_0x_prefix(value)
    return add_0x_prefix(value.zfill(int(bit_size / 4)))


def to_hex(value):
    """
    Auto converts any supported value into it's hex representation.
    """
    if is_boolean(value):
        return "0x1" if value else "0x0"

    if is_dict(value):
        return encode_hex(json.dumps(value, sort_keys=True))

    if isinstance(value, bytes):
        return encode_hex(value)
    elif isinstance(value, str):
        return encode_hex(value.encode('utf-8'))

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
        if is_0x_prefixed(value) or _is_prefixed(value, '-0x'):
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
        if is_0x_prefixed(value) or _is_prefixed(value, '-0x'):
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
