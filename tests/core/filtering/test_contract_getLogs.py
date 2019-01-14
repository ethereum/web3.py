

def test_contract_get_available_events(
    emitter,
):
    """We can iterate over available contract events"""
    contract = emitter
    events = list(contract.events)
    assert len(events) == 18


def test_contract_getLogs_all(
    web3,
    emitter,
    wait_for_transaction,
):
    contract = emitter
    event_id = 1

    txn_hash = contract.functions.logNoArgs(event_id).transact()
    wait_for_transaction(web3, txn_hash)

    log_entries = list(contract.events.LogNoArguments.getLogs())
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hash


def test_contract_getLogs_range(
    web3,
    emitter,
    wait_for_transaction,
):
    contract = emitter
    event_id = 1

    assert web3.eth.blockNumber == 2
    txn_hash = contract.functions.logNoArgs(event_id).transact()
    # Mined as block 3
    wait_for_transaction(web3, txn_hash)
    assert web3.eth.blockNumber == 3

    log_entries = list(contract.events.LogNoArguments.getLogs())
    assert len(log_entries) == 1

    log_entries = list(contract.events.LogNoArguments.getLogs(fromBlock=2, toBlock=3))
    assert len(log_entries) == 1

    log_entries = list(contract.events.LogNoArguments.getLogs(fromBlock=1, toBlock=2))
    assert len(log_entries) == 0
