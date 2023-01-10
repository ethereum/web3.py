import pytest

from eth_utils import (
    decode_hex,
)

from web3 import (
    constants,
)


def test_contract_deployment_no_constructor(w3, MathContract, MATH_RUNTIME):
    deploy_txn = MathContract.constructor().transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(MATH_RUNTIME)


def test_contract_deployment_with_constructor_without_args(
    w3, SimpleConstructorContract, SIMPLE_CONSTRUCTOR_RUNTIME
):
    deploy_txn = SimpleConstructorContract.constructor().transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_RUNTIME)


def test_contract_deployment_with_constructor_with_arguments(
    w3, WithConstructorArgumentsContract, WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME
):
    deploy_txn = WithConstructorArgumentsContract.constructor(1234, "abcd").transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)


@pytest.mark.parametrize(
    "constructor_arg",
    (
        b"1234\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",  # noqa: E501
        constants.HASH_ZERO,
    ),
)
def test_contract_deployment_with_constructor_with_arguments_strict(
    w3,
    WithConstructorArgumentsContract,  # noqa: E501
    WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,  # noqa: E501
    constructor_arg,
):
    deploy_txn = WithConstructorArgumentsContract.constructor(
        1234, constructor_arg
    ).transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)


def test_contract_deployment_with_constructor_with_arguments_strict_error(
    WithConstructorArgumentsContract,  # noqa: E501
    WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
):  # noqa: E501
    with pytest.raises(
        TypeError,
        match="One or more arguments could not be encoded to the necessary ABI type. Expected types are: uint256, bytes32",  # noqa: E501
    ):
        WithConstructorArgumentsContract.constructor(1234, "abcd").transact()


def test_contract_deployment_with_constructor_with_address_argument(
    w3,
    WithConstructorAddressArgumentsContract,  # noqa: E501
    WITH_CONSTRUCTOR_ADDRESS_RUNTIME,
):  # noqa: E501
    deploy_txn = WithConstructorAddressArgumentsContract.constructor(
        "0x16D9983245De15E7A9A73bC586E01FF6E08dE737",
    ).transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)


@pytest.mark.asyncio
async def test_async_contract_deployment_no_constructor(
    async_w3, AsyncMathContract, MATH_RUNTIME
):
    deploy_txn = await AsyncMathContract.constructor().transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(MATH_RUNTIME)


@pytest.mark.asyncio
async def test_async_contract_deployment_with_constructor_without_args(
    async_w3, AsyncSimpleConstructorContract, SIMPLE_CONSTRUCTOR_RUNTIME
):
    deploy_txn = await AsyncSimpleConstructorContract.constructor().transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_RUNTIME)


@pytest.mark.asyncio
async def test_async_contract_deployment_with_constructor_with_arguments(
    async_w3, AsyncWithConstructorArgumentsContract, WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME
):
    deploy_txn = await AsyncWithConstructorArgumentsContract.constructor(
        1234, "abcd"
    ).transact()  # noqa: E501

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "constructor_arg",
    (
        b"1234\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",  # noqa: E501
        constants.HASH_ZERO,
    ),
)
async def test_async_contract_deployment_with_constructor_with_arguments_strict(
    async_w3,
    AsyncWithConstructorArgumentsContract,
    WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
    constructor_arg,
):

    deploy_txn = await AsyncWithConstructorArgumentsContract.constructor(
        1234, constructor_arg
    ).transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)


@pytest.mark.asyncio
async def test_async_contract_deployment_with_constructor_with_arguments_strict_error(
    AsyncWithConstructorArgumentsContract,
    WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
):
    with pytest.raises(
        TypeError,
        match="One or more arguments could not be encoded to the necessary ABI type. Expected types are: uint256, bytes32",  # noqa: E501
    ):
        await AsyncWithConstructorArgumentsContract.constructor(1234, "abcd").transact()


@pytest.mark.asyncio
async def test_async_contract_deployment_with_constructor_with_address_argument(
    async_w3,
    AsyncWithConstructorAddressArgumentsContract,  # noqa: E501
    WITH_CONSTRUCTOR_ADDRESS_RUNTIME,
):  # noqa: E501
    deploy_txn = await AsyncWithConstructorAddressArgumentsContract.constructor(
        "0x16D9983245De15E7A9A73bC586E01FF6E08dE737",
    ).transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)
