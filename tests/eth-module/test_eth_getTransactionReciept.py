import pytest


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


def test_eth_getTransactionReceipt(web3, extra_accounts, wait_for_transaction):
    txn_hash = web3.eth.sendTransaction({
        "from": web3.eth.coinbase,
        "to": extra_accounts[1],
        "value": 1234,
    })

    wait_for_transaction(web3, txn_hash)

    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt['transactionHash'] == txn_hash


def test_eth_getTransactionReceipt_returns_null_for_unresolved_hash(web3):
    txn_hash = b'0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238'
    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt is None
