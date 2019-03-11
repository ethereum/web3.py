from web3.module import (
    Module,
)
from web3.utils.decorators import (
    deprecated_in_v5,
)


class Net(Module):
    @property
    def listening(self):
        return self.web3.manager.request_blocking("net_listening", [])

    @property
    def peerCount(self):
        return self.web3.manager.request_blocking("net_peerCount", [])

    @property
    @deprecated_in_v5
    def chainId(self):
        return None

    @property
    def version(self):
        return self.web3.manager.request_blocking("net_version", [])
