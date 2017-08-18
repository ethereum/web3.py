from web3.utils.module import (
    Module,
)


class Db(Module):
    def putString(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")

    def getString(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")

    def putHex(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")

    def getHex(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")
