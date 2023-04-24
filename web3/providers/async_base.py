import itertools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
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
from web3.exceptions import (
    ProviderConnectionError,
)
from web3.middleware import (
    async_combine_middlewares,
)
from web3.types import (
    AsyncMiddleware,
    AsyncMiddlewareOnion,
    MiddlewareOnion,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import AsyncWeb3  # noqa: F401


class AsyncBaseProvider:
    _middlewares: Tuple[AsyncMiddleware, ...] = ()
    # a tuple of (all_middlewares, request_func)
    _request_func_cache: Tuple[
        Tuple[AsyncMiddleware, ...], Callable[..., Coroutine[Any, Any, RPCResponse]]
    ] = (
        None,
        None,
    )

    is_async = True
    global_ccip_read_enabled: bool = True
    ccip_read_max_redirects: int = 4

    @property
    def middlewares(self) -> Tuple[AsyncMiddleware, ...]:
        return self._middlewares

    @middlewares.setter
    def middlewares(self, values: MiddlewareOnion) -> None:
        # tuple(values) converts to MiddlewareOnion -> Tuple[Middleware, ...]
        self._middlewares = tuple(values)  # type: ignore

    async def request_func(
        self, async_w3: "AsyncWeb3", outer_middlewares: AsyncMiddlewareOnion
    ) -> Callable[..., Coroutine[Any, Any, RPCResponse]]:
        # type ignored b/c tuple(MiddlewareOnion) converts to tuple of middlewares
        all_middlewares: Tuple[AsyncMiddleware] = tuple(outer_middlewares) + tuple(self.middlewares)  # type: ignore  # noqa: E501

        cache_key = self._request_func_cache[0]
        if cache_key is None or cache_key != all_middlewares:
            self._request_func_cache = (
                all_middlewares,
                await self._generate_request_func(async_w3, all_middlewares),
            )
        return self._request_func_cache[-1]

    async def _generate_request_func(
        self, async_w3: "AsyncWeb3", middlewares: Sequence[AsyncMiddleware]
    ) -> Callable[..., Coroutine[Any, Any, RPCResponse]]:
        return await async_combine_middlewares(
            middlewares=middlewares,
            async_w3=async_w3,
            provider_request_fn=self.make_request,
        )

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Providers must implement this method")

    async def is_connected(self, show_traceback: bool = False) -> bool:
        raise NotImplementedError("Providers must implement this method")


class AsyncJSONBaseProvider(AsyncBaseProvider):
    def __init__(self) -> None:
        super().__init__()
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

    async def is_connected(self, show_traceback: bool = False) -> bool:
        try:
            response = await self.make_request(RPCEndpoint("web3_clientVersion"), [])
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
