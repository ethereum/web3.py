from web3.utils.module import (
    Module,
)
<<<<<<< HEAD
from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.utils.module import (
    Module,
)
=======
>>>>>>> 2aa43e0... remove formatters.py


class Net(Module):
    @property
    def listening(self):
        return self.web3.manager.request_blocking("net_listening", [])

    def getListening(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def peerCount(self):
        return self.web3.manager.request_blocking("net_peerCount", [])

    def getPeerCount(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")
