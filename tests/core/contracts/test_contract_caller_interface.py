import pytest

from web3._utils.toolz import (
    identity,
)
from web3.exceptions import (
    MismatchedABI,
    NoABIFunctionsFound,
)


def deploy(web3, Contract, apply_func=identity, args=None):
    args = args or []
    deploy_txn = Contract.constructor(*args).transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    address = apply_func(deploy_receipt['contractAddress'])
    contract = Contract(address=address)
    assert contract.address == address
    assert len(web3.eth.getCode(contract.address)) > 0
    return contract


@pytest.fixture()
def math_contract(web3, MathContract, address_conversion_func):
    return deploy(web3, MathContract, address_conversion_func)


def test_caller_default(math_contract):
    result = math_contract.caller.add(3, 5)
    assert result == 8


def test_caller_with_parens(math_contract):
    result = math_contract.caller().return13()
    assert result == 13


def test_caller_with_parens_and_transaction_dict(math_contract):
    result = math_contract.caller({'from': 'notarealaddress.eth'}).add(2, 3)
    assert result == 5


def test_caller_with_no_abi(web3):
    contract = web3.eth.contract()
    with pytest.raises(NoABIFunctionsFound):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_with_a_nonexistent_function(web3, math_contract):
    contract = math_contract
    with pytest.raises(MismatchedABI):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_with_block_identifier(math_contract):
    # TODO: see how increment in the math contract changes with block_identifier
    # TODO: dig into if we even want this block identifier here
    result = math_contract.caller(block_identifier=10).return13()
    assert result == 13


def test_caller_with_transaction_keyword(math_contract):
    # TODO: Make sure from is actually set correctly here.
    result = math_contract.caller(transaction={'from': 'notarealaddress.eth'}).return13()
    assert result == 13
