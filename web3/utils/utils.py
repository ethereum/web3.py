"""Utility functions"""

import binascii
import json
import sha3
import re

unitMap = {
    'noether':      '0',
    'wei':          '1',
    'kwei':         '1000',
    'Kwei':         '1000',
    'babbage':      '1000',
    'femtoether':   '1000',
    'mwei':         '1000000',
    'Mwei':         '1000000',
    'lovelace':     '1000000',
    'picoether':    '1000000',
    'gwei':         '1000000000',
    'Gwei':         '1000000000',
    'shannon':      '1000000000',
    'nanoether':    '1000000000',
    'nano':         '1000000000',
    'szabo':        '1000000000000',
    'microether':   '1000000000000',
    'micro':        '1000000000000',
    'finney':       '1000000000000000',
    'milliether':    '1000000000000000',
    'milli':         '1000000000000000',
    'ether':        '1000000000000000000',
    'kether':       '1000000000000000000000',
    'grand':        '1000000000000000000000',
    'mether':       '1000000000000000000000000',
    'gether':       '1000000000000000000000000000',
    'tether':       '1000000000000000000000000000000'
}


def padLeft(string, chars, sign="0"):
    """
    Should be called to pad string to expected length
    """
    return sign*(chars-len(string)+1) + string


def padRight(string, chars, sign="0"):
    """
    Should be called to pad string to expected length
    """
    return string + sign*(chars-len(string)+1)


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


def transformToFullName(json):
    """
    Should be used to create full function/event name from json abi
    """
    if json["name"].find("(") != -1:
        return json["name"]

    typeName = ",".join([i.type for i in json["inputs"]])
    return json["name"] + "(" + typeName + ")"


def extractDisplayName(name):
    """
    Should be called to get display name of contract function
    """
    length = name.find("(")
    return name[:length] if length != -1 else name


def extractTypeName(name):
    """
    Returns overloaded part of function/event name
    """
    length = name.find("(")
    return name[length + 1:len(name) - 1 - (length+1)].replace(" ", "") if length != -1 else ""


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


def toHex(val):
    """
    Auto converts any given value into it's hex representation.
    """
    raise NotImplementedError()


def getValueOfUnit(unit="ether"):
    """
    Returns value of unit in Wei
    """
    unit = unit.lower()
    return unitMap[unit]


def fromWei(number, unit):
    """
    Takes a number of wei and converts it to any other ether unit.
    """
    return number/getValueOfUnit(unit)


def toWei(number, unit):
    """
    Takes a number of a unit and converts it to wei.
    """
    returnValue = int(number)*getValueOfUnit(unit)
    return str(returnValue)


def toBigNumber(number):
    raise NotImplementedError()


def toTwosComplement(number):
    raise NotImplementedError()


def isStrictAddress(address):
    """
    Checks if the given string is strictly an address
    """
    return re.match(r"^0x[0-9a-fA-F]{40}$", address) is not None


def isAddress(address):
    """
    Checks if the given string is an address
    """

    if not re.match(r"^(0x)?[0-9a-fA-F]{40}$", address):
        return False
    elif re.match(r"^(0x)?[0-9a-f]{40}", address) or re.match(r"(0x)?[0-9A-F]{40}$", address):
        return True
    else:
        return isChecksumAddress(address)


def isChecksumAddress(address):
    """
    Checks if the given string is a checksummed address
    """
    address = address.replace("0x", "")
    addressHash = sha3.sha3(address.lower())

    for i in range(40):
        if (int(addressHash[i], 16) > 7 and address[i].upper() != address[i]) or \
                (int(addressHash[i]) <= 7 and address[i].lower() != address[i]):
            return False

    return True


def toChecksumAddress(address):
    """
    Makes a checksum address
    """
    address = address.lower().replace("0x", "")
    addressHash = sha3.sha3(address)
    checksumAddress = "0x"

    for i in range(len(address)):
        if int(addressHash[i], 16) > 7:
            checksumAddress += addressHash[i].upper()
        else:
            checksumAddress += addressHash[i]

    return checksumAddress


def toAddress(address):
    """
    Transforms given string to valid 20 bytes-length addres with 0x prefix
    """
    if isStrictAddress(address):
        return address

    if re.match(r"^[0-9a-f]{3}$", address):
        return "0x"+address

    return "0x" + padLeft(toHex(address)[2:], 40)


def isBigNumber(obj):
    """
    Returns true if object is BigNumber, otherwise false
    """
    raise NotImplementedError()


def isString(obj):
    """
    Returns true if object is string, otherwise false
    """
    return isinstance(obj, str)


def isFunction(obj):
    """
    Returns true if object is function, otherwise false
    """
    return hasattr(obj, "__call__")


def isObject(obj):
    """
    Returns true if object is Objet, otherwise false
    """
    return isinstance(obj, dict)


def isBoolean(obj):
    """
    Returns true if object is boolean, otherwise false
    """
    return isinstance(obj, bool)


def isArray(obj):
    """
    Returns true if object is array, otherwise false
    """
    return isinstance(obj, list)


def isJson(string):
    """
    Returns true if given string is valid json object
    """
    try:
        decoded = json.loads(string)
        if decoded:
            return True
    except ValueError:
        pass
    return False
