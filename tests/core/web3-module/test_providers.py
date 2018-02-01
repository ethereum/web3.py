from web3 import Web3
from web3.providers.auto import (
    AutoProvider,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


def test_set_providers(web3):
    providers = [EthereumTesterProvider()]

    web3.providers = providers

    assert web3.providers == providers


def test_set_providers_single(web3):
    providers = [EthereumTesterProvider()]

    web3.providers = providers[0]

    assert web3.providers == providers


def test_auto_provider_none():
    # init without provider succeeds, even when no provider available
    w3 = Web3()

    # non-node requests succeed
    w3.toHex(0) == '0x0'

    type(w3.providers[0]) == AutoProvider
