import pytest

from web3._utils.empty import (
    empty,
)
from web3.exceptions import (
    Web3ValidationError,
)


def test_transacting_with_contract_no_arguments(w3, math_contract, transact, call):
    initial_value = call(contract=math_contract, contract_function="counter")

    txn_hash = transact(contract=math_contract, contract_function="incrementCounter")
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=math_contract, contract_function="counter")

    assert final_value - initial_value == 1


def test_transact_not_sending_ether_to_nonpayable_function(
    w3, payable_tester_contract, transact, call
):
    initial_value = call(
        contract=payable_tester_contract, contract_function="wasCalled"
    )

    assert initial_value is False
    txn_hash = transact(
        contract=payable_tester_contract, contract_function="doNoValueCall"
    )
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=payable_tester_contract, contract_function="wasCalled")

    assert final_value is True


def test_transact_sending_ether_to_nonpayable_function(
    w3, payable_tester_contract, transact, call
):
    initial_value = call(
        contract=payable_tester_contract, contract_function="wasCalled"
    )

    assert initial_value is False
    with pytest.raises(Web3ValidationError):
        txn_hash = transact(
            contract=payable_tester_contract,
            contract_function="doNoValueCall",
            tx_params={"value": 1},
        )
        txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
        assert txn_receipt is not None

    final_value = call(contract=payable_tester_contract, contract_function="wasCalled")

    assert final_value is False


@pytest.mark.parametrize(
    "transact_args,transact_kwargs",
    (
        ((5,), {}),
        (tuple(), {"amount": 5}),
    ),
)
def test_transacting_with_contract_with_arguments(
    w3, math_contract, transact, call, transact_args, transact_kwargs
):
    initial_value = call(contract=math_contract, contract_function="counter")

    txn_hash = transact(
        contract=math_contract,
        contract_function="incrementCounter",
        func_args=transact_args,
        func_kwargs=transact_kwargs,
    )

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=math_contract, contract_function="counter")

    assert final_value - initial_value == 5


def test_deploy_when_default_account_is_set(w3, string_contract_data):
    # default account for tests is set as the first account
    assert w3.eth.default_account is not empty

    StringContract = w3.eth.contract(**string_contract_data)

    deploy_txn = StringContract.constructor("Caqalai").transact()
    w3.eth.wait_for_transaction_receipt(deploy_txn)
    txn_after = w3.eth.get_transaction(deploy_txn)
    assert txn_after["from"] == w3.eth.default_account


def test_transact_when_default_account_is_set(w3, math_contract, transact):
    # default account for tests is set as the first account
    assert w3.eth.default_account is not empty

    txn_hash = transact(contract=math_contract, contract_function="incrementCounter")
    txn_after = w3.eth.get_transaction(txn_hash)
    assert txn_after["from"] == w3.eth.default_account


def test_transacting_with_contract_with_string_argument(
    w3, string_contract, transact, call
):
    txn_hash = transact(
        contract=string_contract,
        contract_function="setValue",
        func_args=["ÄLÄMÖLÖ"],
    )
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=string_contract, contract_function="getValue")

    assert final_value == "ÄLÄMÖLÖ"


def test_transacting_with_contract_with_encoded_string_argument_non_strict(
    w3_non_strict_abi, non_strict_string_contract, transact, call
):
    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = transact(
        contract=non_strict_string_contract,
        contract_function="setValue",
        func_args=["ÄLÄMÖLÖ".encode()],
    )
    txn_receipt = w3_non_strict_abi.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(
        contract=non_strict_string_contract, contract_function="getValue"
    )

    assert final_value == "ÄLÄMÖLÖ"


def test_transacting_with_contract_with_bytes32_array_argument(
    w3, arrays_contract, transact, call
):
    # new_bytes32_array = [keccak('1'), keccak('2'), keccak('3')]
    new_bytes32_array = [
        b"\xc8\x9e\xfd\xaaT\xc0\xf2\x0cz\xdfa(\x82\xdf\tP\xf5\xa9Qc~\x03\x07\xcd\xcbLg/)\x8b\x8b\xc6",  # noqa: E501
        b"\xad|[\xef\x02x\x16\xa8\x00\xda\x176DO\xb5\x8a\x80~\xf4\xc9`;xHg?~:h\xeb\x14\xa5",  # noqa: E501
        b"*\x80\xe1\xef\x1dxB\xf2\x7f.k\xe0\x97+\xb7\x08\xb9\xa15\xc3\x88`\xdb\xe7<'\xc3Hl4\xf4\xde",  # noqa: E501
    ]
    txn_hash = transact(
        contract=arrays_contract,
        contract_function="setBytes32Value",
        func_args=[new_bytes32_array],
    )
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=arrays_contract, contract_function="getBytes32Value")
    assert final_value == new_bytes32_array


