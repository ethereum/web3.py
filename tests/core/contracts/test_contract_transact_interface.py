# -*- coding: utf-8 -*-

import pytest

from eth_utils import (
    to_bytes,
)

from web3.utils.empty import (
    empty,
)

# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


@pytest.fixture()
def math_contract(web3, MathContract, address_conversion_func):
    deploy_txn = MathContract.constructor().transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    address = address_conversion_func(deploy_receipt['contractAddress'])
    _math_contract = MathContract(address=address)
    assert _math_contract.address == address
    return _math_contract


@pytest.fixture()
def string_contract(web3, StringContract, address_conversion_func):
    deploy_txn = StringContract.constructor("Caqalai").transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    address = address_conversion_func(deploy_receipt['contractAddress'])
    _string_contract = StringContract(address=address)
    assert _string_contract.address == address
    return _string_contract


@pytest.fixture()
def fallback_function_contract(web3, FallballFunctionContract, address_conversion_func):
    deploy_txn = FallballFunctionContract.constructor().transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    address = address_conversion_func(deploy_receipt['contractAddress'])
    _fallback_contract = FallballFunctionContract(address=address)
    assert _fallback_contract.address == address
    return _fallback_contract


@pytest.fixture()
def arrays_contract(web3, ArraysContract, address_conversion_func):
    # bytes_32 = [keccak('0'), keccak('1')]
    bytes32_array = [
        b'\x04HR\xb2\xa6p\xad\xe5@~x\xfb(c\xc5\x1d\xe9\xfc\xb9eB\xa0q\x86\xfe:\xed\xa6\xbb\x8a\x11m',  # noqa: E501
        b'\xc8\x9e\xfd\xaaT\xc0\xf2\x0cz\xdfa(\x82\xdf\tP\xf5\xa9Qc~\x03\x07\xcd\xcbLg/)\x8b\x8b\xc6',  # noqa: E501
    ]
    byte_arr = [b'\xff', b'\xff', b'\xff', b'\xff']
    deploy_txn = ArraysContract.constructor(bytes32_array, byte_arr).transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    address = address_conversion_func(deploy_receipt['contractAddress'])
    _arrays_contract = ArraysContract(address=address)
    return _arrays_contract


def test_transacting_with_contract_no_arguments(web3, math_contract, transact, call):
    initial_value = call(contract=math_contract,
                         contract_function='counter')

    txn_hash = transact(contract=math_contract,
                        contract_function='increment')
    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=math_contract,
                       contract_function='counter')

    assert final_value - initial_value == 1


@pytest.mark.parametrize(
    'transact_args,transact_kwargs',
    (
        ((5,), {}),
        (tuple(), {'amt': 5}),
    ),
)
def test_transacting_with_contract_with_arguments(web3,
                                                  math_contract,
                                                  transact,
                                                  call,
                                                  transact_args,
                                                  transact_kwargs):
    initial_value = call(contract=math_contract,
                         contract_function='counter')

    txn_hash = transact(contract=math_contract,
                        contract_function='increment',
                        func_args=transact_args,
                        func_kwargs=transact_kwargs)

    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=math_contract,
                       contract_function='counter')

    assert final_value - initial_value == 5


def test_deploy_when_default_account_is_set(web3,
                                            wait_for_transaction,
                                            STRING_CONTRACT):
    web3.eth.defaultAccount = web3.eth.accounts[1]
    assert web3.eth.defaultAccount is not empty

    StringContract = web3.eth.contract(**STRING_CONTRACT)

    deploy_txn = StringContract.constructor("Caqalai").transact()
    web3.eth.waitForTransactionReceipt(deploy_txn)
    txn_after = web3.eth.getTransaction(deploy_txn)
    assert txn_after['from'] == web3.eth.defaultAccount


def test_transact_when_default_account_is_set(web3,
                                              wait_for_transaction,
                                              math_contract,
                                              transact):
    web3.eth.defaultAccount = web3.eth.accounts[1]
    assert web3.eth.defaultAccount is not empty

    txn_hash = transact(contract=math_contract,
                        contract_function='increment')
    wait_for_transaction(web3, txn_hash)
    txn_after = web3.eth.getTransaction(txn_hash)
    assert txn_after['from'] == web3.eth.defaultAccount


