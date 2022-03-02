import pytest

from web3._utils.threads import (
    Timeout,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


@pytest.fixture()
def filter_id(w3):
    if not isinstance(w3.provider, EthereumTesterProvider):
        w3.provider = EthereumTesterProvider()

    block_filter = w3.eth.filter("latest")
    return block_filter.filter_id


def test_instantiate_existing_filter(w3, sleep_interval, wait_for_block, filter_id):
    with pytest.raises(TypeError):
        w3.eth.filter('latest', filter_id)
    with pytest.raises(TypeError):
        w3.eth.filter('latest', filter_id=filter_id)
    with pytest.raises(TypeError):
        w3.eth.filter(filter_params='latest', filter_id=filter_id)

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
