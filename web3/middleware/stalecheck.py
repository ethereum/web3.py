import time
from typing import (  # noqa: F401
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
)

from web3.exceptions import (
    StaleBlockchain,
)
from web3.types import (
    BlockData,
    Middleware,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401

SKIP_STALECHECK_FOR_METHODS = set([
    'eth_getBlockByNumber',
])


def _isfresh(block: BlockData, allowable_delay: int) -> bool:
    if block and (time.time() - block['timestamp'] <= allowable_delay):
        return True
    else:
        return False


def make_stalecheck_middleware(
    allowable_delay: int,
    skip_stalecheck_for_methods: Collection[str] = SKIP_STALECHECK_FOR_METHODS
) -> Middleware:
    """
    Use to require that a function will run only of the blockchain is recently updated.

    This middleware takes an argument, so unlike other middleware, you must make the middleware
    with a method call.
    For example: `make_stalecheck_middleware(60*5)`

    If the latest block in the chain is older than 5 minutes in this example, then the
    middleware will raise a StaleBlockchain exception.
    """
    if allowable_delay <= 0:
        raise ValueError("You must set a positive allowable_delay in seconds for this middleware")

    def stalecheck_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], web3: "Web3"
    ) -> Callable[[RPCEndpoint, Any], RPCResponse]:
        cache: Dict[str, BlockData] = {'latest': None}

        def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method not in skip_stalecheck_for_methods:
                if _isfresh(cache['latest'], allowable_delay):
                    pass
                else:
                    latest = web3.eth.get_block('latest')
                    if _isfresh(latest, allowable_delay):
                        cache['latest'] = latest
                    else:
                        raise StaleBlockchain(latest, allowable_delay)

            return make_request(method, params)
        return middleware
    return stalecheck_middleware
