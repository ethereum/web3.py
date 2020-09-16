from web3 import Web3
from web3.providers import (
    AutoProvider,
    BaseProvider,
)


class ConnectedProvider(BaseProvider):
    def isConnected(self):
        return True


class DisconnectedProvider(BaseProvider):
    def isConnected(self):
        return False


def test_isConnected_connected():
    """
    Web3.isConnected() returns True when connected to a node.
    """
    web3 = Web3(ConnectedProvider())
    assert web3.isConnected() is True


def test_isConnected_disconnected():
    """
    Web3.isConnected() returns False when configured with a provider
    that's not connected to a node.
    """
    web3 = Web3(DisconnectedProvider())
    assert web3.isConnected() is False


def test_autoprovider_detection():
    def no_provider():
        return None

    def must_not_call():
        assert False

    auto = AutoProvider([
        no_provider,
        DisconnectedProvider,
        ConnectedProvider,
        must_not_call,
    ])

    w3 = Web3(auto)

    assert w3.isConnected()

    assert isinstance(auto._active_provider, ConnectedProvider)
