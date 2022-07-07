import pytest

from eth_utils import (
    decode_hex,
)

TEST_ADDRESS = "0x16D9983245De15E7A9A73bC586E01FF6E08dE737"
EXPECTED_DATA_A = 1234
EXPECTED_DATA_B = (
    b"abcd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)


def test_contract_constructor_abi_encoding_with_no_constructor_fn(
    MathContract, MATH_CODE
):
    deploy_data = MathContract.constructor()._encode_data_in_transaction()
    assert deploy_data == MATH_CODE


def test_contract_constructor_gas_estimate_no_constructor(w3, MathContract):
    gas_estimate = MathContract.constructor().estimate_gas()

    deploy_txn = MathContract.constructor().transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_gas_estimate_with_block_id(w3, MathContract):
    block_identifier = None
    gas_estimate = MathContract.constructor().estimate_gas(
        block_identifier=block_identifier
    )
    deploy_txn = MathContract.constructor().transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_gas_estimate_with_constructor_without_arguments(
    w3, SimpleConstructorContract
):
    gas_estimate = SimpleConstructorContract.constructor().estimate_gas()

    deploy_txn = SimpleConstructorContract.constructor().transact()
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
def test_contract_constructor_gas_estimate_with_constructor_with_arguments(
    w3, WithConstructorArgumentsContract, constructor_args, constructor_kwargs
):
    gas_estimate = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).estimate_gas()

    deploy_txn = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_gas_estimate_with_constructor_with_address_argument(
    w3, WithConstructorAddressArgumentsContract, address_conversion_func
):
    gas_estimate = WithConstructorAddressArgumentsContract.constructor(
        address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")
    ).estimate_gas()

    deploy_txn = WithConstructorAddressArgumentsContract.constructor(
        address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")
    ).transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_transact_no_constructor(
    w3, MathContract, MATH_RUNTIME, address_conversion_func
):
    deploy_txn = MathContract.constructor().transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(MATH_RUNTIME)


def test_contract_constructor_transact_with_constructor_without_arguments(
    w3, SimpleConstructorContract, SIMPLE_CONSTRUCTOR_RUNTIME, address_conversion_func
):
    deploy_txn = SimpleConstructorContract.constructor().transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_RUNTIME)


@pytest.mark.parametrize(
    "constructor_args,constructor_kwargs, expected_a, expected_b",
    (
        ([1234, b"abcd"], {}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([1234], {"b": b"abcd"}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([], {"a": 1234, "b": b"abcd"}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([], {"b": b"abcd", "a": 1234}, EXPECTED_DATA_A, EXPECTED_DATA_B),
    ),
)
def test_contract_constructor_transact_with_constructor_with_arguments(
    w3,
    WithConstructorArgumentsContract,
    WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
    constructor_args,
    constructor_kwargs,
    expected_a,
    expected_b,
    address_conversion_func,
):
    deploy_txn = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)
    assert (
        expected_a
        == WithConstructorArgumentsContract(address=contract_address)
        .functions.data_a()
        .call()
    )
    assert (
        expected_b
        == WithConstructorArgumentsContract(address=contract_address)
        .functions.data_b()
        .call()
    )


def test_contract_constructor_transact_with_constructor_with_address_arguments(
    w3,
    WithConstructorAddressArgumentsContract,
    WITH_CONSTRUCTOR_ADDRESS_RUNTIME,
    address_conversion_func,
):
    deploy_txn = WithConstructorAddressArgumentsContract.constructor(
        TEST_ADDRESS
    ).transact()
    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None
    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])
    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)
    assert (
        TEST_ADDRESS
        == WithConstructorAddressArgumentsContract(address=contract_address)
        .functions.testAddr()
        .call()
    )


def test_contract_constructor_build_transaction_to_field_error(MathContract):
    with pytest.raises(ValueError):
        MathContract.constructor().build_transaction({"to": "123"})


def test_contract_constructor_build_transaction_no_constructor(
    w3, MathContract, address_conversion_func
):
    txn_hash = MathContract.constructor().transact(
        {"from": address_conversion_func(w3.eth.accounts[0])}
    )
    txn = w3.eth.get_transaction(txn_hash)
    nonce = w3.eth.get_transaction_count(w3.eth.coinbase)
    unsent_txn = MathContract.constructor().build_transaction({"nonce": nonce})
    assert txn["data"] == unsent_txn["data"]

    new_txn_hash = w3.eth.send_transaction(unsent_txn)
    new_txn = w3.eth.get_transaction(new_txn_hash)
    assert new_txn["data"] == unsent_txn["data"]
    assert new_txn["nonce"] == nonce


