import pytest


@pytest.fixture()
def math_contract(web3_tester, MathContract):
    deploy_txn = MathContract.deploy()
    deploy_receipt = web3_tester.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _math_contract = MathContract(address=deploy_receipt['contractAddress'])
    return _math_contract


def test_transacting_with_contract_no_arguments(web3_tester, math_contract):
    initial_value = math_contract.call().counter()

    # workaround for bug in eth-tester-client.  The first real transaction
    # after a `.call(..)` doesn't get registered correctly with the test EVM.
    from testrpc import testrpc
    testrpc.evm_mine()

    txn_hash = math_contract.transact().increment()
    txn_receipt = web3_tester.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = math_contract.call().counter()

    assert final_value - initial_value == 1


def test_transacting_with_contract_with_arguments(web3_tester, math_contract):
    initial_value = math_contract.call().counter()

    # workaround for bug in eth-tester-client.  The first real transaction
    # after a `.call(..)` doesn't get registered correctly with the test EVM.
    from testrpc import testrpc
    testrpc.evm_mine()

    txn_hash = math_contract.transact().increment(5)
    txn_receipt = web3_tester.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt is not None

    final_value = math_contract.call().counter()

    assert final_value - initial_value == 5
