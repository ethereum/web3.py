class ParityModuleTest:

    def test_trace_replay_transaction(self, web3, mined_txn_hash):
        trace = web3.parity.traceReplayTransaction(mined_txn_hash)
        print(trace)
        pass

    def test_trace_replay_block_transactions(self, web3, block_with_txn):
        trace = web3.parity.traceReplayBlockTransactions(block_with_txn['number'])
        print(trace)
        pass

    def test_trace_block(self, web3, block_with_txn):
        trace = web3.parity.traceBlock(block_with_txn['number'])
        print(trace)
        pass

    def test_trace_transaction(self, web3, mined_txn_hash):
        trace = web3.parity.traceTransaction(mined_txn_hash)
        print(trace)
        pass
