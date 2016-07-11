import web3.web3.formatters as formatters


# TODO: remove this list
methods = [
    {
        "name": "post",
        "call": "shh_post",
        "params": 1,
        "inputFormatter": [formatters.inputPostFormatter]
    },
    {
        "name": "newIdentity",
        "call": "shh_newIdentity",
        "params": 0
    },
    {
        "name": "hasIdentity",
        "call": "shh_hasIdentity",
        "params": 1
    },
    {
        "name": "newGroup",
        "call": "shh_newGroup",
        "params": 0
    },
    {
        "name": "addToGroup",
        "call": "shh_addToGroup",
        "params": 0
    }
]


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
