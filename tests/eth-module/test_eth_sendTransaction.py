import pytest

from eth_utils import force_bytes


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


def test_eth_sendTransaction_with_value_only_transaction(web3, extra_accounts,
                                                         wait_for_transaction):
    initial_balance = web3.eth.getBalance(extra_accounts[1])

    txn_hash = web3.eth.sendTransaction({
        "from": web3.eth.coinbase,
        "to": extra_accounts[1],
        "value": 1234,
    })

    wait_for_transaction(web3, txn_hash)

    after_balance = web3.eth.getBalance(extra_accounts[1])

    assert after_balance - initial_balance == 1234


def test_eth_sendTransaction_with_data(web3, wait_for_transaction, MATH_CODE, MATH_RUNTIME):
    txn_hash = web3.eth.sendTransaction({
        "from": web3.eth.coinbase,
        "data": MATH_CODE,
        "gas": 3000000,
    })

    wait_for_transaction(web3, txn_hash)

    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
    contract_address = txn_receipt['contractAddress']

    assert force_bytes(web3.eth.getCode(contract_address)) == MATH_RUNTIME


def test_eth_sendTransaction_auto_estimates_gas_if_not_provided(web3, wait_for_transaction, MATH_CODE, MATH_RUNTIME):
    txn_hash = web3.eth.sendTransaction({
        "from": web3.eth.coinbase,
        "data": MATH_CODE,
    })

    wait_for_transaction(web3, txn_hash)

    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
    contract_address = txn_receipt['contractAddress']

    assert force_bytes(web3.eth.getCode(contract_address)) == MATH_RUNTIME
