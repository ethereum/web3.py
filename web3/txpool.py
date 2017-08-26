from web3.module import (
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
