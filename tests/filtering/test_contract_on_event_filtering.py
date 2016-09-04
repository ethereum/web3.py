import pytest
import random
import gevent
from flaky import flaky


@flaky(max_runs=3)
@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_filter_using_get_interface(web3_empty,
                                       emitter,
                                       Emitter,
                                       wait_for_transaction,
                                       emitter_log_topics,
                                       emitter_event_ids,
                                       call_as_instance):
    web3 = web3_empty

    if call_as_instance:
        filter = emitter.on('LogNoArguments', {})
    else:
        filter = Emitter.on('LogNoArguments', {})

    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
    txn_receipt = wait_for_transaction(web3, txn_hash)

    with gevent.Timeout(10):
        while not filter.get(False):
            gevent.sleep(0)

    log_entries = filter.get(False)

    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hash


@flaky(max_runs=3)
@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_filter_with_only_event_name(web3_empty,
                                        emitter,
                                        Emitter,
                                        wait_for_transaction,
                                        emitter_log_topics,
                                        emitter_event_ids,
                                        call_as_instance):
    web3 = web3_empty

    seen_logs = []

    if call_as_instance:
        filter = emitter.on('LogNoArguments', {}, seen_logs.append)
    else:
        filter = Emitter.on('LogNoArguments', {}, seen_logs.append)

    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
    txn_receipt = wait_for_transaction(web3, txn_hash)

    with gevent.Timeout(5):
        while not seen_logs:
            gevent.sleep(random.random())

    filter.stop_watching(10)

    assert len(seen_logs) == 1
    assert seen_logs[0]['transactionHash'] == txn_hash


@flaky(max_runs=3)
@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_filter_with_event_name_and_single_argument(web3_empty,
                                                       emitter,
                                                       Emitter,
                                                       wait_for_transaction,
                                                       emitter_log_topics,
                                                       emitter_event_ids,
                                                       call_as_instance):
    web3 = web3_empty

    seen_logs = []

    if call_as_instance:
        filter = emitter.on('LogTripleWithIndex', {'filter': {
            'arg1': 2,
        }}, seen_logs.append)
    else:
        filter = Emitter.on('LogTripleWithIndex', {'filter': {
            'arg1': 2,
        }}, seen_logs.append)

    txn_hashes = []
    txn_hashes.append(
        emitter.transact().logTriple(emitter_event_ids.LogTripleWithIndex, 2, 1, 3)
    )
    txn_hashes.append(
        emitter.transact().logTriple(emitter_event_ids.LogTripleWithIndex, 1, 2, 3)
    )
    txn_hashes.append(
        emitter.transact().logTriple(emitter_event_ids.LogTripleWithIndex, 12345, 2, 54321)
    )
    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    with gevent.Timeout(5):
        while not seen_logs:
            gevent.sleep(random.random())

    filter.stop_watching(10)

    assert len(seen_logs) == 2
    assert {l['transactionHash'] for l in seen_logs} == set(txn_hashes[1:])


@flaky(max_runs=3)
@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_filter_with_event_name_and_non_indexed_argument(web3_empty,
                                                            emitter,
                                                            Emitter,
                                                            wait_for_transaction,
                                                            emitter_log_topics,
                                                            emitter_event_ids,
                                                            call_as_instance):
    web3 = web3_empty

    seen_logs = []

    if call_as_instance:
        filter = emitter.on('LogTripleWithIndex', {'filter': {
            'arg0': 1, 'arg1': 2,
        }}, seen_logs.append)
    else:
        filter = Emitter.on('LogTripleWithIndex', {'filter': {
            'arg0': 1, 'arg1': 2,
        }}, seen_logs.append)

    txn_hashes = []
    txn_hashes.append(
        emitter.transact().logTriple(emitter_event_ids.LogTripleWithIndex, 2, 1, 3)
    )
    txn_hashes.append(
        emitter.transact().logTriple(emitter_event_ids.LogTripleWithIndex, 1, 2, 3)
    )
    txn_hashes.append(
        emitter.transact().logTriple(emitter_event_ids.LogTripleWithIndex, 12345, 2, 54321)
    )
    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    with gevent.Timeout(5):
        while not seen_logs:
            gevent.sleep(random.random())

    filter.stop_watching(10)

    assert len(seen_logs) == 1
    assert seen_logs[0]['transactionHash'] == txn_hashes[1]
