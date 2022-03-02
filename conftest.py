import pytest
import time
import warnings

from web3._utils.threads import (
    Timeout,
)
from web3.main import (
    Web3,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


class PollDelayCounter:
    def __init__(self, initial_delay=0, max_delay=1, initial_step=0.01):
        self.initial_delay = initial_delay
        self.initial_step = initial_step
        self.max_delay = max_delay
        self.current_delay = initial_delay

    def __call__(self):
        delay = self.current_delay

        if self.current_delay == 0:
            self.current_delay += self.initial_step
        else:
            self.current_delay *= 2
            self.current_delay = min(self.current_delay, self.max_delay)

        return delay

    def reset(self):
        self.current_delay = self.initial_delay


@pytest.fixture()
def sleep_interval():
    return PollDelayCounter()


def is_testrpc_provider(provider):
    return isinstance(provider, EthereumTesterProvider)


@pytest.fixture()
def skip_if_testrpc():

    def _skip_if_testrpc(w3):
        if is_testrpc_provider(w3.provider):
            pytest.skip()
    return _skip_if_testrpc


@pytest.fixture()
def wait_for_miner_start():
    def _wait_for_miner_start(w3, timeout=60):
        poll_delay_counter = PollDelayCounter()
        with Timeout(timeout) as timeout:
            while not w3.eth.mining or not w3.eth.hashrate:
                time.sleep(poll_delay_counter())
                timeout.check()
    return _wait_for_miner_start


@pytest.fixture(scope="module")
def wait_for_block():
    def _wait_for_block(w3, block_number=1, timeout=None):
        if not timeout:
            timeout = (block_number - w3.eth.block_number) * 3
        poll_delay_counter = PollDelayCounter()
        with Timeout(timeout) as timeout:
            while w3.eth.block_number < block_number:
                w3.manager.request_blocking("evm_mine", [])
                timeout.sleep(poll_delay_counter())
    return _wait_for_block


@pytest.fixture(scope="module")
def wait_for_transaction():
    def _wait_for_transaction(w3, txn_hash, timeout=120):
        poll_delay_counter = PollDelayCounter()
        with Timeout(timeout) as timeout:
            while True:
                txn_receipt = w3.eth.get_transaction_receipt(txn_hash)
                if txn_receipt is not None:
                    break
                time.sleep(poll_delay_counter())
                timeout.check()

        return txn_receipt
    return _wait_for_transaction


@pytest.fixture()
def w3():
    provider = EthereumTesterProvider()
    return Web3(provider)


@pytest.fixture(scope="module")
def w3_strict_abi():
    w3 = Web3(EthereumTesterProvider())
    w3.enable_strict_bytes_type_checking()
    return w3


@pytest.fixture(autouse=True)
def print_warnings():
    warnings.simplefilter('always')
