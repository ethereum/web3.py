from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Optional,
    Union,
)

from eth_utils.toolz import (
    curry,
    pipe,
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


@curry
def retrieve_blocking_method_call_fn(
    w3: "Web3", module: Union["Module", "ModuleV2"], method: Method[Callable[..., Any]]
) -> Callable[..., RPCResponse]:
    def caller(*args: Any, **kwargs: Any) -> RPCResponse:
        (method_str, params), response_formatters = method.process_params(module, *args, **kwargs)
        result_formatters, error_formatters = response_formatters
        result = w3.manager.request_blocking(method_str, params, error_formatters)
        return apply_result_formatters(result_formatters, result)
    return caller


@curry
def retrieve_async_method_call_fn(
    w3: "Web3", module: Union["Module", "ModuleV2"], method: Method[Callable[..., Any]]
) -> Callable[..., Coroutine[Any, Any, RPCResponse]]:
    async def caller(*args: Any, **kwargs: Any) -> RPCResponse:
        (method_str, params), response_formatters = method.process_params(module, *args, **kwargs)
        result_formatters, error_formatters = response_formatters
        result = await w3.manager.coro_request(method_str, params, error_formatters)
        return apply_result_formatters(result_formatters, result)
    return caller


#  TODO: Replace this with ModuleV2 when ready.
class Module:
    web3: "Web3" = None

    def __init__(self, web3: "Web3") -> None:
        self.web3 = web3

    @classmethod
    def attach(cls, target: "Web3", module_name: Optional[str] = None) -> None:
        if not module_name:
            module_name = cls.__name__.lower()

        if hasattr(target, module_name):
            raise AttributeError(
                "Cannot set {0} module named '{1}'.  The web3 object "
                "already has an attribute with that name".format(
                    target,
                    module_name,
                )
            )

        if isinstance(target, Module):
            web3 = target.web3
        else:
            web3 = target

        setattr(target, module_name, cls(web3))


#  Module should no longer have access to the full web3 api.
#  Only the calling functions need access to the request methods.
#  Any "re-entrant" shinanigans can go in the middlewares, which do
#  have web3 access.
class ModuleV2(Module):
    is_async = False

    def __init__(self, web3: "Web3") -> None:
        if self.is_async:
            self.retrieve_caller_fn = retrieve_async_method_call_fn(web3, self)
        else:
            self.retrieve_caller_fn = retrieve_blocking_method_call_fn(web3, self)
        self.web3 = web3
