from typing import (
    Callable,
)

from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    Method,
)
from web3.types import (
    TxPoolContent,
    TxPoolInspect,
    TxPoolStatus,
)

content: Method[Callable[[], TxPoolContent]] = Method(
    RPC.txpool_content,
    is_property=True,
)


inspect: Method[Callable[[], TxPoolInspect]] = Method(
    RPC.txpool_inspect,
    is_property=True,
)


status: Method[Callable[[], TxPoolStatus]] = Method(
    RPC.txpool_status,
    is_property=True,
)
