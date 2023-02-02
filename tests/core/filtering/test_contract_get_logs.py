import pytest


def test_contract_get_available_events(
    emitter,
):
    """We can iterate over available contract events"""
    contract = emitter
    events = list(contract.events)
    assert len(events) == 19


def test_contract_get_logs_all(
    w3,
    emitter,
    wait_for_transaction,
    emitter_contract_event_ids,
):
    contract = emitter
    event_id = emitter_contract_event_ids.LogNoArguments

    txn_hash = contract.functions.logNoArgs(event_id).transact()
    wait_for_transaction(w3, txn_hash)

    log_entries = list(contract.events.LogNoArguments.get_logs())
    assert len(log_entries) == 1
    assert log_entries[0]["transactionHash"] == txn_hash


def test_contract_get_logs_range(
    w3,
    emitter,
    wait_for_transaction,
    emitter_contract_event_ids,
):
    contract = emitter
    event_id = emitter_contract_event_ids.LogNoArguments

    assert w3.eth.block_number == 2
    txn_hash = contract.functions.logNoArgs(event_id).transact()
    # Mined as block 3
    wait_for_transaction(w3, txn_hash)
    assert w3.eth.block_number == 3

    log_entries = list(contract.events.LogNoArguments.get_logs())
    assert len(log_entries) == 1

    log_entries = list(contract.events.LogNoArguments.get_logs(fromBlock=2, toBlock=3))
    assert len(log_entries) == 1

    log_entries = list(contract.events.LogNoArguments.get_logs(fromBlock=1, toBlock=2))
    assert len(log_entries) == 0


def test_contract_get_logs_argument_filter(
    w3, emitter, wait_for_transaction, emitter_contract_event_ids
):

    contract = emitter

    txn_hashes = []
    event_id = emitter_contract_event_ids.LogTripleWithIndex
    # 1 = arg0
    # 4 = arg1
    # 1 = arg2
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 4, 1).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 1, 2).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 2, 2).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 3, 1).transact())
    for txn_hash in txn_hashes:
        wait_for_transaction(w3, txn_hash)

    all_logs = contract.events.LogTripleWithIndex.get_logs(fromBlock=1)
    assert len(all_logs) == 4

    # Filter all entries where arg1 in (1, 2)
    partial_logs = contract.events.LogTripleWithIndex.get_logs(
        fromBlock=1,
        argument_filters={"arg1": [1, 2]},
    )
    assert len(partial_logs) == 2

    # Filter all entries where arg0 == 1
    partial_logs = contract.events.LogTripleWithIndex.get_logs(
        fromBlock=1,
        argument_filters={"arg0": 1},
    )
    assert len(partial_logs) == 4


# --- async --- #


def test_async_contract_get_available_events(
    async_emitter,
):
    """We can iterate over available contract events"""
    contract = async_emitter
    events = list(contract.events)
    assert len(events) == 19


@pytest.mark.asyncio
async def test_async_contract_get_logs_all(
    async_w3,
    async_emitter,
    async_wait_for_transaction,
    emitter_contract_event_ids,
):
    contract = async_emitter
    event_id = emitter_contract_event_ids.LogNoArguments

    txn_hash = await contract.functions.logNoArgs(event_id).transact()
    await async_wait_for_transaction(async_w3, txn_hash)

    contract_logs = await contract.events.LogNoArguments.get_logs()
    log_entries = list(contract_logs)
    assert len(log_entries) == 1
    assert log_entries[0]["transactionHash"] == txn_hash


@pytest.mark.asyncio
async def test_async_contract_get_logs_range(
    async_w3,
    async_emitter,
    async_wait_for_transaction,
    emitter_contract_event_ids,
):
    contract = async_emitter
    event_id = emitter_contract_event_ids.LogNoArguments

    eth_block_number = await async_w3.eth.block_number
    assert eth_block_number == 2
    txn_hash = await contract.functions.logNoArgs(event_id).transact()
    # Mined as block 3
    await async_wait_for_transaction(async_w3, txn_hash)
    eth_block_number = await async_w3.eth.block_number
    assert eth_block_number == 3

    contract_logs = await contract.events.LogNoArguments.get_logs()
    log_entries = list(contract_logs)
    assert len(log_entries) == 1

    contract_logs = await contract.events.LogNoArguments.get_logs(
        fromBlock=2, toBlock=3
    )
    log_entries = list(contract_logs)
    assert len(log_entries) == 1

    contract_logs = await contract.events.LogNoArguments.get_logs(
        fromBlock=1, toBlock=2
    )
    log_entries = list(contract_logs)
    assert len(log_entries) == 0


@pytest.mark.asyncio
async def test_async_contract_get_logs_argument_filter(
    async_w3, async_emitter, async_wait_for_transaction, emitter_contract_event_ids
):

    contract = async_emitter

    txn_hashes = []
    event_id = emitter_contract_event_ids.LogTripleWithIndex
    # 1 = arg0
    # 4 = arg1
    # 1 = arg2
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 4, 1).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 1, 2).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 2, 2).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 3, 1).transact()
    )
    for txn_hash in txn_hashes:
        await async_wait_for_transaction(async_w3, txn_hash)

    all_logs = await contract.events.LogTripleWithIndex.get_logs(fromBlock=1)
    assert len(all_logs) == 4

    # Filter all entries where arg1 in (1, 2)
    partial_logs = await contract.events.LogTripleWithIndex.get_logs(
        fromBlock=1,
        argument_filters={"arg1": [1, 2]},
    )
    assert len(partial_logs) == 2

    # Filter all entries where arg0 == 1
    partial_logs = await contract.events.LogTripleWithIndex.get_logs(
        fromBlock=1,
        argument_filters={"arg0": 1},
    )
    assert len(partial_logs) == 4
