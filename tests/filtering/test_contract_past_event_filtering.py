import pytest
import random
from flaky import flaky

from web3.utils.compat import (
    Timeout,
)


@flaky(max_runs=3)
@pytest.mark.parametrize('call_as_instance', (True, False))
def test_past_events_filter_with_callback(web3,
                                          sleep_interval,
                                          emitter,
                                          Emitter,
                                          wait_for_transaction,
                                          emitter_log_topics,
                                          emitter_event_ids,
                                          LogTopics,
                                          call_as_instance):
    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
    txn_receipt = wait_for_transaction(web3, txn_hash)

    seen_logs = []

    if call_as_instance:
        filter = emitter.pastEvents('LogNoArguments', {}, seen_logs.append)
    else:
        filter = Emitter.pastEvents('LogNoArguments', {}, seen_logs.append)

    with Timeout(30) as timeout:
        while not seen_logs:
            timeout.sleep(sleep_interval())

    filter.stop_watching(30)

    assert len(seen_logs) == 1
    event_data = seen_logs[0]
    assert event_data['args'] == {}
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert event_data['address'] == emitter.address
    assert event_data['event'] == 'LogNoArguments'


@flaky(max_runs=3)
@pytest.mark.parametrize('call_as_instance', (True, False))
def test_past_events_filter_using_get_api(web3,
                                          sleep_interval,
                                          emitter,
                                          Emitter,
                                          wait_for_transaction,
                                          emitter_log_topics,
                                          emitter_event_ids,
                                          LogTopics,
                                          call_as_instance):
    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
    txn_receipt = wait_for_transaction(web3, txn_hash)

    if call_as_instance:
        filter = emitter.pastEvents('LogNoArguments')
    else:
        filter = Emitter.pastEvents('LogNoArguments')

    with Timeout(30) as timeout:
        while not filter.get(False):
            timeout.sleep(sleep_interval())

    log_entries = filter.get(False)

    assert len(log_entries) == 1
    event_data = log_entries[0]
    assert event_data['args'] == {}
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert event_data['address'] == emitter.address
    assert event_data['event'] == 'LogNoArguments'
