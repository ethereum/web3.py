from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Sequence,
)

from .attrdict import (
    AttributeDictMiddleware,
)
from .base import (
    Middleware,
)
from .buffered_gas_estimate import (
    BufferedGasEstimateMiddleware,
)
from .filter import (
    LocalFilterMiddleware,
)
from .formatting import (
    FormattingMiddlewareBuilder,
)
from .gas_price_strategy import (
    GasPriceStrategyMiddleware,
)
from .names import (
    ENSNameToAddressMiddleware,
)
from .proof_of_authority import (
    ExtradataToPOAMiddleware,
)
from .pythonic import (
    PythonicMiddleware,
)
from .signing import (
    SignAndSendRawMiddlewareBuilder,
)
from .stalecheck import (
    StalecheckMiddlewareBuilder,
)
from .validation import (
    ValidationMiddleware,
)
from ..types import (
    AsyncMakeRequestFn,
    MakeRequestFn,
)


if TYPE_CHECKING:
    from web3 import (
        AsyncWeb3,
        Web3,
    )
    from web3.types import (
        RPCResponse,
    )


def combine_middlewares(
    middlewares: Sequence[Middleware],
    w3: "Web3",
    provider_request_fn: MakeRequestFn,
) -> Callable[..., "RPCResponse"]:
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
    middlewares: Sequence[Middleware],
    async_w3: "AsyncWeb3",
    provider_request_fn: AsyncMakeRequestFn,
) -> Callable[..., Coroutine[Any, Any, "RPCResponse"]]:
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
