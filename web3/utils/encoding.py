# String encodings and numeric representations
import json
import codecs

from rlp.sedes import big_endian_int

from .types import (
    is_string,
    is_boolean,
    is_object,
    is_integer,
)
from .string import (
    coerce_args_to_text,
    coerce_args_to_bytes,
    coerce_return_to_text,
    coerce_return_to_bytes,
)
from .formatting import (
    remove_0x_prefix,
    add_0x_prefix,
    is_prefixed,
    is_0x_prefixed,
)


@coerce_return_to_bytes
def decode_hex(value):
    if not is_string(value):
        raise TypeError('Value must be an instance of str or unicode')
    return codecs.decode(remove_0x_prefix(value), 'hex')


@coerce_args_to_bytes
@coerce_return_to_text
def encode_hex(value):
    if not is_string(value):
        raise TypeError('Value must be an instance of str or unicode')
    return add_0x_prefix(codecs.encode(value, 'hex'))


@coerce_args_to_text
def to_hex(value):
    """
    Auto converts any supported value into it's hex representation.
    """
    if is_boolean(value):
        return "0x1" if value else "0x0"

    if is_object(value):
        return encode_hex(json.dumps(value, sort_keys=True))

    if is_string(value):
        if is_prefixed(value, '-0x'):
            return from_decimal(value)
        elif is_0x_prefixed(value):
            return value
        else:
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
