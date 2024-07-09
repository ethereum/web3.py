import pytest

import pytest_asyncio

from web3 import (
    AsyncWeb3,
)
from web3._utils.filters import (
    AsyncBlockFilter,
    AsyncLogFilter,
    BlockFilter,
    LogFilter,
)
from web3.providers.eth_tester.main import (
    AsyncEthereumTesterProvider,
)


def test_eth_filter_creates_correct_filter_type(w3):
    filter1 = w3.eth.filter("latest")
    assert isinstance(filter1, BlockFilter)
    filter2 = w3.eth.filter({})
    assert isinstance(filter2, LogFilter)


# --- async --- #


@pytest_asyncio.fixture()
async def async_w3():
    provider = AsyncEthereumTesterProvider()
    w3 = AsyncWeb3(provider)
    return w3


@pytest.mark.asyncio
async def test_async_eth_filter_creates_correct_filter_type(async_w3):
    filter1 = await async_w3.eth.filter("latest")
    assert isinstance(filter1, AsyncBlockFilter)
    filter2 = await async_w3.eth.filter({})
    assert isinstance(filter2, AsyncLogFilter)
