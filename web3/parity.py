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

        if is_integer(block_identifier):
            block = to_hex(block_identifier)
        elif is_predefined_block_number or is_hex_encoded_block_hash:
            block = block_identifier
        else:
            raise ValueError('The block identifier is not valid')

        return self.web3.manager.request_blocking(
            "trace_replayBlockTransactions",
            [block, mode]
        )

    def traceBlock(self, block_identifier):

        if is_integer(block_identifier):
            block = to_hex(block_identifier)
        elif is_predefined_block_number or is_hex_encoded_block_hash:
            block = block_identifier
        else:
            raise ValueError('The block identifier is not valid')

        return self.web3.manager.request_blocking(
            "trace_block",
            [block]
        )

    def traceTransaction(self, transaction_hash):
        return self.web3.manager.request_blocking(
            "trace_transaction",
            [transaction_hash]
        )
