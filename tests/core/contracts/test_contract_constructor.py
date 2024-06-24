import pytest

from eth_utils import (
    decode_hex,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.contract_sources.contract_data.constructor_contracts import (
    CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME,
    CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME,
    SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME,
)
from web3.exceptions import (
    Web3ValueError,
)

TEST_ADDRESS = "0x16D9983245De15E7A9A73bC586E01FF6E08dE737"
EXPECTED_DATA_A = 1234
EXPECTED_DATA_B = (
    b"abcd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)


def test_contract_constructor_abi_encoding_with_no_constructor_fn(
    math_contract_factory, math_contract_bytecode
):
    deploy_data = math_contract_factory.constructor()._encode_data_in_transaction()
    assert deploy_data == math_contract_bytecode


def test_contract_constructor_gas_estimate_no_constructor(w3, math_contract_factory):
    gas_estimate = math_contract_factory.constructor().estimate_gas()

    deploy_txn = math_contract_factory.constructor().transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_gas_estimate_with_block_id(w3, math_contract_factory):
    block_identifier = None
    gas_estimate = math_contract_factory.constructor().estimate_gas(
        block_identifier=block_identifier
    )
    deploy_txn = math_contract_factory.constructor().transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_gas_estimate_without_arguments(
    w3, simple_constructor_contract_factory
):
    gas_estimate = simple_constructor_contract_factory.constructor().estimate_gas()

    deploy_txn = simple_constructor_contract_factory.constructor().transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.parametrize(
    "constructor_args,constructor_kwargs",
    (
        ([1234, b"abcd"], {}),
        ([1234], {"b": b"abcd"}),
        ([], {"a": 1234, "b": b"abcd"}),
        ([], {"b": b"abcd", "a": 1234}),
    ),
)
def test_contract_constructor_gas_estimate_with_arguments_non_strict(
    w3_non_strict_abi,
    non_strict_contract_with_constructor_args_factory,
    constructor_args,
    constructor_kwargs,
):
    gas_estimate = non_strict_contract_with_constructor_args_factory.constructor(
        *constructor_args, **constructor_kwargs
    ).estimate_gas()

    deploy_txn = non_strict_contract_with_constructor_args_factory.constructor(
        *constructor_args, **constructor_kwargs
    ).transact()
    txn_receipt = w3_non_strict_abi.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_gas_estimate_with_address_argument(
    w3, contract_with_constructor_address_factory, address_conversion_func
):
    gas_estimate = contract_with_constructor_address_factory.constructor(
        address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")
    ).estimate_gas()

    deploy_txn = contract_with_constructor_address_factory.constructor(
        address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")
    ).transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_transact_no_constructor(
    w3, math_contract_factory, math_contract_runtime, address_conversion_func
):
    deploy_txn = math_contract_factory.constructor().transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(math_contract_runtime)


def test_contract_constructor_transact_without_arguments(
    w3,
    simple_constructor_contract_factory,
    address_conversion_func,
):
    deploy_txn = simple_constructor_contract_factory.constructor().transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME)


@pytest.mark.parametrize(
    "constructor_args,constructor_kwargs, expected_a, expected_b",
    (
        ([1234, b"abcd"], {}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([1234], {"b": b"abcd"}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([], {"a": 1234, "b": b"abcd"}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([], {"b": b"abcd", "a": 1234}, EXPECTED_DATA_A, EXPECTED_DATA_B),
    ),
)
def test_contract_constructor_transact_with_arguments_non_strict(
    w3_non_strict_abi,
    non_strict_contract_with_constructor_args_factory,
    constructor_args,
    constructor_kwargs,
    expected_a,
    expected_b,
    address_conversion_func,
):
    deploy_txn = non_strict_contract_with_constructor_args_factory.constructor(
        *constructor_args, **constructor_kwargs
    ).transact()

    txn_receipt = w3_non_strict_abi.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = w3_non_strict_abi.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME)
    assert (
        expected_a
        == non_strict_contract_with_constructor_args_factory(address=contract_address)
        .functions.data_a()
        .call()
    )
    assert (
        expected_b
        == non_strict_contract_with_constructor_args_factory(address=contract_address)
        .functions.data_b()
        .call()
    )


def test_contract_constructor_transact_with_address_argument(
    w3,
    contract_with_constructor_address_factory,
    address_conversion_func,
):
    deploy_txn = contract_with_constructor_address_factory.constructor(
        TEST_ADDRESS
    ).transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None
    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])
    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(
        CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME
    )
    assert (
        TEST_ADDRESS
        == contract_with_constructor_address_factory(address=contract_address)
        .functions.testAddr()
        .call()
    )


def test_contract_constructor_build_transaction_to_field_error(math_contract_factory):
    with pytest.raises(Web3ValueError):
        math_contract_factory.constructor().build_transaction({"to": "123"})


def test_contract_constructor_build_transaction_no_constructor(
    w3, math_contract_factory, address_conversion_func
):
    txn_hash = math_contract_factory.constructor().transact(
        {"from": address_conversion_func(w3.eth.default_account)}
    )
    txn = w3.eth.get_transaction(txn_hash)
    nonce = w3.eth.get_transaction_count(w3.eth.default_account)
    unsent_txn = math_contract_factory.constructor().build_transaction({"nonce": nonce})
    assert txn["input"] == HexBytes(unsent_txn["data"])

    new_txn_hash = w3.eth.send_transaction(unsent_txn)
    new_txn = w3.eth.get_transaction(new_txn_hash)
    assert new_txn["input"] == HexBytes(unsent_txn["data"])
    assert new_txn["nonce"] == nonce


def test_contract_constructor_build_transaction_without_arguments(
    w3, math_contract_factory, address_conversion_func
):
    txn_hash = math_contract_factory.constructor().transact(
        {"from": address_conversion_func(w3.eth.default_account)}
    )
    txn = w3.eth.get_transaction(txn_hash)
    nonce = w3.eth.get_transaction_count(w3.eth.default_account)
    unsent_txn = math_contract_factory.constructor().build_transaction({"nonce": nonce})
    assert txn["input"] == HexBytes(unsent_txn["data"])

    new_txn_hash = w3.eth.send_transaction(unsent_txn)
    new_txn = w3.eth.get_transaction(new_txn_hash)
    assert new_txn["input"] == HexBytes(unsent_txn["data"])
    assert new_txn["nonce"] == nonce


@pytest.mark.parametrize(
    "constructor_args,constructor_kwargs",
    (
        ([1234, b"abcd"], {}),
        ([1234], {"b": b"abcd"}),
        ([], {"a": 1234, "b": b"abcd"}),
        ([], {"b": b"abcd", "a": 1234}),
    ),
)
def test_contract_constructor_build_transaction_with_arguments(
    w3_non_strict_abi,
    non_strict_contract_with_constructor_args_factory,
    constructor_args,
    constructor_kwargs,
    address_conversion_func,
):
    txn_hash = non_strict_contract_with_constructor_args_factory.constructor(
        *constructor_args, **constructor_kwargs
    ).transact({"from": address_conversion_func(w3_non_strict_abi.eth.default_account)})
    txn = w3_non_strict_abi.eth.get_transaction(txn_hash)
    nonce = w3_non_strict_abi.eth.get_transaction_count(
        w3_non_strict_abi.eth.default_account
    )
    unsent_txn = non_strict_contract_with_constructor_args_factory.constructor(
        *constructor_args, **constructor_kwargs
    ).build_transaction({"nonce": nonce})
    assert txn["input"] == HexBytes(unsent_txn["data"])

    new_txn_hash = w3_non_strict_abi.eth.send_transaction(unsent_txn)
    new_txn = w3_non_strict_abi.eth.get_transaction(new_txn_hash)
    assert new_txn["input"] == HexBytes(unsent_txn["data"])
    assert new_txn["nonce"] == nonce


def test_async_contract_constructor_abi_encoding_with_no_constructor_fn(
    async_math_contract_factory, math_contract_bytecode
):
    deploy_data = (
        async_math_contract_factory.constructor()._encode_data_in_transaction()
    )
    assert deploy_data == math_contract_bytecode


@pytest.mark.asyncio
async def test_async_contract_constructor_gas_estimate_no_constructor(
    async_w3, async_math_contract_factory
):
    gas_estimate = await async_math_contract_factory.constructor().estimate_gas()

    deploy_txn = await async_math_contract_factory.constructor().transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_constructor_gas_estimate_with_block_id(
    async_w3, async_math_contract_factory
):
    block_identifier = None
    gas_estimate = await async_math_contract_factory.constructor().estimate_gas(
        block_identifier=block_identifier
    )
    deploy_txn = await async_math_contract_factory.constructor().transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_constructor_gas_estimate_without_arguments(
    async_w3, async_simple_constructor_contract_factory
):
    gas_estimate = (
        await async_simple_constructor_contract_factory.constructor().estimate_gas()
    )

    deploy_txn = (
        await async_simple_constructor_contract_factory.constructor().transact()
    )
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "constructor_args,constructor_kwargs",
    (
        ([1234, b"abcd"], {}),
        ([1234], {"b": b"abcd"}),
        ([], {"a": 1234, "b": b"abcd"}),
        ([], {"b": b"abcd", "a": 1234}),
    ),
)
async def test_async_contract_constructor_gas_estimate_with_arguments_non_strict(
    async_w3_non_strict_abi,
    async_non_strict_constructor_with_args_contract_factory,
    constructor_args,
    constructor_kwargs,
):
    gas_estimate = (
        await async_non_strict_constructor_with_args_contract_factory.constructor(
            *constructor_args, **constructor_kwargs
        ).estimate_gas()
    )

    deploy_txn = (
        await async_non_strict_constructor_with_args_contract_factory.constructor(
            *constructor_args, **constructor_kwargs
        ).transact()
    )
    txn_receipt = await async_w3_non_strict_abi.eth.wait_for_transaction_receipt(
        deploy_txn
    )
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_constructor_with_address_argument_gas_estimate(
    async_w3,
    async_constructor_with_address_arg_contract_factory,
    address_conversion_func,
):
    gas_estimate = (
        await async_constructor_with_address_arg_contract_factory.constructor(
            address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")
        ).estimate_gas()
    )

    deploy_txn = await async_constructor_with_address_arg_contract_factory.constructor(
        address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")
    ).transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_constructor_transact_no_constructor(
    async_w3,
    async_math_contract_factory,
    math_contract_runtime,
    address_conversion_func,
):
    deploy_txn = await async_math_contract_factory.constructor().transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(math_contract_runtime)


