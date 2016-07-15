class Shh(object):
    """
    TODO: flesh this out.
    """
    def __init__(self, request_manager):
        self.request_manager = request_manager

    def post(self, *args, **kwargs):
        raise NotImplementedError("Not Implemented")

    def newIdentity(self, *args, **kwargs):
        raise NotImplementedError("Not Implemented")

    def hasIdentity(self, *args, **kwargs):
        raise NotImplementedError("Not Implemented")

    def newGroup(self, *args, **kwargs):
        raise NotImplementedError("Not Implemented")

    def addToGroup(self, *args, **kwargs):
        raise NotImplementedError("Not Implemented")
