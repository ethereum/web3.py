import asyncio
import pytest

from eth_utils import (
    is_address,
)


@pytest.mark.parametrize("call_deployed_contract", (True, False))
def test_create_filter_address_parameter(
    emitter, emitter_contract_factory, call_deployed_contract
):
    if call_deployed_contract:
        event_filter = emitter.events.LogNoArguments.create_filter(from_block="latest")
    else:
        event_filter = emitter_contract_factory.events.LogNoArguments.create_filter(
            from_block="latest"
        )

    if call_deployed_contract:
        # Assert this is a single string value, and not a list of addresses
        assert is_address(event_filter.filter_params["address"])
    else:
        #  Undeployed contract shouldn't have address...
        assert "address" not in event_filter.filter_params


@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
def test_on_filter_using_get_entries_interface(
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
        event_filter = contract.events.LogNoArguments.build_filter().deploy(w3)
    else:
        event_filter = create_filter(emitter, ["LogNoArguments", {}])

    txn_hash = emitter.functions.logNoArgs(
        emitter_contract_event_ids.LogNoArguments
    ).transact()
    wait_for_transaction(w3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]["transactionHash"] == txn_hash

    # a second call is empty because all events have been retrieved
    new_entries = event_filter.get_new_entries()
    assert len(new_entries) == 0


@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
def test_on_sync_filter_with_event_name_and_single_argument(
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
        builder = contract.events.LogTripleWithIndex.build_filter()
        builder.args["arg1"].match_single(2)
        event_filter = builder.deploy(w3)
    else:
        event_filter = create_filter(
            contract,
            [
                "LogTripleWithIndex",
                {
                    "filter": {
                        "arg1": 2,
                    }
                },
            ],
        )

    txn_hashes = []
    event_id = emitter_contract_event_ids.LogTripleWithIndex
    txn_hashes.append(emitter.functions.logTriple(event_id, 2, 1, 3).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 2, 3).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 12345, 2, 54321).transact())
    for txn_hash in txn_hashes:
        wait_for_transaction(w3, txn_hash)

    seen_logs = event_filter.get_new_entries()
    assert len(seen_logs) == 2
    assert {log["transactionHash"] for log in seen_logs} == set(txn_hashes[1:])


@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
def test_on_sync_filter_with_event_name_and_non_indexed_argument(
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
        builder = contract.events.LogTripleWithIndex.build_filter()
        builder.args["arg0"].match_single(1)
        builder.args["arg1"].match_single(2)
        event_filter = builder.deploy(w3)
    else:
        event_filter = create_filter(
            contract,
            [
                "LogTripleWithIndex",
                {
                    "filter": {
                        "arg0": 1,
                        "arg1": 2,
                    }
                },
            ],
        )

    txn_hashes = []
    event_id = emitter_contract_event_ids.LogTripleWithIndex
    txn_hashes.append(emitter.functions.logTriple(event_id, 2, 1, 3).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 2, 3).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 12345, 2, 54321).transact())
    for txn_hash in txn_hashes:
        wait_for_transaction(w3, txn_hash)

    seen_logs = event_filter.get_new_entries()
    assert len(seen_logs) == 1
    assert seen_logs[0]["transactionHash"] == txn_hashes[1]

    post_event_filter = contract.events.LogTripleWithIndex.create_filter(
        argument_filters={"arg0": 1, "arg1": 2},
        from_block=0,
    )

    old_logs = post_event_filter.get_all_entries()
    assert len(old_logs) == 1
    assert old_logs[0]["transactionHash"] == txn_hashes[1]


def test_filter_with_contract_address(
    w3, emitter, emitter_contract_event_ids, wait_for_transaction
):
    event_filter = w3.eth.filter(filter_params={"address": emitter.address})
    txn_hash = emitter.functions.logNoArgs(
        emitter_contract_event_ids.LogNoArguments
    ).transact()
    wait_for_transaction(w3, txn_hash)
    seen_logs = event_filter.get_new_entries()
    assert len(seen_logs) == 1
    assert seen_logs[0]["transactionHash"] == txn_hash


@pytest.mark.parametrize("call_deployed_contract", (True, False))
def test_on_sync_filter_with_topic_filter_options_on_old_apis(
    w3,
    emitter,
    emitter_contract_factory,
    wait_for_transaction,
    emitter_contract_event_ids,
    call_deployed_contract,
    create_filter,
):
    if call_deployed_contract:
        contract = emitter
    else:
        contract = emitter_contract_factory

    event_filter = create_filter(
        contract, ["LogTripleWithIndex", {"filter": {"arg1": [1, 2], "arg2": [1, 2]}}]
    )

    txn_hashes = []
    event_id = emitter_contract_event_ids.LogTripleWithIndex
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 1, 1).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 1, 2).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 2, 2).transact())
    txn_hashes.append(emitter.functions.logTriple(event_id, 1, 2, 1).transact())
    for txn_hash in txn_hashes:
        wait_for_transaction(w3, txn_hash)

    seen_logs = event_filter.get_new_entries()
    assert len(seen_logs) == 4

    post_event_filter = contract.events.LogTripleWithIndex.create_filter(
        argument_filters={"arg1": [1, 2], "arg2": [1, 2]},
        from_block=0,
    )

    old_logs = post_event_filter.get_all_entries()
    assert len(old_logs) == 4


