from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.utils.encoding import (
    to_decimal,
)


class Miner(object):
    def __init__(self, web3):
        self.web3 = web3

    @property
    @apply_formatters_to_return(to_decimal)
    def hashrate(self):
        return self.web3._requestManager.request_blocking("eth_hashrate", [])

    def makeDAG(self, number):
        return self.web3._requestManager.request_blocking("miner_makeDag", [number])

    def setExtra(self, extra):
        return self.web3._requestManager.request_blocking("miner_setExtra", [extra])

    def setGasPrice(self, gas_price):
        return self.web3._requestManager.request_blocking(
            "miner_setGasPrice", [gas_price],
        )

    def start(self, num_threads):
        return self.web3._requestManager.request_blocking(
            "miner_start", [num_threads],
        )

    def stop(self):
        return self.web3._requestManager.request_blocking("miner_stop", [])

    def startAutoDAG(self):
        return self.web3._requestManager.request_blocking("miner_startAutoDag", [])

    def stopAutoDAG(self):
        return self.web3._requestManager.request_blocking("miner_stopAutoDag", [])
