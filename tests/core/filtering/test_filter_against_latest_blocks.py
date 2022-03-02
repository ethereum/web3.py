from web3._utils.threads import (
    Timeout,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


def test_sync_filter_against_latest_blocks(w3, sleep_interval, wait_for_block):
    if not isinstance(w3.provider, EthereumTesterProvider):
        w3.provider = EthereumTesterProvider()

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
