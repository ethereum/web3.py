# String encodings and numeric representations
import binascii
from . import utils
import json


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


def toBigNumber(number):
    raise NotImplementedError()


def toTwosComplement(number):
    raise NotImplementedError()


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