@pytest.mark.asyncio
async def test_async_contract_constructor_transact_without_arguments(
    async_w3,
    async_simple_constructor_contract_factory,
    address_conversion_func,
):
    deploy_txn = (
        await async_simple_constructor_contract_factory.constructor().transact()
    )

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "constructor_args,constructor_kwargs, expected_a, expected_b",
    (
        ([1234, b"abcd"], {}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([1234], {"b": b"abcd"}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([], {"a": 1234, "b": b"abcd"}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([], {"b": b"abcd", "a": 1234}, EXPECTED_DATA_A, EXPECTED_DATA_B),
    ),
)
async def test_async_contract_constructor_transact_with_arguments_non_strict(
    async_w3_non_strict_abi,
    async_non_strict_constructor_with_args_contract_factory,
    constructor_args,
    constructor_kwargs,
    expected_a,
    expected_b,
    address_conversion_func,
):
    deploy_txn = (
        await async_non_strict_constructor_with_args_contract_factory.constructor(
            *constructor_args, **constructor_kwargs
        ).transact()
    )

    txn_receipt = await async_w3_non_strict_abi.eth.wait_for_transaction_receipt(
        deploy_txn
    )
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = await async_w3_non_strict_abi.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME)
    assert (
        expected_a
        == await async_non_strict_constructor_with_args_contract_factory(
            address=contract_address
        )
        .functions.data_a()
        .call()
    )
    assert (
        expected_b
        == await async_non_strict_constructor_with_args_contract_factory(
            address=contract_address
        )
        .functions.data_b()
        .call()
    )


@pytest.mark.asyncio
async def test_async_contract_constructor_transact_with_address_arguments(
    async_w3,
    async_constructor_with_address_arg_contract_factory,
    address_conversion_func,
):
    deploy_txn = await async_constructor_with_address_arg_contract_factory.constructor(
        TEST_ADDRESS
    ).transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None
    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])
    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(
        CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME
    )
    assert (
        TEST_ADDRESS
        == await async_constructor_with_address_arg_contract_factory(
            address=contract_address
        )
        .functions.testAddr()
        .call()
    )


