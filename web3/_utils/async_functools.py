# Imported and updated from the `paco` library (https://pypi.org/project/paco) which
# seems to no longer be maintained.
import asyncio
import functools
import inspect
from typing import (
    Any,
    Awaitable,
    Callable,
    Coroutine,
    Sequence,
    Tuple,
    Union,
    ValuesView,
    cast,
)


def is_func_or_coroutine(x: Any) -> bool:
    """
    Determine if the given value is a function or a coroutine function.

    Arguments:
        x (mixed): value to check.

    Returns:
        bool
    """
    return is_func_or_method(x) or asyncio.iscoroutinefunction(x)


def is_func_or_method(x: Any) -> bool:
    """
    Determines if the given value is a function or method object.

    Arguments:
        x (mixed): value to check.

    Returns:
        bool
    """
    return not asyncio.iscoroutinefunction(x) and (
        inspect.isfunction(x) or inspect.ismethod(x)
    )


def coro_wrap(fn: Callable[..., Any]) -> Callable[..., Coroutine[Any, Any, Any]]:
    """
    Wraps a given function as coroutine function.
    This function can be used as decorator.

    Arguments:
        fn (function): function object to wrap.

    Returns:
        coroutine function: wrapped function as coroutine.

    Usage::
        def mul_2(num):
            return num * 2

        # Use as function wrapper:

        coro = coro_wrap(mul_2)
        await coro(2)
        # => 4

        # Use as decorator
        @coro_wrap
        def mul_2(num):
            return num * 2
        await mul_2(2)
        # => 4
    """

    async def _async_fn(*args: Any, **kwargs: Any) -> Awaitable[Callable[..., Any]]:
        return fn(*args, **kwargs)

    return _async_fn


def async_curry(
    arity_or_fn: Union[int, Callable[..., Any]] = None,
    ignore_kwargs: bool = False,
    evaluator: Callable[..., Any] = None,
    *args: Any,
    **kwargs: Any,
) -> Union[functools.partial[Coroutine[Any, Any, Any]], Callable[..., Any]]:
    """
    Note: functools.curry is preferred for non-async methods.

    Creates a function that accepts one or more arguments of a function and
    either invokes func returning its result if at least arity number of
    arguments have been provided, or returns a function that accepts the
    remaining function arguments until the function arity is satisfied.
    This function is overloaded: you can pass a function or coroutine function
    as first argument or an `int` indicating the explicit function arity.
    Function arity can be inferred via function signature or explicitly
    passed via `arity_or_fn` param.
    You can optionally ignore keyword based arguments as well passing the
    `ignore_kwargs` param with `True` value.

    This function can be used as decorator.

    Arguments:
        arity_or_fn (int|function|coroutine function): function arity to curry
            or function to curry.
        ignore_kwargs (bool): ignore keyword arguments as arity to satisfy
            during curry.
        evaluator (function): use a custom arity evaluator function.
        *args (mixed): mixed variadic arguments for partial function
            application.
        *kwargs (mixed): keyword variadic arguments for partial function
            application.

    Raises:
        TypeError: if function is not a function or a coroutine function.

    Returns:
        function or coroutine function: function will be returned until all the
            function arity is satisfied, where a coroutine function will be
            returned instead.

    Usage:
        # Function signature inferred function arity:

        @curry_with_async_support
        async def task(x, y, z=0):
            return x * y + z
        await task(4)(4)(z=8)
        # => 24

        # User defined function arity:

        @curry_with_async_support(4)
        async def task(x, y, *args, **kw):
            return x * y + args[0] * args[1]
        await task(4)(4)(8)(8)
        # => 80

        # Ignore keyword arguments from arity:

        @curry_with_async_support(ignore_kwargs=True)
        async def task(x, y, z=0):
            return x * y
        await task(4)(4)
        # => 16
    """

    def is_valid_arg(x: Any) -> bool:
        return all(
            [
                x.kind != x.VAR_KEYWORD,
                x.kind != x.VAR_POSITIONAL,
                any([not ignore_kwargs, ignore_kwargs and x.default == x.empty]),
            ]
        )

    def params(fn: Callable[..., Any]) -> ValuesView[Any]:
        return inspect.signature(fn).parameters.values()

    def infer_arity(fn: Callable[..., Any]) -> int:
        return len([x for x in params(fn) if is_valid_arg(x)])

    def merge_args(acc: Sequence[Any], args: Any, kwargs: Any) -> Tuple[Any, Any]:
        _args, _kw = acc
        _args = _args + args
        _kw = _kw or {}
        _kw.update(kwargs)
        return _args, _kw

    def currier(
        arity: int,
        acc: Sequence[Any],
        fn: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> functools.partial[Any]:
        """
        Function either continues curring of the arguments
        or executes function if desired arguments have being collected.
        If function curried is variadic then execution without arguments
        will finish curring and trigger the function
        """
        # Merge call arguments with accumulated ones
        _args, _kwargs = merge_args(acc, args, kwargs)

        # Get current function call accumulated arity
        current_arity = len(args)

        # Count keyword params as arity to satisfy, if required
        if not ignore_kwargs:
            current_arity += len(kwargs)

        # Decrease function arity to satisfy
        arity -= current_arity

        # Use user-defined custom arity evaluator strategy, if present
        currify = evaluator and evaluator(acc, fn)

        # If arity is not satisfied, return recursive partial function
        if currify is not False and arity > 0:
            return functools.partial(currier, arity, (_args, _kwargs), fn)

        # If arity is satisfied, instantiate coroutine and return it
        return fn(*_args, **_kwargs)

    def wrapper(
        fn: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> Union[functools.partial[Any], Callable[..., Any]]:
        if not is_func_or_coroutine(fn):
            raise TypeError(
                "first argument must be a function, coroutine function, or method."
            )

        # Infer function arity, if required
        arity = arity_or_fn if isinstance(arity_or_fn, int) else infer_arity(fn)

        if is_func_or_method(fn):
            fn = coro_wrap(fn)

        # Otherwise return recursive currier function
        return currier(arity, (args, kwargs), fn, *args, **kwargs) if arity > 0 else fn

    # Return currier function or decorator wrapper

    if not is_func_or_coroutine(arity_or_fn):
        return wrapper

    fn = cast(Callable[..., Any], arity_or_fn)
    return wrapper(fn, *args, **kwargs)
