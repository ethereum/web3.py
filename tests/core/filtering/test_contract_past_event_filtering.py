import pytest

# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_filter_using_get_all_entries_interface(
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

    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
    wait_for_transaction(web3, txn_hash)

    log_entries = event_filter.get_all_entries()

    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hash

    # a second call still retrieves all results
    log_entries_2 = event_filter.get_all_entries()

    assert len(log_entries_2) == 1
    assert log_entries_2[0]['transactionHash'] == txn_hash


@pytest.mark.parametrize('call_as_instance', (True, False))
def test_get_all_entries_returned_block_data(
    web3,
    emitter,
    Emitter,
    wait_for_transaction,
    emitter_event_ids,
    call_as_instance,
):
    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
    txn_receipt = wait_for_transaction(web3, txn_hash)

    if call_as_instance:
        filter = emitter.eventFilter('LogNoArguments')
    else:
        filter = Emitter.eventFilter('LogNoArguments')

    log_entries = filter.get_all_entries()

    assert len(log_entries) == 1
    event_data = log_entries[0]
    assert event_data['args'] == {}
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert event_data['address'] == emitter.address
    assert event_data['event'] == 'LogNoArguments'
