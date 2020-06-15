from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Optional,
    Tuple,
    Type,
)

from eth_utils.toolz import (
    excepts,
)

from web3.types import (
    Middleware,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def construct_exception_handler_middleware(
    method_handlers: Optional[Dict[RPCEndpoint,
                                   Tuple[Type[BaseException], Callable[..., None]]]] = None
) -> Middleware:
    if method_handlers is None:
        method_handlers = {}

    def exception_handler_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], web3: "Web3"
    ) -> Callable[[RPCEndpoint, Any], RPCResponse]:
        def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method in method_handlers:
                exc_type, handler = method_handlers[method]
                return excepts(
                    exc_type,
                    make_request,
                    handler,
                )(method, params)
            else:
                return make_request(method, params)
        return middleware
    return exception_handler_middleware
