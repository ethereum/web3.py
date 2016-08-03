import random
import gevent


def test_txpool_content(web3_ipc_empty):
    web3 = web3_ipc_empty

    web3.miner.stop()

    with gevent.Timeout(30):
        while web3.miner.hashrate or web3.eth.mining:
            gevent.sleep(random.random())

    txn_1_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        'value': 12345,
    })
    txn_1 = web3.eth.getTransaction(txn_1_hash)
    txn_2_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        'value': 54321,
    })
    txn_2 = web3.eth.getTransaction(txn_2_hash)

    content = web3.txpool.content

    assert web3.eth.coinbase in content['pending']

    pending_txns = content['pending'][web3.eth.coinbase]

    assert txn_1['nonce'] in pending_txns
    assert txn_2['nonce'] in pending_txns

    assert pending_txns[txn_1['nonce']][0]['hash'] == txn_1_hash
    assert pending_txns[txn_1['nonce']][0]['value'] == 12345
    assert pending_txns[txn_2['nonce']][0]['hash'] == txn_2_hash
    assert pending_txns[txn_2['nonce']][0]['value'] == 54321
