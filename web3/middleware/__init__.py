import functools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Sequence,
)

from web3.types import (
    RPCEndpoint,
    RPCResponse,
    Middleware,
)
from .abi import (  # noqa: F401
    abi_middleware,
)
from .attrdict import (  # noqa: F401
    attrdict_middleware,
)
from .cache import (  # noqa: F401
    _latest_block_based_cache_middleware as latest_block_based_cache_middleware,
    _simple_cache_middleware as simple_cache_middleware,
    _time_based_cache_middleware as time_based_cache_middleware,
    construct_latest_block_based_cache_middleware,
    construct_simple_cache_middleware,
    construct_time_based_cache_middleware,
)
from .exception_handling import (  # noqa: F401
    construct_exception_handler_middleware,
)
from .exception_retry_request import (  # noqa: F401
    http_retry_request_middleware,
)
from .filter import (  # noqa: F401
    local_filter_middleware,
)
from .fixture import (  # noqa: F401
    construct_error_generator_middleware,
    construct_fixture_middleware,
    construct_result_generator_middleware,
)
from .formatting import (  # noqa: F401
    construct_formatting_middleware,
)
from .gas_price_strategy import (  # noqa: F401
    gas_price_strategy_middleware,
)
from .geth_poa import (  # noqa: F401
    geth_poa_middleware,
)
from .names import (  # noqa: F401
    name_to_address_middleware,
)
from .normalize_errors import (  # noqa: F401
    normalize_errors_middleware,
)
from .normalize_request_parameters import (  # noqa: F401
    request_parameter_normalizer,
)
from .pythonic import (  # noqa: F401
    pythonic_middleware,
)
from .signing import (  # noqa: F401
    construct_sign_and_send_raw_middleware,
)
from .stalecheck import (  # noqa: F401
    make_stalecheck_middleware,
)
from .validation import (  # noqa: F401
    validation_middleware,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def combine_middlewares(
    middlewares: Sequence[Middleware],
    web3: 'Web3',
    provider_request_fn: Callable[[RPCEndpoint, Any], Any]
) -> Callable[..., RPCResponse]:
    """
    Returns a callable function which will call the provider.provider_request
    function wrapped with all of the middlewares.
    """
    return functools.reduce(
        lambda request_fn, middleware: middleware(request_fn, web3),
        reversed(middlewares),
        provider_request_fn,
    )
