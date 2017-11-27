import functools

from .abi import (  # noqa: F401
    abi_middleware,
)
from .formatting import (  # noqa: F401
    construct_formatting_middleware,
)
from .exception_handling import (  # noqa: F401
    construct_exception_handler_middleware,
)
from .names import (  # noqa: F401
    name_to_address_middleware,
)
from .pythonic import (  # noqa: F401
    pythonic_middleware,
)
from .stalecheck import (  # noqa: F401
    make_stalecheck_middleware,
)
from .attrdict import (  # noqa: F401
    attrdict_middleware,
)
from .fixture import (  # noqa: F401
    construct_fixture_middleware,
)


def combine_middlewares(middlewares, web3, provider_request_fn):
    """
    Returns a callable function which will call the provider.provider_request
    function wrapped with all of the middlewares.
    """
    return functools.reduce(
        lambda request_fn, middleware: middleware(request_fn, web3),
        reversed(middlewares),
        provider_request_fn,
    )
