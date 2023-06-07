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
    def _check_web3_client_version(self, client_version):
        assert client_version.startswith("Geth/")


class GoEthereumEthModuleTest(EthModuleTest):
    @pytest.mark.xfail(reason="eth_signTypedData has not been released in geth")
    def test_eth_sign_typed_data(self, w3, unlocked_account_dual_type):
        super().test_eth_sign_typed_data(w3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason="eth_signTypedData has not been released in geth")
    def test_invalid_eth_sign_typed_data(self, w3, unlocked_account_dual_type):
        super().test_invalid_eth_sign_typed_data(w3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason="Inconsistently creating timeout issues.", strict=False)
    def test_eth_estimate_gas(
        self, w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_estimate_gas(w3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason="Inconsistently creating timeout issues.", strict=False)
    def test_eth_estimate_gas_with_block(
        self, w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_estimate_gas_with_block(w3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason="Inconsistently creating timeout issues.", strict=False)
    def test_eth_get_transaction_receipt_unmined(
        self, w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_get_transaction_receipt_unmined(w3, unlocked_account_dual_type)

    @pytest.mark.xfail(reason="Inconsistently creating timeout issues.", strict=False)
    def test_eth_wait_for_transaction_receipt_unmined(
        self, w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        super().test_eth_wait_for_transaction_receipt_unmined(
            w3, unlocked_account_dual_type
        )

    @pytest.mark.xfail(reason="Inconsistently creating timeout issues.", strict=False)
    def test_eth_get_raw_transaction_by_block(
        self,
        w3: "Web3",
        unlocked_account_dual_type: ChecksumAddress,
        block_with_txn: BlockData,
    ) -> None:
        super().test_eth_get_raw_transaction_by_block(
            w3, unlocked_account_dual_type, block_with_txn
        )


class GoEthereumNetModuleTest(NetModuleTest):
    pass


class GoEthereumAsyncNetModuleTest(AsyncNetModuleTest):
    pass


class GoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    pass


class GoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass


class GoEthereumAsyncEthModuleTest(AsyncEthModuleTest):
    @pytest.mark.xfail(reason="eth_signTypedData has not been released in geth")
    async def test_eth_sign_typed_data(
        self, async_w3, unlocked_account_dual_type, async_skip_if_testrpc
    ):
        await super().test_eth_sign_typed_data(
            async_w3, unlocked_account_dual_type, async_skip_if_testrpc
        )

    @pytest.mark.xfail(reason="eth_signTypedData has not been released in geth")
    async def test_invalid_eth_sign_typed_data(
        self, async_w3, unlocked_account_dual_type, async_skip_if_testrpc
    ):
        await super().test_invalid_eth_sign_typed_data(
            async_w3, unlocked_account_dual_type, async_skip_if_testrpc
        )
