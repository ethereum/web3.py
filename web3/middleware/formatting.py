from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Optional,
)

from eth_utils.toolz import (
    assoc,
    curry,
    merge,
)

from web3.types import (
    Formatters,
    FormattersDict,
    Middleware,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def construct_formatting_middleware(
    request_formatters: Optional[Formatters] = None,
    result_formatters: Optional[Formatters] = None,
    error_formatters: Optional[Formatters] = None
) -> Middleware:
    def ignore_web3_in_standard_formatters(
        w3: "Web3",
    ) -> FormattersDict:
        return dict(
            request_formatters=request_formatters or {},
            result_formatters=result_formatters or {},
            error_formatters=error_formatters or {},
        )

    return construct_web3_formatting_middleware(ignore_web3_in_standard_formatters)


def construct_web3_formatting_middleware(
    web3_formatters_builder: Callable[["Web3"], FormattersDict]
) -> Middleware:
    def formatter_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], w3: "Web3"
    ) -> Callable[[RPCEndpoint, Any], RPCResponse]:
        formatters = merge(
            {
                "request_formatters": {},
                "result_formatters": {},
                "error_formatters": {},
            },
            web3_formatters_builder(w3),
        )
        return apply_formatters(make_request=make_request, **formatters)

    return formatter_middleware


@curry
def apply_formatters(
    method: RPCEndpoint,
    params: Any,
    make_request: Callable[[RPCEndpoint, Any], RPCResponse],
    request_formatters: Formatters,
    result_formatters: Formatters,
    error_formatters: Formatters,
) -> RPCResponse:
    if method in request_formatters:
        formatter = request_formatters[method]
        formatted_params = formatter(params)
        response = make_request(method, formatted_params)
    else:
        response = make_request(method, params)

    if "result" in response and method in result_formatters:
        formatter = result_formatters[method]
        formatted_response = assoc(
            response,
            "result",
            formatter(response["result"]),
        )
        return formatted_response
    elif "error" in response and method in error_formatters:
        formatter = error_formatters[method]
        formatted_response = assoc(
            response,
            "error",
            formatter(response["error"]),
        )
        return formatted_response
    else:
        return response
