import pytest

from web3.providers.tester import (
    EthereumTesterProvider,
    TestRPCProvider,
)
from web3.utils.compat import (
    Timeout,
    sleep,
)
from web3.main import Web3


class PollDelayCounter(object):
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


def is_all_testrpc_providers(providers):
    return all(
        isinstance(provider, (TestRPCProvider, EthereumTesterProvider))
        for provider
        in providers
    )


@pytest.fixture()
def skip_if_testrpc():

    def _skip_if_testrpc(web3):
        if is_all_testrpc_providers(web3.providers):
            pytest.skip()
    return _skip_if_testrpc


@pytest.fixture()
def wait_for_miner_start():
    def _wait_for_miner_start(web3, timeout=60):
        poll_delay_counter = PollDelayCounter()
        with Timeout(timeout) as timeout:
            while not web3.eth.mining or not web3.eth.hashrate:
                sleep(poll_delay_counter())
                timeout.check()
    return _wait_for_miner_start


@pytest.fixture()
def wait_for_block():
    def _wait_for_block(web3, block_number=1, timeout=60 * 10):
        poll_delay_counter = PollDelayCounter()
        with Timeout(timeout) as timeout:
            while True:
                if web3.eth.blockNumber >= block_number:
                    break
                if is_all_testrpc_providers(web3.providers):
                    web3.manager.request_blocking("evm_mine", [])
                sleep(poll_delay_counter())
                timeout.check()
    return _wait_for_block


@pytest.fixture()
def wait_for_transaction():
    def _wait_for_transaction(web3, txn_hash, timeout=120):
        poll_delay_counter = PollDelayCounter()
        with Timeout(timeout) as timeout:
            while True:
                txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
                if txn_receipt is not None:
                    break
                sleep(poll_delay_counter())
                timeout.check()

        return txn_receipt
    return _wait_for_transaction


@pytest.fixture()
def web3():
    provider = EthereumTesterProvider()
    return Web3(provider)
