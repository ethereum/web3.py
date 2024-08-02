import pytest
from typing import (
    cast,
)

from eth_tester import (
    EELSBackend,
    EthereumTester,
)
from eth_typing import (
    ChecksumAddress,
)

from web3 import (
    Web3,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.types import (  # noqa: F401
    BlockData,
)

from .common import (
    EthereumTesterEthModule,
    EthereumTesterNetModule,
    EthereumTesterWeb3Module,
)


def _eth_tester_state_setup(w3, keyfile_account_address, keyfile_account_pkey):
    provider = cast(EthereumTesterProvider, w3.provider)
    provider.ethereum_tester.add_account(keyfile_account_pkey)

    # fund the account
    w3.eth.send_transaction(
        {
            "from": ChecksumAddress(w3.eth.default_account),
            "to": keyfile_account_address,
            "value": w3.to_wei(0.5, "ether"),
            "gas": 21000,
            "gasPrice": 10**9,  # needs to be > base_fee post London
        }
    )


@pytest.fixture(scope="module")
def eth_tester():
    return EthereumTester(backend=EELSBackend(debug_mode=True))


@pytest.fixture(scope="module")
def w3(eth_tester, keyfile_account_address, keyfile_account_pkey):
    _w3 = Web3(EthereumTesterProvider(eth_tester))
    _w3.eth.default_account = _w3.eth.accounts[0]
    _eth_tester_state_setup(_w3, keyfile_account_address, keyfile_account_pkey)
    return _w3


# -- test classes -- #


class TestEthereumTesterWeb3Module(EthereumTesterWeb3Module):
    pass


class TestEthereumTesterEthModule(EthereumTesterEthModule):
    def test_eth_chain_id(self, w3):
        chain_id = w3.eth.chain_id
        assert chain_id == 1

    @pytest.mark.xfail(reason="EELS backed does not yet support eth_feeHistory")
    def test_eth_fee_history(self, w3: "Web3") -> None:
        super().test_eth_fee_history(w3)

    @pytest.mark.xfail(reason="EELS backed does not yet support eth_feeHistory")
    def test_eth_fee_history_with_integer(
        self, w3: "Web3", empty_block: BlockData
    ) -> None:
        super().test_eth_fee_history_with_integer(w3, empty_block)

    @pytest.mark.xfail(reason="EELS backed does not yet support eth_feeHistory")
    def test_eth_fee_history_no_reward_percentiles(self, w3: "Web3") -> None:
        super().test_eth_fee_history_no_reward_percentiles(w3)


class TestEthereumTesterNetModule(EthereumTesterNetModule):
    pass
