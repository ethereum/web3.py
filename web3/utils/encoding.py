# String encodings and numeric representations
import json
import re
import sys
import warnings

from rlp.sedes import big_endian_int

from eth_utils import (
    add_0x_prefix,
    coerce_args_to_bytes,
    force_bytes,
    force_text,
    int_to_big_endian,
    is_0x_prefixed,
    is_boolean,
    is_bytes,
    is_dict,
    is_integer,
    is_string,
    decode_hex,
    encode_hex,
    remove_0x_prefix,
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
from web3.utils.decorators import (
    deprecated_for,
)
from web3.utils.validation import (
    assert_one_val,
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


def trim_hex(hexstr):
    if hexstr.startswith('0x0'):
        hexstr = re.sub('^0x0+', '0x', hexstr)
        if hexstr == '0x':
            hexstr = '0x0'
    return hexstr


def to_hex(value=None, hexstr=None, text=None):
    """
    Auto converts any supported value into it's hex representation.

    Trims leading zeros, as defined in:
    https://github.com/ethereum/wiki/wiki/JSON-RPC#hex-value-encoding
    """
    assert_one_val(value, hexstr=hexstr, text=text)

    if hexstr is not None:
        return trim_hex(hexstr)

    if text is not None:
        return encode_hex(text.encode('utf-8'))

    if is_boolean(value):
        return "0x1" if value else "0x0"

    if is_dict(value):
        return encode_hex(json.dumps(value, sort_keys=True))

    if isinstance(value, bytes):
        padded = encode_hex(value)
        return trim_hex(padded)
    elif is_string(value):
        return to_hex(text=value)

    if is_integer(value):
        # python2 longs end up with an `L` hanging off the end of their hexidecimal
        # representation.
        return hex(value).rstrip('L')

    raise TypeError(
        "Unsupported type: '{0}'.  Must be one of Boolean, Dictionary, String, "
        "or Integer.".format(repr(type(value)))
    )


def to_decimal(value=None, hexstr=None, text=None):
    """
    Converts value to it's decimal representation in string
    """
    assert_one_val(value, hexstr=hexstr, text=text)

    if hexstr is not None:
        return int(hexstr, 16)
    elif text is not None:
        return int(text)
    elif is_string(value):
        if bytes != str and isinstance(value, bytes):
            return to_decimal(hexstr=to_hex(value))
        elif is_0x_prefixed(value) or _is_prefixed(value, '-0x'):
            warnings.warn(DeprecationWarning(
                "Sending a hex string in the first position has been deprecated. Please use "
                "toDecimal(hexstr='%s') instead." % value
            ))
            return to_decimal(hexstr=value)
        else:
            return int(value)
    else:
        return int(value)


@deprecated_for("to_hex")
def from_decimal(value):
    """
    Converts numeric value to its hex representation
    """
    if is_string(value):
        if is_0x_prefixed(value) or _is_prefixed(value, '-0x'):
            value = int(value, 16)
        else:
            value = int(value)

    return to_hex(value)


def to_bytes(primitive=None, hexstr=None, text=None):
    assert_one_val(primitive, hexstr=hexstr, text=text)

    if is_boolean(primitive):
        return b'\x01' if primitive else b'\x00'
    elif isinstance(primitive, bytes):
        return primitive
    elif isinstance(primitive, int):
        return to_bytes(hexstr=hex(primitive))
    elif hexstr is not None:
        if len(hexstr) % 2:
            hexstr = '0x0' + remove_0x_prefix(hexstr)
        return decode_hex(hexstr)
    elif text is not None:
        return text.encode('utf-8')
    raise TypeError("expected an int in first arg, or keyword of hexstr or text")


def to_text(primitive=None, hexstr=None, text=None):
    if bytes is str:
        # must be able to tell the difference between bytes and a hexstr
        raise NotImplementedError("This method only works in Python 3+.")

    assert_one_val(primitive, hexstr=hexstr, text=text)

    if hexstr is not None:
        return to_bytes(hexstr=hexstr).decode('utf-8')
    elif text is not None:
        return text
    elif isinstance(primitive, str):
        return to_text(hexstr=primitive)
    elif isinstance(primitive, bytes):
        return primitive.decode('utf-8')
    elif isinstance(primitive, int):
        byte_encoding = int_to_big_endian(primitive)
        return to_text(byte_encoding)
    raise TypeError("Expected an int, bytes or hexstr.")


@coerce_args_to_bytes
def decode_big_endian_int(value):
    return big_endian_int.deserialize(value.lstrip(b'\x00'))
