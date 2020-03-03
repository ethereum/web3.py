from typing import (
    NoReturn,
)
import warnings

from web3._utils.rpc_abi import (
    RPC,
)
from web3.module import (
    Module,
)


class Net(Module):
    """
        https://github.com/ethereum/wiki/wiki/JSON-RPC
    """

    @property
    def listening(self) -> bool:
        return self.web3.manager.request_blocking(RPC.net_listening, [])

    @property
    def peer_count(self) -> int:
        return self.web3.manager.request_blocking(RPC.net_peerCount, [])

    @property
    def peerCount(self) -> int:
        warnings.warn(
            "peerCount is deprecated in favor of peer_count",
            category=DeprecationWarning,
        )
        return self.peer_count

    @property
    def chainId(self) -> NoReturn:
        raise DeprecationWarning("This method has been deprecated in EIP 1474.")

    @property
    def version(self) -> str:
        return self.web3.manager.request_blocking(RPC.net_version, [])
