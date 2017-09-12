# String encodings and numeric representations
import json
import sys
import warnings

from rlp.sedes import big_endian_int

from eth_utils import (
    add_0x_prefix,
    coerce_args_to_bytes,
    force_bytes,
    force_text,
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


def to_decimal(value=None, hexstr=None):
    """
    Converts value to it's decimal representation in string
    """
    if (value is None) == (hexstr is None):
        raise TypeError(
            "Only supply one positional argument, or the hexstr keyword, like: "
            "toDecimal('255') or toDecimal(hexstr='FF')"
        )

    if hexstr is not None:
        return int(hexstr, 16)
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


def to_bytes(primitive=None, hexstr=None, text=None):
    args = (arg for arg in (primitive, text, hexstr) if arg is not None)
    if len(list(args)) != 1:
        raise TypeError(
            "Only supply one positional arg, or the text, or hexstr keyword args. "
            "You supplied %r and %r" % (primitive, {'text': text, 'hexstr': hexstr})
        )

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


def to_text(val):
    if bytes is str:
        # must be able to tell the difference between bytes and a hexstr
        raise NotImplementedError("This method only works in Python 3+.")

    if isinstance(val, str):
        return decode_hex(val).decode('utf-8')
    elif isinstance(val, bytes):
        return val.decode('utf-8')
    elif isinstance(val, int):
        return to_text(hex(val))
    raise TypeError("Expected an int, bytes or hexstr.")


@coerce_args_to_bytes
def decode_big_endian_int(value):
    return big_endian_int.deserialize(value.lstrip(b'\x00'))
