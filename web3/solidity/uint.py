import solidity.formatters as f
import solidity.types as types
import re


class SolidityTypeUInt(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputInt
        self._outputFormatter = f.formatOutputUInt

    def isType(self, name):
        return re.match(r"^uint([0-9]*)?(\[([0-9]*)\])*$", name) is not None

    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)