def test_transacting_with_contract_with_byte_array_argument_strict(
    w3, arrays_contract, transact, call
):
    new_byte_array = [b"\x03", b"\x03", b"\x03", b"\x03", b"\x03", b"\x03"]
    txn_hash = transact(
        contract=arrays_contract,
        contract_function="setByteValue",
        func_args=[new_byte_array],
    )
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=arrays_contract, contract_function="getByteValue")
    assert final_value == new_byte_array


def test_transacting_with_contract_with_byte_array_argument_non_strict(
    w3_non_strict_abi, non_strict_arrays_contract, transact, call
):
    new_byte_array = [b"\x03", b"\x03", b"\x03", b"\x03", b"\x03", b"\x03"]
    txn_hash = transact(
        contract=non_strict_arrays_contract,
        contract_function="setByteValue",
        func_args=[new_byte_array],
    )
    txn_receipt = w3_non_strict_abi.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(
        contract=non_strict_arrays_contract, contract_function="getByteValue"
    )
    assert final_value == new_byte_array


def test_transacting_with_contract_respects_explicit_gas(
    w3, string_contract_data, wait_for_block, call, transact
):
    StringContract = w3.eth.contract(**string_contract_data)

    deploy_txn = StringContract.constructor("Caqalai").transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn, 30)
    assert deploy_receipt is not None
    string_contract = StringContract(address=deploy_receipt["contractAddress"])

    txn_hash = transact(
        contract=string_contract,
        contract_function="setValue",
        func_args=["ÄLÄMÖLÖ"],
        tx_params={"gas": 200000},
    )
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash, 30)
    assert txn_receipt is not None

    final_value = call(contract=string_contract, contract_function="getValue")
    assert final_value == "ÄLÄMÖLÖ"

    txn = w3.eth.get_transaction(txn_hash)
    assert txn["gas"] == 200000


def test_auto_gas_computation_when_transacting(
    w3, string_contract_data, wait_for_block, call, transact
):
    StringContract = w3.eth.contract(**string_contract_data)

    deploy_txn = StringContract.constructor("Caqalai").transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn, 30)
    assert deploy_receipt is not None
    string_contract = StringContract(address=deploy_receipt["contractAddress"])

    gas_estimate = string_contract.functions.setValue("ÄLÄMÖLÖ").estimate_gas()
    txn_hash = transact(
        contract=string_contract,
        contract_function="setValue",
        func_args=["ÄLÄMÖLÖ"],
    )
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash, 30)
    assert txn_receipt is not None

    final_value = call(contract=string_contract, contract_function="getValue")
    assert final_value == "ÄLÄMÖLÖ"

    txn = w3.eth.get_transaction(txn_hash)
    assert txn["gas"] == gas_estimate + 100000


def test_fallback_transacting_with_contract(w3, fallback_function_contract, call):
    initial_value = call(
        contract=fallback_function_contract, contract_function="getData"
    )
    txn_hash = fallback_function_contract.fallback.transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=fallback_function_contract, contract_function="getData")

    assert final_value - initial_value == 1


def test_receive_function(receive_function_contract, call):
    initial_value = call(
        contract=receive_function_contract, contract_function="getText"
    )
    assert initial_value == ""
    receive_function_contract.receive.transact()
    final_value = call(contract=receive_function_contract, contract_function="getText")
    assert final_value == "receive"


def test_receive_contract_with_fallback_function(receive_function_contract, call):
    initial_value = call(
        contract=receive_function_contract, contract_function="getText"
    )
    assert initial_value == ""
    receive_function_contract.fallback.transact()
    final_value = call(contract=receive_function_contract, contract_function="getText")
    assert final_value == "receive"


def test_contract_can_transact_without_fn_parens(w3, math_contract, call):
    initial_value = call(contract=math_contract, contract_function="counter")
    txn_hash = math_contract.functions.incrementCounter.transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=math_contract, contract_function="counter")

    assert final_value - initial_value == 1


@pytest.mark.asyncio
async def test_async_transacting_with_contract_no_arguments(
    async_w3, async_math_contract, async_transact, async_call
):
    initial_value = await async_call(
        contract=async_math_contract, contract_function="counter"
    )

    txn_hash = await async_transact(
        contract=async_math_contract, contract_function="incrementCounter"
    )
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=async_math_contract, contract_function="counter"
    )

    assert final_value - initial_value == 1


