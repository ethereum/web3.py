from __future__ import absolute_import
import functools
import itertools

from cytoolz.functoolz import (
    compose,
    partial,
)

from .base import (  # noqa: F401
    BaseMiddleware,
)
from .formatting import (  # noqa: F401
    BaseFormatterMiddleware,
)
from .geth import (  # noqa: F401
    GethFormattingMiddleware,
)
from .snapshot import (  # noqa: F401
    EVMSnapshotFormattingMiddleware,
)


def star_apply(request_fn):
    @functools.wraps(request_fn)
    def inner(request):
        method, params = request
        return request_fn(method, params)
    return inner


def wrap_provider_request(middlewares, request_fn, request_id):
    head = (
        partial(middleware._process_request, request_id=request_id)
        for middleware
        in middlewares
    )
    tail = (
        partial(middleware._process_response, request_id=request_id)
        for middleware
        in reversed(middlewares)
    )
    return compose(*reversed(tuple(itertools.chain(
        head,
        (star_apply(request_fn),),
        tail,
    ))))
