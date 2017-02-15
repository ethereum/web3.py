import pytest

from eth_utils import (
    force_bytes,
)


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


def test_eth_call_with_no_args(web3, wait_for_transaction, MATH_CODE, MATH_RUNTIME):
    txn_hash = web3.eth.sendTransaction({
        "from": web3.eth.coinbase,
        "data": MATH_CODE,
        "gas": 3000000,
    })

    wait_for_transaction(web3, txn_hash)

    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
    contract_address = txn_receipt['contractAddress']

    assert force_bytes(web3.eth.getCode(contract_address)) == MATH_RUNTIME

    abi_signature = web3.sha3("return13()", encoding=None)[:10]
    # sanity
    assert abi_signature == '0x16216f39'
    actual_result_hex = web3.eth.call({
        "from": web3.eth.coinbase,
        "to": contract_address,
        "data": abi_signature,
    })
    actual_result = int(actual_result_hex, 16)
    assert actual_result == 13
