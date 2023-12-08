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
    local_filter_middleware,
)
from .formatting import (
    construct_formatting_middleware,
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
    SignAndSendRawMiddlewareBuilder,
)
from .stalecheck import (
    StaleCheckMiddlewareBuilder,
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
    accumulator_fn = provider_request_fn
    for middleware in reversed(middlewares):
        # initialize the middleware and wrap the accumulator function down the stack
        initialized = middleware(async_w3)
        accumulator_fn = await initialized._async_wrap_make_request(accumulator_fn)
    return accumulator_fn
