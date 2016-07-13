class Db(object):
    def __init__(self, request_manager):
        self.request_manager = request_manager

    def putString(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")

    def getString(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")

    def putHex(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")

    def getHex(self, *args, **kwargs):
        raise DeprecationWarning("This function has been deprecated")
