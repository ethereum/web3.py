import pytest


def test_sync_filter_against_pending_transactions(
    w3,
    wait_for_transaction,
):
    txn_filter = w3.eth.filter("pending")
    txn_1_hash = w3.eth.send_transaction(
        {
            "from": w3.eth.default_account,
            "to": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
            "value": 12345,
        }
    )
    txn_2_hash = w3.eth.send_transaction(
        {
            "from": w3.eth.default_account,
            "to": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
            "value": 54321,
        }
    )

    wait_for_transaction(w3, txn_1_hash)
    wait_for_transaction(w3, txn_2_hash)

    seen_txns = txn_filter.get_new_entries()

    assert txn_1_hash in seen_txns
    assert txn_2_hash in seen_txns


@pytest.mark.asyncio
async def test_async_filter_against_pending_transactions(
    async_w3, async_wait_for_transaction
):
    txn_filter = await async_w3.eth.filter("pending")
    txn_1_hash = await async_w3.eth.send_transaction(
        {
            "from": async_w3.eth.default_account,
            "to": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
            "value": 12345,
        }
    )
    txn_2_hash = await async_w3.eth.send_transaction(
        {
            "from": async_w3.eth.default_account,
            "to": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
            "value": 54321,
        }
    )

    await async_wait_for_transaction(async_w3, txn_1_hash)
    await async_wait_for_transaction(async_w3, txn_2_hash)

    seen_txns = await txn_filter.get_new_entries()

    assert txn_1_hash in seen_txns
    assert txn_2_hash in seen_txns
