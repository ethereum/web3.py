import pytest

from eth_utils import (
    decode_hex,
)
from web3 import (
    Account,
    Web3,
)

# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")

@pytest.fixture(params=['instance', 'class'])
def acct(request, web3):
    if request.param == 'instance':
        return web3.eth.account
    elif request.param == 'class':
        return Account
    raise Exception('Unreachable!')


'''def test_contract_constructor_transact_no_constructor(web3, MathContract,
                                             MATH_RUNTIME):
    deploy_txn = MathContract.constructor().transact()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(MATH_RUNTIME)


def test_contract_constructor_transact_with_constructor_without_args(web3,
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


def test_contract_constructor_transact_with_constructor_with_address_argument(web3,
                                                                     WithConstructorAddressArgumentsContract,
                                                                     # noqa: E501
                                                                     WITH_CONSTRUCTOR_ADDRESS_RUNTIME):  # noqa: E501
    deploy_txn = WithConstructorAddressArgumentsContract.constructor(
        args=["0x16D9983245De15E7A9A73bC586E01FF6E08dE737"],
    ).transact()

    txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert txn_receipt is not None

    assert txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']

    blockchain_code = web3.eth.getCode(contract_address)
    assert blockchain_code == decode_hex(WITH_CONSTRUCTOR_ADDRESS_RUNTIME)


def test_contract_constructor_gas_estimate_no_constructor(web3, MathContract,
                                                          MATH_RUNTIME):
    gas_estimate = MathContract.constructor().estimateGas()

    assert isinstance(gas_estimate, int)  # Assert Estimate is an int


def test_contract_constructor_gas_estimate_with_constructor_without_args(web3,
                                                                         SimpleConstructorContract,
                                                                         SIMPLE_CONSTRUCTOR_RUNTIME):
    gas_estimate = SimpleConstructorContract.constructor().estimateGas()

    assert isinstance(gas_estimate, int)  # Assert Estimate is an int


def test_contract_constructor_gas_estimate_with_constructor_with_arguments(web3,
                                                                           WithConstructorArgumentsContract,
                                                                           WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME):
    gas_estimate = WithConstructorArgumentsContract.constructor(args=[1234, 'abcd']).estimateGas()

    assert isinstance(gas_estimate, int)  # Assert Estimate is an int


def test_contract_constructor_gas_estimate_with_constructor_with_address_argument(web3,
                                                                                  WithConstructorAddressArgumentsContract,
                                                                                  # noqa: E501
                                                                                  WITH_CONSTRUCTOR_ADDRESS_RUNTIME):  # noqa: E501

    gas_estimate = WithConstructorAddressArgumentsContract.constructor(
        args=["0x16D9983245De15E7A9A73bC586E01FF6E08dE737"],
    ).estimateGas()

    assert isinstance(gas_estimate, int)  # Assert Estimate is an int

def test_contract_constructor_build_transaction_to_field_error(MathContract):
    try:

        MathContract.constructor().buildTransaction({'to': ''})

    except Exception as error:
        assert str(error) == "Cannot set to in constructor transaction"

def test_contract_constructor_build_transaction_nonce_field_error(MathContract):
    try:

        MathContract.constructor().buildTransaction({'nonce': ''})

    except Exception as error:
        assert str(error) == "Only the keys 'data/from/gas/gas_price/to/value' are allowed.  Got extra keys: 'nonce'"

def test_contract_constructor_build_transaction_sign_error(MathContract, acct):
    try:

        key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
        _txn = MathContract.constructor().buildTransaction()
        acct.signTransaction(_txn, key)

    except Exception as error:
        assert str(error) == "Not all fields initialized"'''



def test_contract_constructor_build_transaction_no_constructor(MathContract, web3, acct):

    _txn = MathContract.constructor().buildTransaction()

    print(_txn)

    txn_hash = MathContract.constructor().transact({'from': web3.eth.accounts[0]})
    txn = web3.eth.getTransaction(txn_hash)

    #print(txn)

    assert txn['data'] == _txn['data'] # Assert transact Data == buildTransaction Data

    #key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'

    #signed = acct.signTransaction(_txn, key)

    #print(signed)
