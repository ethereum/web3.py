import asyncio
from concurrent.futures import (
    ThreadPoolExecutor,
)
import pytest
import threading

from web3._utils.async_caching import (
    async_lock,
)

# --- async -- #


@pytest.mark.asyncio
async def test_async_lock_releases_if_a_task_is_cancelled():
    # inspired by issue #2693
    # Note: this test will raise a `TimeoutError` if `request.async_lock` is not
    # applied correctly

    _thread_pool = ThreadPoolExecutor(max_workers=1)
    _lock = threading.Lock()

    async def _utilize_async_lock():
        async with async_lock(_thread_pool, _lock):
            await asyncio.sleep(0.2)

    asyncio.create_task(_utilize_async_lock())

    inner = asyncio.create_task(_utilize_async_lock())
    await asyncio.sleep(0.1)
    inner.cancel()

    outer = asyncio.wait_for(_utilize_async_lock(), 2)
    await outer
