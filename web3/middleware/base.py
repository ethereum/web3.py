from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.types import (
        RPCEndpoint,
        RPCResponse,
    )


WEB3 = TypeVar("WEB3", "AsyncWeb3", "Web3")


class Web3Middleware:
    """
    Base class for web3.py middleware. This class is not meant to be used directly,
    but instead inherited from.
    """

    _w3: WEB3

    def request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        return params

    def response_processor(
        self, method: "RPCEndpoint", response: "RPCResponse"
    ) -> "RPCResponse":
        return response

    # -- async -- #

    async def async_request_processor(
        self,
        method: "RPCEndpoint",
        params: Any,
    ) -> Any:
        return params

    async def async_response_processor(
        self,
        method: "RPCEndpoint",
        response: "RPCResponse",
    ) -> "RPCResponse":
        return response
