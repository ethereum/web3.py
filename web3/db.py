class Db(object):
    def __init__(self, web3):
        self.web3 = web3

    def putString(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")

    def getString(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")

    def putHex(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")

    def getHex(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")
