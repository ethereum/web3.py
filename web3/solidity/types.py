import web3.solidity.formatters as f
from web3.solidity.param import SolidityParam
import math
import re


class SolidityType(object):

    def __init__(self, config):
        self._inputFormatter = config._inputFormatter
        self._outputFormatter = config._outputFormatter

    @classmethod
    def isType(self, name):
        raise Exception("this method should be overwritten for type: " + name)

    @classmethod
    def staticPartLength(self, name):
        raise Exception("this method should be overwritten for type: " + name)

    @classmethod
    def isDynamicArray(self, name):
        nestedTypes = self.nestedTypes(name)
        return nestedTypes and not re.match(r"[0-9]{1,}", nestedTypes[-1])  # regex /g

    @classmethod
    def isStaticArray(self, name):
        nestedTypes = self.nestedTypes(name)
        return nestedTypes and re.match(r"[0-9]{1,}", nestedTypes[-1]) is not None

    @classmethod
    def staticArrayLength(self, name):
        nestedTypes = self.nestedTypes(name)
        if nestedTypes:
            return re.findall(r"[0-9]{1,}", nestedTypes[-1])[0]

        return 1

    @classmethod
    def nestedName(self, name):
        nestedTypes = self.nestedTypes(name)
        if not nestedTypes:
            return name

        return name[:-len(nestedTypes[-1])]

    @classmethod
    def isDynamicType(self, name):
        return False

    @classmethod
    def nestedTypes(self, name):
        return re.findall(r"(\[[0-9]*\])", name)

    def encode(self, value, name):
        if self.isDynamicArray(name):
            length = len(value)
            nestedName = self.nestedName(name)
            result = []
            result.append(f.formatInputInt(length).encode())

            for v in value:
                result.append(self.encode(v, nestedName))

            return result

        elif self.isStaticArray(name):
            length = self.staticArrayLength(name)
            nestedName = self.nestedName(name)

            result = []

            for i in range(length):
                result.append(self.encode(value[i], nestedName))

            return result

        return self._inputFormatter(value).encode()

    def decode(self, bytes, offset, name):
        if self.isDynamicArray(name):
            arrayOffset = int(bytes[offset * 2: offset * 2 + 64], 16)
            length = int(bytes[arrayOffset * 2, arrayOffset * 2 + 64], 16)
            arrayStart = arrayOffset + 32

            nestedName = self.nestedName(name)
            nestedStaticPartLength = self.staticPartLength(nestedName)
            roundedNestedStaticPartLength = math.floor(
                float(nestedStaticPartLength + 31) / 32) * 32

            limit = length * roundedNestedStaticPartLength
            step = roundedNestedStaticPartLength

            result = [
                self.decode(bytes, arrayStart + i, nestedName)
                for i in range(0, limit, step)
            ]

            return result

        elif self.isStaticArray(name):
            length = self.staticArrayLength(name)
            arrayStart = offset

            nestedName = self.nestedName(name)
            nestedStaticPartLength = self.staticPartLength(nestedName)
            roundedNestedStaticPartLength = math.floor(
                float(nestedStaticPartLength + 31) / 32
            ) * 32

            limit = length * roundedNestedStaticPartLength
            step = roundedNestedStaticPartLength

            result = [
                self.decode(bytes, arrayStart + i, nestedName)
                for i in range(0, limit, step)
            ]

            return result

        elif self.isDynamicType(name):
            dynamicOffset = int(bytes[offset * 2: offset * 2 + 64], 16)
            length = int(bytes[dynamicOffset * 2, dynamicOffset * 2 + 64], 16)
            roundedLength = math.floor(float(length + 31) / 32)

            return self._outputFormatter(
                SolidityParam(
                    bytes[dynamicOffset * 2: dynamicOffset * 2 + (1 + roundedLength) * 64],
                    0,
                )
            )

        length = self.staticPartLength(name)
        return self._outputFormatter(SolidityParam(bytes[offset * 2: offset * 2 + length * 2]))
