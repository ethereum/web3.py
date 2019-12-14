from typing import (
    Callable,
)

from eth_typing import (
    ChecksumAddress,
)

from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    Method,
    default_root_munger,
)
from web3.types import (
    BlockNumber,
    Wei,
)

makeDag: Method[Callable[[BlockNumber], bool]] = Method(
    RPC.miner_makeDag,
    mungers=[default_root_munger],
)


setExtra: Method[Callable[[str], bool]] = Method(
    RPC.miner_setExtra,
    mungers=[default_root_munger],
)


setEtherbase: Method[Callable[[ChecksumAddress], bool]] = Method(
    RPC.miner_setEtherbase,
    mungers=[default_root_munger],
)


setGasPrice: Method[Callable[[Wei], bool]] = Method(
    RPC.miner_setGasPrice,
    mungers=[default_root_munger],
)


start: Method[Callable[[int], bool]] = Method(
    RPC.miner_start,
    mungers=[default_root_munger],
)


stop: Method[Callable[[], bool]] = Method(
    RPC.miner_stop,
    mungers=None,
)


startAutoDag: Method[Callable[[], bool]] = Method(
    RPC.miner_startAutoDag,
    mungers=None,
)


stopAutoDag: Method[Callable[[], bool]] = Method(
    RPC.miner_stopAutoDag,
    mungers=None,
)
