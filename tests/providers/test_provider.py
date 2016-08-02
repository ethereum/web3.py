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


def test_isConnected(web3):
    """
    Web3.isConnected() returns True when connected to a node.
    """
    assert web3.isConnected() is True


def test_isConnected_no_provider():
    """
    Web3.isConnected() returns False when not configured with a provider.
    """
    web3 = Web3(None)
    assert web3.isConnected() is False


def test_isConnected_disconnected(disconnected_provider):
    """
    Web3.isConnected() returns False when configured with a provider
    that's not connected to a node.
    """
    web3 = Web3(disconnected_provider)
    assert web3.isConnected() is False
