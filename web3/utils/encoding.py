# String encodings and numeric representations
import functools
import sys
import binascii
import json

from .types import (
    is_bytes,
    is_text,
    is_string,
    is_number,
    is_integer,
    is_boolean,
    is_object,
)
from .formatting import (
    remove_0x_prefix,
    add_0x_prefix,
    is_prefixed,
    is_0x_prefixed,
)


if sys.version_info.major == 2:
    def decode_hex(value):
        if isinstance(value, bytearray):
            value = str(value)
        if not is_string(value):
            raise TypeError('Value must be an instance of str or unicode')
        return remove_0x_prefix(value).decode('hex')

    def encode_hex(value):
        if isinstance(value, bytearray):
            value = str(value)
        if not is_string(value):
            raise TypeError('Value must be an instance of str or unicode')
        return add_0x_prefix(value.encode('hex'))
else:
    def decode_hex(s):
        if isinstance(s, str):
            return bytes.fromhex(remove_0x_prefix(s))
        if isinstance(s, bytes):
            return binascii.unhexlify(remove_0x_prefix(s))
        raise TypeError('Value must be an instance of str or bytes')

    def encode_hex(b):
        if isinstance(b, str):
            b = bytes(b, 'utf-8')
        if isinstance(b, bytes):
            return add_0x_prefix(binascii.hexlify(b))
        raise TypeError('Value must be an instance of str or bytes')


def to_hex(value):
    """
    Auto converts any given value into it's hex representation.
    """
    if is_boolean(value):
        return "0x1" if value else "0x0"

    if is_object(value):
        return encode_hex(json.dumps(value))

    if is_string(value):
        if value.startswith("-0x"):
            return fromDecimal(value)
        elif value.startswith("0x"):
            return value
        elif not is_number(value):
            return fromAscii(value)

    return from_decimal(val)


def to_decimal(value):
    """
    Converts value to it's decimal representation in string
    """
    if is_string(value):
        if value.startswith("0x") or value.startswith("-0x"):
            value = int(value, 16)
        else:
            value = int(value)
    else:
        value = int(value)

    return value


def fromDecimal(value):
    """
    Converts value to it's hex representation
    """
    if is_string(value):
        if is_0x_prefixed(value) or is_prefixed(value, '-0x'):
            value = int(value, 16)
        else:
            value = int(value)

    result = hex(value)
    return result


def fromAscii(obj):
    """
    Should be called to get hex representation (prefixed by 0x) of ascii string
    """
    return "0x" + binascii.hexlify(obj.encode("ascii", "ignore")).decode("ascii", "ignore")
