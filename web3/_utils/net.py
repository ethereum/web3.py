from typing import (
    Callable,
)

from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    DeprecatedMethod,
    Method,
    default_root_munger,
)

listening: Method[Callable[[], bool]] = Method(
    RPC.net_listening,
    mungers=[default_root_munger],
)

peer_count: Method[Callable[[], int]] = Method(
    RPC.net_peerCount,
    mungers=[default_root_munger],
)

version: Method[Callable[[], str]] = Method(
    RPC.net_version,
    mungers=[default_root_munger],
)


#
# Deprecated Methods
#
peerCount = DeprecatedMethod(peer_count, 'peerCount', 'peer_count')
