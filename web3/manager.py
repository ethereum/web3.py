import asyncio
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
from web3._utils.compat import (
    Self,
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
    from web3.main import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.providers import (  # noqa: F401
        AsyncBaseProvider,
        BaseProvider,
    )
    from web3.providers.websocket.request_processor import (  # noqa: F401
        RequestProcessor,
    )


NULL_RESPONSES = [None, HexBytes("0x"), "0x"]
METHOD_NOT_FOUND = -32601


def _raise_bad_response_format(response: RPCResponse, error: str = "") -> None:
    message = "The response was in an unexpected format and unable to be parsed."
    raw_response = f"The raw response is: {response}"

    if error is not None and error != "":
        message = f"{message} {error}. {raw_response}"
    else:
        message = f"{message} {raw_response}"

    raise BadResponseFormat(message)


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

        if isinstance(provider, PersistentConnectionProvider):
            # set up the request processor to be able to properly process ordered
            # responses from the persistent connection as FIFO
            provider = cast(PersistentConnectionProvider, self.provider)
            self._request_processor: RequestProcessor = provider._request_processor

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

    #
    # formatted_response parses and validates JSON-RPC responses for expected
    # properties (result or an error) with the expected types.
    #
    # Required properties are not strictly enforced to further determine which
    # exception to raise for specific cases.
    #
    # See also: https://www.jsonrpc.org/specification
    #
    @staticmethod
    def formatted_response(
        response: RPCResponse,
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        # jsonrpc is not enforced (as per the spec) but if present, it must be 2.0
        if "jsonrpc" in response and response["jsonrpc"] != "2.0":
            _raise_bad_response_format(
                response, 'The "jsonrpc" field must be present with a value of "2.0"'
            )

        # id is not enforced (as per the spec) but if present, it must be a
        # string or integer
        # TODO: v7 - enforce id per the spec
        if "id" in response:
            response_id = response["id"]
            # id is always None for errors
            if response_id is None and "error" not in response:
                _raise_bad_response_format(
                    response, '"id" must be None when an error is present'
                )
            elif not isinstance(response_id, (str, int, type(None))):
                _raise_bad_response_format(response, '"id" must be a string or integer')

        # Response may not include both "error" and "result"
        if "error" in response and "result" in response:
            _raise_bad_response_format(
                response, 'Response cannot include both "error" and "result"'
            )

        # Format and validate errors
        elif "error" in response:
            error = response.get("error")
            # Raise the error when the value is a string
            if error is None or isinstance(error, str):
                raise ValueError(error)

            # Errors must include an integer code
            code = error.get("code")
            if not isinstance(code, int):
                _raise_bad_response_format(response, "error['code'] must be an integer")
            elif code == METHOD_NOT_FOUND:
                raise MethodUnavailable(error)

            # Errors must include a message
            if not isinstance(error.get("message"), str):
                _raise_bad_response_format(
                    response, "error['message'] must be a string"
                )

            apply_error_formatters(error_formatters, response)

            raise ValueError(error)

        # Format and validate results
        elif "result" in response:
            # Null values for result should apply null_result_formatters
            # Skip when result not present in the response (fallback to False)
            if response.get("result", False) in NULL_RESPONSES:
                apply_null_result_formatters(null_result_formatters, response, params)
            return response.get("result")

        # Response from eth_subscription includes response["params"]["result"]
        elif (
            response.get("method") == "eth_subscription"
            and response.get("params") is not None
            and response["params"].get("subscription") is not None
            and response["params"].get("result") is not None
        ):
            return {
                "subscription": response["params"]["subscription"],
                "result": response["params"]["result"],
            }

        # Any other response type raises BadResponseFormat
        else:
            _raise_bad_response_format(response)

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
    async def ws_send(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        provider = cast(PersistentConnectionProvider, self._provider)
        request_func = await provider.request_func(
            cast("AsyncWeb3", self.w3),
            cast(AsyncMiddlewareOnion, self.middleware_onion),
        )
        self.logger.debug(
            "Making request to open websocket connection - "
            f"uri: {provider.endpoint_uri}, method: {method}"
        )
        response = await request_func(method, params)
        return await self._process_ws_response(response)

    async def ws_recv(self) -> Any:
        return await self._ws_recv_stream().__anext__()

    def _persistent_recv_stream(self) -> "_AsyncPersistentRecvStream":
        return _AsyncPersistentRecvStream(self)

    async def _ws_recv_stream(self) -> AsyncGenerator[RPCResponse, None]:
        if not isinstance(self._provider, PersistentConnectionProvider):
            raise TypeError(
                "Only websocket providers that maintain an open, persistent connection "
                "can listen to websocket recv streams."
            )

        while True:
            # sleep(0) here seems to be the most efficient way to yield control back to
            # the event loop while waiting for the response to be cached or received on
            # the websocket.
            await asyncio.sleep(0)

            # look in the cache for a response
            response = self._request_processor.pop_raw_response(subscription=True)
            if response is not None:
                break
            else:
                # if no response in the cache, check the websocket connection
                if not self._provider._ws_lock.locked():
                    async with self._provider._ws_lock:
                        try:
                            # keep timeout low but reasonable to check both the cache
                            # and the websocket connection for new responses
                            response = await self._provider._ws_recv(timeout=0.5)
                        except asyncio.TimeoutError:
                            # if no response received, continue to next iteration
                            continue

                    if response.get("method") == "eth_subscription":
                        break
                    else:
                        self._provider._request_processor.cache_raw_response(response)

        yield await self._process_ws_response(response)

    async def _process_ws_response(self, response: RPCResponse) -> RPCResponse:
        provider = cast(PersistentConnectionProvider, self._provider)
        request_info = self._request_processor.get_request_information_for_response(
            response
        )

        if request_info is None:
            self.logger.debug("No cache key found for response, returning raw response")
            return response
        else:
            if request_info.method == "eth_subscribe" and "result" in response.keys():
                # if response for the initial eth_subscribe request, which returns the
                # subscription id
                subscription_id = response["result"]
                cache_key = generate_cache_key(subscription_id)
                if cache_key not in self._request_processor._request_information_cache:
                    # cache by subscription id in order to process each response for the
                    # subscription as it comes in
                    request_info.subscription_id = subscription_id
                    provider.logger.debug(
                        "Caching eth_subscription info:\n    "
                        f"cache_key={cache_key},\n    "
                        f"request_info={request_info.__dict__}"
                    )
                    self._request_processor._request_information_cache.cache(
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
            return apply_result_formatters(result_formatters, partly_formatted_response)


class _AsyncPersistentRecvStream:
    """
    Async generator for receiving responses from a persistent connection. This
    abstraction is necessary to define the `__aiter__()` method required for
    use with "async for" loops.
    """

    def __init__(self, manager: RequestManager, *args: Any, **kwargs: Any) -> None:
        self.manager = manager
        super().__init__(*args, **kwargs)

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> RPCResponse:
        try:
            return await self.manager.ws_recv()
        except ConnectionClosedOK:
            raise StopAsyncIteration
