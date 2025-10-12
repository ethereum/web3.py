import functools
import threading
from typing import (
    Any,
    Callable,
    Final,
    Set,
    Tuple,
    TypeVar,
    cast,
)
import warnings

from faster_web3.exceptions import (
    Web3ValueError,
)

TFunc = TypeVar("TFunc", bound=Callable[..., Any])


get_thread_id: Final = threading.get_ident


def reject_recursive_repeats(to_wrap: Callable[..., Any]) -> Callable[..., Any]:
    """
    Prevent simple cycles by returning None when called recursively with same instance
    """
    already_called: Set[Tuple[int, ...]] = set()

    try:
        to_wrap.__already_called = already_called  # type: ignore [attr-defined]
    except AttributeError:
        # we can't set arbitrary attributes on native functions
        # but this isn't necessary for faster-web3.py
        pass

    @functools.wraps(to_wrap)
    def wrapped(*args: Any) -> Any:
        thread_local_args = (get_thread_id(), *map(id, args))
        if thread_local_args in already_called:
            raise Web3ValueError(f"Recursively called {to_wrap} with {args!r}")
        already_called.add(thread_local_args)
        try:
            return to_wrap(*args)
        finally:
            already_called.remove(thread_local_args)

    return wrapped


def deprecated_for(replace_message: str) -> Callable[..., Any]:
    """
    Decorate a deprecated function, with info about what to use instead, like:

    @deprecated_for("use to_bytes() instead")
    def toAscii(arg):
        ...
    """

    def decorator(to_wrap: TFunc) -> TFunc:
        @functools.wraps(to_wrap)
        def wrapper(*args: Any, **kwargs: Any) -> Callable[..., Any]:
            warnings.warn(
                f"{to_wrap.__name__} is deprecated: {replace_message}",
                category=DeprecationWarning,
                stacklevel=2,
            )
            return to_wrap(*args, **kwargs)

        return cast(TFunc, wrapper)

    return decorator
