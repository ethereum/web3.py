import pytest

from eth_utils import (
    decode_hex,
)

from web3 import (
    constants,
)
from web3._utils.contract_sources.contract_data.constructor_contracts import (
    CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME,
    CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME,
    SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME,
)


def test_contract_deployment_no_constructor(
    w3, math_contract_factory, math_contract_runtime
):
    deploy_txn = math_contract_factory.constructor().transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(math_contract_runtime)


def test_contract_deployment_with_constructor_without_args(
    w3,
    simple_constructor_contract_factory,
):
    deploy_txn = simple_constructor_contract_factory.constructor().transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME)


@pytest.mark.parametrize(
    "constructor_arg",
    (
        b"1234\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",  # noqa: E501
        constants.HASH_ZERO,
    ),
)
def test_contract_deployment_with_constructor_with_arguments_strict_by_default(
    w3,
    contract_with_constructor_args_factory,
    constructor_arg,
):
    deploy_txn = contract_with_constructor_args_factory.constructor(
        1234, constructor_arg
    ).transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME)


def test_contract_deployment_with_constructor_with_arguments_non_strict(
    w3_non_strict_abi,
    non_strict_contract_with_constructor_args_factory,
):
    deploy_txn = non_strict_contract_with_constructor_args_factory.constructor(
        1234, "abcd"
    ).transact()

    txn_receipt = w3_non_strict_abi.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3_non_strict_abi.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME)


def test_contract_deployment_with_constructor_with_arguments_strict_error(
    contract_with_constructor_args_factory,
):
    with pytest.raises(
        TypeError,
        match="One or more arguments could not be encoded to the necessary ABI type. Expected types are: uint256, bytes32",  # noqa: E501
    ):
        contract_with_constructor_args_factory.constructor(1234, "abcd").transact()


def test_contract_deployment_with_constructor_with_address_argument(
    w3,
    contract_with_constructor_address_factory,
):
    deploy_txn = contract_with_constructor_address_factory.constructor(
        "0x16D9983245De15E7A9A73bC586E01FF6E08dE737",
    ).transact()

    txn_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(
        CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME
    )


@pytest.mark.asyncio
async def test_async_contract_deployment_no_constructor(
    async_w3, async_math_contract_factory, math_contract_runtime
):
    deploy_txn = await async_math_contract_factory.constructor().transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(math_contract_runtime)


@pytest.mark.asyncio
async def test_async_contract_deployment_with_constructor_no_args(
    async_w3,
    async_simple_constructor_contract_factory,
):
    deploy_txn = (
        await async_simple_constructor_contract_factory.constructor().transact()
    )

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "constructor_arg",
    (
        b"1234\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",  # noqa: E501
        constants.HASH_ZERO,
    ),
)
async def test_async_contract_deployment_with_constructor_arguments(
    async_w3,
    async_constructor_with_args_contract_factory,
    constructor_arg,
):
    deploy_txn = await async_constructor_with_args_contract_factory.constructor(
        1234, constructor_arg
    ).transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME)


@pytest.mark.asyncio
async def test_async_contract_deployment_with_constructor_with_arguments_non_strict(
    async_w3_non_strict_abi,
    async_non_strict_constructor_with_args_contract_factory,
):
    deploy_txn = (
        await async_non_strict_constructor_with_args_contract_factory.constructor(
            1234, "abcd"
        ).transact()
    )

    txn_receipt = await async_w3_non_strict_abi.eth.wait_for_transaction_receipt(
        deploy_txn
    )
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3_non_strict_abi.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME)


@pytest.mark.asyncio
async def test_async_contract_deployment_with_constructor_arguments_strict_error(
    async_constructor_with_args_contract_factory,
):
    with pytest.raises(
        TypeError,
        match="One or more arguments could not be encoded to the necessary ABI type. Expected types are: uint256, bytes32",  # noqa: E501
    ):
        await async_constructor_with_args_contract_factory.constructor(
            1234, "abcd"
        ).transact()


@pytest.mark.asyncio
async def test_async_contract_deployment_with_constructor_with_address_argument(
    async_w3,
    async_constructor_with_address_arg_contract_factory,
):
    deploy_txn = await async_constructor_with_address_arg_contract_factory.constructor(
        "0x16D9983245De15E7A9A73bC586E01FF6E08dE737",
    ).transact()

    txn_receipt = await async_w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt["contractAddress"]
    contract_address = txn_receipt["contractAddress"]

    blockchain_code = await async_w3.eth.get_code(contract_address)
    assert blockchain_code == decode_hex(
        CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME
    )
