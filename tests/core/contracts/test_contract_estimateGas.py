import pytest

from web3.exceptions import (
    ValidationError,
)


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


@pytest.fixture()
def math_contract(web3,
                  MATH_ABI,
                  MATH_CODE,
                  MATH_RUNTIME,
                  wait_for_transaction,
                  address_conversion_func):
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
    )
    deploy_txn = MathContract.constructor().transact({'from': web3.eth.coinbase})
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)

    assert deploy_receipt is not None
    contract_address = address_conversion_func(deploy_receipt['contractAddress'])
    web3.isAddress(contract_address)

    _math_contract = MathContract(address=contract_address)
    assert _math_contract.address == contract_address
    return _math_contract


@pytest.fixture()
def fallback_function_contract(web3,
                               FALLBACK_FUNCTION_ABI,
                               FALLBACK_FUNCTION_CODE,
                               FALLBACK_FUNCTION_RUNTIME,
                               wait_for_transaction,
                               address_conversion_func):
    fallback_contract = web3.eth.contract(
        abi=FALLBACK_FUNCTION_ABI,
        bytecode=FALLBACK_FUNCTION_CODE,
        bytecode_runtime=FALLBACK_FUNCTION_RUNTIME
    )
    deploy_txn = fallback_contract.constructor().transact({'from': web3.eth.coinbase})
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)

    assert deploy_receipt is not None
    contract_address = address_conversion_func(deploy_receipt['contractAddress'])
    web3.isAddress(contract_address)

    _fallback_function_contract = fallback_contract(address=contract_address)
    assert _fallback_function_contract.address == contract_address
    return _fallback_function_contract


@pytest.fixture()
def payable_tester_contract(web3, PayableTesterContract, address_conversion_func):
    deploy_txn = PayableTesterContract.constructor().transact({'from': web3.eth.coinbase})
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)

    assert deploy_receipt is not None
    payable_tester_address = address_conversion_func(deploy_receipt['contractAddress'])

    _payable_tester = PayableTesterContract(address=payable_tester_address)
    assert _payable_tester.address == payable_tester_address
    return _payable_tester


def test_contract_estimateGas(web3, math_contract, estimateGas, transact):
    gas_estimate = estimateGas(contract=math_contract,
                               contract_function='increment')

    txn_hash = transact(
        contract=math_contract,
        contract_function='increment')

    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    gas_used = txn_receipt.get('gasUsed')

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_fallback_estimateGas(web3, fallback_function_contract):
    gas_estimate = fallback_function_contract.fallback.estimateGas()

    txn_hash = fallback_function_contract.fallback.transact()

    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    gas_used = txn_receipt.get('gasUsed')

    assert abs(gas_estimate - gas_used) < 21000


def test_contract_estimateGas_with_arguments(web3, math_contract, estimateGas, transact):
    gas_estimate = estimateGas(contract=math_contract,
                               contract_function='add',
                               func_args=[5, 6])

    txn_hash = transact(
        contract=math_contract,
        contract_function='add',
        func_args=[5, 6])
    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    gas_used = txn_receipt.get('gasUsed')

    assert abs(gas_estimate - gas_used) < 21000


def test_estimateGas_not_sending_ether_to_nonpayable_function(
        web3,
        payable_tester_contract,
        estimateGas,
        transact):
    gas_estimate = estimateGas(contract=payable_tester_contract,
                               contract_function='doNoValueCall')

    txn_hash = transact(
        contract=payable_tester_contract,
        contract_function='doNoValueCall')

    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    gas_used = txn_receipt.get('gasUsed')

    assert abs(gas_estimate - gas_used) < 21000


def test_estimateGas_sending_ether_to_nonpayable_function(
        web3,
        payable_tester_contract,
        estimateGas):
    with pytest.raises(ValidationError):
        estimateGas(contract=payable_tester_contract,
                    contract_function='doNoValueCall',
                    tx_params={'value': 1})


def test_estimateGas_accepts_latest_block(web3, math_contract, transact):
    gas_estimate = math_contract.functions.counter().estimateGas(block_identifier='latest')

    txn_hash = transact(
        contract=math_contract,
        contract_function='increment')

    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    gas_used = txn_receipt.get('gasUsed')

    assert abs(gas_estimate - gas_used) < 21000


def test_estimateGas_block_identifier_unique_estimates(web3, math_contract, transact):
    txn_hash = transact(contract=math_contract, contract_function="increment")
    web3.eth.waitForTransactionReceipt(txn_hash)

    latest_gas_estimate = math_contract.functions.counter().estimateGas(
        block_identifier="latest"
    )
    earliest_gas_estimate = math_contract.functions.counter().estimateGas(
        block_identifier="earliest"
    )

    assert latest_gas_estimate != earliest_gas_estimate
