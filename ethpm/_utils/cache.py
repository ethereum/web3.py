import functools
from typing import Any, Callable


class cached_property:
    """
    Decorator that converts a method with a single self argument into a
    property cached on the instance.

    Optional ``name`` argument allows you to make cached properties of other
    methods. (e.g.  url = cached_property(get_absolute_url, name='url') )
    """

    def __init__(self, func: Callable[..., Any], name: str = None) -> None:
        self.func = func
        self.name = name or func.__name__
        # type ignored b/c self is 'cached_property' but expects 'Callable[..., Any]'
        functools.update_wrapper(self, func)  # type: ignore

    def __get__(self, instance: Any, cls: Any = None) -> Any:
        """
        Call the function and put the return value in instance.__dict__ so that
        subsequent attribute access on the instance returns the cached value
        instead of calling cached_property.__get__().
        """
        if instance is None:
            return self
        res = instance.__dict__[self.name] = self.func(instance)
        return res
