import pytest

from web3.providers.rpc import TestRPCProvider
from web3.utils.abi import (
    function_abi_to_4byte_selector,
)


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


@pytest.fixture()
def math_contract(web3, MATH_ABI, MATH_CODE, MATH_RUNTIME, MATH_SOURCE,
                  wait_for_transaction):
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        code=MATH_CODE,
        code_runtime=MATH_RUNTIME,
        source=MATH_SOURCE,
    )
    deploy_txn = MathContract.deploy({'from': web3.eth.coinbase})
    deploy_receipt = wait_for_transaction(deploy_txn)

    assert deploy_receipt is not None
    contract_address = deploy_receipt['contractAddress']
    web3.isAddress(contract_address)

    _math_contract = MathContract(address=contract_address)
    return _math_contract


def test_needs_skipping(web3):
    if not isinstance(web3.currentProvider, TestRPCProvider):
        pytest.skip("N/A")
    with pytest.raises(ValueError):
        web3.eth.estimateGas({})


def test_contract_estimateGas(web3, math_contract):
    if isinstance(web3.currentProvider, TestRPCProvider):
        pytest.skip("The testrpc server doesn't implement `eth_estimateGas`")

    increment_abi = math_contract.find_matching_fn_abi('increment', [])
    call_data = function_abi_to_4byte_selector(increment_abi)
    gas_estimate = math_contract.estimateGas().increment()

    assert abs(gas_estimate - 21272) < 200
