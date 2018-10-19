from web3.module import (
    Module,
)


from typing import List, Optional
class Testing(Module):
    def timeTravel(self, timestamp: int) -> None:
        return self.web3.manager.request_blocking("testing_timeTravel", [timestamp])

    def mine(self, num_blocks: int = 1) -> List[str]:
        return self.web3.manager.request_blocking("evm_mine", [num_blocks])

    def snapshot(self) -> int:
        self.last_snapshot_idx = self.web3.manager.request_blocking("evm_snapshot", [])
        return self.last_snapshot_idx

    def reset(self):
        return self.web3.manager.request_blocking("evm_reset", [])

    def revert(self, snapshot_idx: Optional[int] = None) -> None:
        if snapshot_idx is None:
            revert_target = self.last_snapshot_idx
        else:
            revert_target = snapshot_idx
        return self.web3.manager.request_blocking("evm_revert", [revert_target])