def test_contract_constructor_build_transaction_with_constructor_without_argument(
    w3, MathContract, address_conversion_func
):
    txn_hash = MathContract.constructor().transact(
        {"from": address_conversion_func(w3.eth.accounts[0])}
    )
    txn = w3.eth.get_transaction(txn_hash)
    nonce = w3.eth.get_transaction_count(w3.eth.coinbase)
    unsent_txn = MathContract.constructor().build_transaction({"nonce": nonce})
    assert txn["data"] == unsent_txn["data"]

    new_txn_hash = w3.eth.send_transaction(unsent_txn)
    new_txn = w3.eth.get_transaction(new_txn_hash)
    assert new_txn["data"] == unsent_txn["data"]
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
def test_contract_constructor_build_transaction_with_constructor_with_argument(
    w3,
    WithConstructorArgumentsContract,
    constructor_args,
    constructor_kwargs,
    address_conversion_func,
):
    txn_hash = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).transact({"from": address_conversion_func(w3.eth.accounts[0])})
    txn = w3.eth.get_transaction(txn_hash)
    nonce = w3.eth.get_transaction_count(w3.eth.coinbase)
    unsent_txn = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).build_transaction({"nonce": nonce})
    assert txn["data"] == unsent_txn["data"]

    new_txn_hash = w3.eth.send_transaction(unsent_txn)
    new_txn = w3.eth.get_transaction(new_txn_hash)
    assert new_txn["data"] == unsent_txn["data"]
    assert new_txn["nonce"] == nonce


def test_async_contract_constructor_abi_encoding_with_no_constructor_fn(
    AsyncMathContract, MATH_CODE
):
    deploy_data = AsyncMathContract.constructor()._encode_data_in_transaction()
    assert deploy_data == MATH_CODE


@pytest.mark.asyncio
async def test_async_contract_constructor_gas_estimate_no_constructor(
    async_w3, AsyncMathContract
):
    gas_estimate = await AsyncMathContract.constructor().estimate_gas()

    deploy_txn = await AsyncMathContract.constructor().transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_constructor_gas_estimate_with_block_id(
    async_w3, AsyncMathContract
):
    block_identifier = None
    gas_estimate = await AsyncMathContract.constructor().estimate_gas(
        block_identifier=block_identifier
    )
    deploy_txn = await AsyncMathContract.constructor().transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_constructor_gas_estimate_with_constructor_without_arguments(  # noqa: E501
    async_w3, AsyncSimpleConstructorContract
):
    gas_estimate = await AsyncSimpleConstructorContract.constructor().estimate_gas()

    deploy_txn = await AsyncSimpleConstructorContract.constructor().transact()
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
async def test_async_contract_constructor_gas_estimate_with_constructor_with_arguments(
    async_w3,
    AsyncWithConstructorArgumentsContract,
    constructor_args,
    constructor_kwargs,
):
    gas_estimate = await AsyncWithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).estimate_gas()

    deploy_txn = await AsyncWithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_constructor_gas_estimate_with_constructor_with_address_argument(  # noqa: E501
    async_w3, AsyncWithConstructorAddressArgumentsContract, address_conversion_func
):
    gas_estimate = await AsyncWithConstructorAddressArgumentsContract.constructor(
        address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")
    ).estimate_gas()

    deploy_txn = await AsyncWithConstructorAddressArgumentsContract.constructor(
        address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")
    ).transact()
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    gas_used = txn_receipt.get("gasUsed")

    assert abs(gas_estimate - gas_used) < 21000


@pytest.mark.asyncio
async def test_async_contract_constructor_transact_no_constructor(
    async_w3, AsyncMathContract, MATH_RUNTIME, address_conversion_func
):
    deploy_txn = await AsyncMathContract.constructor().transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(MATH_RUNTIME)


@pytest.mark.asyncio
async def test_async_contract_constructor_transact_with_constructor_without_arguments(
    async_w3,
    AsyncSimpleConstructorContract,
    SIMPLE_CONSTRUCTOR_RUNTIME,
    address_conversion_func,
):
    deploy_txn = await AsyncSimpleConstructorContract.constructor().transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_RUNTIME)


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
async def test_async_contract_constructor_transact_with_constructor_with_arguments(
    async_w3,
    AsyncWithConstructorArgumentsContract,
    WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
    constructor_args,
    constructor_kwargs,
    expected_a,
    expected_b,
    address_conversion_func,
):
    deploy_txn = await AsyncWithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)
    assert (
        expected_a
        == await AsyncWithConstructorArgumentsContract(address=contract_address)
        .functions.data_a()
        .call()
    )
    assert (
        expected_b
        == await AsyncWithConstructorArgumentsContract(address=contract_address)
        .functions.data_b()
        .call()
    )


