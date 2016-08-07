import random
import gevent


def wait_for_transaction_receipt(web3, txn_hash, timeout=120):
    with gevent.Timeout(timeout):
        while True:
            txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
            if txn_receipt is not None:
                break
            gevent.sleep(random.random())
    return txn_receipt


def get_block_gas_limit(web3, block_identifier=None):
    if block_identifier is None:
        block_identifier = web3.eth.blockNumber
    block = web3.eth.getBlock(block_identifier)
    return block['gasLimit']
