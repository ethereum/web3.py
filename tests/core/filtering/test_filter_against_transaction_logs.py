import pytest


def test_sync_filter_against_log_events(
    w3, emitter, wait_for_transaction, emitter_contract_event_ids
):
    txn_filter = w3.eth.filter({})
    txn_hashes = set()
    txn_hashes.add(
        emitter.functions.logNoArgs(
            emitter_contract_event_ids.LogNoArguments
        ).transact()
    )

    for txn_hash in txn_hashes:
        wait_for_transaction(w3, txn_hash)

    seen_logs = txn_filter.get_new_entries()

    assert txn_hashes == {log["transactionHash"] for log in seen_logs}


@pytest.mark.asyncio
async def test_async_filter_against_log_events(
    async_w3, async_emitter, async_wait_for_transaction, emitter_contract_event_ids
):
    txn_filter = await async_w3.eth.filter({})
    txn_hashes = set()
    txn_hashes.add(
        await async_emitter.functions.logNoArgs(
            emitter_contract_event_ids.LogNoArguments
        ).transact()
    )

    for txn_hash in txn_hashes:
        await async_wait_for_transaction(async_w3, txn_hash)

    seen_logs = await txn_filter.get_new_entries()

    assert txn_hashes == {log["transactionHash"] for log in seen_logs}
