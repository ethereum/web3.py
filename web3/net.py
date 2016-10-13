from web3.utils.encoding import (
    to_decimal,
)
from web3.utils.functional import (
    apply_formatters_to_return,
)


class Net(object):

    def __init__(self, web3):
        self.web3 = web3

    @property
    def listening(self):
        return self.web3._requestManager.request_blocking("net_listening", [])

    def getListening(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(to_decimal)
    def peerCount(self):
        return self.web3._requestManager.request_blocking("net_peerCount", [])

    def getPeerCount(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")
