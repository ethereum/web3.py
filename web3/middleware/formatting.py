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

from web3.types import (
    AsyncMiddleware,
    AsyncMiddlewareCoroutine,
    Formatters,
    FormattersDict,
    Literal,
    Middleware,
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
        response_type: Literal["result", "error"],
        method_response_formatter: Callable[..., Any],
    ) -> RPCResponse:
        appropriate_response = response[response_type]

        return assoc(
            response, response_type, method_response_formatter(appropriate_response)
        )

    if response.get("result") is not None and method in result_formatters:
        return _format_response("result", result_formatters[method])
    elif "error" in response and method in error_formatters:
        return _format_response("error", error_formatters[method])
    else:
        return response


# --- sync -- #


def construct_formatting_middleware(
    request_formatters: Optional[Formatters] = None,
    result_formatters: Optional[Formatters] = None,
    error_formatters: Optional[Formatters] = None,
) -> Middleware:
    def ignore_web3_in_standard_formatters(
        _w3: "Web3",
        _method: RPCEndpoint,
    ) -> FormattersDict:
        return dict(
            request_formatters=request_formatters or {},
            result_formatters=result_formatters or {},
            error_formatters=error_formatters or {},
        )

    return construct_web3_formatting_middleware(ignore_web3_in_standard_formatters)


def construct_web3_formatting_middleware(
    web3_formatters_builder: Callable[["Web3", RPCEndpoint], FormattersDict],
) -> Middleware:
    def formatter_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any],
        w3: "Web3",
    ) -> Callable[[RPCEndpoint, Any], RPCResponse]:
        def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            formatters = merge(
                FORMATTER_DEFAULTS,
                web3_formatters_builder(w3, method),
            )
            request_formatters = formatters.pop("request_formatters")

            if method in request_formatters:
                formatter = request_formatters[method]
                params = formatter(params)
            response = make_request(method, params)

            return _apply_response_formatters(
                method,
                formatters["result_formatters"],
                formatters["error_formatters"],
                response,
            )

        return middleware

    return formatter_middleware


# --- async --- #


async def async_construct_formatting_middleware(
    request_formatters: Optional[Formatters] = None,
    result_formatters: Optional[Formatters] = None,
    error_formatters: Optional[Formatters] = None,
) -> AsyncMiddleware:
    async def ignore_web3_in_standard_formatters(
        _async_w3: "AsyncWeb3",
        _method: RPCEndpoint,
    ) -> FormattersDict:
        return dict(
            request_formatters=request_formatters or {},
            result_formatters=result_formatters or {},
            error_formatters=error_formatters or {},
        )

    return await async_construct_web3_formatting_middleware(
        ignore_web3_in_standard_formatters
    )


async def async_construct_web3_formatting_middleware(
    async_web3_formatters_builder: Callable[
        ["AsyncWeb3", RPCEndpoint], Coroutine[Any, Any, FormattersDict]
    ]
) -> Callable[
    [Callable[[RPCEndpoint, Any], Any], "AsyncWeb3"],
    Coroutine[Any, Any, AsyncMiddlewareCoroutine],
]:
    async def formatter_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any],
        async_w3: "AsyncWeb3",
    ) -> AsyncMiddlewareCoroutine:
        async def middleware(method: RPCEndpoint, params: Any) -> Optional[RPCResponse]:
            formatters = merge(
                FORMATTER_DEFAULTS,
                await async_web3_formatters_builder(async_w3, method),
            )
            request_formatters = formatters.pop("request_formatters")

            if method in request_formatters:
                formatter = request_formatters[method]
                params = formatter(params)
            response = await make_request(method, params)

            if async_w3.provider.has_persistent_connection:
                # asynchronous response processing
                provider = cast("PersistentConnectionProvider", async_w3.provider)
                provider._append_middleware_response_processor(
                    _apply_response_formatters(
                        method,
                        formatters["result_formatters"],
                        formatters["error_formatters"],
                    )
                )
                return None
            else:
                return _apply_response_formatters(
                    method,
                    formatters["result_formatters"],
                    formatters["error_formatters"],
                    response,
                )

        return middleware

    return formatter_middleware
