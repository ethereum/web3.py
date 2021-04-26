from typing import (
    Callable,
    List,
    Tuple,
)

from web3._utils.compat import (
    Protocol,
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
from web3.types import (
    EnodeURI,
    NodeInfo,
    Peer,
)


def admin_start_params_munger(
    module: Module, host: str = 'localhost', port: int = 8546, cors: str = '',
    apis: str = 'eth,net,web3'
) -> Tuple[str, int, str, str]:
    return (host, port, cors, apis)


add_peer: Method[Callable[[EnodeURI], bool]] = Method(
    RPC.admin_addPeer,
    mungers=[default_root_munger],
)


datadir: Method[Callable[[], str]] = Method(
    RPC.admin_datadir,
    mungers=None,
)


node_info: Method[Callable[[], NodeInfo]] = Method(
    RPC.admin_nodeInfo,
    mungers=None,
)


peers: Method[Callable[[], List[Peer]]] = Method(
    RPC.admin_peers,
    mungers=None,
)


class ServerConnection(Protocol):
    def __call__(
        self, host: str = "localhost", port: int = 8546, cors: str = "", apis: str = "eth,net,web3"
    ) -> bool:
        pass


start_rpc: Method[ServerConnection] = Method(
    RPC.admin_startRPC,
    mungers=[admin_start_params_munger],
)


start_ws: Method[ServerConnection] = Method(
    RPC.admin_startWS,
    mungers=[admin_start_params_munger],
)


stop_rpc: Method[Callable[[], bool]] = Method(
    RPC.admin_stopRPC,
    mungers=None,
)


stop_ws: Method[Callable[[], bool]] = Method(
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
