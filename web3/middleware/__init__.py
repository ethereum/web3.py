from __future__ import absolute_import
import functools

from cytoolz.functoolz import (
    partial,
    curry,
)

from .formatting import (  # noqa: F401
    construct_formatting_middleware,
)
from .pythonic import (  # noqa: F401
    pythonic_middleware,
)


@curry
def _reduce_middleware_fn(request_fn, middleware, web3, request_id):
    """
    The reduce function for wrapping the provider request in the middlewares.
    """
    return partial(
        middleware(request_fn, web3),
        request_id=request_id,
    )


def wrap_provider_request(middlewares, web3, make_request_fn, request_id):
    """
    Returns a callable function which will call the provider.make_request
    function wrapped with all of the middlewares.
    """
    return functools.reduce(
        _reduce_middleware_fn(web3=web3, request_id=request_id),
        reversed(middlewares),
        make_request_fn,
    )
