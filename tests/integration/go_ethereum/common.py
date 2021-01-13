from concurrent.futures._base import (
    TimeoutError as FuturesTimeoutError,
)
import pytest

from web3._utils.module_testing import (  # noqa: F401
    EthModuleTest,
    GoEthereumAdminModuleTest,
    GoEthereumPersonalModuleTest,
    NetModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)


class GoEthereumTest(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('Geth/')


class GoEthereumEthModuleTest(EthModuleTest):
    @pytest.mark.xfail(reason='eth_submitHashrate deprecated in 1.8.22 for ethash_submitHashRate')
    def test_eth_submitHashrate(self, web3):
        # https://github.com/ethereum/go-ethereum/commit/51db5975cc5fb88db6a0dba1826b534fd4df29d7
        super().test_eth_submitHashrate(web3)

    @pytest.mark.xfail(
        strict=False,
        raises=FuturesTimeoutError,
        reason='Sometimes a TimeoutError is hit when waiting for the txn to be mined',
    )
    def test_eth_replaceTransaction_already_mined(self, web3, unlocked_account_dual_type):
        web3.geth.miner.start()
        super().test_eth_replaceTransaction_already_mined(web3, unlocked_account_dual_type)
        web3.geth.miner.stop()

    @pytest.mark.xfail(reason='Block identifier has not been implemented in geth')
    def test_eth_estimateGas_with_block(self,
                                        web3,
                                        unlocked_account_dual_type):
        super().test_eth_estimateGas_with_block(
            web3, unlocked_account_dual_type
        )

    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_eth_signTypedData(self,
                               web3,
                               unlocked_account_dual_type):
        super().test_eth_signTypedData(
            web3, unlocked_account_dual_type
        )

    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_invalid_eth_signTypedData(self,
                                       web3,
                                       unlocked_account_dual_type):
        super().test_invalid_eth_signTypedData(
            web3, unlocked_account_dual_type
        )


class GoEthereumVersionModuleTest(VersionModuleTest):
    pass


class GoEthereumNetModuleTest(NetModuleTest):
    pass


class GoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    pass


class GoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass
