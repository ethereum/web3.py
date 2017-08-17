<<<<<<< HEAD
from web3.formatters import (
    transaction_pool_content_formatter,
    transaction_pool_inspect_formatter,
)

from web3.utils.functional import (
    apply_formatters_to_return,
)
=======
>>>>>>> 2aa43e0... remove formatters.py
from web3.utils.module import (
    Module,
)


class TxPool(Module):
    @property
    def content(self):
        return self.web3.manager.request_blocking("txpool_content", [])

    @property
    def inspect(self):
        return self.web3.manager.request_blocking("txpool_inspect", [])

    @property
    def status(self):
        return self.web3.manager.request_blocking("txpool_status", [])
