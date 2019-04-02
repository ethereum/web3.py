from web3.method import (
    Method,
    default_root_munger,
)


def admin_start_params_munger(module, host='localhost', port='8546', cors='', apis='eth,net,web3'):
    return (host, port, cors, apis)


addPeer = Method(
    "admin_addPeer",
    mungers=[default_root_munger],
)


datadir = Method(
    "admin_datadir",
    mungers=None,
)


nodeInfo = Method(
    "admin_nodeInfo",
    mungers=None,
)


peers = Method(
    "admin_peers",
    mungers=None,
)


setSolc = Method(
    "admin_setSolc",
    mungers=[default_root_munger],
)


startRPC = Method(
    "admin_startRPC",
    mungers=[admin_start_params_munger],
)


startWS = Method(
    "admin_startWS",
    mungers=[admin_start_params_munger],
)


stopRPC = Method(
    "admin_stopRPC",
    mungers=None,
)


stopWS = Method(
    "admin_stopWS",
    mungers=None,
)
