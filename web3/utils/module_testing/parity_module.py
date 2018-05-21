class ParityModuleTest:

    def test_trace_replay_transaction(self, web3, parity_fixture_data):
        trace = web3.parity.traceReplayTransaction(parity_fixture_data['mined_txn_hash'])

        assert trace['stateDiff'] is None
        assert trace['vmTrace'] is None
        assert trace['trace'][0]['action']['from'] == '0x'+parity_fixture_data['coinbase']
        pass

    def test_trace_replay_block_transactions(self, web3, block_with_txn):
        trace = web3.parity.traceReplayBlockTransactions(block_with_txn['number'])
        pass

    def test_trace_block(self, web3, block_with_txn):
        trace = web3.parity.traceBlock(block_with_txn['number'])
        assert trace[0]['blockNumber'] == block_with_txn['number']
        pass

    def test_trace_transaction(self, web3, parity_fixture_data):
        trace = web3.parity.traceTransaction(parity_fixture_data['mined_txn_hash'])
        print(trace)
        assert trace[0]['action']['from'] == '0x'+parity_fixture_data['coinbase']
        pass
