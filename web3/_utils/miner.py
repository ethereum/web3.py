from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    Method,
    default_root_munger,
)

makeDag = Method(
    RPC.miner_makeDag,
    mungers=[default_root_munger],
)


setExtra = Method(
    RPC.miner_setExtra,
    mungers=[default_root_munger],
)


setEtherbase = Method(
    RPC.miner_setEtherbase,
    mungers=[default_root_munger],
)


setGasPrice = Method(
    RPC.miner_setGasPrice,
    mungers=[default_root_munger],
)


start = Method(
    RPC.miner_start,
    mungers=[default_root_munger],
)


stop = Method(
    RPC.miner_stop,
    mungers=None,
)


startAutoDag = Method(
    RPC.miner_startAutoDag,
    mungers=None,
)


stopAutoDag = Method(
    RPC.miner_stopAutoDag,
    mungers=None,
)