@pytest.mark.asyncio
async def test_async_contract_constructor_build_transaction_to_field_error(
    async_math_contract_factory,
):
    with pytest.raises(Web3ValueError):
        await async_math_contract_factory.constructor().build_transaction({"to": "123"})


@pytest.mark.asyncio
async def test_async_contract_constructor_build_transaction_no_constructor(
    async_w3, async_math_contract_factory, address_conversion_func
):
    txn_hash = await async_math_contract_factory.constructor().transact(
        {"from": address_conversion_func(async_w3.eth.default_account)}
    )
    txn = await async_w3.eth.get_transaction(txn_hash)
    nonce = await async_w3.eth.get_transaction_count(async_w3.eth.default_account)
    unsent_txn = await async_math_contract_factory.constructor().build_transaction(
        {"nonce": nonce}
    )
    assert txn["input"] == HexBytes(unsent_txn["data"])

    new_txn_hash = await async_w3.eth.send_transaction(unsent_txn)
    new_txn = await async_w3.eth.get_transaction(new_txn_hash)
    assert new_txn["input"] == HexBytes(unsent_txn["data"])
    assert new_txn["nonce"] == nonce


@pytest.mark.asyncio
async def test_async_contract_constructor_build_transaction_without_arguments(
    async_w3, async_math_contract_factory, address_conversion_func
):
    txn_hash = await async_math_contract_factory.constructor().transact(
        {"from": address_conversion_func(async_w3.eth.default_account)}
    )
    txn = await async_w3.eth.get_transaction(txn_hash)
    nonce = await async_w3.eth.get_transaction_count(async_w3.eth.default_account)
    unsent_txn = await async_math_contract_factory.constructor().build_transaction(
        {"nonce": nonce}
    )
    assert txn["input"] == HexBytes(unsent_txn["data"])

    new_txn_hash = await async_w3.eth.send_transaction(unsent_txn)
    new_txn = await async_w3.eth.get_transaction(new_txn_hash)
    assert new_txn["input"] == HexBytes(unsent_txn["data"])
    assert new_txn["nonce"] == nonce


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "constructor_args,constructor_kwargs",
    (
        ([1234, b"abcd"], {}),
        ([1234], {"b": b"abcd"}),
        ([], {"a": 1234, "b": b"abcd"}),
        ([], {"b": b"abcd", "a": 1234}),
    ),
)
async def test_async_contract_constructor_build_transaction_with_arguments(
    async_w3_non_strict_abi,
    async_non_strict_constructor_with_args_contract_factory,
    constructor_args,
    constructor_kwargs,
    address_conversion_func,
):
    txn_hash = (
        await async_non_strict_constructor_with_args_contract_factory.constructor(
            *constructor_args, **constructor_kwargs
        ).transact(
            {
                "from": address_conversion_func(
                    async_w3_non_strict_abi.eth.default_account
                )
            }
        )
    )
    txn = await async_w3_non_strict_abi.eth.get_transaction(txn_hash)
    nonce = await async_w3_non_strict_abi.eth.get_transaction_count(
        async_w3_non_strict_abi.eth.default_account
    )
    unsent_txn = (
        await async_non_strict_constructor_with_args_contract_factory.constructor(
            *constructor_args, **constructor_kwargs
        ).build_transaction({"nonce": nonce})
    )
    assert txn["input"] == HexBytes(unsent_txn["data"])

    new_txn_hash = await async_w3_non_strict_abi.eth.send_transaction(unsent_txn)
    new_txn = await async_w3_non_strict_abi.eth.get_transaction(new_txn_hash)
    assert new_txn["input"] == HexBytes(unsent_txn["data"])
    assert new_txn["nonce"] == nonce
