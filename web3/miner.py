from web3.method import (
    Method,
    default_root_munger,
)


def makeDag():
    return Method(
        "miner_makeDag",
        mungers=[default_root_munger],
    )


def setExtra():
    return Method(
        "miner_setExtra",
        mungers=[default_root_munger],
    )


def setEtherbase():
    return Method(
        "miner_setEtherbase",
        mungers=[default_root_munger],
    )


def setGasPrice():
    return Method(
        "miner_setGasPrice",
        mungers=[default_root_munger],
    )


def start():
    return Method(
        "miner_start",
        mungers=[default_root_munger],
    )


def stop():
    return Method(
        "miner_stop",
        mungers=None,
    )


def startAutoDag():
    return Method(
        "miner_startAutoDag",
        mungers=None,
    )


def stopAutoDag():
    return Method(
        "miner_stopAutoDag",
        mungers=None,
    )
