from web3.module import (
    Module,
)


class Net(Module):
    @property
    def listening(self):
        return self.web3.manager.request_blocking("net_listening", [])

    @property
    def peerCount(self):
        return self.web3.manager.request_blocking("net_peerCount", [])

    @property
    def chainId(self):
        return self.version

    @property
    def version(self):
        return self.web3.manager.request_blocking("net_version", [])
