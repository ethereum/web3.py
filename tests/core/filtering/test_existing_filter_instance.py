import pytest

from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.utils.threads import (
    Timeout,
)


@pytest.fixture()
def filter_id(web3):
    if EthereumTesterProvider not in map(type, web3.providers):
        web3.providers = EthereumTesterProvider()

    block_filter = web3.eth.filter("latest")
    return block_filter.filter_id


def test_instatiate_existing_filter(web3, sleep_interval, wait_for_block, filter_id):
    with pytest.raises(TypeError):
        web3.eth.filter('latest', filter_id)
    with pytest.raises(TypeError):
        web3.eth.filter('latest', filter_id=filter_id)
    with pytest.raises(TypeError):
        web3.eth.filter(filter_params='latest', filter_id=filter_id)

    block_filter = web3.eth.filter(filter_id=filter_id)

    current_block = web3.eth.blockNumber

    wait_for_block(web3, current_block + 3)

    found_block_hashes = []
    with Timeout(5) as timeout:
        while len(found_block_hashes) < 3:
            found_block_hashes.extend(block_filter.get_new_entries())
            timeout.sleep(sleep_interval())

    assert len(found_block_hashes) == 3

    expected_block_hashes = [
        web3.eth.getBlock(n + 1).hash for n in range(current_block, current_block + 3)
    ]
    assert found_block_hashes == expected_block_hashes
