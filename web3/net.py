from typing import (
    NoReturn,
)

from web3.module import (
    Module,
)


class Net(Module):
    @property
    def listening(self) -> bool:
        return self.web3.manager.request_blocking("net_listening", [])

    @property
    def peerCount(self) -> int:
        return self.web3.manager.request_blocking("net_peerCount", [])

    @property
    def chainId(self) -> NoReturn:
        raise DeprecationWarning("This method has been deprecated in EIP 1474.")

    @property
    def version(self) -> int:
        return self.web3.manager.request_blocking("net_version", [])
