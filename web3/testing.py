from web3.utils.encoding import (
    to_decimal,
)
from web3.utils.functional import (
    apply_formatters_to_return,
)


class Testing(object):
    def __init__(self, web3):
        self.web3 = web3

    def timeTravel(self, timestamp):
        return self.web3._requestManager.request_blocking("testing_timeTravel", [timestamp])

    def mine(self, num_blocks=1):
        return self.web3._requestManager.request_blocking("evm_mine", [num_blocks])

    @apply_formatters_to_return(to_decimal)
    def snapshot(self):
        return self.web3._requestManager.request_blocking("evm_snapshot", [])

    def reset(self):
        return self.web3._requestManager.request_blocking("evm_reset", [])

    def revert(self, snapshot_idx=None):
        if snapshot_idx is None:
            return self.web3._requestManager.request_blocking("evm_revert", [])
        else:
            return self.web3._requestManager.request_blocking("evm_revert", [snapshot_idx])