@pytest.mark.asyncio
async def test_async_contract_constructor_transact_with_constructor_with_address_arguments(  # noqa: E501
    async_w3,
    AsyncWithConstructorAddressArgumentsContract,
    WITH_CONSTRUCTOR_ADDRESS_RUNTIME,
    address_conversion_func,
):
    deploy_txn = await AsyncWithConstructorAddressArgumentsContract.constructor(
        TEST_ADDRESS
    ).transact()  # noqa: E501
    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None
    assert txn_receipt["contractAddress"]
    contract_address = address_conversion_func(txn_receipt["contractAddress"])
    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)
    assert (
        TEST_ADDRESS
        == await AsyncWithConstructorAddressArgumentsContract(address=contract_address)
        .functions.testAddr()
        .call()
    )


@pytest.mark.asyncio
async def test_async_contract_constructor_build_transaction_to_field_error(
    AsyncMathContract,
):
    with pytest.raises(ValueError):
        await AsyncMathContract.constructor().build_transaction({"to": "123"})


@pytest.mark.asyncio
async def test_async_contract_constructor_build_transaction_no_constructor(
    async_w3, AsyncMathContract, address_conversion_func
):
    async_w3_accounts = await async_w3.eth.accounts
    txn_hash = await AsyncMathContract.constructor().transact(
        {"from": address_conversion_func(async_w3_accounts[0])}
    )
    txn = await async_w3.eth.get_transaction(txn_hash)
    async_w3_coinbase = await async_w3.eth.coinbase
    nonce = await async_w3.eth.get_transaction_count(async_w3_coinbase)
    unsent_txn = await AsyncMathContract.constructor().build_transaction(
        {"nonce": nonce}
    )
    assert txn["data"] == unsent_txn["data"]

    new_txn_hash = await async_w3.eth.send_transaction(unsent_txn)
    new_txn = await async_w3.eth.get_transaction(new_txn_hash)
    assert new_txn["data"] == unsent_txn["data"]
    assert new_txn["nonce"] == nonce


@pytest.mark.asyncio
async def test_async_contract_constructor_build_transaction_with_constructor_without_argument(  # noqa: E501
    async_w3, AsyncMathContract, address_conversion_func
):
    async_w3_accounts = await async_w3.eth.accounts
    txn_hash = await AsyncMathContract.constructor().transact(
        {"from": address_conversion_func(async_w3_accounts[0])}
    )
    txn = await async_w3.eth.get_transaction(txn_hash)
    async_w3_coinbase = await async_w3.eth.coinbase
    nonce = await async_w3.eth.get_transaction_count(async_w3_coinbase)
    unsent_txn = await AsyncMathContract.constructor().build_transaction(
        {"nonce": nonce}
    )
    assert txn["data"] == unsent_txn["data"]

    new_txn_hash = await async_w3.eth.send_transaction(unsent_txn)
    new_txn = await async_w3.eth.get_transaction(new_txn_hash)
    assert new_txn["data"] == unsent_txn["data"]
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
async def test_async_contract_constructor_build_transaction_with_constructor_with_argument(  # noqa: E501
    async_w3,
    AsyncWithConstructorArgumentsContract,
    constructor_args,
    constructor_kwargs,
    address_conversion_func,
):
    async_w3_accounts = await async_w3.eth.accounts
    txn_hash = await AsyncWithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).transact({"from": address_conversion_func(async_w3_accounts[0])})
    txn = await async_w3.eth.get_transaction(txn_hash)
    async_w3_coinbase = await async_w3.eth.coinbase
    nonce = await async_w3.eth.get_transaction_count(async_w3_coinbase)
    unsent_txn = await AsyncWithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs
    ).build_transaction({"nonce": nonce})
    assert txn["data"] == unsent_txn["data"]

    new_txn_hash = await async_w3.eth.send_transaction(unsent_txn)
    new_txn = await async_w3.eth.get_transaction(new_txn_hash)
    assert new_txn["data"] == unsent_txn["data"]
    assert new_txn["nonce"] == nonce
