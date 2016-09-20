from web3.utils.encoding import (
    to_decimal,
)
from web3.utils.functional import (
    apply_formatters_to_return,
)


class Shh(object):
    """
    TODO: flesh this out.
    """
    def __init__(self, request_manager):
        self.request_manager = request_manager

    @property
    @apply_formatters_to_return(to_decimal)
    def version(self):
        return self.request_manager.request_blocking("shh_version", [])

    def post(self, params):
        if params and ("topic" in params) and ("payload" in params):
            return self.request_manager.request_blocking("shh_post", [params])
        else:
            raise ValueError("params cannot be None or doesnot contain fields 'topic' or 'payload'")

    def newIdentity(self):
        return self.request_manager.request_blocking("shh_newIdentity", [])

    def hasIdentity(self, identity):
        return self.request_manager.request_blocking("shh_hasIdentity", [identity])

    def newGroup(self):
        return self.request_manager.request_blocking("shh_newGroup", [])

    def addToGroup(self, params):
        return self.request_manager.request_blocking("shh_addToGroup", params)
