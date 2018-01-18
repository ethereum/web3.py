import pytest

# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_filter_using_get_entries_interface(
    web3,
    emitter,
    Emitter,
    wait_for_transaction,
    emitter_event_ids,
    call_as_instance,
):
    if call_as_instance:
        event_filter = emitter.eventFilter('LogNoArguments', {})
    else:
        event_filter = Emitter.eventFilter('LogNoArguments', {})

    txn_hash = emitter.functions.logNoArgs(emitter_event_ids.LogNoArguments).transact()
    wait_for_transaction(web3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hash

    # a second call is empty because all events have been retrieved
    new_entries = event_filter.get_new_entries()
    assert len(new_entries) == 0


@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_sync_filter_with_event_name_and_single_argument(web3,
                                                            emitter,
                                                            Emitter,
                                                            wait_for_transaction,
                                                            emitter_event_ids,
                                                            call_as_instance
                                                            ):
    if call_as_instance:
        event_filter = emitter.eventFilter('LogTripleWithIndex', {'filter': {
            'arg1': 2,
        }})
    else:
        event_filter = Emitter.eventFilter('LogTripleWithIndex', {'filter': {
            'arg1': 2,
        }})

    txn_hashes = []
    event_id = emitter_event_ids.LogTripleWithIndex
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 2, 1, 3).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 2, 3).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 12345, 2, 54321).transact()
    )
    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    seen_logs = event_filter.get_new_entries()
    assert len(seen_logs) == 2
    assert {l['transactionHash'] for l in seen_logs} == set(txn_hashes[1:])


@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_sync_filter_with_event_name_and_non_indexed_argument(web3,
                                                                 emitter,
                                                                 Emitter,
                                                                 wait_for_transaction,
                                                                 emitter_event_ids,
                                                                 call_as_instance
                                                                 ):
    if call_as_instance:
        event_filter = emitter.eventFilter('LogTripleWithIndex', {'filter': {
            'arg0': 1, 'arg1': 2,
        }})
    else:
        event_filter = Emitter.eventFilter('LogTripleWithIndex', {'filter': {
            'arg0': 1, 'arg1': 2,
        }})

    txn_hashes = []
    event_id = emitter_event_ids.LogTripleWithIndex
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 2, 1, 3).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 2, 3).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 12345, 2, 54321).transact()
    )
    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    seen_logs = event_filter.get_new_entries()
    assert len(seen_logs) == 1
    assert seen_logs[0]['transactionHash'] == txn_hashes[1]
