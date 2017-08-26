from web3.module import (
    Module,
)


class Miner(Module):
    @property
    def hashrate(self):
        return self.web3.manager.request_blocking("eth_hashrate", [])

    def makeDAG(self, number):
        return self.web3.manager.request_blocking("miner_makeDag", [number])

    def setExtra(self, extra):
        return self.web3.manager.request_blocking("miner_setExtra", [extra])

    def setEtherBase(self, etherbase):
        return self.web3.manager.request_blocking("miner_setEtherbase", [etherbase])

    def setGasPrice(self, gas_price):
        return self.web3.manager.request_blocking(
            "miner_setGasPrice", [gas_price],
        )

    def start(self, num_threads):
        return self.web3.manager.request_blocking(
            "miner_start", [num_threads],
        )

    def stop(self):
        return self.web3.manager.request_blocking("miner_stop", [])

    def startAutoDAG(self):
        return self.web3.manager.request_blocking("miner_startAutoDag", [])

    def stopAutoDAG(self):
        return self.web3.manager.request_blocking("miner_stopAutoDag", [])
