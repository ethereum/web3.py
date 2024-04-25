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
            raise ValueError(f"Recursively called {to_wrap} with {args!r}")
        to_wrap.__already_called[thread_local_args] = True  # type: ignore
        try:
            wrapped_val = to_wrap(*args)
        finally:
            del to_wrap.__already_called[thread_local_args]  # type: ignore
        return wrapped_val

    return wrapped


def deprecate_method(
    replacement_method: str = None, deprecation_msg: str = None
) -> Callable[..., Any]:
    """
    Decorate a deprecated function with info on its replacement method OR a clarifying
    reason for the deprecation.

    @deprecate_method("to_bytes()")
    def to_ascii(arg):
        ...

    @deprecate_method(deprecation_msg=(
        "This method is no longer supported and will be removed in the next release."
    ))
    def some_method(arg):
        ...
    """
    if replacement_method is None and deprecation_msg is None:
        raise ValueError(
            "Must provide either `replacement_method` or `deprecation_msg`"
        )

    def decorator(to_wrap: TFunc) -> TFunc:
        @functools.wraps(to_wrap)
        def wrapper(*args: Any, **kwargs: Any) -> Callable[..., Any]:
            msg = (
                f"{to_wrap.__name__} is deprecated in favor of {replacement_method}"
                if replacement_method is not None
                else deprecation_msg
            )
            warnings.warn(msg, category=DeprecationWarning)
            return to_wrap(*args, **kwargs)

        return cast(TFunc, wrapper)

    return decorator
