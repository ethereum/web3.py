def test_filter_against_pending_transactions(web3, wait_for_transaction):
    seen_txns = []
    txn_filter = web3.eth.filter("pending")
    txn_filter.watch(seen_txns.append)

    txn_1_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        'value': 12345,
    })
    txn_2_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        'value': 54321,
    })

    wait_for_transaction(txn_1_hash)
    wait_for_transaction(txn_2_hash)

    txn_filter.stop_watching(30)

    assert txn_1_hash in seen_txns
    assert txn_2_hash in seen_txns
