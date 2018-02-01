from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.utils.threads import (
    Timeout,
)


def test_sync_filter_against_latest_blocks(web3, sleep_interval, wait_for_block):
    if EthereumTesterProvider not in map(type, web3.providers):
        web3.providers = EthereumTesterProvider()

    txn_filter = web3.eth.filter("latest")

    current_block = web3.eth.blockNumber

    wait_for_block(web3, current_block + 3)

    found_block_hashes = []
    with Timeout(5) as timeout:
        while len(found_block_hashes) < 3:
            found_block_hashes.extend(txn_filter.get_new_entries())
            timeout.sleep(sleep_interval())

    assert len(found_block_hashes) == 3

    expected_block_hashes = [
        web3.eth.getBlock(n + 1).hash for n in range(current_block, current_block + 3)
    ]
    assert found_block_hashes == expected_block_hashes
