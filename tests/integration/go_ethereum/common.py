import pytest
from typing import (
    TYPE_CHECKING,
)

from eth_typing import (
    ChecksumAddress,
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
from web3.types import (
    BlockData,
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

    @pytest.mark.xfail(reason='Inconsistently creating timeout issues.', strict=False)
    def test_eth_estimate_gas(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_estimate_gas(web3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='Inconsistently creating timeout issues.', strict=False)
    def test_eth_estimateGas_deprecated(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_estimateGas_deprecated(web3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='Inconsistently creating timeout issues.', strict=False)
    def test_eth_estimate_gas_with_block(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_estimate_gas_with_block(web3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='Inconsistently creating timeout issues.', strict=False)
    def test_eth_get_transaction_receipt_unmined(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_get_transaction_receipt_unmined(web3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='Inconsistently creating timeout issues.', strict=False)
    def test_eth_wait_for_transaction_receipt_unmined(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_wait_for_transaction_receipt_unmined(web3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason='Inconsistently creating timeout issues.', strict=False)
    def test_eth_get_raw_transaction_by_block(
        self, web3: "Web3",
        unlocked_account_dual_type: ChecksumAddress,
        block_with_txn: BlockData,
    ) -> None:
        super().test_eth_get_raw_transaction_by_block(
            web3, unlocked_account_dual_type, block_with_txn
        )


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
