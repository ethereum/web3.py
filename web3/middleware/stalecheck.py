import time
from typing import (  # noqa: F401
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
    Optional,
)

from web3.exceptions import (
    StaleBlockchain,
)
from web3.middleware.base import (
    Web3Middleware,
)
from web3.types import (
    BlockData,
    RPCEndpoint,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )

SKIP_STALECHECK_FOR_METHODS = ("eth_getBlockByNumber",)


def _is_fresh(block: BlockData, allowable_delay: int) -> bool:
    if block and (time.time() - block["timestamp"] <= allowable_delay):
        return True
    return False


class StaleCheckMiddleware(Web3Middleware):
    def __init__(
        self,
        allowable_delay: int,
        skip_stalecheck_for_methods: Collection[str] = SKIP_STALECHECK_FOR_METHODS,
    ) -> None:
        if allowable_delay <= 0:
            raise ValueError(
                "You must set a positive allowable_delay in seconds for this middleware"
            )

        self.allowable_delay = allowable_delay
        self.skip_stalecheck_for_methods = skip_stalecheck_for_methods
        self.cache: Dict[str, Optional[BlockData]] = {"latest": None}

    def request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        if method not in self.skip_stalecheck_for_methods:
            if not _is_fresh(self.cache["latest"], self.allowable_delay):
                latest = self._w3.eth.get_block("latest")
                if _is_fresh(latest, self.allowable_delay):
                    self.cache["latest"] = latest
                else:
                    raise StaleBlockchain(latest, self.allowable_delay)

        return params

    # -- async -- #

    async def async_request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        if method not in self.skip_stalecheck_for_methods:
            if not _is_fresh(self.cache["latest"], self.allowable_delay):
                latest = await self._w3.eth.get_block("latest")
                if _is_fresh(latest, self.allowable_delay):
                    self.cache["latest"] = latest
                else:
                    raise StaleBlockchain(latest, self.allowable_delay)

        return params


make_stalecheck_middleware = StaleCheckMiddleware
