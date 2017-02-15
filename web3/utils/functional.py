import functools

from eth_utils import (
    compose,
)


def apply_formatters_to_return(*formatters):
    formatter = compose(*formatters)

    def outer(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            value = fn(*args, **kwargs)
            return formatter(value)
        return inner
    return outer
