def test_filter_against_log_events(web3,
                                   emitter,
                                   wait_for_transaction,
                                   emitter_log_topics,
                                   emitter_event_ids):

    seen_logs = []
    txn_filter = web3.eth.filter({})
    txn_filter.watch(seen_logs.append)

    txn_hashes = []

    txn_hashes.append(emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments))

    for txn_hash in txn_hashes:
        wait_for_transaction(txn_hash)

    txn_filter.stop_watching(30)

    assert set(txn_hashes) == set(log['transactionHash'] for log in seen_logs)
