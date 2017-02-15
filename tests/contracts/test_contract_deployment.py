from eth_utils import (
    force_bytes,
)


def test_contract_deployment_no_constructor(web3, MathContract,
                                            MATH_RUNTIME):
    deploy_txn = MathContract.deploy()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert force_bytes(blockchain_code) == force_bytes(MATH_RUNTIME)


def test_contract_deployment_with_constructor_without_args(web3,
                                                           SimpleConstructorContract,
                                                           SIMPLE_CONSTRUCTOR_RUNTIME):
    deploy_txn = SimpleConstructorContract.deploy()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert force_bytes(blockchain_code) == force_bytes(SIMPLE_CONSTRUCTOR_RUNTIME)


def test_contract_deployment_with_constructor_with_arguments(web3,
                                                             WithConstructorArgumentsContract,
                                                             WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME):
    deploy_txn = WithConstructorArgumentsContract.deploy(args=[1234, 'abcd'])

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert force_bytes(blockchain_code) == force_bytes(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)


def test_contract_deployment_with_constructor_with_address_argument(web3,
                                                                    WithConstructorAddressArgumentsContract,
                                                                    WITH_CONSTRUCTOR_ADDRESS_RUNTIME):
    deploy_txn = WithConstructorAddressArgumentsContract.deploy(args=["0x16d9983245de15e7a9a73bc586e01ff6e08de737"])

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert force_bytes(blockchain_code) == force_bytes(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)
