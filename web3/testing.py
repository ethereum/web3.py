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


class Testing(Module):
    def timeTravel(self, timestamp):
        return self.web3.manager.request_blocking("testing_timeTravel", [timestamp])

    def mine(self, num_blocks=1):
        return self.web3.manager.request_blocking("evm_mine", [num_blocks])

    def snapshot(self):
        return self.web3.manager.request_blocking("evm_snapshot", [])

    def reset(self):
        return self.web3.manager.request_blocking("evm_reset", [])

    def revert(self, snapshot_idx=None):
        if snapshot_idx is None:
            return self.web3.manager.request_blocking("evm_revert", [])
        else:
            return self.web3.manager.request_blocking("evm_revert", [snapshot_idx])
