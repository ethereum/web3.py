import pytest
import socket

from web3.utils.module_testing import (
    EthModuleTest,
    PersonalModuleTest,
    Web3ModuleTest,
    ParityModuleTest,
)


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
    def test_eth_uninstallFilter(self, web3):
        pytest.xfail('eth_uninstallFilter calls to parity always return true')
        super().test_eth_uninstallFilter(web3)

    def test_eth_newBlockFilter(self, web3):
        pytest.xfail('Parity returns latest block on first polling for new blocks')
        super().test_eth_newBlockFilter(web3)

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


class ParityParityModuleTest(ParityModuleTest):
    def test_trace_replay_transaction(self, web3, mined_txn_hash):
        super().test_trace_replay_transaction(web3, mined_txn_hash)

    def test_trace_replay_block_transactions(self, web3, block_with_txn):
        super().test_trace_replay_block_transactions(web3, block_with_txn)

    def test_trace_block(self, web3, block_with_txn):
        super().test_trace_block(web3, block_with_txn)

    def test_trace_transaction(self, web3, mined_txn_hash):
        super().test_trace_transaction(web3, mined_txn_hash)
