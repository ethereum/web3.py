import pytest

from web3._utils.threads import (
    Timeout,
)


def test_sync_filter_against_latest_blocks(w3, sleep_interval, wait_for_block):
    txn_filter = w3.eth.filter("latest")
    current_block = w3.eth.block_number
    wait_for_block(w3, current_block + 3)

    found_block_hashes = []
    with Timeout(5) as timeout:
        while len(found_block_hashes) < 3:
            found_block_hashes.extend(txn_filter.get_new_entries())
            timeout.sleep(sleep_interval())

    assert len(found_block_hashes) == 3

    expected_block_hashes = [
        w3.eth.get_block(n + 1).hash for n in range(current_block, current_block + 3)
    ]
    assert found_block_hashes == expected_block_hashes


# --- async --- #


@pytest.mark.asyncio
async def test_async_filter_against_latest_blocks(
    async_w3, sleep_interval, async_wait_for_block
):
    txn_filter = await async_w3.eth.filter("latest")
    current_block = await async_w3.eth.block_number
    await async_wait_for_block(async_w3, current_block + 3)

    found_block_hashes = []
    with Timeout(5) as timeout:
        while len(found_block_hashes) < 3:
            new_entries = await txn_filter.get_new_entries()
            found_block_hashes.extend(new_entries)
            await timeout.async_sleep(sleep_interval())

    assert len(found_block_hashes) == 3

    expected_block_hashes = []
    for n in range(current_block, current_block + 3):
        block = await async_w3.eth.get_block(n + 1)
        expected_block_hashes.append(block.hash)

    assert found_block_hashes == expected_block_hashes
