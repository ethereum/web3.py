# -*- coding: utf-8 -*-

import pytest

from eth_utils import (
    force_bytes,
)

from web3.utils.empty import (
    empty,
)
from web3.utils.transactions import (
    wait_for_transaction_receipt,
)

# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


@pytest.fixture()
def math_contract(web3, MathContract):
    deploy_txn = MathContract.deploy()
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _math_contract = MathContract(address=deploy_receipt['contractAddress'])
    return _math_contract


def test_prepare_transacting_with_contract_no_arguments(web3, math_contract):
    txn = math_contract.prepareTransaction().increment()
    assert txn is not None
    assert txn['to'] == math_contract.address
    assert txn['data'] == '0xd09de08a'


@pytest.mark.parametrize(
    'transaction_args,method_args,method_kwargs,expected',
    (
        ({}, (5,), {}, {'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005'}),
    ),
)
def test_prepare_transacting_with_contract_with_arguments(web3, math_contract, transaction_args, method_args, method_kwargs, expected):
    txn = math_contract.prepareTransaction(transaction_args).increment(*method_args, **method_kwargs)
    expected['to'] = math_contract.address
    assert txn is not None
    assert txn == expected
