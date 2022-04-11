import pytest
from typing import (
    TYPE_CHECKING,
)

from eth_typing import (
    ChecksumAddress,
)
from flaky import (
    flaky,
)

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

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        Web3,
    )


class GoEthereumTest(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('Geth/')


class GoEthereumEthModuleTest(EthModuleTest):
    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_eth_sign_typed_data(self, w3, unlocked_account_dual_type):
        super().test_eth_sign_typed_data(w3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_eth_signTypedData_deprecated(self, w3, unlocked_account_dual_type):
        super().test_eth_signTypedData_deprecated(w3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_invalid_eth_sign_typed_data(self, w3, unlocked_account_dual_type):
        super().test_invalid_eth_sign_typed_data(w3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='eth_protocolVersion was removed in Geth 1.10.0')
    def test_eth_protocol_version(self, w3):
        super().test_eth_protocol_version(w3)

    @pytest.mark.xfail(reason='eth_protocolVersion was removed in Geth 1.10.0')
    def test_eth_protocolVersion(self, w3):
        super().test_eth_protocolVersion(w3)

    @flaky(max_runs=3)
    def test_eth_estimate_gas(
        self, w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_estimate_gas(w3, unlocked_account_dual_type)

    @flaky(max_runs=3)
    def test_eth_estimateGas_deprecated(
        self, w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_estimateGas_deprecated(w3, unlocked_account_dual_type)

    @flaky(max_runs=3)
    def test_eth_estimate_gas_with_block(
        self, w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_estimate_gas_with_block(w3, unlocked_account_dual_type)


class GoEthereumVersionModuleTest(VersionModuleTest):
    @pytest.mark.xfail(reason='eth_protocolVersion was removed in Geth 1.10.0')
    def test_eth_protocol_version(self, w3):
        super().test_eth_protocol_version(w3)

    @pytest.mark.xfail(reason='eth_protocolVersion was removed in Geth 1.10.0')
    def test_eth_protocolVersion(self, w3):
        super().test_eth_protocolVersion(w3)


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
