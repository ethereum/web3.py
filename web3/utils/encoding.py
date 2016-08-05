# String encodings and numeric representations
import json
import codecs

from .types import (
    is_string,
    is_boolean,
    is_object,
)
from .string import (
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


def to_hex(value):
    """
    Auto converts any given value into it's hex representation.
    """
    if is_boolean(value):
        return "0x1" if value else "0x0"

    if is_object(value):
        return encode_hex(json.dumps(value))

    if is_string(value):
        if is_prefixed(value, '-0x'):
            return from_decimal(value)
        elif is_0x_prefixed(value):
            return value
        else:
            return encode_hex(value)

    return from_decimal(value)


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
    Converts value to it's hex representation
    """
    if is_string(value):
        if is_0x_prefixed(value) or is_prefixed(value, '-0x'):
            value = int(value, 16)
        else:
            value = int(value)

    result = hex(value).rstrip('L')
    return result
