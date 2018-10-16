import asyncio
import pytest

from web3._utils.async_tools import (
    sync,
)


async def nested_sync():
    await asyncio.sleep(0)
    return sync(asyncio.sleep(0))


@pytest.mark.asyncio
async def test_async_calling_sync(w3):
    sync(nested_sync)
