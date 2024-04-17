import asyncio
import pytest

from eth_utils import (
    is_same_address,
)


@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
def test_on_filter_using_get_all_entries_interface(
    w3,
    emitter,
    emitter_contract_factory,
    wait_for_transaction,
    emitter_contract_event_ids,
    call_deployed_contract,
    api_style,
    create_filter,
):
    if call_deployed_contract:
        contract = emitter
    else:
        contract = emitter_contract_factory

    if api_style == "build_filter":
        builder = contract.events.LogNoArguments.build_filter()
        builder.from_block = "latest"
        event_filter = builder.deploy(w3)
    else:
        event_filter = create_filter(
            contract, ["LogNoArguments", {"from_block": "latest"}]
        )

    txn_hash = emitter.functions.logNoArgs(
        emitter_contract_event_ids.LogNoArguments
    ).transact()
    wait_for_transaction(w3, txn_hash)

    log_entries = event_filter.get_all_entries()

    assert len(log_entries) == 1
    assert log_entries[0]["transactionHash"] == txn_hash

    # a second call still retrieves all results
    log_entries_2 = event_filter.get_all_entries()

    assert len(log_entries_2) == 1
    assert log_entries_2[0]["transactionHash"] == txn_hash


@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
def test_get_all_entries_returned_block_data(
    w3,
    emitter,
    emitter_contract_factory,
    wait_for_transaction,
    emitter_contract_event_ids,
    call_deployed_contract,
    api_style,
    create_filter,
):
    txn_hash = emitter.functions.logNoArgs(
        emitter_contract_event_ids.LogNoArguments
    ).transact()
    txn_receipt = wait_for_transaction(w3, txn_hash)

    if call_deployed_contract:
        contract = emitter
    else:
        contract = emitter_contract_factory

    if api_style == "build_filter":
        builder = contract.events.LogNoArguments.build_filter()
        builder.from_block = txn_receipt["blockNumber"]
        event_filter = builder.deploy(w3)
    else:
        event_filter = create_filter(
            contract, ["LogNoArguments", {"from_block": txn_receipt["blockNumber"]}]
        )

    log_entries = event_filter.get_all_entries()

    assert len(log_entries) == 1
    event_data = log_entries[0]
    assert event_data["args"] == {}
    assert event_data["blockHash"] == txn_receipt["blockHash"]
    assert event_data["blockNumber"] == txn_receipt["blockNumber"]
    assert event_data["transactionIndex"] == txn_receipt["transactionIndex"]
    assert is_same_address(event_data["address"], emitter.address)
    assert event_data["event"] == "LogNoArguments"


# --- async --- #


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
async def test_on_async_filter_using_get_all_entries_interface(
    async_w3,
    async_emitter,
    async_emitter_contract_factory,
    async_wait_for_transaction,
    emitter_contract_event_ids,
    call_deployed_contract,
    api_style,
    async_create_filter,
):
    if call_deployed_contract:
        contract = async_emitter
    else:
        contract = async_emitter_contract_factory

    if api_style == "build_filter":
        builder = contract.events.LogNoArguments.build_filter()
        builder.from_block = "latest"
        event_filter = await builder.deploy(async_w3)
    else:
        event_filter = await async_create_filter(
            contract, ["LogNoArguments", {"from_block": "latest"}]
        )

    txn_hash = await async_emitter.functions.logNoArgs(
        emitter_contract_event_ids.LogNoArguments
    ).transact()
    await async_wait_for_transaction(async_w3, txn_hash)

    log_entries = await event_filter.get_all_entries()

    assert len(log_entries) == 1
    assert log_entries[0]["transactionHash"] == txn_hash

    # a second call still retrieves all results
    log_entries_2 = await event_filter.get_all_entries()

    assert len(log_entries_2) == 1
    assert log_entries_2[0]["transactionHash"] == txn_hash


@pytest.mark.asyncio
@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
async def test_async_get_all_entries_returned_block_data(
    async_w3,
    async_emitter,
    async_emitter_contract_factory,
    async_wait_for_transaction,
    emitter_contract_event_ids,
    call_deployed_contract,
    api_style,
    async_create_filter,
):
    txn_hash = await async_emitter.functions.logNoArgs(
        emitter_contract_event_ids.LogNoArguments
    ).transact()
    txn_receipt = await async_wait_for_transaction(async_w3, txn_hash)

    if call_deployed_contract:
        contract = async_emitter
    else:
        contract = async_emitter_contract_factory

    if api_style == "build_filter":
        builder = contract.events.LogNoArguments.build_filter()
        builder.from_block = txn_receipt["blockNumber"]
        event_filter = await builder.deploy(async_w3)
    else:
        event_filter = await async_create_filter(
            contract, ["LogNoArguments", {"from_block": txn_receipt["blockNumber"]}]
        )

    log_entries = await event_filter.get_all_entries()

    assert len(log_entries) == 1
    event_data = log_entries[0]
    assert event_data["args"] == {}
    assert event_data["blockHash"] == txn_receipt["blockHash"]
    assert event_data["blockNumber"] == txn_receipt["blockNumber"]
    assert event_data["transactionIndex"] == txn_receipt["transactionIndex"]
    assert is_same_address(event_data["address"], async_emitter.address)
    assert event_data["event"] == "LogNoArguments"
