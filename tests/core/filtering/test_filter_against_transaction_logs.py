import pytest
import random

from flaky import (
    flaky,
)

from web3._utils.threads import (
    Timeout,
)


@pytest.mark.skip(reason="fixture 'w3_empty' not found")
@flaky(max_runs=3)
def test_sync_filter_against_log_events(w3_empty,
                                        emitter,
                                        wait_for_transaction,
                                        emitter_log_topics,
                                        emitter_event_ids
                                        ):
    w3 = w3_empty

    txn_filter = w3.eth.filter({})

    txn_hashes = set()
    txn_hashes.add(emitter.functions.logNoArgs(emitter_event_ids.LogNoArguments).transact())

    for txn_hash in txn_hashes:
        wait_for_transaction(w3, txn_hash)

    with Timeout(5) as timeout:
        while not txn_filter.get_new_entries():
            timeout.sleep(random.random())

    seen_logs = txn_filter.get_new_entries()

    assert txn_hashes == {log['transactionHash'] for log in seen_logs}


@pytest.mark.skip(reason="fixture 'w3_empty' not found")
@flaky(max_runs=3)
def test_async_filter_against_log_events(w3_empty,
                                         emitter,
                                         wait_for_transaction,
                                         emitter_log_topics,
                                         emitter_event_ids
                                         ):
    w3 = w3_empty

    seen_logs = []
    txn_filter = w3.eth.filter({})
    txn_filter.watch(seen_logs.append)

    txn_hashes = set()

    txn_hashes.add(emitter.functions.logNoArgs(emitter_event_ids.LogNoArguments).transact())

    for txn_hash in txn_hashes:
        wait_for_transaction(w3, txn_hash)

    with Timeout(5) as timeout:
        while not seen_logs:
            timeout.sleep(random.random())

    txn_filter.stop_watching(30)

    assert txn_hashes == {log['transactionHash'] for log in seen_logs}
