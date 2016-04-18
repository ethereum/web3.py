import formatters as f
import types
import re

class SolidityTypeInt(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputInt
        self._outputFormatter = f.formatOutputInt

    def isType(self, name):
        return re.match(r"^int([0-9]*)?(\[([0-9]*)\])*$", name) is not None

    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)