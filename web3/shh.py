from web3 import formatters
from web3.utils.encoding import (
    to_decimal,
)
from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.utils.filters import (
    ShhFilter,
)


class Shh(object):
    """
    TODO: flesh this out.
    """
    def __init__(self, web3):
        self.web3 = web3

    @property
    def request_manager(self):
        return self.web3._requestManager

    @property
    @apply_formatters_to_return(to_decimal)
    def version(self):
        return self.request_manager.request_blocking("shh_version", [])

    def post(self, params):
        if params and ("topics" in params) and ("payload" in params):
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

    def filter(self, filter_params):
        if "topics" in filter_params:
            filter_id = self.request_manager.request_blocking("shh_newFilter", [filter_params])
            return ShhFilter(self.web3, filter_id)
        else:
            raise ValueError("filter params doesnot contain 'topics' to subsrcibe")

    def uninstallFilter(self, filter_id):
        return self.request_manager.request_blocking("shh_uninstallFilter", [filter_id])

    @apply_formatters_to_return(formatters.log_array_formatter)
    def getMessages(self, filter_id):
        return self.request_manager.request_blocking("shh_getMessages", [filter_id])

    @apply_formatters_to_return(formatters.log_array_formatter)
    def getFilterChanges(self, filter_id):
        return self.request_manager.request_blocking("shh_getFilterChanges", [filter_id])
