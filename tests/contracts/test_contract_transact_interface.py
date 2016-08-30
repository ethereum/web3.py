# -*- coding: utf-8 -*-

import pytest

from web3.utils.transactions import (
    wait_for_transaction_receipt,
)
from web3.utils.string import (
    force_text,
    force_bytes,
)


@pytest.fixture()
def math_contract(web3_tester, MathContract):
    deploy_txn = MathContract.deploy()
    deploy_receipt = web3_tester.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _math_contract = MathContract(address=deploy_receipt['contractAddress'])
    return _math_contract


@pytest.fixture()
def string_contract(web3_tester, StringContract):
    deploy_txn = StringContract.deploy(arguments=["Caqalai"])
    deploy_receipt = web3_tester.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _math_contract = StringContract(address=deploy_receipt['contractAddress'])
    return _math_contract


def test_transacting_with_contract_no_arguments(web3_tester, math_contract):
    initial_value = math_contract.call().counter()

    txn_hash = math_contract.transact().increment()
    txn_receipt = web3_tester.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = math_contract.call().counter()

    assert final_value - initial_value == 1


def test_transacting_with_contract_with_arguments(web3_tester, math_contract):
    initial_value = math_contract.call().counter()

    txn_hash = math_contract.transact().increment(5)
    txn_receipt = web3_tester.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = math_contract.call().counter()

    assert final_value - initial_value == 5


def test_transacting_with_contract_with_string_argument(web3_tester, string_contract):
    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = string_contract.transact().setValue(force_bytes("ÄLÄMÖLÖ"))
    txn_receipt = web3_tester.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = string_contract.call().getValue()

    assert force_bytes(final_value) == force_bytes("ÄLÄMÖLÖ")


def test_transacting_with_contract_with_string_argument(web3_tester, string_contract):

    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = string_contract.transact().setValue(force_bytes("ÄLÄMÖLÖ"))
    txn_receipt = web3_tester.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = string_contract.call().getValue()

    assert force_bytes(final_value) == force_bytes("ÄLÄMÖLÖ")


def test_transacting_with_contract_respects_explicit_gas(web3,
                                                         STRING_CONTRACT,
                                                         skip_if_testrpc,
                                                         wait_for_block):
    skip_if_testrpc(web3)

    wait_for_block(web3)

    StringContract = web3.eth.contract(**STRING_CONTRACT)

    deploy_txn = StringContract.deploy(arguments=["Caqalai"])
    deploy_receipt = wait_for_transaction_receipt(web3, deploy_txn, 30)
    assert deploy_receipt is not None
    string_contract = StringContract(address=deploy_receipt['contractAddress'])

    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = string_contract.transact({'gas': 200000}).setValue(force_bytes("ÄLÄMÖLÖ"))
    txn_receipt = wait_for_transaction_receipt(web3, txn_hash, 30)
    assert txn_receipt is not None

    final_value = string_contract.call().getValue()
    assert force_bytes(final_value) == force_bytes("ÄLÄMÖLÖ")

    txn = web3.eth.getTransaction(txn_hash)
    assert txn['gas'] == 200000


def test_auto_gas_computation_when_transacting(web3,
                                               STRING_CONTRACT,
                                               skip_if_testrpc,
                                               wait_for_block):
    skip_if_testrpc(web3)

    wait_for_block(web3)

    StringContract = web3.eth.contract(**STRING_CONTRACT)

    deploy_txn = StringContract.deploy(arguments=["Caqalai"])
    deploy_receipt = wait_for_transaction_receipt(web3, deploy_txn, 30)
    assert deploy_receipt is not None
    string_contract = StringContract(address=deploy_receipt['contractAddress'])

    gas_estimate = string_contract.estimateGas().setValue(force_bytes("ÄLÄMÖLÖ"))

    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = string_contract.transact().setValue(force_bytes("ÄLÄMÖLÖ"))
    txn_receipt = wait_for_transaction_receipt(web3, txn_hash, 30)
    assert txn_receipt is not None

    final_value = string_contract.call().getValue()
    assert force_bytes(final_value) == force_bytes("ÄLÄMÖLÖ")

    txn = web3.eth.getTransaction(txn_hash)
    assert txn['gas'] == gas_estimate + string_contract.gas_buffer
