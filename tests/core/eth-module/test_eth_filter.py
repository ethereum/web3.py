import pytest

import pytest_asyncio

from web3 import (
    Web3,
)
from web3._utils.filters import (
    AsyncBlockFilter,
    AsyncLogFilter,
    AsyncTransactionFilter,
    BlockFilter,
    LogFilter,
    TransactionFilter,
)
from web3.eth import (
    AsyncEth,
)
from web3.providers.eth_tester.main import (
    AsyncEthereumTesterProvider,
)


def test_Eth_filter_creates_correct_filter_type(w3):
    filter1 = w3.eth.filter("latest")
    assert isinstance(filter1, BlockFilter)
    filter2 = w3.eth.filter("pending")
    assert isinstance(filter2, TransactionFilter)
    filter3 = w3.eth.filter({})
    assert isinstance(filter3, LogFilter)


# --- async --- #


@pytest_asyncio.fixture()
async def async_w3():
    provider = AsyncEthereumTesterProvider()
    w3 = Web3(provider, modules={"eth": [AsyncEth]}, middlewares=[])
    return w3


@pytest.mark.asyncio
async def test_AsyncEth_filter_creates_correct_filter_type(async_w3):
    filter1 = await async_w3.eth.filter("latest")
    assert isinstance(filter1, AsyncBlockFilter)
    filter2 = await async_w3.eth.filter("pending")
    assert isinstance(filter2, AsyncTransactionFilter)
    filter3 = await async_w3.eth.filter({})
    assert isinstance(filter3, AsyncLogFilter)
