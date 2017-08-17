from __future__ import absolute_import

from web3.utils.formatters import (
    hex_to_integer,
)

from .formatting import (
    BaseFormatterMiddleware,
)


class EVMSnapshotFormattingMiddleware(BaseFormatterMiddleware):
    result_formatters = {
        # EVM Snapshot and Reset
        'evm_snapshot': hex_to_integer,
    }
