import pytest


def test_contract_get_available_events(
    emitter,
):
    """We can iterate over available contract events"""
    contract = emitter
    events = list(contract.events)
    assert len(events) == 19


def test_contract_get_logs_all(
    web3,
    emitter,
    wait_for_transaction,
    emitter_event_ids,
):
    contract = emitter
    event_id = emitter_event_ids.LogNoArguments

    txn_hash = contract.functions.logNoArgs(event_id).transact()
    wait_for_transaction(web3, txn_hash)

    log_entries = list(contract.events.LogNoArguments.get_logs())
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hash


def test_contract_get_logs_range(
    web3,
    emitter,
    wait_for_transaction,
    emitter_event_ids,
):
    contract = emitter
    event_id = emitter_event_ids.LogNoArguments

    assert web3.eth.block_number == 2
    txn_hash = contract.functions.logNoArgs(event_id).transact()
    # Mined as block 3
    wait_for_transaction(web3, txn_hash)
    assert web3.eth.block_number == 3

    log_entries = list(contract.events.LogNoArguments.get_logs())
    assert len(log_entries) == 1

    log_entries = list(contract.events.LogNoArguments.get_logs(fromBlock=2, toBlock=3))
    assert len(log_entries) == 1

    log_entries = list(contract.events.LogNoArguments.get_logs(fromBlock=1, toBlock=2))
    assert len(log_entries) == 0


def test_contract_get_logs_argument_filter(
        web3,
        emitter,
        wait_for_transaction,
        emitter_event_ids):

    contract = emitter

    txn_hashes = []
    event_id = emitter_event_ids.LogTripleWithIndex
    # 1 = arg0
    # 4 = arg1
    # 1 = arg2
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 4, 1).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 1, 2).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 2, 2).transact()
    )
    txn_hashes.append(
        emitter.functions.logTriple(event_id, 1, 3, 1).transact()
    )
    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    all_logs = contract.events.LogTripleWithIndex.get_logs(fromBlock=1)
    assert len(all_logs) == 4

    # Filter all entries where arg1 in (1, 2)
    partial_logs = contract.events.LogTripleWithIndex.get_logs(
        fromBlock=1,
        argument_filters={'arg1': [1, 2]},
    )
    assert len(partial_logs) == 2

    # Filter all entries where arg0 == 1
    partial_logs = contract.events.LogTripleWithIndex.get_logs(
        fromBlock=1,
        argument_filters={'arg0': 1},
    )
    assert len(partial_logs) == 4


#
# Deprecated
#
def test_contract_getLogs_all(
    web3,
    emitter,
    wait_for_transaction,
    emitter_event_ids,
):
    contract = emitter
    event_id = emitter_event_ids.LogNoArguments

    txn_hash = contract.functions.logNoArgs(event_id).transact()
    wait_for_transaction(web3, txn_hash)

    with pytest.warns(
        DeprecationWarning,
        match="getLogs is deprecated in favor of get_logs"
    ):
        log_entries = list(contract.events.LogNoArguments.getLogs())
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hash
