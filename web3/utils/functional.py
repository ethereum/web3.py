import functools


def identity(value):
    return value


def combine(f, g):
    return lambda x: f(g(x))


def compose(*functions):
    return functools.reduce(combine, reversed(functions), identity)


def apply_formatters_to_return(*formatters):
    formatter = compose(*formatters)

    def outer(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            value = fn(*args, **kwargs)
            return formatter(value)
        return inner
    return outer
