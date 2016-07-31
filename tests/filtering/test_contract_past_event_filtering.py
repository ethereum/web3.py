import random
import gevent


def test_past_events_filter_with_only_event_name(web3,
                                                 emitter,
                                                 wait_for_transaction,
                                                 emitter_log_topics,
                                                 emitter_event_ids):
    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
    txn_receipt = wait_for_transaction(txn_hash)

    seen_logs = []

    filter = emitter.pastEvents('LogNoArguments', {}, seen_logs.append)

    with gevent.Timeout(5):
        while not seen_logs:
            gevent.sleep(random.random())

    filter.stop_watching(10)

    assert len(seen_logs) == 1
    assert seen_logs[0]['transactionHash'] == txn_hash
