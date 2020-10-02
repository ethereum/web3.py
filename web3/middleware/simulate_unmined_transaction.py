import collections
import itertools
from typing import (
    Any,
    Callable,
)

from eth_typing import (
    Hash32,
)

from web3 import Web3
from web3.types import (
    RPCEndpoint,
    RPCResponse,
    TxReceipt,
)

counter = itertools.count()

INVOCATIONS_BEFORE_RESULT = 5


def unmined_receipt_simulator_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], web3: Web3
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    receipt_counters: DefaultDict[Hash32, TxReceipt] = collections.defaultdict(  # type: ignore # noqa: F821, E501
        itertools.count
    )

    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method == 'eth_getTransactionReceipt':
            txn_hash = params[0]
            if next(receipt_counters[txn_hash]) < INVOCATIONS_BEFORE_RESULT:
                return {'result': None}
            else:
                return make_request(method, params)
        else:
            return make_request(method, params)
    return middleware