def test_transacting_with_contract_with_string_argument(web3, string_contract, transact, call):
    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = transact(contract=string_contract,
                        contract_function='setValue',
                        func_args=["ÄLÄMÖLÖ".encode('utf8')])
    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=string_contract,
                       contract_function='getValue')

    assert final_value == "ÄLÄMÖLÖ"


def test_transacting_with_contract_with_bytes32_array_argument(web3,
                                                               arrays_contract,
                                                               transact,
                                                               call):
    # new_bytes32_array = [keccak('1'), keccak('2'), keccak('3')]
    new_bytes32_array = [
        b'\xc8\x9e\xfd\xaaT\xc0\xf2\x0cz\xdfa(\x82\xdf\tP\xf5\xa9Qc~\x03\x07\xcd\xcbLg/)\x8b\x8b\xc6',  # noqa: E501
        b'\xad|[\xef\x02x\x16\xa8\x00\xda\x176DO\xb5\x8a\x80~\xf4\xc9`;xHg?~:h\xeb\x14\xa5',
        b"*\x80\xe1\xef\x1dxB\xf2\x7f.k\xe0\x97+\xb7\x08\xb9\xa15\xc3\x88`\xdb\xe7<'\xc3Hl4\xf4\xde",  # noqa: E501
    ]
    txn_hash = transact(contract=arrays_contract,
                        contract_function="setBytes32Value",
                        func_args=[new_bytes32_array])
    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=arrays_contract,
                       contract_function="getBytes32Value")
    assert final_value == new_bytes32_array


def test_transacting_with_contract_with_byte_array_argument(web3, arrays_contract, transact, call):
    new_byte_array = [b'\x03', b'\x03', b'\x03', b'\x03', b'\x03', b'\x03']
    txn_hash = transact(contract=arrays_contract,
                        contract_function='setByteValue',
                        func_args=[new_byte_array])
    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=arrays_contract,
                       contract_function='getByteValue')
    assert final_value == new_byte_array


def test_transacting_with_contract_respects_explicit_gas(web3,
                                                         STRING_CONTRACT,
                                                         skip_if_testrpc,
                                                         wait_for_block,
                                                         call,
                                                         transact):
    skip_if_testrpc(web3)

    wait_for_block(web3)

    StringContract = web3.eth.contract(**STRING_CONTRACT)

    deploy_txn = StringContract.constructor("Caqalai").transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn, 30)
    assert deploy_receipt is not None
    string_contract = StringContract(address=deploy_receipt['contractAddress'])

    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = transact(contract=string_contract,
                        contract_function='setValue',
                        func_args=[to_bytes(text="ÄLÄMÖLÖ")],
                        tx_kwargs={'gas': 200000})
    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash, 30)
    assert txn_receipt is not None

    final_value = call(contract=string_contract,
                       contract_function='getValue')
    assert to_bytes(text=final_value) == to_bytes(text="ÄLÄMÖLÖ")

    txn = web3.eth.getTransaction(txn_hash)
    assert txn['gas'] == 200000


def test_auto_gas_computation_when_transacting(web3,
                                               STRING_CONTRACT,
                                               skip_if_testrpc,
                                               wait_for_block,
                                               call,
                                               transact):
    skip_if_testrpc(web3)

    wait_for_block(web3)

    StringContract = web3.eth.contract(**STRING_CONTRACT)

    deploy_txn = StringContract.constructor("Caqalai").transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn, 30)
    assert deploy_receipt is not None
    string_contract = StringContract(address=deploy_receipt['contractAddress'])

    gas_estimate = string_contract.functions.setValue(to_bytes(text="ÄLÄMÖLÖ")).estimateGas()

    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = transact(contract=string_contract,
                        contract_function="setValue",
                        func_args=[to_bytes(text="ÄLÄMÖLÖ")])
    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash, 30)
    assert txn_receipt is not None

    final_value = call(contract=string_contract,
                       contract_function='getValue')
    assert to_bytes(text=final_value) == to_bytes(text="ÄLÄMÖLÖ")

    txn = web3.eth.getTransaction(txn_hash)
    assert txn['gas'] == gas_estimate + 100000


def test_fallback_transacting_with_contract(web3, fallback_function_contract, call):
    initial_value = call(contract=fallback_function_contract,
                         contract_function='getData')
    txn_hash = fallback_function_contract.fallback.transact()
    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = call(contract=fallback_function_contract,
                       contract_function='getData')

    assert final_value - initial_value == 1
