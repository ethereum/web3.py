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

    @property
    def info(self):
        return self.web3.manager.request_blocking("shh_info", [])

    def setMaxMessageSize(self, size):
        return self.web3.manager.request_blocking("shh_setMaxMessageSize", [size])

    def setMinPoW(self, min_pow):
        return self.web3.manager.request_blocking("shh_setMinPoW", [min_pow])

    def markTrustedPeer(self, enode):
        return self.web3.manager.request_blocking("shh_markTrustedPeer", [enode])

    def newKeyPair(self):
        return self.web3.manager.request_blocking("shh_newKeyPair", [])

    def addPrivateKey(self, key):
        return self.web3.manager.request_blocking("shh_addPrivateKey", [key])

    def deleteKeyPair(self, id):
        return self.web3.manager.request_blocking("shh_deleteKeyPair", [id])

    def hasKeyPair(self, id):
        return self.web3.manager.request_blocking("shh_hasKeyPair", [id])

    def getPublicKey(self, id):
        return self.web3.manager.request_blocking("shh_getPublicKey", [id])

    def getPrivateKey(self, id):
        return self.web3.manager.request_blocking("shh_getPrivateKey", [id])

    def newSymKey(self):
        return self.web3.manager.request_blocking("shh_newSymKey", [])

    def addSymKey(self, key):
        return self.web3.manager.request_blocking("shh_addSymKey", [key])

    def generateSymKeyFromPassword(self, password):
        return self.web3.manager.request_blocking("shh_generateSymKeyFromPassword", [password])

    def hasSymKey(self, id):
        return self.web3.manager.request_blocking("shh_hasSymKey", [id])

    def getSymKey(self, id):
        return self.web3.manager.request_blocking("shh_getSymKey", [id])

    def deleteSymKey(self, id):
        return self.web3.manager.request_blocking("shh_deleteSymKey", [id])

    def post(self, message):
        if message and ("payload" in message):
            return self.web3.manager.request_blocking("shh_post", [message])
        else:
            raise ValueError(
                "message cannot be None or does not contain field 'payload'"
            )

    def newMessageFilter(self, criteria, poll_interval=None):
        filter_id = self.web3.manager.request_blocking("shh_newMessageFilter", [criteria])
        return ShhFilter(self.web3, filter_id, poll_interval=poll_interval)

    def deleteMessageFilter(self, filter_id):
        return self.web3.manager.request_blocking("shh_deleteMessageFilter", [filter_id])

    def getMessages(self, filter_id):
        return self.web3.manager.request_blocking("shh_getFilterMessages", [filter_id])
