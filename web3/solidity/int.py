import web3.solidity.formatters as f
import web3.solidity.types as types
import re


class SolidityTypeInt(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputInt
        self._outputFormatter = f.formatOutputInt

    @classmethod
    def isType(self, name):
        return re.match(r"^int([0-9]*)?(\[([0-9]*)\])*$", name) is not None

    @classmethod
    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)
