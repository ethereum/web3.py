from eth_utils import decode_hex


def test_contract_constructor_abi_encoding_with_no_constructor_fn(MathContract, MATH_CODE):
    deploy_data = MathContract.constructor()._encode_data_in_transaction()
    assert deploy_data == MATH_CODE


def test_contract_constructor_gas_estimate_no_constructor(MathContract):
    gas_estimate = MathContract.constructor().estimateGas()
    # How are the expected value calculated?
    try:
        assert abs(gas_estimate - 21472) < 200  # Geth
    except AssertionError:
        # assert abs(gas_estimate - 29910) < 200  # eth-tester with py-evm
        assert abs(gas_estimate - 200361) < 200  # eth-tester with py-evm


def test_contract_constructor_gas_estimate_with_constructor_without_arguments(SimpleConstructorContract):
    gas_estimate = SimpleConstructorContract.constructor().estimateGas()
    try:
        assert abs(gas_estimate - 21472) < 200  # Geth
    except AssertionError:
        # assert abs(gas_estimate - 29910) < 200  # eth-tester with py-evm
        assert abs(gas_estimate - 85734) < 200  # eth-tester with py-evm


def test_contract_constructor_gas_estimate_with_constructor_with_arguments(WithConstructorArgumentsContract):
    gas_estimate = WithConstructorArgumentsContract.constructor(args=[1234, 'abcd']).estimateGas()
    try:
        assert abs(gas_estimate - 21472) < 200  # Geth
    except AssertionError:
        # assert abs(gas_estimate - 29910) < 200  # eth-tester with py-evm
        assert abs(gas_estimate - 112486) < 200


def test_contract_constructor_gas_estimate_with_constructor_with_address_argument(
        WithConstructorAddressArgumentsContract # noqa: E501
    ):
    gas_estimate = WithConstructorAddressArgumentsContract.constructor(
        args=["0x16D9983245De15E7A9A73bC586E01FF6E08dE737"],
    ).estimateGas()
    try:
        assert abs(gas_estimate - 21472) < 200  # Geth
    except AssertionError:
        # assert abs(gas_estimate - 29910) < 200  # eth-tester with py-evm
        assert abs(gas_estimate - 95439) < 200


def test_contract_constructor_transact_no_constructor(web3, MathContract, MATH_RUNTIME):
    deploy_txn = MathContract.constructor().transact()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(MATH_RUNTIME)


def test_contract_constructor_transact_with_constructor_without_arguments(web3,
                                                                          SimpleConstructorContract,
                                                                          SIMPLE_CONSTRUCTOR_RUNTIME):
    deploy_txn = SimpleConstructorContract.constructor().transact()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_RUNTIME)


def test_contract_constructor_transact_with_constructor_with_arguments(web3,
                                                                       WithConstructorArgumentsContract,
                                                                       WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME):
    deploy_txn = WithConstructorArgumentsContract.constructor(args=[1234, 'abcd']).transact()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)


def test_contract_constructor_transact_with_constructor_with_address_arguments(web3,
                                                                               WithConstructorAddressArgumentsContract,
                                                                               WITH_CONSTRUCTOR_ADDRESS_RUNTIME):
    deploy_txn = WithConstructorAddressArgumentsContract.constructor(
        args=['0x16D9983245De15E7A9A73bC586E01FF6E08dE737']
    ).transact()
    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None
    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']
    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)
