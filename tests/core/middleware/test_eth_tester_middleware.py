import pytest

from web3.types import (
    BlockData,
)


@pytest.mark.parametrize("block_number", {0, "0x0", "earliest"})
def test_get_transaction_count_formatters(w3, block_number):
    tx_counts = w3.eth.get_transaction_count(w3.eth.accounts[-1], block_number)
    assert tx_counts == 0


def test_get_block_formatters(w3):
    latest_block = w3.eth.get_block("latest")

    all_block_keys = set(BlockData.__annotations__.keys())
    latest_block_keys = set(latest_block.keys())

    keys_diff = all_block_keys.difference(latest_block_keys)
    assert len(keys_diff) == 1
    assert keys_diff.pop() == "mixHash"  # mixHash is not implemented in eth-tester
