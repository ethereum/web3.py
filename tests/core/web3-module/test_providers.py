from web3 import Web3
from web3.providers.auto import (
    AutoProvider,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


def test_set_provider(w3):
    provider = EthereumTesterProvider()

    w3.provider = provider

    assert w3.provider == provider


def test_auto_provider_none():
    # init without provider succeeds, even when no provider available
    w3 = Web3()

    # non-node requests succeed
    w3.toHex(0) == '0x0'

    type(w3.provider) == AutoProvider


def test_provider_default_value_for_ccip_read_redirect(w3):
    assert w3.provider.ccip_read_calls_enabled
    assert w3.provider.ccip_read_max_redirects == 4
