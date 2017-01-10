import random
from flaky import flaky

from web3.utils.compat import (
    Timeout,
)


@flaky(max_runs=3)
def test_filter_against_latest_blocks(web3, sleep_interval, wait_for_block, skip_if_testrpc):
    skip_if_testrpc(web3)

    seen_blocks = []
    txn_filter = web3.eth.filter("latest")
    txn_filter.watch(seen_blocks.append)

    current_block = web3.eth.blockNumber

    wait_for_block(web3, current_block + 3)

    with Timeout(5) as timeout:
        while len(seen_blocks) < 2:
            timeout.sleep(sleep_interval())

    txn_filter.stop_watching(3)

    expected_block_hashes = [
        web3.eth.getBlock(n)['hash'] for n in range(current_block + 1, current_block + 3)
    ]
    assert len(seen_blocks) >= 2

    assert set(expected_block_hashes).issubset(seen_blocks)
