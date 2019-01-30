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


@pytest.fixture()
def return_args_contract(web3, ReturnArgsContract, address_conversion_func):
    return deploy(web3, ReturnArgsContract, address_conversion_func)


def test_caller_default(math_contract):
    result = math_contract.caller.add(3, 5)
    assert result == 8


def test_caller_with_parens(math_contract):
    result = math_contract.caller().return13()
    assert result == 13


def test_caller_with_no_abi(web3):
    contract = web3.eth.contract()
    with pytest.raises(NoABIFunctionsFound):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_with_a_nonexistent_function(math_contract):
    contract = math_contract
    with pytest.raises(MismatchedABI):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_with_block_identifier(web3, math_contract):
    start_num = web3.eth.getBlock('latest').number
    assert math_contract.caller.counter() == 0

    web3.provider.make_request(method='evm_mine', params=[5])
    math_contract.functions.increment().transact()
    math_contract.functions.increment().transact()

    output1 = math_contract.caller(block_identifier=start_num + 6).counter()
    output2 = math_contract.caller(block_identifier=start_num + 7).counter()

    assert output1 == 1
    assert output2 == 2


def test_caller_with_transaction_keyword(web3, return_args_contract):
    address = web3.eth.accounts[0]
    contract = return_args_contract.caller(transaction_dict={'from': address})
    assert contract.returnMeta() == [address, b'\xc7\xfa}f', 45532, 0]


def test_caller_with_dict_but_no_transaction_keyword(web3, return_args_contract):
    address = web3.eth.accounts[0]
    contract = return_args_contract.caller({'from': address})
    assert contract.returnMeta() == [address, b'\xc7\xfa}f', 45532, 0]
