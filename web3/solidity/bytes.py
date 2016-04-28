import web3.solidity.formatters as f
import web3.solidity.types as types
import re


class SolidityTypeBytes(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputBytes
        self._outputFormatter = f.formatOutputBytes

    @classmethod
    def isType(self, name):
        return re.match(r"^bytes([0-9]{1,})(\[([0-9]*)\])*$", name) is not None

    @classmethod
    def staticPartLength(self, name):
        matches = re.search(r"^bytes([0-9]*)", name)
        size = int(matches.groups(1)[0])
        return size * self.staticArrayLength(name)
