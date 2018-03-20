import pytest

from eth_utils import (
    decode_hex,
)


def test_contract_constructor_abi_encoding_with_no_constructor_fn(MathContract, MATH_CODE):
    deploy_data = MathContract.constructor()._encode_data_in_transaction()
    assert deploy_data == MATH_CODE


def test_contract_constructor_gas_estimate_no_constructor(MathContract):
    gas_estimate = MathContract.constructor().estimateGas()
    try:
        assert abs(gas_estimate - 21472) < 200  # Geth
    except AssertionError:
        assert abs(gas_estimate - 200321) < 200  # eth-tester with py-evm


def test_contract_constructor_gas_estimate_with_constructor_without_arguments(
        SimpleConstructorContract):
    gas_estimate = SimpleConstructorContract.constructor().estimateGas()
    try:
        assert abs(gas_estimate - 21472) < 200  # Geth
    except AssertionError:
        assert abs(gas_estimate - 85694) < 200  # eth-tester with py-evm


@pytest.mark.parametrize(
    'constructor_args,constructor_kwargs',
    (
        ([1234, b'abcd'], {}),
        ([1234], {'b': b'abcd'}),
        ([], {'a': 1234, 'b': b'abcd'}),
        ([], {'b': b'abcd', 'a': 1234}),
    ),
)
def test_contract_constructor_gas_estimate_with_constructor_with_arguments(
        WithConstructorArgumentsContract,
        constructor_args,
        constructor_kwargs):
    gas_estimate = WithConstructorArgumentsContract.constructor(
        constructor_args, constructor_kwargs).estimateGas()
    try:
        assert abs(gas_estimate - 21472) < 200  # Geth
    except AssertionError:
        assert abs(gas_estimate - 112574) < 200  # eth-tester with py-evm


def test_contract_constructor_gas_estimate_with_constructor_with_address_argument(
        WithConstructorAddressArgumentsContract):
    gas_estimate = WithConstructorAddressArgumentsContract.constructor(
        args=["0x16D9983245De15E7A9A73bC586E01FF6E08dE737"],
    ).estimateGas()
    try:
        assert abs(gas_estimate - 21472) < 200  # Geth
    except AssertionError:
        assert abs(gas_estimate - 95399) < 200  # eth-tester with py-evm


def test_contract_constructor_transact_no_constructor(web3, MathContract, MATH_RUNTIME):
    deploy_txn = MathContract.constructor().transact()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(MATH_RUNTIME)


def test_contract_constructor_transact_with_constructor_without_arguments(
        web3, SimpleConstructorContract, SIMPLE_CONSTRUCTOR_RUNTIME):
    deploy_txn = SimpleConstructorContract.constructor().transact()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_RUNTIME)


@pytest.mark.parametrize(
    'constructor_args,constructor_kwargs',
    (
        ([1234, b'abcd'], {}),
        ([1234], {'b': b'abcd'}),
        ([], {'a': 1234, 'b': b'abcd'}),
        ([], {'b': b'abcd', 'a': 1234}),
    ),
)
def test_contract_constructor_transact_with_constructor_with_arguments(
        web3,
        WithConstructorArgumentsContract,
        WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
        constructor_args,
        constructor_kwargs):
    deploy_txn = WithConstructorArgumentsContract.constructor(
        constructor_args, constructor_kwargs).transact()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)


def test_contract_constructor_transact_with_constructor_with_address_arguments(
        web3, WithConstructorAddressArgumentsContract, WITH_CONSTRUCTOR_ADDRESS_RUNTIME):
    deploy_txn = WithConstructorAddressArgumentsContract.constructor(
        args=['0x16D9983245De15E7A9A73bC586E01FF6E08dE737']
    ).transact()
    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None
    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']
    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)


def test_contract_constructor_build_transaction_to_field_error(MathContract):
    with pytest.raises(ValueError):
        MathContract.constructor().buildTransaction({'to': '123'})


def test_contract_constructor_build_transaction_nonce_field_error(MathContract):
    with pytest.raises(ValueError):
        MathContract.constructor().buildTransaction({'nonce': '123'})


def test_contract_constructor_build_transaction_no_constructor(web3, MathContract):
    txn_hash = MathContract.constructor().transact({'from': web3.eth.accounts[0]})
    txn = web3.eth.getTransaction(txn_hash)
    unsent_txn = MathContract.constructor().buildTransaction()
    assert txn['data'] == unsent_txn['data']

    new_txn_hash = web3.eth.sendTransaction(unsent_txn)
    new_txn = web3.eth.getTransaction(new_txn_hash)
    assert new_txn['data'] == unsent_txn['data']


def test_contract_constructor_build_transaction_with_constructor_without_argument(web3,
                                                                                  MathContract):
    txn_hash = MathContract.constructor().transact({'from': web3.eth.accounts[0]})
    txn = web3.eth.getTransaction(txn_hash)
    unsent_txn = MathContract.constructor().buildTransaction()
    assert txn['data'] == unsent_txn['data']

    new_txn_hash = web3.eth.sendTransaction(unsent_txn)
    new_txn = web3.eth.getTransaction(new_txn_hash)
    assert new_txn['data'] == unsent_txn['data']


@pytest.mark.parametrize(
    'constructor_args,constructor_kwargs',
    (
        ([1234, b'abcd'], {}),
        ([1234], {'b': b'abcd'}),
        ([], {'a': 1234, 'b': b'abcd'}),
        ([], {'b': b'abcd', 'a': 1234}),
    ),
)
def test_contract_constructor_build_transaction_with_constructor_with_argument(
        web3,
        WithConstructorArgumentsContract,
        constructor_args,
        constructor_kwargs):
    txn_hash = WithConstructorArgumentsContract.constructor(
        constructor_args, constructor_kwargs).transact({'from': web3.eth.accounts[0]})
    txn = web3.eth.getTransaction(txn_hash)
    unsent_txn = WithConstructorArgumentsContract.constructor(
        constructor_args, constructor_kwargs).buildTransaction()
    assert txn['data'] == unsent_txn['data']

    new_txn_hash = web3.eth.sendTransaction(unsent_txn)
    new_txn = web3.eth.getTransaction(new_txn_hash)
    assert new_txn['data'] == unsent_txn['data']
