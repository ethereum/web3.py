import time
from typing import (  # noqa: F401
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
    Optional,
)

from toolz import curry

from web3.exceptions import (
    StaleBlockchain,
)
from web3.middleware.base import (
    Web3Middleware,
    Web3MiddlewareBuilder,
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


class StaleCheckMiddlewareBuilder(Web3MiddlewareBuilder):
    allowable_delay: int
    skip_stalecheck_for_methods: Collection[str]
    cache: Dict[str, Optional[BlockData]]

    @staticmethod
    @curry
    def build(
        allowable_delay: int,
        w3,
        skip_stalecheck_for_methods: Collection[str] = SKIP_STALECHECK_FOR_METHODS,
    ) -> Web3Middleware:
        if allowable_delay <= 0:
            raise ValueError(
                "You must set a positive allowable_delay in seconds for this middleware"
            )
        middleware = StaleCheckMiddlewareBuilder(w3)
        middleware.allowable_delay = allowable_delay
        middleware.skip_stalecheck_for_methods = skip_stalecheck_for_methods
        middleware.cache = {"latest": None}
        return middleware

    def request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        if method not in self.skip_stalecheck_for_methods:
            if not _is_fresh(self.cache["latest"], self.allowable_delay):
                latest = self._w3.eth.get_block("latest")
                if _is_fresh(latest, self.allowable_delay):
                    self.cache["latest"] = latest
                else:
                    raise StaleBlockchain(latest, self.allowable_delay)

        return method, params

    # -- async -- #

    async def async_request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        if method not in self.skip_stalecheck_for_methods:
            if not _is_fresh(self.cache["latest"], self.allowable_delay):
                latest = await self._w3.eth.get_block("latest")
                if _is_fresh(latest, self.allowable_delay):
                    self.cache["latest"] = latest
                else:
                    raise StaleBlockchain(latest, self.allowable_delay)

        return method, params


make_stalecheck_middleware = StaleCheckMiddlewareBuilder.build
