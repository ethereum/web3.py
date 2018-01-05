from web3.module import (
    Module,
)


class Testing(Module):
    def timeTravel(self, timestamp):
        return self.web3.manager.request_blocking("testing_timeTravel", [timestamp])

    def mine(self, num_blocks=1):
        return self.web3.manager.request_blocking("evm_mine", [num_blocks])

    def snapshot(self):
        self.last_snapshot_idx = self.web3.manager.request_blocking("evm_snapshot", [])
        return self.last_snapshot_idx

    def reset(self):
        return self.web3.manager.request_blocking("evm_reset", [])

    def revert(self, snapshot_idx=None):
        if snapshot_idx is None:
            revert_target = self.last_snapshot_idx
        else:
            revert_target = snapshot_idx
        return self.web3.manager.request_blocking("evm_revert", [revert_target])
