
import pytest

from eth_utils import (
    decode_hex,
)


def test_contract_deployment_no_constructor(web3, MathContract,
                                            MATH_RUNTIME):
    deploy_txn = MathContract.constructor().transact()

    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(MATH_RUNTIME)


def test_contract_deployment_with_constructor_without_args(web3,
                                                           SimpleConstructorContract,
                                                           SIMPLE_CONSTRUCTOR_RUNTIME):
    deploy_txn = SimpleConstructorContract.constructor().transact()

    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_RUNTIME)


def test_contract_deployment_with_constructor_with_arguments(web3,
                                                             WithConstructorArgumentsContract,
                                                             WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME):
    with pytest.warns(
        DeprecationWarning,
        match='in v6 it will be invalid to pass a hex string without the "0x" prefix'
    ):
        deploy_txn = WithConstructorArgumentsContract.constructor(1234, 'abcd').transact()

        txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
        assert txn_receipt is not None

        assert txn_receipt['contractAddress']
        contract_address = txn_receipt['contractAddress']

        blockchain_code = web3.eth.getCode(contract_address)
        assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)


@pytest.mark.parametrize('constructor_arg', (
    b'1234\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',  # noqa: E501
    '0x0000000000000000000000000000000000000000000000000000000000000000')
)
def test_contract_deployment_with_constructor_with_arguments_strict(w3_strict_abi,
                                                                    WithConstructorArgumentsContractStrict,  # noqa: E501
                                                                    WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,  # noqa: E501
                                                                    constructor_arg):
    deploy_txn = WithConstructorArgumentsContractStrict.constructor(
        1234, constructor_arg
    ).transact()

    txn_receipt = w3_strict_abi.eth.waitForTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = w3_strict_abi.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)


def test_contract_deployment_with_constructor_with_arguments_strict_error(w3_strict_abi,
                                                                          WithConstructorArgumentsContractStrict,  # noqa: E501
                                                                          WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME):  # noqa: E501
    with pytest.raises(
        TypeError,
        match="One or more arguments could not be encoded to the necessary ABI type.  Expected types are: uint256, bytes32"  # noqa: E501
    ):
        WithConstructorArgumentsContractStrict.constructor(1234, 'abcd').transact()


def test_contract_deployment_with_constructor_with_address_argument(web3,
                                                                    WithConstructorAddressArgumentsContract,  # noqa: E501
                                                                    WITH_CONSTRUCTOR_ADDRESS_RUNTIME):  # noqa: E501
    deploy_txn = WithConstructorAddressArgumentsContract.constructor(
        "0x16D9983245De15E7A9A73bC586E01FF6E08dE737",
    ).transact()

    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)