@pytest.mark.asyncio
async def test_async_transacting_with_contract_no_arguments_no_parens(
    async_w3, async_math_contract, async_transact, async_call
):
    initial_value = await async_call(
        contract=async_math_contract, contract_function="counter"
    )

    txn_hash = await async_math_contract.functions.incrementCounter.transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=async_math_contract, contract_function="counter"
    )

    assert final_value - initial_value == 1


@pytest.mark.asyncio
async def test_async_transact_not_sending_ether_to_nonpayable_function(
    async_w3, async_payable_tester_contract, async_transact, async_call
):
    initial_value = await async_call(
        contract=async_payable_tester_contract, contract_function="wasCalled"
    )

    assert initial_value is False
    txn_hash = await async_transact(
        contract=async_payable_tester_contract, contract_function="doNoValueCall"
    )
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=async_payable_tester_contract, contract_function="wasCalled"
    )

    assert final_value is True


@pytest.mark.asyncio
async def test_async_transact_sending_ether_to_nonpayable_function(
    async_w3, async_payable_tester_contract, async_transact, async_call
):
    initial_value = await async_call(
        contract=async_payable_tester_contract, contract_function="wasCalled"
    )

    assert initial_value is False
    with pytest.raises(Web3ValidationError):
        txn_hash = await async_transact(
            contract=async_payable_tester_contract,
            contract_function="doNoValueCall",
            tx_params={"value": 1},
        )
        txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
        assert txn_receipt is not None

    final_value = await async_call(
        contract=async_payable_tester_contract, contract_function="wasCalled"
    )

    assert final_value is False


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "transact_args,transact_kwargs",
    (
        ((5,), {}),
        (tuple(), {"amount": 5}),
    ),
)
async def test_async_transacting_with_contract_with_arguments(
    async_w3,
    async_math_contract,
    async_transact,
    async_call,
    transact_args,
    transact_kwargs,
):
    initial_value = await async_call(
        contract=async_math_contract, contract_function="counter"
    )

    txn_hash = await async_transact(
        contract=async_math_contract,
        contract_function="incrementCounter",
        func_args=transact_args,
        func_kwargs=transact_kwargs,
    )

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=async_math_contract, contract_function="counter"
    )

    assert final_value - initial_value == 5


@pytest.mark.asyncio
async def test_async_deploy_when_default_account_is_set(async_w3, string_contract_data):
    # default account for tests is set as the first account
    assert async_w3.eth.default_account is not empty

    StringContract = async_w3.eth.contract(**string_contract_data)

    deploy_txn = await StringContract.constructor("Caqalai").transact()
    await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    txn_after = await async_w3.eth.get_transaction(deploy_txn)
    assert txn_after["from"] == async_w3.eth.default_account


@pytest.mark.asyncio
async def test_async_transact_when_default_account_is_set(
    async_w3, async_math_contract, async_transact
):
    # default account for tests is set as the first account
    assert async_w3.eth.default_account is not empty

    txn_hash = await async_transact(
        contract=async_math_contract, contract_function="incrementCounter"
    )
    txn_after = await async_w3.eth.get_transaction(txn_hash)
    assert txn_after["from"] == async_w3.eth.default_account


@pytest.mark.asyncio
async def test_async_transacting_with_contract_with_string_argument(
    async_w3, async_string_contract, async_transact, async_call
):
    txn_hash = await async_transact(
        contract=async_string_contract,
        contract_function="setValue",
        func_args=["ÄLÄMÖLÖ"],
    )
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=async_string_contract, contract_function="getValue"
    )
    assert final_value == "ÄLÄMÖLÖ"


@pytest.mark.asyncio
async def test_async_transacting_with_contract_with_bytes32_array_argument(
    async_w3, async_arrays_contract, async_transact, async_call
):
    # new_bytes32_array = [keccak('1'), keccak('2'), keccak('3')]
    new_bytes32_array = [
        b"\xc8\x9e\xfd\xaaT\xc0\xf2\x0cz\xdfa(\x82\xdf\tP\xf5\xa9Qc~\x03\x07\xcd\xcbLg/)\x8b\x8b\xc6",  # noqa: E501
        b"\xad|[\xef\x02x\x16\xa8\x00\xda\x176DO\xb5\x8a\x80~\xf4\xc9`;xHg?~:h\xeb\x14\xa5",  # noqa: E501
        b"*\x80\xe1\xef\x1dxB\xf2\x7f.k\xe0\x97+\xb7\x08\xb9\xa15\xc3\x88`\xdb\xe7<'\xc3Hl4\xf4\xde",  # noqa: E501
    ]
    txn_hash = await async_transact(
        contract=async_arrays_contract,
        contract_function="setBytes32Value",
        func_args=[new_bytes32_array],
    )
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=async_arrays_contract, contract_function="getBytes32Value"
    )
    assert final_value == new_bytes32_array


