import pytest


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


@pytest.fixture()
def math_contract(web3,
                  MATH_ABI,
                  MATH_CODE,
                  MATH_RUNTIME,
                  wait_for_transaction):
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
    )
    deploy_txn = MathContract.deploy({'from': web3.eth.coinbase})
    deploy_receipt = wait_for_transaction(web3, deploy_txn)

    assert deploy_receipt is not None
    contract_address = deploy_receipt['contractAddress']
    web3.isAddress(contract_address)

    _math_contract = MathContract(address=contract_address)
    return _math_contract


def test_contract_estimateGas(web3, math_contract, estimateGas):
    gas_estimate = estimateGas(contract=math_contract,
                               contract_function='increment')
    try:
        assert abs(gas_estimate - 21472) < 200  # Geth
    except AssertionError:
        assert abs(gas_estimate - 32772) < 200  # eth-tester with py-evm
        pass
