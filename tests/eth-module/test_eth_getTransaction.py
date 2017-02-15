import pytest


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


def test_eth_getTransaction_for_unknown_transaction(web3):
    txn_hash = b'0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238'
    txn = web3.eth.getTransaction(txn_hash)
    assert txn is None


def test_eth_getTransaction(web3, extra_accounts, wait_for_transaction):
    txn_hash = web3.eth.sendTransaction({
        "from": web3.eth.coinbase,
        "to": extra_accounts[1],
        "value": 1234,
    })

    wait_for_transaction(web3, txn_hash)

    txn = web3.eth.getTransaction(txn_hash)
    assert txn['hash'] == txn_hash
