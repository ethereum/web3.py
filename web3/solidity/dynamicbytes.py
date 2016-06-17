import web3.solidity.formatters as f
import web3.solidity.types as types
import re


class SolidityTypeDynamicBytes(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputDynamicBytes
        self._outputFormatter = f.formatOutputDynamicBytes

    @classmethod
    def isType(self, name):
        return re.match(r"^bytes(\[([0-9]*)\])*$", name) is not None

    @classmethod
    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)

    @classmethod
    def isDynamicType(self, name):
        return True
