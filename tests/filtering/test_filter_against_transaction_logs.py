import random
import gevent
from flaky import flaky


reset_chain = True


@flaky(max_runs=3)
def test_filter_against_log_events(web3,
                                   emitter,
                                   wait_for_transaction,
                                   emitter_log_topics,
                                   emitter_event_ids):

    seen_logs = []
    txn_filter = web3.eth.filter({})
    txn_filter.watch(seen_logs.append)

    txn_hashes = []

    txn_hashes.append(emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments))

    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    with gevent.Timeout(5):
        while not seen_logs:
            gevent.sleep(random.random())

    txn_filter.stop_watching(30)

    assert set(txn_hashes) == set(log['transactionHash'] for log in seen_logs)
