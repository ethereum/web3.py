import pytest

from web3._utils.module_testing import (  # noqa: F401
    EthModuleTest,
    GoEthereumPersonalModuleTest,
    NetModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)

GETH_17_SIGNED_TX = b'\xf8j\x80\x85\x040\xe24\x00\x82R\x08\x94\xdcTM\x1a\xa8\x8f\xf8\xbb\xd2\xf2\xae\xc7T\xb1\xf1\xe9\x9e\x18\x12\xfd\x01\x80\x86\xee\xca\xc4f\xe1\x16\xa0\xbb7^\x1f\xf0\x03(P\x07|\x053Q\xd3M\xf1\x83\xe9\xdcp\xdc\x02\xb4\xe7`\x85\xcd\x84\xdb\xb4\xd0\xaa\xa07\x8cl\xd7\xa6R\x01\xfaW\x0e\x0f\xc1_$\xdf`\x8dO\x18\x1dC\xbc\x87\x8fud\xd2R*W\xfd4'  # noqa: E501
GETH_18_SIGNED_TX = b'\xf8i\x80\x84;\x9a\xca\x00\x82R\x08\x94\xdcTM\x1a\xa8\x8f\xf8\xbb\xd2\xf2\xae\xc7T\xb1\xf1\xe9\x9e\x18\x12\xfd\x01\x80\x86\xee\xca\xc4f\xe1\x16\xa0W\x91\xe6a\xb7l\x93,\xd3\xdd?;\xa8\x0e\xd3\xbe\x04\x89(\xd49\x1e+\xd6\xee\x88k\xfb\xe7\x83\xeb(\xa0\x04\x9a%`\x91uc\x1a\xdd\xb8\x96\xbb\x10\xb5v|\xcf\x03\xb6\x90\xbb\x93x\xfef\xae\xe1L\xbc7\xafJ'  # noqa: E501


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

    def test_eth_estimateGas_with_block(self,
                                        web3,
                                        unlocked_account_dual_type):
        pytest.xfail('Block identifier has not been implemented in geth')
        super().test_eth_estimateGas_with_block(
            web3, unlocked_account_dual_type
        )

    def test_eth_signTransaction(self, web3, unlocked_account):
        if 'v1.8.22' in web3.clientVersion:
            super().test_eth_signTransaction(web3, unlocked_account, GETH_18_SIGNED_TX)
        else:
            super().test_eth_signTransaction(web3, unlocked_account, GETH_17_SIGNED_TX)

    def test_eth_submitHashrate(self, web3):
        if 'v1.8.22' in web3.clientVersion:
            # https://github.com/ethereum/go-ethereum/commit/51db5975cc5fb88db6a0dba1826b534fd4df29d7
            pytest.xfail('eth_submitHashrate endpoint updated in 1.8.22 to ethash_submitHashRate')
        super().test_eth_submitHashrate(web3)


class GoEthereumVersionModuleTest(VersionModuleTest):
    pass


class GoEthereumNetModuleTest(NetModuleTest):
    pass
