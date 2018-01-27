from web3.module import (
    Module,
)
from web3.utils.filters import (
    ShhFilter,
)


class Shh(Module):
    @property
    def version(self):
        return self.web3.manager.request_blocking("shh_version", [])

    def post(self, params):
        if params and ("topics" in params) and ("payload" in params):
            return self.web3.manager.request_blocking("shh_post", [params])
        else:
            raise ValueError(
                "params cannot be None or does not contain fields 'topic' or "
                "'payload'"
            )

    def newIdentity(self):
        return self.web3.manager.request_blocking("shh_newIdentity", [])

    def hasIdentity(self, identity):
        return self.web3.manager.request_blocking("shh_hasIdentity", [identity])

    def newGroup(self):
        return self.web3.manager.request_blocking("shh_newGroup", [])

    def addToGroup(self, params):
        return self.web3.manager.request_blocking("shh_addToGroup", params)

    def filter(self, filter_params):
        if "topics" in filter_params:
            filter_id = self.web3.manager.request_blocking("shh_newFilter", [filter_params])
            return ShhFilter(self.web3, filter_id)
        else:
            raise ValueError("filter params doesnot contain 'topics' to subsrcibe")

    def uninstallFilter(self, filter_id):
        return self.web3.manager.request_blocking("shh_uninstallFilter", [filter_id])

    def getMessages(self, filter_id):
        return self.web3.manager.request_blocking("shh_getMessages", [filter_id])

    def getFilterChanges(self, filter_id):
        return self.web3.manager.request_blocking("shh_getFilterChanges", [filter_id])
