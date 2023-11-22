from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Optional,
    cast,
)

from eth_utils.toolz import (
    assoc,
    curry,
    merge,
)

from web3.middleware.base import (
    Web3Middleware,
)
from web3.types import (
    EthSubscriptionParams,
    Formatters,
    FormattersDict,
    Literal,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.providers import (  # noqa: F401
        PersistentConnectionProvider,
    )

FORMATTER_DEFAULTS: FormattersDict = {
    "request_formatters": {},
    "result_formatters": {},
    "error_formatters": {},
}


@curry
def _apply_response_formatters(
    method: RPCEndpoint,
    result_formatters: Formatters,
    error_formatters: Formatters,
    response: RPCResponse,
) -> RPCResponse:
    def _format_response(
        response_type: Literal["result", "error", "params"],
        method_response_formatter: Callable[..., Any],
    ) -> RPCResponse:
        appropriate_response = response[response_type]

        if response_type == "params":
            appropriate_response = cast(EthSubscriptionParams, response[response_type])
            return assoc(
                response,
                response_type,
                assoc(
                    response["params"],
                    "result",
                    method_response_formatter(appropriate_response["result"]),
                ),
            )
        else:
            return assoc(
                response, response_type, method_response_formatter(appropriate_response)
            )

    if response.get("result") is not None and method in result_formatters:
        return _format_response("result", result_formatters[method])
    elif (
        # eth_subscription responses
        response.get("params") is not None
        and response["params"].get("result") is not None
        and method in result_formatters
    ):
        return _format_response("params", result_formatters[method])
    elif "error" in response and method in error_formatters:
        return _format_response("error", error_formatters[method])
    else:
        return response


SYNC_FORMATTERS_BUILDER = Callable[["Web3", RPCEndpoint], FormattersDict]
ASYNC_FORMATTERS_BUILDER = Callable[
    ["AsyncWeb3", RPCEndpoint], Coroutine[Any, Any, FormattersDict]
]


class FormattingMiddleware(Web3Middleware):
    def __init__(
        self,
        # formatters option:
        request_formatters: Optional[Formatters] = None,
        result_formatters: Optional[Formatters] = None,
        error_formatters: Optional[Formatters] = None,
        # formatters builder option:
        sync_formatters_builder: Optional[SYNC_FORMATTERS_BUILDER] = None,
        async_formatters_builder: Optional[ASYNC_FORMATTERS_BUILDER] = None,
    ):
        # if not both sync and async formatters are specified, raise error
        if (
            sync_formatters_builder is None and async_formatters_builder is not None
        ) or (sync_formatters_builder is not None and async_formatters_builder is None):
            raise ValueError(
                "Must specify both sync_formatters_builder and async_formatters_builder"
            )

        if sync_formatters_builder is not None and async_formatters_builder is not None:
            if (
                request_formatters is not None
                or result_formatters is not None
                or error_formatters is not None
            ):
                raise ValueError(
                    "Cannot specify formatters_builder and formatters at the same time"
                )

        self.request_formatters = request_formatters or {}
        self.result_formatters = result_formatters or {}
        self.error_formatters = error_formatters or {}
        self.sync_formatters_builder = sync_formatters_builder
        self.async_formatters_builder = async_formatters_builder

    def request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        if self.sync_formatters_builder is not None:
            formatters = merge(
                FORMATTER_DEFAULTS,
                self.sync_formatters_builder(self._w3, method),
            )
            self.request_formatters = formatters.pop("request_formatters")

        if method in self.request_formatters:
            formatter = self.request_formatters[method]
            params = formatter(params)

        return params

    def response_processor(self, method: RPCEndpoint, response: "RPCResponse") -> Any:
        if self.sync_formatters_builder is not None:
            formatters = merge(
                FORMATTER_DEFAULTS,
                self.sync_formatters_builder(self._w3, method),
            )
            self.result_formatters = formatters["result_formatters"]
            self.error_formatters = formatters["error_formatters"]

        return _apply_response_formatters(
            method,
            self.result_formatters,
            self.error_formatters,
            response,
        )

    # -- async -- #

    async def async_request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        if self.async_formatters_builder is not None:
            formatters = merge(
                FORMATTER_DEFAULTS,
                await self.async_formatters_builder(self._w3, method),
            )
            self.request_formatters = formatters.pop("request_formatters")

        if method in self.request_formatters:
            formatter = self.request_formatters[method]
            params = formatter(params)

        return params

    async def async_response_processor(
        self, method: RPCEndpoint, response: "RPCResponse"
    ) -> Any:
        if self.async_formatters_builder is not None:
            formatters = merge(
                FORMATTER_DEFAULTS,
                await self.async_formatters_builder(self._w3, method),
            )
            self.result_formatters = formatters["result_formatters"]
            self.error_formatters = formatters["error_formatters"]

        if self._w3.provider.has_persistent_connection:
            # asynchronous response processing
            provider = cast("PersistentConnectionProvider", self._w3.provider)
            provider._request_processor.append_middleware_response_processor(
                response,
                _apply_response_formatters(
                    method,
                    self.result_formatters,
                    self.error_formatters,
                ),
            )
            return response
        else:
            return _apply_response_formatters(
                method,
                self.result_formatters,
                self.error_formatters,
                response,
            )
