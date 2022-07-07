import pytest


@pytest.mark.parametrize("block_number", {0, "0x0", "earliest"})
def test_get_transaction_count_formatters(w3, block_number):
    tx_counts = w3.eth.get_transaction_count(w3.eth.accounts[-1], block_number)
    assert tx_counts == 0
