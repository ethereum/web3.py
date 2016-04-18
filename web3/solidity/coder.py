import formatters as f
from address import SolidityTypeAddress
from bool import SolidityTypeBool
from int import SolidityTypeInt
from uint import SolidityTypeUInt
from dynamicbytes import SolidityTypeDynamicBytes
from string import SolidityTypeString
from real import SolidityTypeReal
from ureal import SolidityTypeUReal
from bytes import SolidityTypeBytes

class SolidityCoder(object):

    def __init__(self, types):
        self._types = types

    def requireType(type):
        try:
            solidityType = [t for t in self._types if t.isType(type)][0]
        except KeyError:
            raise Exception("invalid solidity type!: " + type)

        return solidityType

    def encodeParam(type, param):
        return self.encodeParams([type], [param])

    def encodeParams(types, params):
        solidityTypes = self.getSolidityTypes(types)

        for index, solidityType in enumerate(solidityTypes):
            solidityTypes[index] = solidityType.encode(params[index], types[index])

        dynamicOffset = 0
        #look at what solidityType returns