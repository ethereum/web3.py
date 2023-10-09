from typing import (
    Callable,
    List,
)

from eth_typing import HexAddress

from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    Method,
)
from web3.module import (
    Module,
)
from web3.types import Snapshot


class Clique(Module):
    _getSnpashot: Method[Callable[[int], Snapshot]] = Method(
        RPC.clique_getSnapshot
    )
    
    _geSigners: Method[Callable[[], List[HexAddress]]] = Method(
        RPC.clique_getSigners,
        is_property=True,
    )

    _propose: Method[Callable[[str, bool], int]] = Method(
        RPC.clique_propose
    )

    def get_snapshot(self, block_number: int) :
        return self._getSnpashot(block_number)

    @property
    def signers(self) -> List[HexAddress]:
        return self._geSigners()

    def propose(self, signer: HexAddress, a:bool) -> None:
        return self._propose(signer, a)
