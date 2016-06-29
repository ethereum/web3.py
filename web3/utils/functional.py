import functools


def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def apply_formatters(*formatters):
    formatter = compose(*formatters)

    def outer(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            value = fn(*args, **kwargs)
            return formatter(value)
        return inner
    return outer
