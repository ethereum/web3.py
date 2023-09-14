import functools
from typing import (
    Coroutine,
    TYPE_CHECKING,
    Any,
    Callable,
    Sequence,
)

from web3.types import (
    AsyncMiddleware,
    Middleware,
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
    async_attrdict_middleware,
    attrdict_middleware,
)
from .buffered_gas_estimate import (
    async_buffered_gas_estimate_middleware,
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
from .exception_handling import (
    construct_exception_handler_middleware,
)
from .exception_retry_request import (
    async_http_retry_request_middleware,
    http_retry_request_middleware,
)
from .filter import (
    async_local_filter_middleware,
    local_filter_middleware,
)
from .fixture import (
    async_construct_error_generator_middleware,
    async_construct_result_generator_middleware,
    construct_error_generator_middleware,
    construct_fixture_middleware,
    construct_result_generator_middleware,
)
from .formatting import (
    construct_formatting_middleware,
)
from .gas_price_strategy import (
    async_gas_price_strategy_middleware,
    gas_price_strategy_middleware,
)
from .geth_poa import (
    async_geth_poa_middleware,
    geth_poa_middleware,
)
from .names import (
    async_name_to_address_middleware,
    name_to_address_middleware,
)
from .normalize_request_parameters import (
    request_parameter_normalizer,
)
from .pythonic import (
    pythonic_middleware,
)
from .signing import (
    construct_sign_and_send_raw_middleware,
)
from .stalecheck import (
    async_make_stalecheck_middleware,
    make_stalecheck_middleware,
)
from .validation import (
    async_validation_middleware,
    validation_middleware,
)

if TYPE_CHECKING:
    from web3 import AsyncWeb3, Web3


def combine_middlewares(
    middlewares: Sequence[Middleware],
    w3: "Web3",
    provider_request_fn: Callable[[RPCEndpoint, Any], Any],
) -> Callable[..., RPCResponse]:
    """
    Returns a callable function which will call the provider.provider_request
    function wrapped with all of the middlewares.
    """
    return functools.reduce(
        lambda request_fn, middleware: middleware(request_fn, w3),
        reversed(middlewares),
        provider_request_fn,
    )


async def async_combine_middlewares(
    middlewares: Sequence[AsyncMiddleware],
    async_w3: "AsyncWeb3",
    provider_request_fn: Callable[[RPCEndpoint, Any], Any],
) -> Callable[..., Coroutine[Any, Any, RPCResponse]]:
    """
    Returns a callable function which will call the provider.provider_request
    function wrapped with all of the middlewares.
    """
    accumulator_fn = provider_request_fn
    for middleware in reversed(middlewares):
        accumulator_fn = await construct_middleware(
            middleware, accumulator_fn, async_w3
        )
    return accumulator_fn


async def construct_middleware(
    async_middleware: AsyncMiddleware,
    fn: Callable[..., RPCResponse],
    async_w3: "AsyncWeb3",
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    return await async_middleware(fn, async_w3)
