from web3.utils import (
    utils,
    encoding,
)
from web3.solidity.param import SolidityParam
from math import floor


def formatInputInt(value):
    if utils.isString(value) and value.startswith("0x"):
        value = int(value, 16)
    else:
        value = int(value)
    result = utils.padLeft(hex(value)[2:], 64)  # utils.toTwosComplement
    return SolidityParam(result)


def formatInputBytes(value):
    result = encoding.toHex(value)[2:]
    l = floor(float(len(result) + 63) / 64)
    result = utils.padRight(result, l * 64)
    return SolidityParam(result)


def formatInputDynamicBytes(value):
    result = encoding.toHex(value)[2:]
    length = len(result) / 2
    l = floor(float(len(result) + 63) / 64)
    result = utils.padRight(result, l * 64)
    return SolidityParam(formatInputInt(length).value + result)


def formatInputString(value):
    result = encoding.fromUtf8(value)[2:]
    length = len(result) / 2
    l = floor(float(len(result) + 63) / 64)
    result = utils.padRight(result, l * 64)
    return SolidityParam(formatInputInt(length).value + result)


def formatInputBool(value):
    result = "0" * 63 + ("1" if value else "0")
    return SolidityParam(result)


def formatInputReal(value):
    return formatInputInt(value * 2 ** 128)


def formatOutputInt(param):
    value = param.staticPart()
    if not value:
        value = "0"

    # if value < 0:
    #    return int(value, 16) - int("f" * 64, 16) + 1

    return int(value, 16)


def formatOutputUInt(param):
    value = param.staticPart()
    if not value:
        value = "0"
    return int(value, 16)


def formatOutputReal(param):
    return formatOutputInt(param) / 2 ** 128


def formatOutputUReal(param):
    return formatOutputInt(param) / 2 ** 128


def formatOutputBool(param):
    if param.staticPart() == "0" * 63 + "1":
        return True
    else:
        return False


def formatOutputBytes(param):
    return "0x" + param.staticPart()


def formatOutputDynamicBytes(param):
    length = int(param.dynamicPart()[:64], 16) * 2
    return "0x" + param.dynamicPart()[64:64 + length]


def formatOutputString(param):
    length = int(param.dynamicPart()[:64], 16) * 2
    return encoding.toUtf8(param.dynamicPart()[64:64 + length])


def formatOutputAddress(param):
    value = param.staticPart()
    return "0x" + value[len(value) - 40:]
