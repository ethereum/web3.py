import pytest

from web3._utils.module_testing import (  # noqa: F401
    AsyncEthModuleTest,
    AsyncNetModuleTest,
    EthModuleTest,
    GoEthereumAdminModuleTest,
    GoEthereumAsyncTxPoolModuleTest,
    GoEthereumPersonalModuleTest,
    GoEthereumTxPoolModuleTest,
    NetModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)


class GoEthereumTest(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('Geth/')


class GoEthereumEthModuleTest(EthModuleTest):
    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_eth_sign_typed_data(self, web3, unlocked_account_dual_type):
        super().test_eth_sign_typed_data(web3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_eth_signTypedData_deprecated(self, web3, unlocked_account_dual_type):
        super().test_eth_signTypedData_deprecated(web3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_invalid_eth_sign_typed_data(self, web3, unlocked_account_dual_type):
        super().test_invalid_eth_sign_typed_data(web3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='eth_protocolVersion was removed in Geth 1.10.0')
    def test_eth_protocol_version(self, web3):
        super().test_eth_protocol_version(web3)

    @pytest.mark.xfail(reason='eth_protocolVersion was removed in Geth 1.10.0')
    def test_eth_protocolVersion(self, web3):
        super().test_eth_protocolVersion(web3)


class GoEthereumVersionModuleTest(VersionModuleTest):
    @pytest.mark.xfail(reason='eth_protocolVersion was removed in Geth 1.10.0')
    def test_eth_protocol_version(self, web3):
        super().test_eth_protocol_version(web3)

    @pytest.mark.xfail(reason='eth_protocolVersion was removed in Geth 1.10.0')
    def test_eth_protocolVersion(self, web3):
        super().test_eth_protocolVersion(web3)


class GoEthereumNetModuleTest(NetModuleTest):
    pass


class GoEthereumAsyncNetModuleTest(AsyncNetModuleTest):
    pass


class GoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    pass


class GoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass


class GoEthereumAsyncEthModuleTest(AsyncEthModuleTest):
    pass
