from web3.module import (
    Module,
)


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
