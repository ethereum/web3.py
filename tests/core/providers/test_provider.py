import pytest as pytest

from eth_tester.exceptions import (
    TransactionFailed,
)

from web3 import (
    EthereumTesterProvider,
    Web3,
)
from web3.providers import (
    AutoProvider,
    BaseProvider,
)
from web3.types import (
    RPCEndpoint,
)


class ConnectedProvider(BaseProvider):
    def is_connected(self):
        return True


class DisconnectedProvider(BaseProvider):
    def is_connected(self):
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
        assert False

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


@pytest.mark.parametrize(
    "exception_case",
    (
        # exception with bytes-encoded reason:
        TransactionFailed(
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12The error message.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"  # noqa: E501
        ),
        # wrapped exceptions with bytes-encoded reason:
        TransactionFailed(
            Exception(
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12The error message.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"  # noqa: E501
            )
        ),
        TransactionFailed("The error message."),
        TransactionFailed(Exception("The error message.")),
    ),
)
def test_eth_tester_provider_properly_handles_eth_tester_error_messages(
    mocker,
    exception_case,
):
    mocker.patch(
        "eth_tester.main.EthereumTester.get_block_by_number", side_effect=exception_case
    )

    provider = EthereumTesterProvider()
    with pytest.raises(
        TransactionFailed, match="execution reverted: The error message."
    ):
        provider.make_request(RPCEndpoint("eth_blockNumber"), [])
