import pytest


def test_eth_chain_id(w3):
    assert w3.eth.chain_id == 61


def test_set_chain_id(w3):
    assert w3.eth.chain_id == 61

    w3.eth.chain_id = 72
    assert w3.eth.chain_id == 72

    w3.eth.chain_id = None
    assert w3.eth.chain_id == 61


@pytest.mark.asyncio
async def test_async_set_chain_id(async_w3):
    assert await async_w3.eth.chain_id == 61

    async_w3.eth.chain_id = 72
    assert await async_w3.eth.chain_id == 72

    async_w3.eth.chain_id = None
    assert await async_w3.eth.chain_id == 61
