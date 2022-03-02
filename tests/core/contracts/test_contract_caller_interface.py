import pytest

from eth_utils.toolz import (
    identity,
)

from web3.exceptions import (
    MismatchedABI,
    NoABIFound,
    NoABIFunctionsFound,
)


def deploy(w3, Contract, apply_func=identity, args=None):
    args = args or []
    deploy_txn = Contract.constructor(*args).transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    address = apply_func(deploy_receipt['contractAddress'])
    contract = Contract(address=address)
    assert contract.address == address
    assert len(w3.eth.get_code(contract.address)) > 0
    return contract


@pytest.fixture()
def address(w3):
    return w3.eth.accounts[1]


@pytest.fixture()
def math_contract(w3, MathContract, address_conversion_func):
    return deploy(w3, MathContract, address_conversion_func)


@pytest.fixture()
def caller_tester_contract(w3, CallerTesterContract, address_conversion_func):
    return deploy(w3, CallerTesterContract, address_conversion_func)


@pytest.fixture()
def transaction_dict(w3, address):
    return {
        'from': address,
        'gas': 210000,
        'maxFeePerGas': w3.toWei(1, 'gwei'),
        'maxPriorityFeePerGas': w3.toWei(1, 'gwei'),
        'value': 12345,
    }


def test_caller_default(math_contract):
    result = math_contract.caller.add(3, 5)
    assert result == 8


def test_caller_with_parens(math_contract):
    result = math_contract.caller().add(3, 5)
    assert result == 8


def test_caller_with_no_abi(w3):
    contract = w3.eth.contract()
    with pytest.raises(NoABIFound):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_with_no_abi_and_parens(w3):
    contract = w3.eth.contract()
    with pytest.raises(NoABIFound):
        contract.caller().thisFunctionDoesNotExist()


def test_caller_with_empty_abi_and_parens(w3):
    contract = w3.eth.contract(abi=[])
    with pytest.raises(NoABIFunctionsFound):
        contract.caller().thisFunctionDoesNotExist()


def test_caller_with_empty_abi(w3):
    contract = w3.eth.contract(abi=[])
    with pytest.raises(NoABIFunctionsFound):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_raw_getattr_with_missing_element(math_contract):
    with pytest.raises(MismatchedABI, match="not found in this contract's ABI"):
        math_contract.caller.__getattr__('notafunction')


def test_caller_raw_getattr_with_present_element(math_contract):
    attr = math_contract.caller.__getattr__('return13')
    assert attr


def test_caller_with_a_nonexistent_function(math_contract):
    contract = math_contract
    with pytest.raises(MismatchedABI, match="not found in this contract's ABI"):
        contract.caller.thisFunctionDoesNotExist()


def test_caller_with_block_identifier(w3, math_contract):
    start_num = w3.eth.get_block('latest').number
    assert math_contract.caller.counter() == 0

    w3.provider.make_request(method='evm_mine', params=[5])
    math_contract.functions.increment().transact()
    math_contract.functions.increment().transact()

    output1 = math_contract.caller(block_identifier=start_num + 6).counter()
    output2 = math_contract.caller(block_identifier=start_num + 7).counter()

    assert output1 == 1
    assert output2 == 2


def test_caller_with_block_identifier_and_transaction_dict(w3,
                                                           caller_tester_contract,
                                                           transaction_dict,
                                                           address):
    start_num = w3.eth.get_block('latest').number
    assert caller_tester_contract.caller.counter() == 0

    w3.provider.make_request(method='evm_mine', params=[5])
    caller_tester_contract.functions.increment().transact()

    block_id = start_num + 6
    contract = caller_tester_contract.caller(
        transaction=transaction_dict,
        block_identifier=block_id
    )

    sender, _, gasLeft, value, block_num = contract.returnMeta()
    counter = contract.counter()

    assert sender == address
    assert gasLeft <= transaction_dict['gas']
    assert value == transaction_dict['value']
    assert block_num == block_id
    assert counter == 1


def test_caller_with_transaction_keyword(w3,
                                         caller_tester_contract,
                                         transaction_dict,
                                         address):
    contract = caller_tester_contract.caller(transaction=transaction_dict)

    sender, _, gasLeft, value, _ = contract.returnMeta()

    assert address == sender
    assert gasLeft <= transaction_dict['gas']
    assert value == transaction_dict['value']


def test_caller_with_dict_but_no_transaction_keyword(w3,
                                                     caller_tester_contract,
                                                     transaction_dict,
                                                     address):
    contract = caller_tester_contract.caller(transaction_dict)

    sender, _, gasLeft, value, _ = contract.returnMeta()

    assert address == sender
    assert gasLeft <= transaction_dict['gas']
    assert value == transaction_dict['value']


def test_caller_with_args_and_no_transaction_keyword(w3,
                                                     caller_tester_contract,
                                                     transaction_dict,
                                                     address):
    contract = caller_tester_contract.caller(transaction_dict)

    sender, _, gasLeft, value, _ = contract.returnMeta()

    assert address == sender
    assert gasLeft <= transaction_dict['gas']
    assert value == transaction_dict['value']

    add_result = contract.add(3, 5)
    assert add_result == 8
