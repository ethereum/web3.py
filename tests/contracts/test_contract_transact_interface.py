# -*- coding: utf-8 -*-

import pytest

from eth_utils import (
    force_text,
    force_bytes,
)

from web3.utils.empty import (
    empty,
)
from web3.utils.transactions import (
    wait_for_transaction_receipt,
)


@pytest.fixture()
def math_contract(web3, MathContract):
    deploy_txn = MathContract.deploy()
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _math_contract = MathContract(address=deploy_receipt['contractAddress'])
    return _math_contract


@pytest.fixture()
def string_contract(web3, StringContract):
    deploy_txn = StringContract.deploy(args=["Caqalai"])
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _math_contract = StringContract(address=deploy_receipt['contractAddress'])
    return _math_contract


def test_transacting_with_contract_no_arguments(web3, math_contract):
    initial_value = math_contract.call().counter()

    txn_hash = math_contract.transact().increment()
    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = math_contract.call().counter()

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
                                                  transact_args,
                                                  transact_kwargs):
    initial_value = math_contract.call().counter()

    txn_hash = math_contract.transact().increment(*transact_args, **transact_kwargs)
    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = math_contract.call().counter()

    assert final_value - initial_value == 5


def test_deploy_when_default_account_is_set(web3,
                                            wait_for_transaction,
                                            STRING_CONTRACT):
    web3.eth.defaultAccount = web3.eth.accounts[1]
    assert web3.eth.defaultAccount is not empty

    StringContract = web3.eth.contract(**STRING_CONTRACT)

    deploy_txn = StringContract.deploy(args=["Caqalai"])
    wait_for_transaction(web3, deploy_txn)
    txn_after = web3.eth.getTransaction(deploy_txn)
    assert txn_after['from'] == web3.eth.defaultAccount


def test_transact_when_default_account_is_set(web3,
                                              wait_for_transaction,
                                              math_contract):
    web3.eth.defaultAccount = web3.eth.accounts[1]
    assert web3.eth.defaultAccount is not empty

    txn_hash = math_contract.transact().increment()
    wait_for_transaction(web3, txn_hash)
    txn_after = web3.eth.getTransaction(txn_hash)
    assert txn_after['from'] == web3.eth.defaultAccount


def test_transacting_with_contract_with_string_argument(web3, string_contract):
    # eth_abi will pass as raw bytes, no encoding
    # unless we encode ourselves
    txn_hash = string_contract.transact().setValue(force_bytes("ÄLÄMÖLÖ"))
    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
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

    deploy_txn = StringContract.deploy(args=["Caqalai"])
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

    deploy_txn = StringContract.deploy(args=["Caqalai"])
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
    assert txn['gas'] == gas_estimate + 100000
