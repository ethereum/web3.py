import random
import gevent


def test_on_filter_with_only_event_name(web3,
                                        emitter,
                                        wait_for_transaction,
                                        emitter_log_topics,
                                        emitter_event_ids):

    seen_logs = []

    filter = emitter.on('LogNoArguments', {}, seen_logs.append)

    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
    txn_receipt = wait_for_transaction(txn_hash)

    with gevent.Timeout(5):
        while not seen_logs:
            gevent.sleep(random.random())

    filter.stop_watching(10)

    assert len(seen_logs) == 1
    assert seen_logs[0]['transactionHash'] == txn_hash


def test_on_filter_with_event_name_and_single_argument(web3,
                                                       emitter,
                                                       wait_for_transaction,
                                                       emitter_log_topics,
                                                       emitter_event_ids):

    seen_logs = []

    filter = emitter.on('LogTripleWithIndex', {'filter': {
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
        wait_for_transaction(txn_hash)

    with gevent.Timeout(5):
        while not seen_logs:
            gevent.sleep(random.random())

    filter.stop_watching(10)

    assert len(seen_logs) == 2
    assert {l['transactionHash'] for l in seen_logs} == set(txn_hashes[1:])


def test_on_filter_with_event_name_and_non_indexed_argument(web3,
                                                            emitter,
                                                            wait_for_transaction,
                                                            emitter_log_topics,
                                                            emitter_event_ids):

    seen_logs = []

    filter = emitter.on('LogTripleWithIndex', {'filter': {
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
        wait_for_transaction(txn_hash)

    with gevent.Timeout(5):
        while not seen_logs:
            gevent.sleep(random.random())

    filter.stop_watching(10)

    assert len(seen_logs) == 1
    assert seen_logs[0]['transactionHash'] == txn_hashes[1]
