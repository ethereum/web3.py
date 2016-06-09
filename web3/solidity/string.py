import web3.solidity.formatters as f
import web3.solidity.types as types
import re


class SolidityTypeString(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputString
        self._outputFormatter = f.formatOutputString

    @classmethod
    def isType(self, name):
        return re.match(r"^string(\[([0-9]*)\])*$", name) is not None

    @classmethod
    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)

    @classmethod
    def isDynamicType(self, name):
        return True
