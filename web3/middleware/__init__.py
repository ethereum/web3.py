import functools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Sequence,
)

from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from .abi import (
    abi_middleware,
)
from .async_cache import (
    _async_simple_cache_middleware as async_simple_cache_middleware,
    async_construct_simple_cache_middleware,
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
from .cache import (
    _latest_block_based_cache_middleware as latest_block_based_cache_middleware,
    _simple_cache_middleware as simple_cache_middleware,
    _time_based_cache_middleware as time_based_cache_middleware,
    construct_latest_block_based_cache_middleware,
    construct_simple_cache_middleware,
    construct_time_based_cache_middleware,
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
    SignAndSendRawMiddleware,
)
from .stalecheck import (
    StaleCheckMiddleware,
)
from .validation import (
    validation_middleware,
)

if TYPE_CHECKING:
    from web3 import AsyncWeb3, Web3


def combine_middlewares(
    middlewares: Sequence[Web3Middleware],
    w3: "Web3",
    provider_request_fn: Callable[[RPCEndpoint, Any], Any],
) -> Callable[..., RPCResponse]:
    """
    Returns a callable function which takes method and params as positional arguments
    and passes these args through the request processors, makes the request, and passes
    the response through the response processors.
    """
    [setattr(middleware, "_w3", w3) for middleware in middlewares]
    request_processors = [middleware.request_processor for middleware in middlewares]
    response_processors = [
        middleware.response_processor for middleware in reversed(middlewares)
    ]
    return lambda method, params_or_response: functools.reduce(
        lambda p_o_r, processor: processor(method, p_o_r),
        response_processors,
        provider_request_fn(
            method,
            functools.reduce(
                lambda p, processor: processor(method, p),
                request_processors,
                params_or_response,
            ),
        ),
    )


async def async_combine_middlewares(
    middlewares: Sequence[Web3Middleware],
    async_w3: "AsyncWeb3",
    provider_request_fn: Callable[[RPCEndpoint, Any], Any],
) -> Callable[..., Coroutine[Any, Any, RPCResponse]]:
    """
    Returns a callable function which takes method and params as positional arguments
    and passes these args through the request processors, makes the request, and passes
    the response through the response processors.
    """
    [setattr(middleware, "_w3", async_w3) for middleware in middlewares]
    async_request_processors = [
        middleware.async_request_processor for middleware in middlewares
    ]
    async_response_processors = [
        middleware.async_response_processor for middleware in reversed(middlewares)
    ]

    async def async_request_fn(method: RPCEndpoint, params: Any) -> RPCResponse:
        for processor in async_request_processors:
            params = await processor(method, params)
        response = await provider_request_fn(method, params)
        for processor in async_response_processors:
            response = await processor(method, response)
        return response

    return async_request_fn
