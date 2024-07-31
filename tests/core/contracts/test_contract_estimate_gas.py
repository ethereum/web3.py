import pytest

from web3.exceptions import (
    Web3ValidationError,
)


def test_contract_estimate_gas(w3, math_contract, estimate_gas, transact):
    gas_estimate = estimate_gas(
        contract=math_contract, contract_function="incrementCounter"
    )

    txn_hash = transact(contract=math_contract, contract_function="incrementCounter")

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_estimate_gas_can_be_called_without_parens(
    w3, math_contract, estimate_gas, transact
):
    gas_estimate = math_contract.functions.incrementCounter.estimate_gas()

    txn_hash = transact(contract=math_contract, contract_function="incrementCounter")

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_fallback_estimate_gas(w3, fallback_function_contract):
    gas_estimate = fallback_function_contract.fallback.estimate_gas()

    txn_hash = fallback_function_contract.fallback.transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_estimate_gas_with_arguments(
    w3, math_contract, estimate_gas, transact
):
    gas_estimate = estimate_gas(
        contract=math_contract, contract_function="add", func_args=[5, 6]
    )

    txn_hash = transact(
        contract=math_contract, contract_function="add", func_args=[5, 6]
    )
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_estimate_gas_not_sending_ether_to_nonpayable_function(
    w3, payable_tester_contract, estimate_gas, transact
):
    gas_estimate = estimate_gas(
        contract=payable_tester_contract, contract_function="doNoValueCall"
    )

    txn_hash = transact(
        contract=payable_tester_contract, contract_function="doNoValueCall"
    )

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_estimate_gas_sending_ether_to_nonpayable_function(
    w3, payable_tester_contract, estimate_gas
):
    with pytest.raises(Web3ValidationError):
        estimate_gas(
            contract=payable_tester_contract,
            contract_function="doNoValueCall",
            tx_params={"value": 1},
        )


def test_estimate_gas_accepts_latest_block(w3, math_contract, transact):
    gas_estimate = math_contract.functions.counter().estimate_gas(
        block_identifier="latest"
    )

    txn_hash = transact(contract=math_contract, contract_function="incrementCounter")

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_estimate_gas_block_identifier_unique_estimates(w3, math_contract, transact):
    txn_hash = transact(contract=math_contract, contract_function="incrementCounter")
    w3.eth.wait_for_transaction_receipt(txn_hash)

    latest_gas_estimate = math_contract.functions.counter().estimate_gas(
        block_identifier="latest"
    )
    earliest_gas_estimate = math_contract.functions.counter().estimate_gas(
        block_identifier="earliest"
    )

    assert latest_gas_estimate != earliest_gas_estimate


@pytest.mark.asyncio
async def test_async_contract_estimate_gas(
    async_w3, async_math_contract, async_estimate_gas, async_transact
):
    gas_estimate = await async_estimate_gas(
        contract=async_math_contract, contract_function="incrementCounter"
    )

    txn_hash = await async_transact(
        contract=async_math_contract, contract_function="incrementCounter"
    )

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_fallback_estimate_gas(
    async_w3, async_fallback_function_contract
):
    gas_estimate = await async_fallback_function_contract.fallback.estimate_gas()

    txn_hash = await async_fallback_function_contract.fallback.transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_estimate_gas_with_arguments(
    async_w3, async_math_contract, async_estimate_gas, async_transact
):
    gas_estimate = await async_estimate_gas(
        contract=async_math_contract, contract_function="add", func_args=[5, 6]
    )

    txn_hash = await async_transact(
        contract=async_math_contract, contract_function="add", func_args=[5, 6]
    )
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_estimate_gas_not_sending_ether_to_nonpayable_function(
    async_w3, async_payable_tester_contract, async_estimate_gas, async_transact
):
    gas_estimate = await async_estimate_gas(
        contract=async_payable_tester_contract, contract_function="doNoValueCall"
    )

    txn_hash = await async_transact(
        contract=async_payable_tester_contract, contract_function="doNoValueCall"
    )

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_estimate_gas_sending_ether_to_nonpayable_function(
    async_w3, async_payable_tester_contract, async_estimate_gas
):
    with pytest.raises(Web3ValidationError):
        await async_estimate_gas(
            contract=async_payable_tester_contract,
            contract_function="doNoValueCall",
            tx_params={"value": 1},
        )


@pytest.mark.asyncio
async def test_async_estimate_gas_accepts_latest_block(
    async_w3, async_math_contract, async_transact
):
    gas_estimate = await async_math_contract.functions.counter().estimate_gas(
        block_identifier="latest"
    )

    txn_hash = await async_transact(
        contract=async_math_contract, contract_function="incrementCounter"
    )

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_estimate_gas_can_be_called_without_parens(
    async_w3, async_math_contract, async_transact
):
    gas_estimate = await async_math_contract.functions.counter.estimate_gas(
        block_identifier="latest"
    )

    txn_hash = await async_transact(
        contract=async_math_contract, contract_function="incrementCounter"
    )

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_estimate_gas_block_identifier_unique_estimates(
    async_w3, async_math_contract, async_transact
):
    txn_hash = await async_transact(
        contract=async_math_contract, contract_function="incrementCounter"
    )
    await async_w3.eth.wait_for_transaction_receipt(txn_hash)

    latest_gas_estimate = await async_math_contract.functions.counter().estimate_gas(
        block_identifier="latest"
    )
    earliest_gas_estimate = await async_math_contract.functions.counter().estimate_gas(
        block_identifier="earliest"
    )

    assert latest_gas_estimate != earliest_gas_estimate
