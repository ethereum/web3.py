import asyncio
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
        raise TypeError("Cannot use sync() inside a running event loop")
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
            raise TypeError("Cannot use sync() inside a running event loop")
        else:
            return loop.run_until_complete(f(*args, **kwargs))
    return run


async def coro_pipe(data, *coros):
    for coro in coros:
        data = await coro(data)
    return data
