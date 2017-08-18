from web3.utils.module import (
    Module,
)


class Net(Module):
    @property
    def listening(self):
        return self.web3.manager.request_blocking("net_listening", [])

    def getListening(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def peerCount(self):
        return self.web3.manager.request_blocking("net_peerCount", [])

    def getPeerCount(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")
