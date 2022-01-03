from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    TypeVar,
    Union,
)

from eth_abi.codec import (
    ABICodec,
)
from eth_utils.toolz import (
    curry,
    pipe,
)

from web3._utils.filters import (
    LogFilter,
    _UseExistingFilter,
)
from web3.method import (
    Method,
)
from web3.types import (
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


@curry
def apply_result_formatters(
    result_formatters: Callable[..., Any], result: RPCResponse
) -> RPCResponse:
    if result_formatters:
        formatted_result = pipe(result, result_formatters)
        return formatted_result
    else:
        return result


TReturn = TypeVar('TReturn')


@curry
def retrieve_blocking_method_call_fn(
    w3: "Web3", module: "Module", method: Method[Callable[..., TReturn]]
) -> Callable[..., Union[TReturn, LogFilter]]:
    def caller(*args: Any, **kwargs: Any) -> Union[TReturn, LogFilter]:
        try:
            (method_str, params), response_formatters = method.process_params(module, *args, **kwargs)  # noqa: E501
        except _UseExistingFilter as err:
            return LogFilter(eth_module=module, filter_id=err.filter_id)
        result_formatters, error_formatters, null_result_formatters = response_formatters
        result = w3.manager.request_blocking(method_str,
                                             params,
                                             error_formatters,
                                             null_result_formatters)
        return apply_result_formatters(result_formatters, result)
    return caller


@curry
def retrieve_async_method_call_fn(
    w3: "Web3", module: "Module", method: Method[Callable[..., Any]]
) -> Callable[..., Coroutine[Any, Any, RPCResponse]]:
    async def caller(*args: Any, **kwargs: Any) -> RPCResponse:
        (method_str, params), response_formatters = method.process_params(module, *args, **kwargs)
        result_formatters, error_formatters, null_result_formatters = response_formatters
        result = await w3.manager.coro_request(method_str,
                                               params,
                                               error_formatters,
                                               null_result_formatters)
        return apply_result_formatters(result_formatters, result)
    return caller


#  Module should no longer have access to the full web3 api.
#  Only the calling functions need access to the request methods.
#  Any "re-entrant" shenanigans can go in the middlewares, which do
#  have web3 access.
class Module:
    is_async = False

    def __init__(self, web3: "Web3") -> None:
        if self.is_async:
            self.retrieve_caller_fn = retrieve_async_method_call_fn(web3, self)
        else:
            self.retrieve_caller_fn = retrieve_blocking_method_call_fn(web3, self)
        self.web3 = web3
        self.codec: ABICodec = web3.codec