# --- async --- #


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
@pytest.mark.parametrize("call_deployed_contract", (True, False))
async def test_async_create_filter_address_parameter(
    async_emitter, async_emitter_contract_factory, call_deployed_contract
):
    if call_deployed_contract:
        event_filter = await async_emitter.events.LogNoArguments.create_filter(
            from_block="latest"
        )
    else:
        event_filter = (
            await async_emitter_contract_factory.events.LogNoArguments.create_filter(
                from_block="latest"
            )
        )

    if call_deployed_contract:
        # Assert this is a single string value, and not a list of addresses
        assert is_address(event_filter.filter_params["address"])
    else:
        #  Undeployed contract shouldn't have address...
        assert "address" not in event_filter.filter_params


@pytest.mark.asyncio
@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
async def test_on_async_filter_using_get_entries_interface(
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
        event_filter = await contract.events.LogNoArguments.build_filter().deploy(
            async_w3
        )
    else:
        event_filter = await async_create_filter(async_emitter, ["LogNoArguments", {}])

    txn_hash = await async_emitter.functions.logNoArgs(
        emitter_contract_event_ids.LogNoArguments
    ).transact()
    await async_wait_for_transaction(async_w3, txn_hash)

    log_entries = await event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]["transactionHash"] == txn_hash

    # a second call is empty because all events have been retrieved
    new_entries = await event_filter.get_new_entries()
    assert len(new_entries) == 0


@pytest.mark.asyncio
@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
async def test_on_async_filter_with_event_name_and_single_argument(
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
        builder = contract.events.LogTripleWithIndex.build_filter()
        builder.args["arg1"].match_single(2)
        event_filter = await builder.deploy(async_w3)
    else:
        event_filter = await async_create_filter(
            contract,
            [
                "LogTripleWithIndex",
                {
                    "filter": {
                        "arg1": 2,
                    }
                },
            ],
        )

    txn_hashes = []
    event_id = emitter_contract_event_ids.LogTripleWithIndex
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 2, 1, 3).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 2, 3).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 12345, 2, 54321).transact()
    )
    for txn_hash in txn_hashes:
        await async_wait_for_transaction(async_w3, txn_hash)

    seen_logs = await event_filter.get_new_entries()
    assert len(seen_logs) == 2
    assert {log["transactionHash"] for log in seen_logs} == set(txn_hashes[1:])


@pytest.mark.asyncio
@pytest.mark.parametrize("call_deployed_contract", (True, False))
@pytest.mark.parametrize("api_style", ("v4", "build_filter"))
async def test_on_async_filter_with_event_name_and_non_indexed_argument(
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
        builder = contract.events.LogTripleWithIndex.build_filter()
        builder.args["arg0"].match_single(1)
        builder.args["arg1"].match_single(2)
        event_filter = await builder.deploy(async_w3)
    else:
        event_filter = await async_create_filter(
            contract,
            [
                "LogTripleWithIndex",
                {
                    "filter": {
                        "arg0": 1,
                        "arg1": 2,
                    }
                },
            ],
        )

    txn_hashes = []
    event_id = emitter_contract_event_ids.LogTripleWithIndex
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 2, 1, 3).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 2, 3).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 12345, 2, 54321).transact()
    )
    for txn_hash in txn_hashes:
        await async_wait_for_transaction(async_w3, txn_hash)

    seen_logs = await event_filter.get_new_entries()
    assert len(seen_logs) == 1
    assert seen_logs[0]["transactionHash"] == txn_hashes[1]

    post_event_filter = await contract.events.LogTripleWithIndex.create_filter(
        argument_filters={"arg0": 1, "arg1": 2},
        from_block=0,
    )

    old_logs = await post_event_filter.get_all_entries()
    assert len(old_logs) == 1
    assert old_logs[0]["transactionHash"] == txn_hashes[1]


@pytest.mark.asyncio
async def test_async_filter_with_contract_address(
    async_w3, async_emitter, emitter_contract_event_ids, async_wait_for_transaction
):
    event_filter = await async_w3.eth.filter(
        filter_params={"address": async_emitter.address}
    )
    txn_hash = await async_emitter.functions.logNoArgs(
        emitter_contract_event_ids.LogNoArguments
    ).transact()
    await async_wait_for_transaction(async_w3, txn_hash)
    seen_logs = await event_filter.get_new_entries()
    assert len(seen_logs) == 1
    assert seen_logs[0]["transactionHash"] == txn_hash


@pytest.mark.asyncio
@pytest.mark.parametrize("call_deployed_contract", (True, False))
async def test_on_async_filter_with_topic_filter_options_on_old_apis(
    async_w3,
    async_emitter,
    async_emitter_contract_factory,
    async_wait_for_transaction,
    emitter_contract_event_ids,
    call_deployed_contract,
    async_create_filter,
):
    if call_deployed_contract:
        contract = async_emitter
    else:
        contract = async_emitter_contract_factory

    event_filter = await async_create_filter(
        contract, ["LogTripleWithIndex", {"filter": {"arg1": [1, 2], "arg2": [1, 2]}}]
    )

    txn_hashes = []
    event_id = emitter_contract_event_ids.LogTripleWithIndex
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 1, 1).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 1, 2).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 2, 2).transact()
    )
    txn_hashes.append(
        await async_emitter.functions.logTriple(event_id, 1, 2, 1).transact()
    )
    for txn_hash in txn_hashes:
        await async_wait_for_transaction(async_w3, txn_hash)

    seen_logs = await event_filter.get_new_entries()
    assert len(seen_logs) == 4

    post_event_filter = await contract.events.LogTripleWithIndex.create_filter(
        argument_filters={"arg1": [1, 2], "arg2": [1, 2]},
        from_block=0,
    )

    old_logs = await post_event_filter.get_all_entries()
    assert len(old_logs) == 4
