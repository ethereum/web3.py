import web3.solidity.formatters as f
from web3.solidity.address import SolidityTypeAddress
from web3.solidity.bool import SolidityTypeBool
from web3.solidity.int import SolidityTypeInt
from web3.solidity.uint import SolidityTypeUInt
from web3.solidity.dynamicbytes import SolidityTypeDynamicBytes
from web3.solidity.string import SolidityTypeString
from web3.solidity.real import SolidityTypeReal
from web3.solidity.ureal import SolidityTypeUReal
from web3.solidity.bytes import SolidityTypeBytes
import math


class SolidityCoder(object):

    def __init__(self, types):
        self._types = types

    def requireType(self, type):
        """
        This method should be used to transform type to SolidityType
        """
        try:
            solidityType = [t for t in self._types if t.isType(type)][0]
        except KeyError:
            raise Exception("invalid solidity type!: " + type)

        return solidityType

    def encodeParam(self, type, param):
        return self.encodeParams([type], [param])

    def encodeParams(self, types, params):
        solidityTypes = self.getSolidityTypes(types)

        encodeds = []
        for index, solidityType in enumerate(solidityTypes):
            encodeds.append(solidityType.encode(params[index], types[index]))

        dynamicOffset = 0
        for index, solidityType in enumerate(solidityTypes):
            staticPartLength = solidityType.staticPartLength(types[index])
            roundedStaticPartLength = math.floor(
                (staticPartLength + 31) / 32) * 32
            dynamicOffset += roundedStaticPartLength

        result = self.encodeMultiWithOffset(
            types, solidityTypes, encodeds, dynamicOffset)

        return result

    def encodeMultiWithOffset(self, types, solidityTypes, encodeds, dynamicOffset):
        result = u""

        def isDynamic(i):
            if solidityTypes[i].isDynamicArray(types[i]):
                return True
            elif solidityTypes[i].isDynamicType(types[i]):
                return True
            else:
                return False

        for i, t in enumerate(types):
            if isDynamic(i):
                result += f.formatInputInt(dynamicOffset).encode()
                e = self.encodeWithOffset(
                    types[i], solidityTypes[i], encodeds[i], dynamicOffset)
                dynamicOffset += len(e) / 2
            else:
                result += self.encodeWithOffset(
                    types[i], solidityTypes[i], encodeds[i], dynamicOffset)

            # TODO: figure out nested arrays

        for i, t in enumerate(types):
            if isDynamic(i):
                e = self.encodeWithOffset(
                    types[i], solidityTypes[i], encodeds[i], dynamicOffset)
                dynamicOffset += len(e) / 2
                result += e

        return result

    # TODO: refactor whole encoding!
    def encodeWithOffset(self, type, solidityType, encoded, offset):
        if solidityType.isDynamicArray(type):
            nestedName = solidityType.nestedName(type)
            nestedStaticPartLength = solidityType.staticPartLength(nestedName)

            result = encoded[0]

            previousLength = 2
            if solidityType.isDynamicArray(nestedName):
                for i in range(1, len(encoded)):
                    previousLength += encoded[i - 1][0] or 0
                    result += f.formatInputInt(
                        offset + i * nestedStaticPartLength + previousLength * 32).encode()

            for i in range(len(encoded) - 1):
                additionalOffset = result / 2
                result += self.encodeWithOffset(
                    nestedName, solidityType, encoded[i + 1], offset + additionalOffset)

            return result

        elif solidityType.isStaticArray(type):
            nestedName = solidityType.nestedName(type)
            nestedStaticPartLength = solidityType.staticPartLength(nestedName)
            result = ""

            if solidityType.isDynamicArray(nestedName):
                previousLength = 0
                for i in range(len(encoded)):
                    previousLength += encoded[i - 1][0] or 0
                    result += f.formatInputInt(
                        offset + i * nestedStaticPartLength + previousLength * 32).encode()

            for i in range(len(encoded)):
                additionalOffset = result / 2
                result += self.encodeWithOffset(
                    nestedName, solidityType, encoded[i], offset + additionalOffset)

            return result

        return encoded

    def decodeParam(self, type, bytes):
        """
        Should be used to decode bytes to plain param
        """
        return self.decodeParams([type], bytes)[0]

    def decodeParams(self, types, bytes):
        """
        Should be used to decode list of params
        """
        solidityTypes = self.getSolidityTypes(types)
        offsets = self.getOffsets(types, solidityTypes)

        result = []
        for index, solidityType in enumerate(solidityTypes):
            result.append(solidityType.decode(
                bytes, offsets[index], types[index]))

        return result

    def getOffsets(self, types, solidityTypes):
        lengths = []
        for index, solidityType in enumerate(solidityTypes):
            lengths.append(solidityType.staticPartLength(types[index]))

        for i in range(1, len(lengths)):
            lengths[i] += lengths[i - 1]

        for index, length in enumerate(lengths):
            staticPartLength = solidityTypes[
                index].staticPartLength(types[index])
            lengths[index] = length - staticPartLength

        return lengths

    def getSolidityTypes(self, types):
        return [self.requireType(type) for type in types]

coder = SolidityCoder([
    SolidityTypeAddress(),
    SolidityTypeBool(),
    SolidityTypeInt(),
    SolidityTypeUInt(),
    SolidityTypeDynamicBytes(),
    SolidityTypeBytes(),
    SolidityTypeString(),
    SolidityTypeReal(),
    SolidityTypeUReal
])
