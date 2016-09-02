import random
import gevent
from flaky import flaky


#@flaky(max_runs=3)
def test_past_events_filter_with_only_event_name(web3_empty,
                                                 emitter,
                                                 wait_for_transaction,
                                                 emitter_log_topics,
                                                 emitter_event_ids):
    web3 = web3_empty

    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
    txn_receipt = wait_for_transaction(web3, txn_hash)

    seen_logs = []

    filter = emitter.pastEvents('LogNoArguments', {}, seen_logs.append)

    with gevent.Timeout(5):
        while not seen_logs:
            gevent.sleep(random.random())

    filter.stop_watching(10)

    assert len(seen_logs) == 1
    assert seen_logs[0]['transactionHash'] == txn_hash
