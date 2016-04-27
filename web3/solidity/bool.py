import web3.solidity.formatters as f
import web3.solidity.types as types
import re


class SolidityTypeBool(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputBool
        self._outputFormatter = f.formatOutputBool

    @classmethod
    def isType(self, name):
        return re.match(r"^bool(\[([0-9]*)\])*$", name) is not None

    @classmethod
    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)
