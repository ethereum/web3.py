import itertools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Sequence,
    Tuple,
    cast,
)
import warnings

from eth_utils import (
    to_bytes,
    to_text,
)

from web3._utils.encoding import (
    FriendlyJsonSerde,
)
from web3.middleware import (
    async_combine_middlewares,
)
from web3.types import (
    Middleware,
    MiddlewareOnion,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


class AsyncBaseProvider:
    _middlewares: Tuple[Middleware, ...] = ()
    # a tuple of (all_middlewares, request_func)
    _request_func_cache: Tuple[Tuple[Middleware, ...], Callable[..., RPCResponse]] = (None, None)

    def __init__(self) -> None:
        warnings.warn(
            "Async providers are still being developed and refined. "
            "Expect breaking changes in minor releases.")

    @property
    def middlewares(self) -> Tuple[Middleware, ...]:
        return self._middlewares

    @middlewares.setter
    def middlewares(
        self, values: MiddlewareOnion
    ) -> None:
        # tuple(values) converts to MiddlewareOnion -> Tuple[Middleware, ...]
        self._middlewares = tuple(values)  # type: ignore

    async def request_func(
        self, web3: "Web3", outer_middlewares: MiddlewareOnion
    ) -> Callable[[RPCEndpoint], Any]:
        all_middlewares: Tuple[Middleware] = tuple(outer_middlewares) + tuple(self.middlewares)  # type: ignore # noqa: E501

        cache_key = self._request_func_cache[0]
        if cache_key is None or cache_key != all_middlewares:
            self._request_func_cache = (
                all_middlewares,
                await self._generate_request_func(web3, all_middlewares)
            )
        return self._request_func_cache[-1]

    async def _generate_request_func(
        self, web3: "Web3", middlewares: Sequence[Middleware]
    ) -> Callable[..., RPCResponse]:
        return await async_combine_middlewares(
            middlewares=middlewares,
            web3=web3,
            provider_request_fn=self.make_request,
        )

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Providers must implement this method")

    async def isConnected(self) -> bool:
        raise NotImplementedError("Providers must implement this method")


class AsyncJSONBaseProvider(AsyncBaseProvider):
    def __init__(self) -> None:
        self.request_counter = itertools.count()

    def encode_rpc_request(self, method: RPCEndpoint, params: Any) -> bytes:
        rpc_dict = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(self.request_counter),
        }
        encoded = FriendlyJsonSerde().json_encode(rpc_dict)
        return to_bytes(text=encoded)

    def decode_rpc_response(self, raw_response: bytes) -> RPCResponse:
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
