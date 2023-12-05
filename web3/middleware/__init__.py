from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Sequence,
    Type,
)

from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from .abi import (
    abi_middleware,
)
from .attrdict import (
    attrdict_middleware,
)
from .base import (
    Web3Middleware,
)
from .buffered_gas_estimate import (
    buffered_gas_estimate_middleware,
)
from .gas_price_strategy import (
    gas_price_strategy_middleware,
)
from .proof_of_authority import (
    extradata_to_poa_middleware,
)
from .names import (
    ens_name_to_address_middleware,
)
from .filter import (
    async_local_filter_middleware,
    local_filter_middleware,
)
from .gas_price_strategy import (
    GasPriceStrategyMiddleware,
)
from .normalize_request_parameters import (
    request_parameter_normalizer,
)
from .pythonic import (
    pythonic_middleware,
)
from .signing import (
    construct_sign_and_send_raw_middleware,
    SignAndSendRawMiddleware,
)
from .stalecheck import (
    StaleCheckMiddleware,
    make_stalecheck_middleware,
)
from .validation import (
    validation_middleware,
)

if TYPE_CHECKING:
    from web3 import AsyncWeb3, Web3


def combine_middlewares(
    middlewares: Sequence[Type[Web3Middleware]],
    w3: "Web3",
    provider_request_fn: Callable[[RPCEndpoint, Any], Any],
) -> Callable[..., RPCResponse]:
    """
    Returns a callable function which takes method and params as positional arguments
    and passes these args through the request processors, makes the request, and passes
    the response through the response processors.
    """
    accumulator_fn = provider_request_fn
    for middleware in reversed(middlewares):
        # initialize the middleware and wrap the accumulator function down the stack
        accumulator_fn = middleware(w3)._wrap_make_request(accumulator_fn)
    return accumulator_fn


async def async_combine_middlewares(
    middlewares: Sequence[Type[Web3Middleware]],
    async_w3: "AsyncWeb3",
    provider_request_fn: Callable[[RPCEndpoint, Any], Any],
) -> Callable[..., Coroutine[Any, Any, RPCResponse]]:
    """
    Returns a callable function which takes method and params as positional arguments
    and passes these args through the request processors, makes the request, and passes
    the response through the response processors.
    """
    middlewares = [middleware(async_w3) for middleware in middlewares]
    async_request_processors = [
        middleware.async_request_processor for middleware in middlewares
    ]
    async_response_processors = [
        middleware.async_response_processor for middleware in reversed(middlewares)
    ]

    async def async_request_fn(method: RPCEndpoint, params: Any) -> RPCResponse:
        for processor in async_request_processors:
            method, params = await processor(method, params)
        response = await provider_request_fn(method, params)
        for processor in async_response_processors:
            response = await processor(method, response)
        return response

    return async_request_fn
