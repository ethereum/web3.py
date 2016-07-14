from web3 import Web3


def test_setProvider(disconnected_provider):
    """
    Web3.setProvider() sets the current provider.
    """
    web3 = Web3(None)
    assert web3.currentProvider is None
    assert web3._requestManager.provider is None

    web3.setProvider(disconnected_provider)
    assert web3.currentProvider is disconnected_provider
    assert web3._requestManager.provider is disconnected_provider

    web3.setProvider(None)
    assert web3.currentProvider is None
    assert web3._requestManager.provider is None
