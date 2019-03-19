from web3.method import (
    Method,
    default_root_munger,
)


def admin_start_params_munger(module, host='localhost', port='8546', cors='', apis='eth,net,web3'):
    return module, [host, port, cors, apis]


def addPeer():
    return Method(
        "admin_addPeer",
        mungers=[default_root_munger],
    )


def datadir():
    return Method(
        "admin_datadir",
        mungers=None,
    )


def nodeInfo():
    return Method(
        "admin_nodeInfo",
        mungers=None,
    )


def peers():
    return Method(
        "admin_peers",
        mungers=None,
    )


def setSolc():
    return Method(
        "admin_setSolc",
        mungers=[default_root_munger],
    )


def startRPC():
    return Method(
        "admin_startRPC",
        mungers=[admin_start_params_munger],
    )


def startWS():
    return Method(
        "admin_startWS",
        mungers=[admin_start_params_munger],
    )


def stopRPC():
    return Method(
        "admin_stopRPC",
        mungers=None,
    )


def stopWS():
    return Method(
        "admin_stopWS",
        mungers=None,
    )
