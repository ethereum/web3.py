from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    Method,
)

content = Method(
    RPC.txpool_content,
    mungers=None,
)


inspect = Method(
    RPC.txpool_inspect,
    mungers=None,
)


status = Method(
    RPC.txpool_status,
    mungers=None,
)
