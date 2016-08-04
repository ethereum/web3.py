# -*- coding: utf-8 -*-

import pytest


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


@pytest.fixture()
def address_contract(web3_tester, WithConstructorAddressArgumentsContract):
    deploy_txn = WithConstructorAddressArgumentsContract.deploy(arguments=[
        "0xd3cda913deb6f67967b99d67acdfa1712c293601",
    ])
    deploy_receipt = web3_tester.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _address_contract = WithConstructorAddressArgumentsContract(address=deploy_receipt['contractAddress'])
    return _address_contract


def test_call_with_no_arguments(math_contract):
    result = math_contract.call().return13()
    assert result == 13


def test_call_with_one_argument(math_contract):
    result = math_contract.call().multiply7(3)
    assert result == 21


def test_call_with_multiple_arguments(math_contract):
    result = math_contract.call().add(9, 7)
    assert result == 16


def test_call_get_string_value(string_contract):
    result = string_contract.call().getValue()
    # eth_abi.decode_api() does not assume implicit utf-8
    # encoding of string return values. Thus, we need to decode
    # ourselves for fair comparison.
    assert result == "Caqalai"


def test_call_read_string_variable(string_contract):
    result = string_contract.call().constString()
    assert result == "ToholampiÅÄÖ"


def test_call_read_address_variable(address_contract):
    result = address_contract.call().testAddr()
    assert result == "0xd3cda913deb6f67967b99d67acdfa1712c293601"
