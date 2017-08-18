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
from .snapshot import (  # noqa: F401
    EVMSnapshotFormattingMiddleware,
)


@curry
def _reduce_middleware_fn(request_fn, middleware, provider, request_id):
    """
    The reduce function for wrapping the provider request in the middlewares.
    """
    return partial(
        middleware(provider, request_fn),
        request_id=request_id,
    )


def wrap_provider_request(middlewares, provider, request_id):
    """
    Returns a callable function which will call the provider.make_request
    function wrapped with all of the middlewares.
    """
    return functools.reduce(
        _reduce_middleware_fn(provider=provider, request_id=request_id),
        reversed(middlewares),
        provider.make_request,
    )
