import solidity.formatters as f
import solidity.types as types
import re


class SolidityTypeString(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputString
        self._outputFormatter = f.formatOutputString

    def isType(self, name):
        return re.match(r"^string(\[([0-9]*)\])*$", name) is not None

    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)

    def isDynamicType(self):
        return True
