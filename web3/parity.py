from eth_utils import (
    is_checksum_address,
)

from web3.module import (
    Module,
)
from web3.utils.toolz import (
    assoc,
)


class Parity(Module):
    """
    https://paritytech.github.io/wiki/JSONRPC-parity-module
    """
    defaultBlock = "latest"

    def enode(self):
        return self.web3.manager.request_blocking(
            "parity_enode",
            [],
        )

    def netPeers(self):
        return self.web3.manager.request_blocking(
            "parity_netPeers",
            [],
        )

    def traceReplayTransaction(self, transaction_hash, mode=['trace']):
        return self.web3.manager.request_blocking(
            "trace_replayTransaction",
            [transaction_hash, mode],
        )

    def traceReplayBlockTransactions(self, block_identifier, mode=['trace']):
        return self.web3.manager.request_blocking(
            "trace_replayBlockTransactions",
            [block_identifier, mode]
        )

    def traceBlock(self, block_identifier):
        return self.web3.manager.request_blocking(
            "trace_block",
            [block_identifier]
        )

    def traceTransaction(self, transaction_hash):
        return self.web3.manager.request_blocking(
            "trace_transaction",
            [transaction_hash]
        )

    def traceCall(self, transaction, mode=['trace'], block_identifier=None):
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "trace_call",
            [transaction, mode, block_identifier],
        )

    def traceRawTransaction(self, raw_transaction, mode=['trace']):
        return self.web3.manager.request_blocking(
            "trace_rawTransaction",
            [raw_transaction, mode],
        )
