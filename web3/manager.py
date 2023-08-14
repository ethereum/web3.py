import asyncio
import json
import logging
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    Callable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

from eth_utils.toolz import (
    pipe,
)
from hexbytes import (
    HexBytes,
)
from websockets.exceptions import (
    ConnectionClosedOK,
)

from web3._utils.caching import (
    generate_cache_key,
)
from web3.datastructures import (
    NamedElementOnion,
)
from web3.exceptions import (
    BadResponseFormat,
    MethodUnavailable,
)
from web3.middleware import (
    abi_middleware,
    async_attrdict_middleware,
    async_buffered_gas_estimate_middleware,
    async_gas_price_strategy_middleware,
    async_name_to_address_middleware,
    async_validation_middleware,
    attrdict_middleware,
    buffered_gas_estimate_middleware,
    gas_price_strategy_middleware,
    name_to_address_middleware,
    validation_middleware,
)
from web3.module import (
    apply_result_formatters,
)
from web3.providers import (
    AutoProvider,
    PersistentConnectionProvider,
)
from web3.types import (
    AsyncMiddleware,
    AsyncMiddlewareOnion,
    Middleware,
    MiddlewareOnion,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.providers import (  # noqa: F401
        AsyncBaseProvider,
        BaseProvider,
    )


NULL_RESPONSES = [None, HexBytes("0x"), "0x"]


def apply_error_formatters(
    error_formatters: Callable[..., Any],
    response: RPCResponse,
) -> RPCResponse:
    if error_formatters:
        formatted_resp = pipe(response, error_formatters)
        return formatted_resp
    else:
        return response


def apply_null_result_formatters(
    null_result_formatters: Callable[..., Any],
    response: RPCResponse,
    params: Optional[Any] = None,
) -> RPCResponse:
    if null_result_formatters:
        formatted_resp = pipe(params, null_result_formatters)
        return formatted_resp
    else:
        return response


class RequestManager:
    logger = logging.getLogger("web3.RequestManager")

    middleware_onion: Union[
        MiddlewareOnion, AsyncMiddlewareOnion, NamedElementOnion[None, None]
    ]

    def __init__(
        self,
        w3: Union["AsyncWeb3", "Web3"],
        provider: Optional[Union["BaseProvider", "AsyncBaseProvider"]] = None,
        middlewares: Optional[
            Union[
                Sequence[Tuple[Middleware, str]], Sequence[Tuple[AsyncMiddleware, str]]
            ]
        ] = None,
    ) -> None:
        self.w3 = w3

        if provider is None:
            self.provider = AutoProvider()
        else:
            self.provider = provider

        if middlewares is None:
            middlewares = (
                self.async_default_middlewares()
                if self.provider.is_async
                else self.default_middlewares(cast("Web3", w3))
            )

        self.middleware_onion = NamedElementOnion(middlewares)

    w3: Union["AsyncWeb3", "Web3"] = None
    _provider = None

    @property
    def provider(self) -> Union["BaseProvider", "AsyncBaseProvider"]:
        return self._provider

    @provider.setter
    def provider(self, provider: Union["BaseProvider", "AsyncBaseProvider"]) -> None:
        self._provider = provider

    @staticmethod
    def default_middlewares(w3: "Web3") -> List[Tuple[Middleware, str]]:
        """
        List the default middlewares for the request manager.
        Leaving w3 unspecified will prevent the middleware from resolving names.
        Documentation should remain in sync with these defaults.
        """
        return [
            (gas_price_strategy_middleware, "gas_price_strategy"),
            (name_to_address_middleware(w3), "name_to_address"),
            (attrdict_middleware, "attrdict"),
            (validation_middleware, "validation"),
            (abi_middleware, "abi"),
            (buffered_gas_estimate_middleware, "gas_estimate"),
        ]

    @staticmethod
    def async_default_middlewares() -> List[Tuple[AsyncMiddleware, str]]:
        """
        List the default async middlewares for the request manager.
        Documentation should remain in sync with these defaults.
        """
        return [
            (async_gas_price_strategy_middleware, "gas_price_strategy"),
            (async_name_to_address_middleware, "name_to_address"),
            (async_attrdict_middleware, "attrdict"),
            (async_validation_middleware, "validation"),
            (async_buffered_gas_estimate_middleware, "gas_estimate"),
        ]

    #
    # Provider requests and response
    #
    def _make_request(
        self, method: Union[RPCEndpoint, Callable[..., RPCEndpoint]], params: Any
    ) -> RPCResponse:
        provider = cast("BaseProvider", self.provider)
        request_func = provider.request_func(
            cast("Web3", self.w3), cast(MiddlewareOnion, self.middleware_onion)
        )
        self.logger.debug(f"Making request. Method: {method}")
        return request_func(method, params)

    async def _coro_make_request(
        self, method: Union[RPCEndpoint, Callable[..., RPCEndpoint]], params: Any
    ) -> RPCResponse:
        provider = cast("AsyncBaseProvider", self.provider)
        request_func = await provider.request_func(
            cast("AsyncWeb3", self.w3),
            cast(AsyncMiddlewareOnion, self.middleware_onion),
        )
        self.logger.debug(f"Making request. Method: {method}")
        return await request_func(method, params)

    @staticmethod
    def formatted_response(
        response: RPCResponse,
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        if "error" in response:
            apply_error_formatters(error_formatters, response)

            # guard against eth-tester case - eth-tester returns a string
            # with no code, so can't parse what the error is.
            if isinstance(response["error"], dict):
                resp_code = response["error"].get("code")
                if resp_code == -32601:
                    raise MethodUnavailable(response["error"])
            raise ValueError(response["error"])
        # NULL_RESPONSES includes None, so return False here as the default
        # so we don't apply the null_result_formatters if there is no 'result' key
        elif response.get("result", False) in NULL_RESPONSES:
            # null_result_formatters raise either a BlockNotFound
            # or a TransactionNotFound error, depending on the method called
            apply_null_result_formatters(null_result_formatters, response, params)
            return response["result"]
        elif response.get("result") is not None:
            return response["result"]
        elif (
            # eth_subscribe case
            response.get("params") is not None
            and response["params"].get("result") is not None
        ):
            return response["params"]["result"]
        else:
            raise BadResponseFormat(
                "The response was in an unexpected format and unable to be parsed. "
                f"The raw response is: {response}"
            )

    def request_blocking(
        self,
        method: Union[RPCEndpoint, Callable[..., RPCEndpoint]],
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        """
        Make a synchronous request using the provider
        """
        response = self._make_request(method, params)
        return self.formatted_response(
            response, params, error_formatters, null_result_formatters
        )

    async def coro_request(
        self,
        method: Union[RPCEndpoint, Callable[..., RPCEndpoint]],
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        """
        Coroutine for making a request using the provider
        """
        response = await self._coro_make_request(method, params)
        return self.formatted_response(
            response, params, error_formatters, null_result_formatters
        )

    # persistent connection
    async def ws_send(
        self,
        method: Union[RPCEndpoint, Callable[..., RPCEndpoint]],
        params: Any,
    ) -> RPCResponse:
        provider = cast(PersistentConnectionProvider, self._provider)
        request_func = await provider.request_func(
            cast("AsyncWeb3", self.w3),
            cast(AsyncMiddlewareOnion, self.middleware_onion),
        )
        self.logger.debug(
            "Making request to open websocket connection - "
            f"uri: {provider.endpoint_uri}, method: {method}"
        )
        await request_func(method, params)
        return await asyncio.wait_for(
            self.ws_recv(),
            timeout=provider.call_timeout,
        )

    async def ws_recv(self) -> Any:
        return await self._ws_recv_stream().__anext__()

    def persistent_recv_stream(self) -> "_AsyncPersistentRecvStream":
        return _AsyncPersistentRecvStream(self)

    async def _ws_recv_stream(self) -> AsyncGenerator[RPCResponse, None]:
        if not isinstance(self._provider, PersistentConnectionProvider):
            raise TypeError(
                "Only websocket providers that maintain an open, persistent connection "
                "can listen to websocket recv streams."
            )

        response = json.loads(
            await asyncio.wait_for(
                self._provider.ws.recv(),
                timeout=self._provider.call_timeout,
            )
        )
        request_info = self._provider._get_request_information_for_response(response)

        if request_info is None:
            self.logger.debug("No cache key found for response, returning raw response")
            yield response

        else:
            if request_info.method == "eth_subscribe" and "result" in response.keys():
                # if response for the initial eth_subscribe request, which returns the
                # subscription id
                subscription_id = response["result"]
                cache_key = generate_cache_key(subscription_id)
                if cache_key not in self._provider._async_response_processing_cache:
                    # cache by subscription id in order to process each response for the
                    # subscription as it comes in
                    self._provider.logger.debug(
                        f"Caching eth_subscription info:\n    "
                        f"cache_key={cache_key},\n    "
                        f"request_info={request_info.__dict__}"
                    )
                    self._provider._async_response_processing_cache.cache(
                        cache_key, request_info
                    )

            # pipe response back through middleware response processors
            if len(request_info.middleware_response_processors) > 0:
                response = pipe(response, *request_info.middleware_response_processors)

            (
                result_formatters,
                error_formatters,
                null_formatters,
            ) = request_info.response_formatters
            partly_formatted_response = self.formatted_response(
                response,
                request_info.params,
                error_formatters,
                null_formatters,
            )
            yield apply_result_formatters(result_formatters, partly_formatted_response)


class _AsyncPersistentRecvStream:
    """
    Async generator for receiving responses from a persistent connection. This
    abstraction is necessary to define the `__aiter__()` method required for
    use with "async for" loops.
    """

    def __init__(self, manager: RequestManager, *args: Any, **kwargs: Any) -> None:
        self.manager = manager
        super().__init__(*args, **kwargs)

    def __aiter__(self) -> AsyncGenerator[RPCResponse, None]:
        while True:
            try:
                return self.manager._ws_recv_stream()
            except ConnectionClosedOK:
                pass
