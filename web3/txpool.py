from web3.formatters import (
    transaction_pool_content_formatter,
    transaction_pool_inspect_formatter,
)

from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.utils.module import (
    Module,
)


class TxPool(Module):
    @property
    @apply_formatters_to_return(transaction_pool_content_formatter)
    def content(self):
        return self.web3._requestManager.request_blocking("txpool_content", [])

    @property
    @apply_formatters_to_return(transaction_pool_inspect_formatter)
    def inspect(self):
        return self.web3._requestManager.request_blocking("txpool_inspect", [])

    @property
    def status(self):
        return self.web3._requestManager.request_blocking("txpool_status", [])
