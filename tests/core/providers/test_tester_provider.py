import pytest as pytest

from eth_abi.exceptions import (
    DecodingError,
    InsufficientDataBytes,
    NonEmptyPaddingBytes,
)
from eth_tester.exceptions import (
    TransactionFailed,
)

from web3 import (
    EthereumTesterProvider,
)
from web3.types import (
    RPCEndpoint,
)


def test_tester_provider_is_connected() -> None:
    provider = EthereumTesterProvider()
    connected = provider.is_connected()
    assert connected


def test_tester_provider_creates_a_block() -> None:
    provider = EthereumTesterProvider()
    accounts = provider.make_request("eth_accounts", [])
    a, b = accounts["result"][:2]
    current_block = provider.make_request("eth_blockNumber", [])
    assert current_block["result"] == 0
    tx = provider.make_request(
        "eth_sendTransaction", [{"from": a, "to": b, "gas": 21000}]
    )
    assert tx
    current_block = provider.make_request("eth_blockNumber", [])
    assert current_block["result"] == 1


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


def test_eth_tester_provider_properly_handles_eth_tester_key_error_messages():
    provider = EthereumTesterProvider(api_endpoints={})
    response = provider.make_request(RPCEndpoint("eth_blockNumber"), [])

    assert response["error"]["code"] == -32601
    assert response["error"]["message"] == "Unknown RPC Endpoint: eth_blockNumber"


def test_eth_tester_provider_properly_handles_eth_tester_not_implmented_error_messages(
    mocker,
):
    mocker.patch(
        "eth_tester.main.EthereumTester.get_block_by_number",
        side_effect=NotImplementedError("The error message."),
    )

    provider = EthereumTesterProvider()
    response = provider.make_request(RPCEndpoint("eth_blockNumber"), [])

    assert response["error"]["code"] == -32601
    assert (
        response["error"]["message"]
        == "RPC Endpoint has not been implemented: eth_blockNumber"
    )


@pytest.mark.parametrize(
    "exception_type",
    (
        DecodingError,
        InsufficientDataBytes,
        NonEmptyPaddingBytes,
    ),
)
def test_eth_tester_provider_properly_handles_transaction_failed_with_decode_error(
    exception_type,
    mocker,
):
    mocker.patch(
        "eth_tester.main.EthereumTester.get_block_by_number",
        side_effect=TransactionFailed(b"0x1234"),
    )
    mocker.patch("eth_abi.abi.decode", side_effect=exception_type())

    provider = EthereumTesterProvider()
    with pytest.raises(TransactionFailed, match="execution reverted: b'0x1234'"):
        # Assert that parametrized ``exception_type`` exception is caught and that
        # the original message is re-raised inside a ``TransactionFailed``.
        provider.make_request(RPCEndpoint("eth_blockNumber"), [])
