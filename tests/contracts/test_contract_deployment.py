from web3.utils.string import force_bytes


def test_contract_deployment_no_constructor(web3_tester, MathContract,
                                            MATH_RUNTIME):
    deploy_txn = MathContract.deploy()

    txn_receipt = web3_tester.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3_tester.eth.getCode(contract_address)
    assert force_bytes(blockchain_code) == force_bytes(MATH_RUNTIME)


def test_contract_deployment_with_constructor_without_args(web3_tester,
                                                           SimpleConstructorContract,
                                                           SIMPLE_CONSTRUCTOR_RUNTIME):
    deploy_txn = SimpleConstructorContract.deploy()

    txn_receipt = web3_tester.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3_tester.eth.getCode(contract_address)
    assert force_bytes(blockchain_code) == force_bytes(SIMPLE_CONSTRUCTOR_RUNTIME)


def test_contract_deployment_with_constructor_with_arguments(web3_tester,
                                                             WithConstructorArgumentsContract,
                                                             WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME):
    deploy_txn = WithConstructorArgumentsContract.deploy(arguments=[1234, 'abcd'])

    txn_receipt = web3_tester.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3_tester.eth.getCode(contract_address)
    assert force_bytes(blockchain_code) == force_bytes(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)
