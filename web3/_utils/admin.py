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
    _module: Module,
    host: str = "localhost",
    port: int = 8546,
    cors: str = "",
    apis: str = "eth,net,web3",
) -> Tuple[str, int, str, str]:
    return (host, port, cors, apis)


add_peer: Method[Callable[[EnodeURI], bool]] = Method(
    RPC.admin_addPeer,
    mungers=[default_root_munger],
)


datadir: Method[Callable[[], str]] = Method(
    RPC.admin_datadir,
    is_property=True,
)


node_info: Method[Callable[[], NodeInfo]] = Method(
    RPC.admin_nodeInfo,
    is_property=True,
)


peers: Method[Callable[[], List[Peer]]] = Method(
    RPC.admin_peers,
    is_property=True,
)


class ServerConnection(Protocol):
    def __call__(
        self,
        host: str = "localhost",
        port: int = 8546,
        cors: str = "",
        apis: str = "eth,net,web3",
    ) -> bool:
        pass


start_http: Method[ServerConnection] = Method(
    RPC.admin_startHTTP,
    mungers=[admin_start_params_munger],
)


start_ws: Method[ServerConnection] = Method(
    RPC.admin_startWS,
    mungers=[admin_start_params_munger],
)


stop_http: Method[Callable[[], bool]] = Method(
    RPC.admin_stopHTTP,
    is_property=True,
)


stop_ws: Method[Callable[[], bool]] = Method(
    RPC.admin_stopWS,
    is_property=True,
)
