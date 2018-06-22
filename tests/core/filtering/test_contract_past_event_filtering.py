import pytest

from eth_utils import (
    is_same_address,
)

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
        event_filter = emitter.events.LogNoArguments.createFilter(fromBlock='latest')
    else:
        event_filter = Emitter.events.LogNoArguments.createFilter(fromBlock='latest')

    txn_hash = emitter.functions.logNoArgs(emitter_event_ids.LogNoArguments).transact()
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
    txn_hash = emitter.functions.logNoArgs(emitter_event_ids.LogNoArguments).transact()
    txn_receipt = wait_for_transaction(web3, txn_hash)

    if call_as_instance:
        contract = emitter
    else:
        contract = Emitter

    events = contract.events.LogNoArguments.createFilter(fromBlock=txn_receipt['blockNumber'])

    log_entries = events.get_all_entries()

    assert len(log_entries) == 1
    event_data = log_entries[0]
    assert event_data['args'] == {}
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert is_same_address(event_data['address'], emitter.address)
    assert event_data['event'] == 'LogNoArguments'
