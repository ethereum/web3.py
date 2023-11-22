import itertools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Set,
    Tuple,
    cast,
)

from eth_utils import (
    to_bytes,
    to_text,
)

from web3._utils.encoding import (
    FriendlyJsonSerde,
    Web3JsonEncoder,
)
from web3.exceptions import (
    ProviderConnectionError,
)
from web3.middleware import (
    Web3Middleware,
    combine_middlewares,
)
from web3.types import (
    Middleware,
    MiddlewareOnion,
    RPCEndpoint,
    RPCResponse,
)
from web3.utils import (
    SimpleCache,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


CACHEABLE_REQUESTS = cast(
    Set[RPCEndpoint],
    (
        "eth_chainId",
        "eth_getBlockByHash",
        "eth_getBlockTransactionCountByHash",
        "eth_getRawTransactionByHash",
        "eth_getTransactionByBlockHashAndIndex",
        "eth_getTransactionByHash",
        "eth_getUncleByBlockHashAndIndex",
        "eth_getUncleCountByBlockHash",
        "net_version",
        "web3_clientVersion",
    ),
)


class BaseProvider:
    _middlewares: Tuple[Middleware, ...] = ()
    _request_func_cache: Tuple[
        Tuple[Web3Middleware, ...], Callable[..., RPCResponse]
    ] = (None, None)

    _request_cache: SimpleCache = SimpleCache(size=500)
    _cache_allowed_requests: bool = True
    _cacheable_requests: Set[RPCEndpoint] = CACHEABLE_REQUESTS

    is_async = False
    has_persistent_connection = False
    global_ccip_read_enabled: bool = True
    ccip_read_max_redirects: int = 4

    @property
    def middlewares(self) -> Tuple[Web3Middleware, ...]:
        return self._middlewares

    @middlewares.setter
    def middlewares(self, values: MiddlewareOnion) -> None:
        # tuple(values) converts to MiddlewareOnion -> Tuple[Middleware, ...]
        self._middlewares = tuple(values)  # type: ignore

    def request_func(
        self, w3: "Web3", outer_middlewares: MiddlewareOnion
    ) -> Callable[..., RPCResponse]:
        """
        @param w3 is the web3 instance
        @param outer_middlewares is an iterable of middlewares,
            ordered by first to execute
        @returns a function that calls all the middleware and
            eventually self.make_request()
        """
        # type ignored b/c tuple(MiddlewareOnion) converts to tuple of middlewares
        all_middlewares: Tuple[Web3Middleware] = tuple(outer_middlewares) + tuple(self.middlewares)  # type: ignore # noqa: E501

        cache_key = self._request_func_cache[0]
        if cache_key != all_middlewares:
            self._request_func_cache = (
                all_middlewares,
                combine_middlewares(
                    middlewares=all_middlewares,
                    w3=w3,
                    provider_request_fn=self.make_request,
                ),
            )

        return self._request_func_cache[-1]

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Providers must implement this method")

    def is_connected(self, show_traceback: bool = False) -> bool:
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
        encoded = FriendlyJsonSerde().json_encode(rpc_dict, Web3JsonEncoder)
        return to_bytes(text=encoded)

    def is_connected(self, show_traceback: bool = False) -> bool:
        try:
            response = self.make_request(RPCEndpoint("web3_clientVersion"), [])
        except OSError as e:
            if show_traceback:
                raise ProviderConnectionError(
                    f"Problem connecting to provider with error: {type(e)}: {e}"
                )
            return False

        if "error" in response:
            if show_traceback:
                raise ProviderConnectionError(
                    f"Error received from provider: {response}"
                )
            return False

        if response["jsonrpc"] == "2.0":
            return True
        else:
            if show_traceback:
                raise ProviderConnectionError(f"Bad jsonrpc version: {response}")
            return False
