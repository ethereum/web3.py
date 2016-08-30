import random
import gevent
from flaky import flaky


@flaky(max_runs=3)
def test_filter_against_latest_blocks(web3_empty, wait_for_block):
    web3 = web3_empty

    seen_blocks = []
    txn_filter = web3.eth.filter("latest")
    txn_filter.watch(seen_blocks.append)

    current_block = web3.eth.blockNumber

    wait_for_block(web3, current_block + 3)

    with gevent.Timeout(5):
        while len(seen_blocks) < 2:
            gevent.sleep(random.random())

    txn_filter.stop_watching(3)

    expected_block_hashes = [
        web3.eth.getBlock(n)['hash'] for n in range(current_block + 1, current_block + 3)
    ]
    assert len(seen_blocks) >= 2

    assert set(expected_block_hashes).issubset(seen_blocks)
