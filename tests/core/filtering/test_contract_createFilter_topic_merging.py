def test_merged_topic_list_event(
        web3,
        emitter,
        emitter_event_ids,
        wait_for_transaction):
    manual_topics = [
        '0xf16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec',  # event sig
        '0x0000000000000000000000000000000000000000000000000000000000000457',  # 1111
        '0x0000000000000000000000000000000000000000000000000000000000000457',  # 1111
        '0x0000000000000000000000000000000000000000000000000000000000000457',  # 1111
    ]
    log_filter = emitter.events.LogTripleWithIndex().createFilter(
        fromBlock="latest",
        topics=manual_topics,
        argument_filters={'arg0': 2222, 'arg1': 2222, 'arg2': 2222})
    event_id = getattr(emitter_event_ids, 'LogTripleWithIndex')
    txn_hashes = [
        emitter.functions.logTriple(event_id, 1111, 1111, 1111).transact(),
        emitter.functions.logTriple(event_id, 1111, 1111, 2222).transact(),
        emitter.functions.logTriple(event_id, 1111, 2222, 1111).transact(),
        emitter.functions.logTriple(event_id, 2222, 1111, 1111).transact(),
        emitter.functions.logTriple(event_id, 2222, 1111, 2222).transact(),
        emitter.functions.logTriple(event_id, 1111, 2222, 2222).transact(),
        emitter.functions.logTriple(event_id, 2222, 2222, 1111).transact(),
        emitter.functions.logTriple(event_id, 2222, 2222, 2222).transact()
    ]
    while True:
        if all(wait_for_transaction(web3, txn_hash) for txn_hash in txn_hashes):
            break
    assert len(log_filter.get_all_entries()) == 2
