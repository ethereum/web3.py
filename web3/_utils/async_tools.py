import asyncio
from concurrent.futures import (
    ThreadPoolExecutor,
)
from functools import (
    singledispatch,
    wraps,
)
import inspect
import types
from typing import (
    Any,
    Callable,
    Generator,
)

_DEFAULT_POOL = ThreadPoolExecutor()


def threadpool(f, executor=None):
    @wraps(f)
    def wrap(*args, **kwargs):
        return (executor or _DEFAULT_POOL).submit(f, *args, **kwargs)
    return wrap


@singledispatch
@threadpool
def run_in_new_loop_in_thread(co: Any, args, kwargs):
    raise TypeError('Called with unsupported argument: {}'.format(co))


@run_in_new_loop_in_thread.register(asyncio.Future)
@run_in_new_loop_in_thread.register(types.GeneratorType)
@run_in_new_loop_in_thread.register(types.CoroutineType)
@threadpool
def run_co_in_new_loop_in_thread(co: Generator[Any, None, Any]) -> Any:
    loop = asyncio.new_event_loop()
    return loop.run_until_complete(co)


@run_in_new_loop_in_thread.register(types.FunctionType)
@run_in_new_loop_in_thread.register(types.MethodType)
@threadpool
def run_f_in_new_loop_in_thread(f: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(f)
    def run(*args, **kwargs):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(f(*args, **kwargs))
    return run


@singledispatch
def sync(co: Any):
    raise TypeError('Called with unsupported argument: {}'.format(co))


@sync.register(asyncio.Future)
@sync.register(types.GeneratorType)
@sync.register(types.CoroutineType)
def sync_co(co: Generator[Any, None, Any]) -> Any:
    if not inspect.isawaitable(co):
        raise TypeError('Called with unsupported argument: {}'.format(co))
    loop = asyncio.get_event_loop()
    if loop.is_running():
        return run_in_new_loop_in_thread(co).result()
    else:
        return loop.run_until_complete(co)


@sync.register(types.FunctionType)
@sync.register(types.MethodType)
def sync_fu(f: Callable[..., Any]) -> Callable[..., Any]:
    if not asyncio.iscoroutinefunction(f):
        raise TypeError('Called with unsupported argument: {}'.format(f))

    @wraps(f)
    def run(*args, **kwargs):
        loop = asyncio.get_event_loop()
        if loop.is_running():
            run_in_new_loop_in_thread(f(*args, **kwargs))
        else:
            return loop.run_until_complete(f(*args, **kwargs))
    return run
