import pytest
import socket

from web3.utils.module_testing import (
    EthModuleTest,
    NetModuleTest,
    PersonalModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)


def get_open_port():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
    sock.close()
    return str(port)


class GoEthereumTest(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('Geth/')


class GoEthereumEthModuleTest(EthModuleTest):
    def test_eth_replaceTransaction(self, web3, unlocked_account):
        pytest.xfail('Needs ability to efficiently control mining')
        super().test_eth_replaceTransaction(web3, unlocked_account)

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


class GoEthereumVersionModuleTest(VersionModuleTest):
    pass


class GoEthereumNetModuleTest(NetModuleTest):
    pass


class GoEthereumPersonalModuleTest(PersonalModuleTest):
    pass
