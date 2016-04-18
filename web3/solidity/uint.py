import formatters as f
import types
import re

class SolidityTypeUInt(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputUInt
        self._outputFormatter = f.formatOutputUInt

    def isType(self, name):
        return re.match(r"^uint([0-9]*)?(\[([0-9]*)\])*$", name) is not None

    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)