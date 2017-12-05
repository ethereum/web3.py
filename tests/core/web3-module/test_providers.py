from web3.providers.eth_tester import EthereumTesterProvider


def test_set_providers(web3):
    providers = [EthereumTesterProvider()]

    web3.providers = providers

    assert web3.providers == providers


def test_set_providers_single(web3):
    providers = [EthereumTesterProvider()]

    web3.providers = providers[0]

    assert web3.providers == providers
