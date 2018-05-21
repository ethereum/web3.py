from web3.module import (
    Module,
)

from web3.utils.blocks import (
    is_predefined_block_number,
    is_hex_encoded_block_hash
)

from eth_utils import (
    is_integer,
)

from web3.utils.encoding import (
    to_hex
)


class Parity(Module):
    """
    https://paritytech.github.io/wiki/JSONRPC-parity-module
    """
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
