import asyncio
import logging
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    Callable,
    Coroutine,
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

from web3._utils.batching import (
    RequestBatcher,
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
    ProviderConnectionError,
    RequestTimedOut,
    TaskNotRunning,
    TransactionNotFound,
    Web3RPCError,
    Web3TypeError,
)
from web3.method import (
    Method,
)
from web3.middleware import (
    AttributeDictMiddleware,
    BufferedGasEstimateMiddleware,
    ENSNameToAddressMiddleware,
    GasPriceStrategyMiddleware,
    ValidationMiddleware,
)
from web3.middleware.base import (
    Middleware,
    MiddlewareOnion,
)
from web3.module import (
    apply_result_formatters,
)
from web3.providers import (
    AutoProvider,
    JSONBaseProvider,
    PersistentConnectionProvider,
)
from web3.providers.async_base import (
    AsyncJSONBaseProvider,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3.main import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.middleware.base import (  # noqa: F401
        Web3Middleware,
    )
    from web3.providers import (  # noqa: F401
        AsyncBaseProvider,
        BaseProvider,
    )
    from web3.providers.persistent.request_processor import (  # noqa: F401
        RequestProcessor,
    )


NULL_RESPONSES = [None, HexBytes("0x"), "0x"]
KNOWN_REQUEST_TIMEOUT_MESSAGING = {
    # Note: It's important to be very explicit here and not too broad. We don't want
    # to accidentally catch a message that is not for a request timeout. In the worst
    # case, we raise something more generic like `Web3RPCError`. JSON-RPC unfortunately
    # has not standardized error codes for request timeouts.
    "request timed out",  # go-ethereum
}
METHOD_NOT_FOUND = -32601


def _raise_bad_response_format(response: RPCResponse, error: str = "") -> None:
    message = "The response was in an unexpected format and unable to be parsed."
    raw_response = f"The raw response is: {response}"

    if error is not None and error != "":
        error = error[:-1] if error.endswith(".") else error
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


def _validate_subscription_fields(response: RPCResponse) -> None:
    params = response["params"]
    subscription = params["subscription"]
    if not isinstance(subscription, str) and not len(subscription) == 34:
        _raise_bad_response_format(
            response, "eth_subscription 'params' must include a 'subscription' field."
        )


def _validate_response(
    response: RPCResponse,
    error_formatters: Optional[Callable[..., Any]],
    is_subscription_response: bool = False,
    logger: Optional[logging.Logger] = None,
    params: Optional[Any] = None,
) -> None:
    if "jsonrpc" not in response or response["jsonrpc"] != "2.0":
        _raise_bad_response_format(
            response, 'The "jsonrpc" field must be present with a value of "2.0".'
        )

    response_id = response.get("id")
    if "id" in response:
        int_error_msg = (
            '"id" must be an integer or a string representation of an integer.'
        )
        if response_id is None and "error" in response:
            # errors can sometimes have null `id`, according to the JSON-RPC spec
            pass
        elif not isinstance(response_id, (str, int)):
            _raise_bad_response_format(response, int_error_msg)
        elif isinstance(response_id, str):
            try:
                int(response_id)
            except ValueError:
                _raise_bad_response_format(response, int_error_msg)
    elif is_subscription_response:
        # if `id` is not present, this must be a subscription response
        _validate_subscription_fields(response)
    else:
        _raise_bad_response_format(
            response,
            'Response must include an "id" field or be formatted as an '
            "`eth_subscription` response.",
        )

    if all(key in response for key in {"error", "result"}):
        _raise_bad_response_format(
            response, 'Response cannot include both "error" and "result".'
        )
    elif (
        not any(key in response for key in {"error", "result"})
        and not is_subscription_response
    ):
        _raise_bad_response_format(
            response, 'Response must include either "error" or "result".'
        )
    elif "error" in response:
        web3_rpc_error: Optional[Web3RPCError] = None
        error = response["error"]

        # raise the error when the value is a string
        if error is None or not isinstance(error, dict):
            _raise_bad_response_format(
                response,
                'response["error"] must be a valid object as defined by the '
                "JSON-RPC 2.0 specification.",
            )

        # errors must include a message
        error_message = error.get("message")
        if not isinstance(error_message, str):
            _raise_bad_response_format(
                response, 'error["message"] is required and must be a string value.'
            )
        elif error_message == "transaction not found":
            transaction_hash = params[0]
            web3_rpc_error = TransactionNotFound(
                repr(error),
                rpc_response=response,
                user_message=(f"Transaction with hash {transaction_hash!r} not found."),
            )

        # errors must include an integer code
        code = error.get("code")
        if not isinstance(code, int):
            _raise_bad_response_format(
                response, 'error["code"] is required and must be an integer value.'
            )
        elif code == METHOD_NOT_FOUND:
            web3_rpc_error = MethodUnavailable(
                repr(error),
                rpc_response=response,
                user_message=(
                    "This method is not available. Check your node provider or your "
                    "client's API docs to see what methods are supported and / or "
                    "currently enabled."
                ),
            )
        elif any(
            # parse specific timeout messages
            timeout_str in error_message.lower()
            for timeout_str in KNOWN_REQUEST_TIMEOUT_MESSAGING
        ):
            web3_rpc_error = RequestTimedOut(
                repr(error),
                rpc_response=response,
                user_message=(
                    "The request timed out. Check the connection to your node and "
                    "try again."
                ),
            )

        if web3_rpc_error is None:
            # if no condition was met above, raise a more generic `Web3RPCError`
            web3_rpc_error = Web3RPCError(repr(error), rpc_response=response)

        response = apply_error_formatters(error_formatters, response)

        logger.error(web3_rpc_error.user_message)
        logger.debug(f"RPC error response: {response}")
        raise web3_rpc_error

    elif "result" not in response and not is_subscription_response:
        _raise_bad_response_format(response)


class RequestManager:
    logger = logging.getLogger("web3.manager.RequestManager")

    middleware_onion: Union["MiddlewareOnion", NamedElementOnion[None, None]]

    def __init__(
        self,
        w3: Union["AsyncWeb3", "Web3"],
        provider: Optional[Union["BaseProvider", "AsyncBaseProvider"]] = None,
        middleware: Optional[Sequence[Tuple[Middleware, str]]] = None,
    ) -> None:
        self.w3 = w3

        if provider is None:
            self.provider = AutoProvider()
        else:
            self.provider = provider

        if middleware is None:
            middleware = self.get_default_middleware()

        self.middleware_onion = NamedElementOnion(middleware)

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
    def get_default_middleware() -> List[Tuple[Middleware, str]]:
        """
        List the default middleware for the request manager.
        Documentation should remain in sync with these defaults.
        """
        return [
            (GasPriceStrategyMiddleware, "gas_price_strategy"),
            (ENSNameToAddressMiddleware, "ens_name_to_address"),
            (AttributeDictMiddleware, "attrdict"),
            (ValidationMiddleware, "validation"),
            (BufferedGasEstimateMiddleware, "gas_estimate"),
        ]

    #
    # Provider requests and response
    #
    def _make_request(
        self, method: Union[RPCEndpoint, Callable[..., RPCEndpoint]], params: Any
    ) -> RPCResponse:
        provider = cast("BaseProvider", self.provider)
        request_func = provider.request_func(
            cast("Web3", self.w3), cast("MiddlewareOnion", self.middleware_onion)
        )
        self.logger.debug(f"Making request. Method: {method}")
        return request_func(method, params)

    async def _coro_make_request(
        self, method: Union[RPCEndpoint, Callable[..., RPCEndpoint]], params: Any
    ) -> RPCResponse:
        provider = cast("AsyncBaseProvider", self.provider)
        request_func = await provider.request_func(
            cast("AsyncWeb3", self.w3), cast("MiddlewareOnion", self.middleware_onion)
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
    def formatted_response(
        self,
        response: RPCResponse,
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        is_subscription_response = (
            response.get("method") == "eth_subscription"
            and response.get("params") is not None
            and response["params"].get("subscription") is not None
            and response["params"].get("result") is not None
        )

        _validate_response(
            response,
            error_formatters,
            is_subscription_response=is_subscription_response,
            logger=self.logger,
            params=params,
        )

        # format results
        if "result" in response:
            # Null values for result should apply null_result_formatters
            # Skip when result not present in the response (fallback to False)
            if response.get("result", False) in NULL_RESPONSES:
                apply_null_result_formatters(null_result_formatters, response, params)
            return response.get("result")

        # response from eth_subscription includes response["params"]["result"]
        elif is_subscription_response:
            return {
                "subscription": response["params"]["subscription"],
                "result": response["params"]["result"],
            }

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

    # -- batch requests management -- #

    def _batch_requests(self) -> RequestBatcher[Method[Callable[..., Any]]]:
        """
        Context manager for making batch requests
        """
        if not isinstance(self.provider, (AsyncJSONBaseProvider, JSONBaseProvider)):
            raise Web3TypeError("Batch requests are not supported by this provider.")
        return RequestBatcher(self.w3)

    def _make_batch_request(
        self, requests_info: List[Tuple[Tuple["RPCEndpoint", Any], Sequence[Any]]]
    ) -> List[RPCResponse]:
        """
        Make a batch request using the provider
        """
        provider = cast(JSONBaseProvider, self.provider)
        request_func = provider.batch_request_func(
            cast("Web3", self.w3), cast("MiddlewareOnion", self.middleware_onion)
        )
        responses = request_func(
            [
                (method, params)
                for (method, params), _response_formatters in requests_info
            ]
        )
        formatted_responses = [
            self._format_batched_response(info, resp)
            for info, resp in zip(requests_info, responses)
        ]
        return list(formatted_responses)

    async def _async_make_batch_request(
        self,
        requests_info: List[
            Coroutine[Any, Any, Tuple[Tuple["RPCEndpoint", Any], Sequence[Any]]]
        ],
    ) -> List[RPCResponse]:
        """
        Make an asynchronous batch request using the provider
        """
        provider = cast(AsyncJSONBaseProvider, self.provider)
        request_func = await provider.batch_request_func(
            cast("AsyncWeb3", self.w3),
            cast("MiddlewareOnion", self.middleware_onion),
        )
        # since we add items to the batch without awaiting, we unpack the coroutines
        # and await them all here
        unpacked_requests_info = await asyncio.gather(*requests_info)
        responses = await request_func(
            [
                (method, params)
                for (method, params), _response_formatters in unpacked_requests_info
            ]
        )

        if isinstance(self.provider, PersistentConnectionProvider):
            # call _process_response for each response in the batch
            return [await self._process_response(resp) for resp in responses]

        formatted_responses = [
            self._format_batched_response(info, resp)
            for info, resp in zip(unpacked_requests_info, responses)
        ]
        return list(formatted_responses)

    def _format_batched_response(
        self,
        requests_info: Tuple[Tuple[RPCEndpoint, Any], Sequence[Any]],
        response: RPCResponse,
    ) -> RPCResponse:
        result_formatters, error_formatters, null_result_formatters = requests_info[1]
        return apply_result_formatters(
            result_formatters,
            self.formatted_response(
                response,
                requests_info[0][1],
                error_formatters,
                null_result_formatters,
            ),
        )

    # -- persistent connection -- #

    async def socket_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        provider = cast(PersistentConnectionProvider, self._provider)
        request_func = await provider.request_func(
            cast("AsyncWeb3", self.w3), cast("MiddlewareOnion", self.middleware_onion)
        )
        self.logger.debug(
            "Making request to open socket connection and waiting for response: "
            f"{provider.get_endpoint_uri_or_ipc_path()}, method: {method}"
        )
        response = await request_func(method, params)
        return await self._process_response(response)

    async def send(self, method: RPCEndpoint, params: Any) -> None:
        provider = cast(PersistentConnectionProvider, self._provider)
        # run through the request processors of the middleware
        for mw_class in self.middleware_onion.as_tuple_of_middleware():
            mw = mw_class(self.w3)
            method, params = mw.request_processor(method, params)

        self.logger.debug(
            "Sending request to open socket connection: "
            f"{provider.get_endpoint_uri_or_ipc_path()}, method: {method}"
        )
        await provider.socket_send(provider.encode_rpc_request(method, params))

    async def recv(self) -> RPCResponse:
        provider = cast(PersistentConnectionProvider, self._provider)
        self.logger.debug(
            "Getting next response from open socket connection: "
            f"{provider.get_endpoint_uri_or_ipc_path()}"
        )
        # pop from the queue since the listener task is responsible for reading
        # directly from the socket
        request_response_cache = self._request_processor._request_response_cache
        _key, response = await request_response_cache.async_await_and_popitem(
            last=False,
            timeout=provider.request_timeout,
        )
        return await self._process_response(response)

    def _persistent_message_stream(self) -> "_AsyncPersistentMessageStream":
        return _AsyncPersistentMessageStream(self)

    async def _get_next_message(self) -> RPCResponse:
        return await self._message_stream().__anext__()

    async def _message_stream(self) -> AsyncGenerator[RPCResponse, None]:
        if not isinstance(self._provider, PersistentConnectionProvider):
            raise Web3TypeError(
                "Only providers that maintain an open, persistent connection "
                "can listen to streams."
            )

        if self._provider._message_listener_task is None:
            raise ProviderConnectionError(
                "No listener found for persistent connection."
            )

        while True:
            try:
                response = await self._request_processor.pop_raw_response(
                    subscription=True
                )
                if (
                    response is not None
                    and response.get("params", {}).get("subscription")
                    in self._request_processor.active_subscriptions
                ):
                    # if response is an active subscription response, process it
                    yield await self._process_response(response)
            except TaskNotRunning:
                await asyncio.sleep(0)
                self._provider._handle_listener_task_exceptions()
                self.logger.error(
                    "Message listener background task has stopped unexpectedly. "
                    "Stopping message stream."
                )
                return

    async def _process_response(self, response: RPCResponse) -> RPCResponse:
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


class _AsyncPersistentMessageStream:
    """
    Async generator for pulling subscription responses from the request processor
    subscription queue. This abstraction is necessary to define the `__aiter__()`
    method required for use with "async for" loops.
    """

    def __init__(self, manager: RequestManager, *args: Any, **kwargs: Any) -> None:
        self.manager = manager
        self.provider: PersistentConnectionProvider = cast(
            PersistentConnectionProvider, manager._provider
        )
        super().__init__(*args, **kwargs)

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> RPCResponse:
        return await self.manager._get_next_message()
