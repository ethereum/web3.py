import pytest
import socket

from flaky import (
    flaky,
)

from web3.utils.module_testing import (
    EthModuleTest,
    ParityModuleTest as TraceModuleTest,
    PersonalModuleTest,
    Web3ModuleTest,
)

# some tests appear flaky with Parity v1.10.x
MAX_FLAKY_RUNS = 3


def get_open_port():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
    sock.close()
    return str(port)


class ParityWeb3ModuleTest(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('Parity/')


class ParityEthModuleTest(EthModuleTest):
    def test_eth_getBlockByNumber_pending(self, web3):
        pytest.xfail('Parity dropped "pending" option in 1.11.1')
        super().test_eth_getBlockByNumber_pending(web3)

    def test_eth_uninstallFilter(self, web3):
        pytest.xfail('eth_uninstallFilter calls to parity always return true')
        super().test_eth_uninstallFilter(web3)

    def test_eth_replaceTransaction(self, web3, unlocked_account):
        pytest.xfail('Needs ability to efficiently control mining')
        super().test_eth_replaceTransaction(web3, unlocked_account)

    def test_eth_replaceTransaction_already_mined(self, web3, unlocked_account):
        pytest.xfail('Parity is not setup to auto mine')
        super().test_eth_replaceTransaction_already_mined(web3, unlocked_account)

    def test_eth_replaceTransaction_incorrect_nonce(self, web3, unlocked_account):
        pytest.xfail('Needs ability to efficiently control mining')
        super().test_eth_replaceTransaction_incorrect_nonce(web3, unlocked_account)

    def test_eth_replaceTransaction_gas_price_too_low(self, web3, unlocked_account):
        pytest.xfail('Needs ability to efficiently control mining')
        super().test_eth_replaceTransaction_gas_price_too_low(web3, unlocked_account)

    def test_eth_replaceTransaction_gas_price_defaulting_minimum(self, web3, unlocked_account):
        pytest.xfail('Needs ability to efficiently control mining')
        super().test_eth_replaceTransaction_gas_price_defaulting_minimum(web3, unlocked_account)

    def test_eth_replaceTransaction_gas_price_defaulting_strategy_higher(self,
                                                                         web3,
                                                                         unlocked_account):
        pytest.xfail('Needs ability to efficiently control mining')
        super().test_eth_replaceTransaction_gas_price_defaulting_strategy_higher(
            web3, unlocked_account
        )

    def test_eth_replaceTransaction_gas_price_defaulting_strategy_lower(self,
                                                                        web3,
                                                                        unlocked_account):
        pytest.xfail('Needs ability to efficiently control mining')
        super().test_eth_replaceTransaction_gas_price_defaulting_strategy_lower(
            web3, unlocked_account
        )

    def test_eth_modifyTransaction(self, web3, unlocked_account):
        pytest.xfail('Needs ability to efficiently control mining')
        super().test_eth_modifyTransaction(web3, unlocked_account)

    @flaky(max_runs=MAX_FLAKY_RUNS)
    def test_eth_getTransactionReceipt_unmined(self, web3, unlocked_account):
        # Parity diverges from json-rpc spec and retrieves pending block
        # transactions with getTransactionReceipt.
        txn_hash = web3.eth.sendTransaction({
            'from': unlocked_account,
            'to': unlocked_account,
            'value': 1,
            'gas': 21000,
            'gasPrice': web3.eth.gasPrice,
        })
        receipt = web3.eth.getTransactionReceipt(txn_hash)
        assert receipt is not None
        assert receipt['blockHash'] is None

    def test_eth_getLogs_with_logs_none_topic_args(self, web3):
        pytest.xfail("Parity matches None to asbent values")
        super().test_eth_getLogs_with_logs_none_topic_args(web3)

    @flaky(max_runs=MAX_FLAKY_RUNS)
    def test_eth_call_old_contract_state(self, web3, math_contract, unlocked_account):
        start_block = web3.eth.getBlock('latest')
        block_num = start_block.number
        block_hash = start_block.hash

        math_contract.functions.increment().transact({'from': unlocked_account})

        # This isn't an incredibly convincing test since we can't mine, and
        # the default resolved block is latest, So if block_identifier was ignored
        # we would get the same result. For now, we mostly depend on core tests.
        # Ideas to improve this test:
        #  - Enable on-demand mining in more clients
        #  - Increment the math contract in all of the fixtures, and check the value in an old block

        block_hash_call_result = math_contract.functions.counter().call(block_identifier=block_hash)
        block_num_call_result = math_contract.functions.counter().call(block_identifier=block_num)
        latest_call_result = math_contract.functions.counter().call(block_identifier='latest')
        default_call_result = math_contract.functions.counter().call()

        assert block_hash_call_result == 0
        assert block_num_call_result == 0
        assert latest_call_result == 0
        assert default_call_result == 0

        # retrieve this right before using - Parity tests might hit a race otherwise
        pending_call_result = math_contract.functions.counter().call(block_identifier='pending')
        # should be '1' on first flaky run, '2' on second, or '3' on third
        if pending_call_result not in range(1, MAX_FLAKY_RUNS + 1):
            raise AssertionError("pending call result was %d!" % pending_call_result)


class ParityPersonalModuleTest(PersonalModuleTest):
    def test_personal_importRawKey(self, web3):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_importRawKey(web3)

    def test_personal_listAccounts(self, web3):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_listAccounts(web3)

    def test_personal_lockAccount(self, web3, unlocked_account):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_lockAccount(web3, unlocked_account)

    def test_personal_unlockAccount_success(self, web3):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_unlockAccount_success(web3)

    def test_personal_unlockAccount_failure(self, web3, unlockable_account):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_unlockAccount_failure(web3, unlockable_account)

    def test_personal_newAccount(self, web3):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_newAccount(web3)

    def test_personal_sendTransaction(
            self,
            web3,
            unlockable_account,
            unlockable_account_pw):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_sendTransaction(
            web3,
            unlockable_account,
            unlockable_account_pw)

    def test_personal_sign_and_ecrecover(
            self,
            web3,
            unlockable_account,
            unlockable_account_pw):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_sign_and_ecrecover(
            web3,
            unlockable_account,
            unlockable_account_pw)


class ParityTraceModuleTest(TraceModuleTest):
    def test_trace_replay_transaction(self, web3, parity_fixture_data):
        super().test_trace_replay_transaction(web3, parity_fixture_data)

    def test_trace_replay_block_with_transactions(self,
                                                  web3,
                                                  block_with_txn,
                                                  parity_fixture_data):
        pytest.xfail('This method does not exist in older parity versions')
        super().test_trace_replay_block_with_transactions(web3,
                                                          block_with_txn,
                                                          parity_fixture_data)

    def test_trace_replay_block_without_transactions(self, web3, empty_block):
        pytest.xfail('This method does not exist in older parity versions')
        super().test_trace_replay_block_without_transactions(web3, empty_block)

    def test_trace_block(self, web3, block_with_txn):
        super().test_trace_block(web3, block_with_txn)

    def test_trace_transaction(self, web3, parity_fixture_data):
        super().test_trace_transaction(web3, parity_fixture_data)

    def test_trace_call(self, web3, math_contract, math_contract_address):
        super().test_trace_call(web3, math_contract, math_contract_address)

    def test_eth_call_with_0_result(self, web3, math_contract, math_contract_address):
        super().test_eth_call_with_0_result(web3, math_contract, math_contract_address)

    def test_trace_filter(self, web3, txn_filter_params, parity_fixture_data):
        super().test_trace_filter(web3, txn_filter_params, parity_fixture_data)
