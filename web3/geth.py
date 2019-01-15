from web3.module import (
    Module,
)
from web3.personal import (
    Personal,
)


class GethPersonal(Personal):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal
    """
    def __init__(self, w3):
        self.w3 = w3


class Geth(Module):
    @property
    def personal(self):
        return GethPersonal(self.web3)
