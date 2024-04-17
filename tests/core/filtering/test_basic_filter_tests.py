import pytest


def test_filtering_sequential_blocks_with_bounded_range(
    w3, emitter, wait_for_transaction
):
    builder = emitter.events.LogNoArguments.build_filter()
    builder.from_block = "latest"

    initial_block_number = w3.eth.block_number

    builder.toBlock = initial_block_number + 100
    filter_ = builder.deploy(w3)
    for _ in range(100):
        emitter.functions.logNoArgs(which=1).transact()
    assert w3.eth.block_number == initial_block_number + 100
    assert len(filter_.get_new_entries()) == 100


def test_filtering_starting_block_range(w3, emitter, wait_for_transaction):
    for _ in range(10):
        emitter.functions.logNoArgs(which=1).transact()
    builder = emitter.events.LogNoArguments.build_filter()
    filter_ = builder.deploy(w3)
    initial_block_number = w3.eth.block_number
    for _ in range(10):
        emitter.functions.logNoArgs(which=1).transact()
    assert w3.eth.block_number == initial_block_number + 10
    assert len(filter_.get_new_entries()) == 10


def test_requesting_results_with_no_new_blocks(w3, emitter):
    builder = emitter.events.LogNoArguments.build_filter()
    filter_ = builder.deploy(w3)
    assert len(filter_.get_new_entries()) == 0


# --- async --- #


@pytest.mark.asyncio
async def test_async_filtering_sequential_blocks_with_bounded_range(
    async_w3, async_emitter
):
    builder = async_emitter.events.LogNoArguments.build_filter()
    builder.from_block = "latest"
    initial_block_number = await async_w3.eth.block_number
    builder.toBlock = initial_block_number + 100
    filter_ = await builder.deploy(async_w3)
    for _ in range(100):
        await async_emitter.functions.logNoArgs(which=1).transact()
    eth_block_number = await async_w3.eth.block_number
    assert eth_block_number == initial_block_number + 100
    new_entries = await filter_.get_new_entries()
    assert len(new_entries) == 100


@pytest.mark.asyncio
async def test_async_filtering_starting_block_range(async_w3, async_emitter):
    for _ in range(10):
        await async_emitter.functions.logNoArgs(which=1).transact()
    builder = async_emitter.events.LogNoArguments.build_filter()
    filter_ = await builder.deploy(async_w3)
    initial_block_number = await async_w3.eth.block_number
    for _ in range(10):
        await async_emitter.functions.logNoArgs(which=1).transact()
    eth_block_number = await async_w3.eth.block_number
    assert eth_block_number == initial_block_number + 10
    new_entries = await filter_.get_new_entries()
    assert len(new_entries) == 10


@pytest.mark.asyncio
async def test_async_requesting_results_with_no_new_blocks(async_w3, async_emitter):
    builder = async_emitter.events.LogNoArguments.build_filter()
    filter_ = await builder.deploy(async_w3)
    new_entries = await filter_.get_new_entries()
    assert len(new_entries) == 0
