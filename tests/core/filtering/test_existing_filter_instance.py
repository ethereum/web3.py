import pytest

import pytest_asyncio

from web3._utils.threads import (
    Timeout,
)


@pytest.fixture()
def filter_id(w3):
    block_filter = w3.eth.filter("latest")
    return block_filter.filter_id


def test_instantiate_existing_filter(w3, sleep_interval, wait_for_block, filter_id):
    with pytest.raises(TypeError):
        w3.eth.filter("latest", filter_id)
    with pytest.raises(TypeError):
        w3.eth.filter("latest", filter_id=filter_id)
    with pytest.raises(TypeError):
        w3.eth.filter(filter_params="latest", filter_id=filter_id)

    block_filter = w3.eth.filter(filter_id=filter_id)

    current_block = w3.eth.block_number

    wait_for_block(w3, current_block + 3)

    found_block_hashes = []
    with Timeout(5) as timeout:
        while len(found_block_hashes) < 3:
            found_block_hashes.extend(block_filter.get_new_entries())
            timeout.sleep(sleep_interval())

    assert len(found_block_hashes) == 3

    expected_block_hashes = [
        w3.eth.get_block(n + 1).hash for n in range(current_block, current_block + 3)
    ]
    assert found_block_hashes == expected_block_hashes


# --- async --- #


@pytest_asyncio.fixture()
async def async_filter_id(async_w3):
    block_filter = await async_w3.eth.filter("latest")
    return block_filter.filter_id


@pytest.mark.asyncio
async def test_async_instantiate_existing_filter(
    async_w3, sleep_interval, async_wait_for_block, async_filter_id
):
    with pytest.raises(TypeError):
        await async_w3.eth.filter("latest", async_filter_id)
    with pytest.raises(TypeError):
        await async_w3.eth.filter("latest", filter_id=async_filter_id)
    with pytest.raises(TypeError):
        await async_w3.eth.filter(filter_params="latest", filter_id=async_filter_id)

    block_filter = await async_w3.eth.filter(filter_id=async_filter_id)

    current_block = await async_w3.eth.block_number

    await async_wait_for_block(async_w3, current_block + 3)

    found_block_hashes = []
    with Timeout(5) as timeout:
        while len(found_block_hashes) < 3:
            new_entries = await block_filter.get_new_entries()
            found_block_hashes.extend(new_entries)
            await timeout.async_sleep(sleep_interval())

    assert len(found_block_hashes) == 3

    expected_block_hashes = []
    for n in range(current_block, current_block + 3):
        next_block = await async_w3.eth.get_block(n + 1)
        expected_block_hashes.append(next_block.hash)

    assert found_block_hashes == expected_block_hashes
