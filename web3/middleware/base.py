from abc import abstractmethod
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:
    from web3 import (
        AsyncWeb3,
        Web3,
    )
    from web3.types import (
        RPCEndpoint,
        RPCResponse,
    )


class Web3Middleware:
    @abstractmethod
    def process_request_params(
        self, w3: "Web3", method: "RPCEndpoint", params: Any
    ) -> Any:
        return params

    @abstractmethod
    def process_response(
        self, w3: "Web3", method: "RPCEndpoint", response: "RPCResponse"
    ) -> Any:
        return response

    # -- async -- #

    @abstractmethod
    async def async_process_request_params(
        self, async_w3: "AsyncWeb3", method: "RPCEndpoint", params: Any
    ) -> Any:
        return params

    @abstractmethod
    async def async_process_response(
        self, async_w3: "AsyncWeb3", method: "RPCEndpoint", response: "RPCResponse"
    ) -> Any:
        return response
