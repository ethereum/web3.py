import formatters as f
import types
import re

class SolidityTypeDynamicBytes(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputDynamicBytes
        self._outputFormatter = f.formatOutputDynamicBytes

    def isType(self, name):
        return re.match(r"^bytes(\[([0-9]*)\])*$", name) is not None

    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)

    def isDynamicType(self):
        return True