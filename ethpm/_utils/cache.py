from typing import (
    Any,
    Callable,
)


class cached_property:
    """
    Decorator that converts a method with a single self argument into a
    property cached on the instance.

    Optional ``name`` argument allows you to make cached properties of other
    methods. (e.g.  url = cached_property(get_absolute_url, name='url') )
    """

    def __init__(self, func: Callable[..., Any], name: str = None) -> None:
        self.wrapped_func = func
        self.name = name
        self.__doc__ = getattr(func, '__doc__')

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

    def __set_name__(self, cls: Any = None, name: str = None) -> None:
        """
        The function is called at the time the cls class is created.
        The descriptor would be assigned to name.
        """
        if self.name is None:
            self.name = name
            self.func = self.wrapped_func
        if name != self.name:
            raise TypeError(
                "Unable to assign cached_property for two different names "
                f"(%{self.name} and {name})."
            )
