import itertools
import threading
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

from web3._utils.caching import (
    handle_request_caching,
)
from web3._utils.encoding import (
    FriendlyJsonSerde,
    Web3JsonEncoder,
)
from web3.exceptions import (
    ProviderConnectionError,
)
from web3.middleware import (
    combine_middleware,
)
from web3.middleware.base import (
    Middleware,
    MiddlewareOnion,
)
from web3.types import (
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
    # a tuple of (middleware, request_func)
    _request_func_cache: Tuple[Tuple[Middleware, ...], Callable[..., RPCResponse]] = (
        None,
        None,
    )

    is_async = False
    has_persistent_connection = False
    global_ccip_read_enabled: bool = True
    ccip_read_max_redirects: int = 4

    # request caching
    cache_allowed_requests: bool = False
    cacheable_requests: Set[RPCEndpoint] = CACHEABLE_REQUESTS
    _request_cache: SimpleCache
    _request_cache_lock: threading.Lock = threading.Lock()

    def __init__(self) -> None:
        self._request_cache = SimpleCache(1000)

    def request_func(
        self, w3: "Web3", middleware_onion: MiddlewareOnion
    ) -> Callable[..., RPCResponse]:
        """
        @param w3 is the web3 instance
        @param middleware_onion is an iterable of middleware,
            ordered by first to execute
        @returns a function that calls all the middleware and
            eventually self.make_request()
        """
        middleware: Tuple[Middleware, ...] = middleware_onion.as_tuple_of_middleware()

        cache_key = self._request_func_cache[0]
        if cache_key != middleware:
            self._request_func_cache = (
                middleware,
                combine_middleware(
                    middleware=middleware,
                    w3=w3,
                    provider_request_fn=self.make_request,
                ),
            )

        return self._request_func_cache[-1]

    @handle_request_caching
    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Providers must implement this method")

    def is_connected(self, show_traceback: bool = False) -> bool:
        raise NotImplementedError("Providers must implement this method")


class JSONBaseProvider(BaseProvider):
    def __init__(self) -> None:
        self.request_counter = itertools.count()
        super().__init__()

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
