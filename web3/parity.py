from web3.module import (
    Module,
)


class Parity(Module):
    """
    https://paritytech.github.io/wiki/JSONRPC-parity-module
    """
    def enode(self):
        return self.web3.manager.request_blocking(
            "parity_enode",
            [],
        )

    def netPeers(self):
        return self.web3.manager.request_blocking(
            "parity_netPeers",
            [],
        )
