import pytest

from eth_utils import (
    decode_hex,
)

TEST_ADDRESS = '0x16D9983245De15E7A9A73bC586E01FF6E08dE737'
EXPECTED_DATA_A = 1234
EXPECTED_DATA_B = (b'abcd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                   b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')


def test_contract_constructor_abi_encoding_with_no_constructor_fn(MathContract, MATH_CODE):
    deploy_data = MathContract.constructor()._encode_data_in_transaction()
    assert deploy_data == MATH_CODE


def test_contract_constructor_gas_estimate_no_constructor(web3, MathContract):
    gas_estimate = MathContract.constructor().estimateGas()

    deploy_txn = MathContract.constructor().transact()
    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    gas_used = txn_receipt.get('gasUsed')

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_gas_estimate_with_constructor_without_arguments(
        web3,
        SimpleConstructorContract):
    gas_estimate = SimpleConstructorContract.constructor().estimateGas()

    deploy_txn = SimpleConstructorContract.constructor().transact()
    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    gas_used = txn_receipt.get('gasUsed')

    assert abs(gas_estimate - gas_used) < 21000


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
        web3,
        WithConstructorArgumentsContract,
        constructor_args,
        constructor_kwargs):
    gas_estimate = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs).estimateGas()

    deploy_txn = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs).transact()
    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    gas_used = txn_receipt.get('gasUsed')

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_gas_estimate_with_constructor_with_address_argument(
        web3,
        WithConstructorAddressArgumentsContract,
        address_conversion_func):
    gas_estimate = WithConstructorAddressArgumentsContract.constructor(
        address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")).estimateGas()

    deploy_txn = WithConstructorAddressArgumentsContract.constructor(
        address_conversion_func("0x16D9983245De15E7A9A73bC586E01FF6E08dE737")).transact()
    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    gas_used = txn_receipt.get('gasUsed')

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_constructor_transact_no_constructor(
        web3,
        MathContract,
        MATH_RUNTIME,
        address_conversion_func):
    deploy_txn = MathContract.constructor().transact()

    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = address_conversion_func(txn_receipt['contractAddress'])

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(MATH_RUNTIME)


def test_contract_constructor_transact_with_constructor_without_arguments(
        web3,
        SimpleConstructorContract,
        SIMPLE_CONSTRUCTOR_RUNTIME,
        address_conversion_func):
    deploy_txn = SimpleConstructorContract.constructor().transact()

    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = address_conversion_func(txn_receipt['contractAddress'])

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(SIMPLE_CONSTRUCTOR_RUNTIME)


@pytest.mark.parametrize(
    'constructor_args,constructor_kwargs, expected_a, expected_b',
    (
        ([1234, b'abcd'], {}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([1234], {'b': b'abcd'}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([], {'a': 1234, 'b': b'abcd'}, EXPECTED_DATA_A, EXPECTED_DATA_B),
        ([], {'b': b'abcd', 'a': 1234}, EXPECTED_DATA_A, EXPECTED_DATA_B),
    ),
)
def test_contract_constructor_transact_with_constructor_with_arguments(
        web3,
        WithConstructorArgumentsContract,
        WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
        constructor_args,
        constructor_kwargs,
        expected_a,
        expected_b,
        address_conversion_func):
    deploy_txn = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs).transact()

    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = address_conversion_func(txn_receipt['contractAddress'])

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME)
    assert expected_a == WithConstructorArgumentsContract(
        address=contract_address).functions.data_a().call()
    assert expected_b == WithConstructorArgumentsContract(
        address=contract_address).functions.data_b().call()


def test_contract_constructor_transact_with_constructor_with_address_arguments(
        web3,
        WithConstructorAddressArgumentsContract,
        WITH_CONSTRUCTOR_ADDRESS_RUNTIME,
        address_conversion_func):
    deploy_txn = WithConstructorAddressArgumentsContract.constructor(TEST_ADDRESS).transact()
    txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert txn_receipt is not None
    assert txn_receipt['contractAddress']
    contract_address = address_conversion_func(txn_receipt['contractAddress'])
    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)
    assert TEST_ADDRESS == WithConstructorAddressArgumentsContract(
        address=contract_address).functions.testAddr().call()


def test_contract_constructor_build_transaction_to_field_error(MathContract):
    with pytest.raises(ValueError):
        MathContract.constructor().buildTransaction({'to': '123'})


def test_contract_constructor_build_transaction_no_constructor(
        web3,
        MathContract,
        address_conversion_func):
    txn_hash = MathContract.constructor().transact(
        {'from': address_conversion_func(web3.eth.accounts[0])}
    )
    txn = web3.eth.getTransaction(txn_hash)
    nonce = web3.eth.getTransactionCount(web3.eth.coinbase)
    unsent_txn = MathContract.constructor().buildTransaction({'nonce': nonce})
    assert txn['data'] == unsent_txn['data']

    new_txn_hash = web3.eth.sendTransaction(unsent_txn)
    new_txn = web3.eth.getTransaction(new_txn_hash)
    assert new_txn['data'] == unsent_txn['data']
    assert new_txn['nonce'] == nonce


def test_contract_constructor_build_transaction_with_constructor_without_argument(
        web3,
        MathContract,
        address_conversion_func):
    txn_hash = MathContract.constructor().transact(
        {'from': address_conversion_func(web3.eth.accounts[0])}
    )
    txn = web3.eth.getTransaction(txn_hash)
    nonce = web3.eth.getTransactionCount(web3.eth.coinbase)
    unsent_txn = MathContract.constructor().buildTransaction({'nonce': nonce})
    assert txn['data'] == unsent_txn['data']

    new_txn_hash = web3.eth.sendTransaction(unsent_txn)
    new_txn = web3.eth.getTransaction(new_txn_hash)
    assert new_txn['data'] == unsent_txn['data']
    assert new_txn['nonce'] == nonce


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
        constructor_kwargs,
        address_conversion_func):
    txn_hash = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs).transact(
        {'from': address_conversion_func(web3.eth.accounts[0])}
    )
    txn = web3.eth.getTransaction(txn_hash)
    nonce = web3.eth.getTransactionCount(web3.eth.coinbase)
    unsent_txn = WithConstructorArgumentsContract.constructor(
        *constructor_args, **constructor_kwargs).buildTransaction({'nonce': nonce})
    assert txn['data'] == unsent_txn['data']

    new_txn_hash = web3.eth.sendTransaction(unsent_txn)
    new_txn = web3.eth.getTransaction(new_txn_hash)
    assert new_txn['data'] == unsent_txn['data']
    assert new_txn['nonce'] == nonce
