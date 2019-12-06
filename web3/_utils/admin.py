from typing import (
    Tuple,
)

from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    DeprecatedMethod,
    Method,
    default_root_munger,
)
from web3.module import (
    Module,
)


def admin_start_params_munger(
    module: Module, host: str='localhost', port: str='8546', cors: str='', apis: str='eth,net,web3'
) -> Tuple[str, str, str, str]:
    return (host, port, cors, apis)


add_peer = Method(
    RPC.admin_addPeer,
    mungers=[default_root_munger],
)


datadir = Method(
    RPC.admin_datadir,
    mungers=None,
)


node_info = Method(
    RPC.admin_nodeInfo,
    mungers=None,
)


peers = Method(
    RPC.admin_peers,
    mungers=None,
)


start_rpc = Method(
    RPC.admin_startRPC,
    mungers=[admin_start_params_munger],
)


start_ws = Method(
    RPC.admin_startWS,
    mungers=[admin_start_params_munger],
)


stop_rpc = Method(
    RPC.admin_stopRPC,
    mungers=None,
)


stop_ws = Method(
    RPC.admin_stopWS,
    mungers=None,
)

#
# Deprecated Methods
#
addPeer = DeprecatedMethod(add_peer, 'addPeer', 'add_peer')
nodeInfo = DeprecatedMethod(node_info, 'nodeInfo', 'node_info')
startRPC = DeprecatedMethod(start_rpc, 'startRPC', 'start_rpc')
stopRPC = DeprecatedMethod(stop_rpc, 'stopRPC', 'stop_rpc')
startWS = DeprecatedMethod(start_ws, 'startWS', 'start_ws')
stopWS = DeprecatedMethod(stop_ws, 'stopWS', 'stop_ws')
