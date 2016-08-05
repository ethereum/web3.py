import collections
import itertools
import pytest


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block, skip_if_testrpc):
    skip_if_testrpc(web3)
    wait_for_block(web3)


def test_eth_getTransactionFromBlock(web3, extra_accounts, wait_for_transaction):
    current_block_number = web3.eth.blockNumber

    transaction_hashes = []

    for _ in range(5):
        transaction_hashes.append(web3.eth.sendTransaction({
            "from": web3.eth.coinbase,
            "to": extra_accounts[1],
            "value": 1,
        }))

    # wait for them to resolve
    for txn_hash in transaction_hashes:
        wait_for_transaction(web3, txn_hash)

    # gather all receipts and sort/group them by block number.
    all_receipts = sorted(
        [web3.eth.getTransactionReceipt(txn_hash) for txn_hash in transaction_hashes],
        key=lambda r: r['blockNumber'],
    )
    all_receipts_by_block = {
        key: tuple(value)
        for key, value in itertools.groupby(all_receipts, lambda r: r['blockNumber'])
    }

    for block_number, block_receipts in all_receipts_by_block.items():
        block = web3.eth.getBlock(block_number)
        block_hash = block['hash']
        block_transactions = block['transactions']

        for txn_idx, txn_hash in enumerate(block_transactions):
            for block_identifier in [block_number, block_hash]:
                txn = web3.eth.getTransactionFromBlock(block_identifier, txn_idx)
                assert txn['hash'] == txn_hash
