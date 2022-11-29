import pytest

from web3._utils.method_formatters import (
    get_error_formatters,
    raise_contract_logic_error_on_revert,
)
from web3._utils.rpc_abi import (
    RPC,
)
from web3.exceptions import (
    ContractLogicError,
)
from web3.types import (
    RPCResponse,
)

# OpenEthereum/default case:
REVERT_WITH_MSG = RPCResponse(
    {
        "jsonrpc": "2.0",
        "error": {
            "code": -32015,
            "message": "VM execution error.",
            "data": (
                "Reverted "
                "0x08c379a"
                "00000000000000000000000000000000000000000000000000000000000000020"
                "0000000000000000000000000000000000000000000000000000000000000016"
                "6e6f7420616c6c6f77656420746f206d6f6e69746f7200000000000000000000"
            ),
        },
        "id": 2987,
    }
)

REVERT_WITHOUT_MSG = RPCResponse(
    {
        "jsonrpc": "2.0",
        "error": {
            "code": -32015,
            "message": "VM execution error.",
            "data": "Reverted 0x",
        },
        "id": 2987,
    }
)

OTHER_ERROR = RPCResponse(
    {
        "jsonrpc": "2.0",
        "error": {
            "code": -32601,
            "message": "Method not found",
        },
        "id": 1,
    }
)

GETH_RESPONSE = RPCResponse(
    {
        "jsonrpc": "2.0",
        "id": 2,
        "error": {
            "code": 3,
            "message": "execution reverted: Function has been reverted.",
            "data": (
                "0x08c379a0000000000000000000000000000000000000000000000"
                "0000000000000000020000000000000000000000000000000000000"
                "000000000000000000000000001b46756e6374696f6e20686173206"
                "265656e2072657665727465642e0000000000"
            ),
        },
    }
)

GANACHE_RESPONSE = RPCResponse(
    {
        "id": 24,
        "jsonrpc": "2.0",
        "error": {
            "message": "VM Exception while processing transaction: revert Custom revert message",  # noqa: E501
            "code": -32000,
            "data": {
                "stack": "o: VM Exception while processing transaction: revert Custom revert message\n",  # noqa: E501
                "name": "o",
            },
        },
    }
)


SPACENETH_RESPONSE = RPCResponse(
    {
        "name": "Error",
        "message": "Internal JSON-RPC error.",
        "stack": "Error: Internal JSON-RPC error",
        "code": -32603,
        "data": {
            "code": -32015,
            "message": "Reverted 0x4d6172656b74706c6163653a3a63616e63656c4d61726b65744974656d3a20494e56414c49445f4954454d",
        },
    }
)


@pytest.mark.parametrize(
    "response,expected",
    (
        (REVERT_WITH_MSG, "execution reverted: not allowed to monitor"),
        (REVERT_WITHOUT_MSG, "execution reverted"),
        (GETH_RESPONSE, "execution reverted: Function has been reverted."),
        (
            GANACHE_RESPONSE,
            "execution reverted: VM Exception while processing transaction: revert Custom revert message",  # noqa: 501
        ),
        (
            SPACENETH_RESPONSE,
            "execution reverted: Marektplace::cancelMarketItem: INVALID_ITEM",
        ),
    ),
    ids=[
        "test-get-revert-reason-with-msg",
        "test-get-revert-reason-without-msg",
        "test-get-geth-revert-reason",
        "test_get-ganache-revert-reason",
    ],
)
def test_get_revert_reason(response, expected) -> None:
    with pytest.raises(ContractLogicError, match=expected):
        raise_contract_logic_error_on_revert(response)


def test_get_revert_reason_other_error() -> None:
    assert raise_contract_logic_error_on_revert(OTHER_ERROR) is OTHER_ERROR


def test_get_error_formatters() -> None:
    formatters = get_error_formatters(RPC.eth_call)
    with pytest.raises(ContractLogicError, match="not allowed to monitor"):
        formatters(REVERT_WITH_MSG)
    with pytest.raises(ContractLogicError):
        formatters(REVERT_WITHOUT_MSG)
    assert formatters(OTHER_ERROR) == OTHER_ERROR
