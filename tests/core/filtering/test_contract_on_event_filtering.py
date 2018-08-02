import pytest

from eth_utils import (
    is_address,
)

# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


@pytest.mark.parametrize('call_as_instance', (True, False))
def test_create_filter_address_parameter(web3, emitter, Emitter, call_as_instance):
    if call_as_instance:
        event_filter = emitter.events.LogNoArguments.createFilter(fromBlock="latest")
    else:
        event_filter = Emitter.events.LogNoArguments.createFilter(fromBlock="latest")

    if call_as_instance:
        # Assert this is a single string value, and not a list of addresses
        assert is_address(event_filter.filter_params['address'])
    else:
        #  Undeployed contract shouldnt have address...
        assert 'address' not in event_filter.filter_params


@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_filter_using_get_entries_interface(
        web3,
        emitter,
        Emitter,
        wait_for_transaction,
        emitter_event_ids,
        call_as_instance,
        create_filter):

    if call_as_instance:
        event_filter = create_filter(emitter, ['LogNoArguments', {}])
    else:
        event_filter = create_filter(Emitter, ['LogNoArguments', {}])

    txn_hash = emitter.functions.logNoArgs(emitter_event_ids.LogNoArguments).transact()
    wait_for_transaction(web3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hash

    # a second call is empty because all events have been retrieved
    new_entries = event_filter.get_new_entries()
    assert len(new_entries) == 0


@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_sync_filter_with_event_name_and_single_argument(
        web3,
        emitter,
        Emitter,
        wait_for_transaction,
        emitter_event_ids,
        call_as_instance,
        create_filter):

    if call_as_instance:
        event_filter = create_filter(emitter, ['LogTripleWithIndex', {'filter': {
            'arg1': 2,
        }}])
    else:
        event_filter = create_filter(Emitter, ['LogTripleWithIndex', {'filter': {
            'arg1': 2,
        }}])

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
def test_on_sync_filter_with_event_name_and_non_indexed_argument(
        web3,
        emitter,
        Emitter,
        wait_for_transaction,
        emitter_event_ids,
        call_as_instance,
        create_filter):

    if call_as_instance:
        contract = emitter
    else:
        contract = Emitter

    event_filter = create_filter(contract, ['LogTripleWithIndex', {'filter': {
        'arg0': 1,
        'arg1': 2,
    }}])

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

    post_event_filter = contract.events.LogTripleWithIndex.createFilter(
        argument_filters={'arg0': 1, 'arg1': 2},
        fromBlock=0,
    )

    old_logs = post_event_filter.get_all_entries()
    assert len(old_logs) == 1
    assert old_logs[0]['transactionHash'] == txn_hashes[1]


def test_filter_with_contract_address(web3, emitter, emitter_event_ids, wait_for_transaction):
    event_filter = web3.eth.filter(filter_params={'address': emitter.address})
    txn_hash = emitter.functions.logNoArgs(emitter_event_ids.LogNoArguments).transact()
    wait_for_transaction(web3, txn_hash)
    seen_logs = event_filter.get_new_entries()
    assert len(seen_logs) == 1
    assert seen_logs[0]['transactionHash'] == txn_hash


@pytest.mark.parametrize('call_as_instance', (True, False))
def test_on_sync_filter_with_topic_filter_options(
        web3,
        emitter,
        Emitter,
        wait_for_transaction,
        emitter_event_ids,
        call_as_instance,
        create_filter):

    if call_as_instance:
        contract = emitter
    else:
        contract = Emitter

    event_filter = create_filter(contract, ['LogTripleWithIndex', {'filter': {
        'arg1': [1, 2],
        'arg2': [1, 2]
    }}])

    txn_hashes = []
    event_id = emitter_event_ids.LogTripleWithIndex
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 1, 1).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 1, 2).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 2, 2).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 2, 1).transact()
    )
    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    seen_logs = event_filter.get_new_entries()
    assert len(seen_logs) == 4

    post_event_filter = contract.events.LogTripleWithIndex.createFilter(
        argument_filters={'arg1': [1, 2], 'arg2': [1, 2]},
        fromBlock=0,
    )

    old_logs = post_event_filter.get_all_entries()
    assert len(old_logs) == 4
