import asyncio
from web3._utils.async_tools import (
    sync,
)


async def coro_sleeper():
    await asyncio.sleep(0)
    return "Im awake!"


def test_sync_coro():
    sleeper = sync(coro_sleeper)
    assert sleeper() == "Im awake!"


def test_sync_awaitable():
    assert sync(coro_sleeper()) == "Im awake!"
