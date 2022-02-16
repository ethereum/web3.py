import functools
import threading
from typing import (
    Any,
    Callable,
    TypeVar,
    cast,
)
import warnings

TFunc = TypeVar("TFunc", bound=Callable[..., Any])


def reject_recursive_repeats(to_wrap: Callable[..., Any]) -> Callable[..., Any]:
    """
    Prevent simple cycles by returning None when called recursively with same instance
    """
    # types ignored b/c dynamically set attribute
    to_wrap.__already_called = {}  # type: ignore

    @functools.wraps(to_wrap)
    def wrapped(*args: Any) -> Any:
        arg_instances = tuple(map(id, args))
        thread_id = threading.get_ident()
        thread_local_args = (thread_id,) + arg_instances
        if thread_local_args in to_wrap.__already_called:  # type: ignore
            raise ValueError('Recursively called %s with %r' % (to_wrap, args))
        to_wrap.__already_called[thread_local_args] = True  # type: ignore
        try:
            wrapped_val = to_wrap(*args)
        finally:
            del to_wrap.__already_called[thread_local_args]  # type: ignore
        return wrapped_val
    return wrapped


def deprecated_for(replace_message: str) -> Callable[..., Any]:
    """
    Decorate a deprecated function, with info about what to use instead, like:

    @deprecated_for("toBytes()")
    def toAscii(arg):
        ...
    """
    def decorator(to_wrap: TFunc) -> TFunc:
        @functools.wraps(to_wrap)
        def wrapper(*args: Any, **kwargs: Any) -> Callable[..., Any]:
            warnings.warn(
                f"{to_wrap.__name__} is deprecated in favor of {replace_message}",
                category=DeprecationWarning)
            return to_wrap(*args, **kwargs)
        return cast(TFunc, wrapper)
    return decorator


class DeprecationMetaClass(type):
    """ A custom class that intercepts the __call__ method to decide whether
    or not to raize a warning against the loop argument.
    """
    def __call__(cls, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        new_kwargs = {key: val for key, val in kwargs.items() if key != 'loop'}
        if 'loop' in kwargs:
            warnings.warn(
                "The loop parameter is deprecated and was removed from "
                "websocket provider as of web3 v5. Consider instantiating "
                "this class without passing this argument instead.",
                category=DeprecationWarning,
                stacklevel=2,
            )
        obj = cls.__new__(cls, *args, **new_kwargs)  # type: ignore
        obj.__init__(*args, **new_kwargs)
        return obj
