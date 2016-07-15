import pytest


@pytest.fixture(autouse=True)
def wait_for_first_block(web3_tester, wait_for_block):
    wait_for_block(web3_tester)


@pytest.fixture()
def math_contract(web3_tester, MathContract):
    deploy_txn = MathContract.deploy()
    deploy_receipt = web3_tester.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _math_contract = MathContract(address=deploy_receipt['contractAddress'])
    return _math_contract


def test_call_with_no_arguments(math_contract):
    result = math_contract.call().return13()
    assert result == 13


def test_call_with_one_argument(math_contract):
    result = math_contract.call().multiply7(3)
    assert result == 21


def test_call_with_multiple_arguments(math_contract):
    result = math_contract.call().add(9, 7)
    assert result == 16
