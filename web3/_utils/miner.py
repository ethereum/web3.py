from web3.method import (
    Method,
    default_root_munger,
)

makeDag = Method(
    "miner_makeDag",
    mungers=[default_root_munger],
)


setExtra = Method(
    "miner_setExtra",
    mungers=[default_root_munger],
)


setEtherbase = Method(
    "miner_setEtherbase",
    mungers=[default_root_munger],
)


setGasPrice = Method(
    "miner_setGasPrice",
    mungers=[default_root_munger],
)


start = Method(
    "miner_start",
    mungers=[default_root_munger],
)


stop = Method(
    "miner_stop",
    mungers=None,
)


startAutoDag = Method(
    "miner_startAutoDag",
    mungers=None,
)


stopAutoDag = Method(
    "miner_stopAutoDag",
    mungers=None,
)
