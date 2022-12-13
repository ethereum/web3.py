import asyncio

from web3._utils.async_functools import (
    async_curry,
    is_func_or_coroutine,
)


def run_in_loop(coro, *args, **kw):
    loop = asyncio.get_event_loop()
    if is_func_or_coroutine(coro):
        coro = coro(*args, **kw)
    return loop.run_until_complete(coro)


def task(x, y, baz=None, *args, **kw):
    return x + y, baz, kw


async def coro(x, y, baz=None, *args, **kw):
    async def _task():
        return task(x, y, baz=baz, *args, **kw)

    return await _task()


def test_curry_function_arity():
    num, val, kw = run_in_loop(async_curry(task)(2)(4)(baz="foo"))
    assert num == 6
    assert val == "foo"
    assert kw == {}

    num, val, kw = run_in_loop(async_curry(task)(2, 4)(baz="foo"))
    assert num == 6
    assert val == "foo"
    assert kw == {}

    num, val, kw = run_in_loop(async_curry(task)(2, 4, baz="foo"))
    assert num == 6
    assert val == "foo"
    assert kw == {}

    num, val, kw = run_in_loop(async_curry(task)(2, 4, baz="foo", fee=True))
    assert num == 6
    assert val == "foo"
    assert kw == {"fee": True}


def test_curry_single_arity():
    assert run_in_loop(async_curry(lambda x: x)(True))


def test_curry_zero_arity():
    assert run_in_loop(async_curry(lambda: True))


def test_curry_custom_arity():
    currier = async_curry(4)
    num, val, kw = run_in_loop(currier(task)(2)(4)(baz="foo")(tee=True))
    assert num == 6
    assert val == "foo"
    assert kw == {"tee": True}


def test_curry_ignore_kwargs():
    currier = async_curry(ignore_kwargs=True)
    num, val, kw = run_in_loop(currier(task)(2)(4))
    assert num == 6
    assert val is None
    assert kw == {}

    currier = async_curry(ignore_kwargs=True)
    num, val, kw = run_in_loop(currier(task)(2)(4, baz="foo", tee=True))
    assert num == 6
    assert val == "foo"
    assert kw == {"tee": True}


def test_curry_extra_arguments():
    currier = async_curry(4)
    num, val, kw = run_in_loop(currier(task)(2)(4)(baz="foo")(tee=True))
    assert num == 6
    assert val == "foo"
    assert kw == {"tee": True}

    currier = async_curry(4)
    num, val, kw = run_in_loop(currier(task)(2)(4)(baz="foo")(tee=True))
    assert num == 6
    assert val == "foo"
    assert kw == {"tee": True}


def test_curry_evaluator_function():
    def evaluator(acc, fn):
        return len(acc[0]) < 3

    def task(x, y):
        return x * y

    currier = async_curry(evaluator=evaluator)
    assert run_in_loop(currier(task)(4, 4)) == 16


def test_curry_decorator():
    @async_curry
    def task(x, y, z):
        return x + y + z

    assert run_in_loop(task(2)(4)(8)) == 14

    @async_curry(4)
    def task(x, y, *args):
        return x + y + args[0] + args[1]

    assert run_in_loop(task(2)(4)(8)(10)) == 24

    @async_curry(4)
    async def _task(x, y, *args):
        return x + y + args[0] + args[1]

    assert run_in_loop(_task(2)(4)(8)(10)) == 24


def test_curry_coroutine():
    num, val, kw = run_in_loop(async_curry(coro)(2)(4)(baz="foo", tee=True))
    assert num == 6
    assert val == "foo"
    assert kw == {"tee": True}
