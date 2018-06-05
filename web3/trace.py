from web3 import formatters
from web3.utils.empty import (
    empty,
)

class Trace(object):
    def __init__(self, web3):
        self.web3 = web3

    defaultAccount = empty
    defaultBlock = "latest"

    def call(self, transaction, types, block_identifier=None):
        formatted_transaction = formatters.input_transaction_formatter(self, transaction)
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3._requestManager.request_blocking(
            "trace_call",
            [
                formatted_transaction,
                types,
                formatters.input_block_identifier_formatter(block_identifier),
            ],
        )

    def rawTransaction(self, rtransaction, types):
        return self.web3._requestManager.request_blocking(
            "trace_rawTransaction",
            [
                rtransaction,
                types,
            ],
        )

    def replayTransaction(self, transaction, types):
        return self.web3._requestManager.request_blocking(
            "trace_replayTransaction",
            [
                transaction,
                types,
            ],
        )

    def block(self, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3._requestManager.request_blocking(
            "trace_block",
            [
                formatters.input_block_identifier_formatter(block_identifier),
            ],
        )

    def filter(self, tfilter):
        return self.web3._requestManager.request_blocking(
            "trace_filter",
            [
                tfilter,
            ],
        )

    def get(self, transaction, indices):
        return self.web3._requestManager.request_blocking(
            "trace_get",
            [
                transaction,
                indices,
            ],
        )

    def transaction(self, transaction):
        return self.web3._requestManager.request_blocking(
            "trace_transaction",
            [
                transaction,
            ],
        )
