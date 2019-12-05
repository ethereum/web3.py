import itertools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Sequence,
    Tuple,
    cast,
)

from eth_utils import (
    to_bytes,
    to_text,
)

from web3._utils.encoding import (
    FriendlyJsonSerde,
)
from web3.middleware import (
    combine_middlewares,
)
from web3.types import (
    Middleware,
    MiddlewareOnion,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


class BaseProvider:
    _middlewares: Tuple[Middleware, ...] = ()
    # a tuple of (all_middlewares, request_func)
    _request_func_cache: Tuple[Tuple[Middleware, ...], Callable[..., RPCResponse]] = (None, None)

    @property
    def middlewares(self) -> Tuple[Middleware, ...]:
        return self._middlewares

    @middlewares.setter
    def middlewares(
        self, values: MiddlewareOnion
    ) -> None:
        # tuple(values) converts to MiddlewareOnion -> Tuple[Middleware, ...]
        self._middlewares = tuple(values)  # type: ignore

    def request_func(
        self, web3: "Web3", outer_middlewares: MiddlewareOnion
    ) -> Callable[..., RPCResponse]:
        """
        @param outer_middlewares is an iterable of middlewares, ordered by first to execute
        @returns a function that calls all the middleware and eventually self.make_request()
        """
        # type ignored b/c tuple(MiddlewareOnion) converts to tuple of middlewares
        all_middlewares: Tuple[Middleware] = tuple(outer_middlewares) + tuple(self.middlewares)  # type: ignore # noqa: E501

        cache_key = self._request_func_cache[0]
        if cache_key is None or cache_key != all_middlewares:
            self._request_func_cache = (
                all_middlewares,
                self._generate_request_func(web3, all_middlewares)
            )
        return self._request_func_cache[-1]

    def _generate_request_func(
        self, web3: "Web3", middlewares: Sequence[Middleware]
    ) -> Callable[..., RPCResponse]:
        return combine_middlewares(
            middlewares=middlewares,
            web3=web3,
            provider_request_fn=self.make_request,
        )

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Providers must implement this method")

    def isConnected(self) -> bool:
        raise NotImplementedError("Providers must implement this method")


class JSONBaseProvider(BaseProvider):
    def __init__(self) -> None:
        self.request_counter = itertools.count()

    def decode_rpc_response(self, raw_response: bytes) -> RPCResponse:
        text_response = to_text(raw_response)
        return cast(RPCResponse, FriendlyJsonSerde().json_decode(text_response))

    def encode_rpc_request(self, method: RPCEndpoint, params: Any) -> bytes:
        rpc_dict = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(self.request_counter),
        }
        encoded = FriendlyJsonSerde().json_encode(rpc_dict)
        return to_bytes(text=encoded)

    def isConnected(self) -> bool:
        try:
            response = self.make_request(RPCEndpoint('web3_clientVersion'), [])
        except IOError:
            return False

        assert response['jsonrpc'] == '2.0'
        assert 'error' not in response

        return True
