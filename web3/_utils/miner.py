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

make_dag: Method[Callable[[BlockNumber], bool]] = Method(
    RPC.miner_makeDag,
    mungers=[default_root_munger],
)


set_extra: Method[Callable[[str], bool]] = Method(
    RPC.miner_setExtra,
    mungers=[default_root_munger],
)


set_etherbase: Method[Callable[[ChecksumAddress], bool]] = Method(
    RPC.miner_setEtherbase,
    mungers=[default_root_munger],
)


set_gas_price: Method[Callable[[Wei], bool]] = Method(
    RPC.miner_setGasPrice,
    mungers=[default_root_munger],
)


start: Method[Callable[[int], bool]] = Method(
    RPC.miner_start,
    mungers=[default_root_munger],
)


stop: Method[Callable[[], bool]] = Method(
    RPC.miner_stop,
    is_property=True,
)


start_auto_dag: Method[Callable[[], bool]] = Method(
    RPC.miner_startAutoDag,
    is_property=True,
)


stop_auto_dag: Method[Callable[[], bool]] = Method(
    RPC.miner_stopAutoDag,
    is_property=True,
)
