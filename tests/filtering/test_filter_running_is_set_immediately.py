def test_filter_runs_immediately(web3):
    seen_logs = []
    txn_filter = web3.eth.filter({})
    assert txn_filter.running is None

    txn_filter.watch(lambda _: _)

    assert txn_filter.running is True
