# String encodings and numeric representations
import binascii


def toHex(val):
    """
    Auto converts any given value into it's hex representation.
    """
    raise NotImplementedError()


def toBigNumber(number):
    raise NotImplementedError()


def toTwosComplement(number):
    raise NotImplementedError()


def toDecimal(value):
    """
    Converts value to it's decimal representation in string
    """
    return int(value)


def fromDecimal(value):
    """
    Converts value to it's hex representation
    """
    number = int(value)
    result = str(number, 16)

    if number < 0:
        return "-0x"+result[1:]
    else:
        return "0x"+result


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
    return binascii.hexlify(str.encode("utf8"))


def fromAscii(str):
    """
    Should be called to get hex representation (prefixed by 0x) of ascii string
    """
    return binascii.hexlify(str.encode("ascii"))
