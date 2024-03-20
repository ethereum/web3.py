from web3 import (
    Web3,
)
from web3.providers import (
    AutoProvider,
    BaseProvider,
)


class ConnectedProvider(BaseProvider):
    def is_connected(self, show_traceback: bool = False):
        return True


class DisconnectedProvider(BaseProvider):
    def is_connected(self, show_traceback: bool = False):
        return False


def test_is_connected_connected():
    """
    Web3.is_connected() returns True when connected to a node.
    """
    w3 = Web3(ConnectedProvider())
    assert w3.is_connected() is True


def test_is_connected_disconnected():
    """
    Web3.is_connected() returns False when configured with a provider
    that's not connected to a node.
    """
    w3 = Web3(DisconnectedProvider())
    assert w3.is_connected() is False


def test_autoprovider_detection():
    def no_provider():
        return None

    def must_not_call():
        raise AssertionError

    auto = AutoProvider(
        [
            no_provider,
            DisconnectedProvider,
            ConnectedProvider,
            must_not_call,
        ]
    )

    w3 = Web3(auto)

    assert w3.is_connected()

    assert isinstance(auto._active_provider, ConnectedProvider)
