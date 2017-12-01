# -*- coding: utf-8 -*-

import pytest

# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


@pytest.fixture()
def math_contract(web3, MathContract):
    deploy_txn = MathContract.deploy()
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _math_contract = MathContract(address=deploy_receipt['contractAddress'])
    return _math_contract


def test_prepare_transaction_with_contract_no_arguments(web3, math_contract):
    txn = math_contract.prepareTransaction().increment()
    assert txn == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'gas': 43120,
        'gasPrice': 1,
        'chainId': 1
    }


def test_prepare_transaction_with_contract_class_method(web3, MathContract, math_contract):
    txn = MathContract.prepareTransaction({'to': math_contract.address}).increment()
    assert txn == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'gas': 43120,
        'gasPrice': 1,
        'chainId': 1
    }


def test_prepare_transaction_with_contract_default_account_is_set(web3, math_contract):
    txn = math_contract.prepareTransaction().increment()
    assert txn == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'gas': 43120,
        'gasPrice': 1,
        'chainId': 1
    }


def test_prepare_transaction_with_contract_data_supplied_errors(web3, math_contract):
    with pytest.raises(ValueError):
        math_contract.prepareTransaction({
            'data': '0x000'
        }).increment()


def test_prepare_transaction_with_contract_to_address_supplied_errors(web3, math_contract):
    with pytest.raises(ValueError):
        math_contract.prepareTransaction({
            'to': '0xb2930B35844a230f00E51431aCAe96Fe543a0347'
        }).increment()


@pytest.mark.parametrize(
    'transaction_args,method_args,method_kwargs,expected,skip_testrpc',
    (
        (
            {}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'gas': 43242, 'gasPrice': 1, 'chainId': 1
            }, False
        ),
        (
            {'gas': 800000}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'gas': 800000, 'gasPrice': 1, 'chainId': 1
            }, False
        ),
        (
            {'gasPrice': 21000000000}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'gas': 43242, 'gasPrice': 21000000000, 'chainId': 1
            }, False
        ),
        (
            {'nonce': 7}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'gas': 43242, 'gasPrice': 1, 'nonce': 7, 'chainId': 1
            }, True
        ),
        (
            {'value': 20000}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 20000, 'gas': 43242, 'gasPrice': 1, 'chainId': 1
            }, False
        ),
    ),
    ids=[
        'Standard',
        'Explicit Gas',
        'Explicit Gas Price',
        'Explicit Nonce',
        'With Value',
    ]
)
def test_prepare_transaction_with_contract_with_arguments(web3, skip_if_testrpc, math_contract,
                                                          transaction_args,
                                                          method_args,
                                                          method_kwargs,
                                                          expected,
                                                          skip_testrpc):
    if skip_testrpc:
        skip_if_testrpc(web3)

    txn = math_contract.prepareTransaction(transaction_args).increment(
        *method_args, **method_kwargs
    )
    expected['to'] = math_contract.address
    assert txn is not None
    assert txn == expected