@pytest.mark.asyncio
async def test_async_transacting_with_contract_with_byte_array_argument(
    async_w3,
    async_arrays_contract,
    async_transact,
    async_call,
):
    new_byte_array = [b"\x03", b"\x03", b"\x03", b"\x03", b"\x03", b"\x03"]
    txn_hash = await async_transact(
        contract=async_arrays_contract,
        contract_function="setByteValue",
        func_args=[new_byte_array],
    )
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=async_arrays_contract, contract_function="getByteValue"
    )
    assert final_value == new_byte_array


@pytest.mark.asyncio
async def test_async_transacting_with_contract_with_byte_array_argument_non_strict(
    async_w3_non_strict_abi,
    async_non_strict_arrays_contract,
    async_transact,
    async_call,
):
    new_byte_array = [b"\x03", b"\x03", b"\x03", b"\x03", b"\x03", b"\x03"]
    txn_hash = await async_transact(
        contract=async_non_strict_arrays_contract,
        contract_function="setByteValue",
        func_args=[new_byte_array],
    )
    txn_receipt = await async_w3_non_strict_abi.eth.wait_for_transaction_receipt(
        txn_hash
    )
    assert txn_receipt is not None

    final_value = await async_call(
        contract=async_non_strict_arrays_contract, contract_function="getByteValue"
    )
    assert final_value == new_byte_array


@pytest.mark.asyncio
async def test_async_transacting_with_contract_respects_explicit_gas(
    async_w3, string_contract_data, async_call, async_transact
):
    StringContract = async_w3.eth.contract(**string_contract_data)

    deploy_txn = await StringContract.constructor("Caqalai").transact()
    deploy_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn, 30)
    assert deploy_receipt is not None
    string_contract = StringContract(address=deploy_receipt["contractAddress"])

    txn_hash = await async_transact(
        contract=string_contract,
        contract_function="setValue",
        func_args=["ÄLÄMÖLÖ"],
        tx_params={"gas": 200000},
    )
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash, 30)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=string_contract, contract_function="getValue"
    )
    assert final_value == "ÄLÄMÖLÖ"

    txn = await async_w3.eth.get_transaction(txn_hash)
    assert txn["gas"] == 200000


@pytest.mark.asyncio
async def test_async_auto_gas_computation_when_transacting(
    async_w3, string_contract_data, async_call, async_transact
):
    StringContract = async_w3.eth.contract(**string_contract_data)

    deploy_txn = await StringContract.constructor("Caqalai").transact()
    deploy_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn, 30)
    assert deploy_receipt is not None
    string_contract = StringContract(address=deploy_receipt["contractAddress"])

    gas_estimate = await string_contract.functions.setValue("ÄLÄMÖLÖ").estimate_gas()

    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = await async_transact(
        contract=string_contract,
        contract_function="setValue",
        func_args=["ÄLÄMÖLÖ"],
    )
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash, 30)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=string_contract, contract_function="getValue"
    )
    assert final_value == "ÄLÄMÖLÖ"

    txn = await async_w3.eth.get_transaction(txn_hash)
    assert txn["gas"] == gas_estimate + 100000


@pytest.mark.asyncio
async def test_async_fallback_transacting_with_contract(
    async_w3, async_fallback_function_contract, async_call
):
    initial_value = await async_call(
        contract=async_fallback_function_contract, contract_function="getData"
    )
    txn_hash = await async_fallback_function_contract.fallback.transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt is not None

    final_value = await async_call(
        contract=async_fallback_function_contract, contract_function="getData"
    )

    assert final_value - initial_value == 1


@pytest.mark.asyncio
async def test_async_receive_function(async_receive_function_contract, async_call):
    initial_value = await async_call(
        contract=async_receive_function_contract, contract_function="getText"
    )
    assert initial_value == ""
    await async_receive_function_contract.receive.transact()
    final_value = await async_call(
        contract=async_receive_function_contract, contract_function="getText"
    )
    assert final_value == "receive"


@pytest.mark.asyncio
async def test_async_receive_contract_with_fallback_function(
    async_receive_function_contract, async_call
):
    initial_value = await async_call(
        contract=async_receive_function_contract, contract_function="getText"
    )
    assert initial_value == ""
    await async_receive_function_contract.fallback.transact()
    final_value = await async_call(
        contract=async_receive_function_contract, contract_function="getText"
    )
    assert final_value == "receive"
