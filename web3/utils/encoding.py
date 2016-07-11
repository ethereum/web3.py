# String encodings and numeric representations
import functools
import sys
import binascii
import json

from . import utils

from rlp.utils import (
    decode_hex as _decode_hex,
    encode_hex as _encode_hex,
)


def toHex(val):
    """
    Auto converts any given value into it's hex representation.
    """
    if utils.isBoolean(val):
        return "0x1" if val else "0x0"

    if utils.isObject(val):
        return fromUtf8(json.dumps(val))

    if utils.isString(val):
        if val.startswith("-0x"):
            return fromDecimal(val)
        elif val.startswith("0x"):
            return val
        elif not utils.isNumber(val):
            return fromAscii(val)

    return fromDecimal(val)


def toDecimal(value):
    """
    Converts value to it's decimal representation in string
    """
    if utils.isString(value):
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
    if utils.isString(value):
        if value.startswith("0x") or value.startswith("-0x"):
            value = int(value, 16)
        else:
            value = int(value)

    result = hex(value)
    return result


def toUtf8(hex):
    """
    Should be called to get utf8 from it's hex representation
    """
    if hex.startswith("0x"):
        hex = hex[2:]
    return binascii.unhexlify(hex).decode("utf8")


def toAscii(hex):
    """
    Should be called to get ascii from it's hex representation
    """
    if hex.startswith("0x"):
        hex = hex[2:]
    return binascii.unhexlify(hex).decode("ascii")


def fromUtf8(str):
    """
    Should be called to get hex representation (prefixed by 0x) of utf8 string
    """
    return "0x" + binascii.hexlify(str.encode("utf8")).decode("utf8")


def fromAscii(obj):
    """
    Should be called to get hex representation (prefixed by 0x) of ascii string
    """
    return "0x" + binascii.hexlify(obj.encode("ascii", "ignore")).decode("ascii", "ignore")


def abiToJson(obj):
    """
    Converts abi string to python object
    """
    return json.loads(obj)


if sys.version_info.major == 2:
    integer_types = (int, long)  # NOQA
    bytes_types = (bytes, bytearray)
    text_types = (unicode,)  # NOQA
    string_types = (basestring, bytearray)  # NOQA
else:
    integer_types = (int,)
    bytes_types = (bytes, bytearray)
    text_types = (str,)
    string_types = (bytes, str, bytearray)


def is_integer(value):
    return isinstance(value, integer_types)


def is_bytes(value):
    return isinstance(value, bytes_types)


def is_text(value):
    return isinstance(value, text_types)


def is_string(value):
    return isinstance(value, string_types)


if sys.version_info.major == 2:
    def force_bytes(value):
        if is_bytes(value):
            return str(value)
        elif is_text(value):
            return value.encode('latin1')
        else:
            raise TypeError("Unsupported type: {0}".format(type(value)))

    def force_text(value):
        if is_text(value):
            return value
        elif is_bytes(value):
            return unicode(force_bytes(value), 'latin1')  # NOQA
        else:
            raise TypeError("Unsupported type: {0}".format(type(value)))
else:
    def force_bytes(value):
        if is_bytes(value):
            return bytes(value)
        elif is_text(value):
            return bytes(value, 'latin1')
        else:
            raise TypeError("Unsupported type: {0}".format(type(value)))

    def force_text(value):
        if isinstance(value, text_types):
            return value
        elif isinstance(value, bytes_types):
            return str(value, 'latin1')
        else:
            raise TypeError("Unsupported type: {0}".format(type(value)))


def force_obj_to_bytes(obj):
    if is_string(obj):
        return force_bytes(obj)
    elif isinstance(obj, dict):
        return {
            k: force_obj_to_bytes(v) for k, v in obj.items()
        }
    elif isinstance(obj, (list, tuple)):
        return type(obj)(force_obj_to_bytes(v) for v in obj)
    else:
        return obj


def force_obj_to_text(obj):
    if is_string(obj):
        return force_text(obj)
    elif isinstance(obj, dict):
        return {
            k: force_obj_to_text(v) for k, v in obj.items()
        }
    elif isinstance(obj, (list, tuple)):
        return type(obj)(force_obj_to_text(v) for v in obj)
    else:
        return obj


def coerce_args_to_bytes(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        bytes_args = force_obj_to_bytes(args)
        bytes_kwargs = force_obj_to_bytes(kwargs)
        return fn(*bytes_args, **bytes_kwargs)
    return inner


def coerce_return_to_bytes(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        return force_obj_to_bytes(fn(*args, **kwargs))
    return inner


@coerce_args_to_bytes
def remove_0x_prefix(value):
    if value.startswith(b'0x'):
        return value[2:]
    return value


@coerce_args_to_bytes
def add_0x_prefix(value):
    return b'0x' + remove_0x_prefix(value)


@coerce_args_to_bytes
def decode_hex(value):
    return _decode_hex(remove_0x_prefix(value))


@coerce_args_to_bytes
def encode_hex(value):
    return add_0x_prefix(_encode_hex(value))
