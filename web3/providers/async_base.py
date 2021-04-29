import itertools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    cast,
)

from eth_utils import (
    to_bytes,
    to_text,
)

from web3._utils.encoding import (
    FriendlyJsonSerde,
)
from web3.types import (
    MiddlewareOnion,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


class AsyncBaseProvider:
    def request_func(
        self, web3: "Web3", outer_middlewares: MiddlewareOnion
    ) -> Callable[[RPCEndpoint, Any], Coroutine[Any, Any, RPCResponse]]:
        # Placeholder - manager calls self.provider.request_func
        # Eventually this will handle caching and return make_request
        # along with all the middleware
        return self.make_request

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Providers must implement this method")

    async def isConnected(self) -> bool:
        raise NotImplementedError("Providers must implement this method")


class AsyncJSONBaseProvider(AsyncBaseProvider):
    def __init__(self) -> None:
        self.request_counter = itertools.count()

    async def encode_rpc_request(self, method: RPCEndpoint, params: Any) -> bytes:
        rpc_dict = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(self.request_counter),
        }
        encoded = FriendlyJsonSerde().json_encode(rpc_dict)
        return to_bytes(text=encoded)

    async def decode_rpc_response(self, raw_response: bytes) -> RPCResponse:
        text_response = to_text(raw_response)
        return cast(RPCResponse, FriendlyJsonSerde().json_decode(text_response))

    async def isConnected(self) -> bool:
        try:
            response = await self.make_request(RPCEndpoint('web3_clientVersion'), [])
        except IOError:
            return False

        assert response['jsonrpc'] == '2.0'
        assert 'error' not in response

        return True
