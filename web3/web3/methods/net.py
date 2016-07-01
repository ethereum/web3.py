import web3.utils.encoding as encoding
from web3.utils.functional import (
    apply_formatters_to_return,
)

properties = [
    {
        "name": "listening",
        "call": "net_listening",
    },
    {
        "name": "peerCount",
        "call": "net_peerCount",
        "outputFormatter": encoding.toDecimal
    }
]


class Net(object):

    def __init__(self, request_manager):
        self.request_manager = request_manager

    @property
    def listening(self):
        return self.request_manager.request_blocking("net_listening", [])

    def getListening(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(encoding.toDecimal)
    def peerCount(self):
        return self.request_manager.request_blocking("net_peerCount", [])

    def getPeerCount(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")
