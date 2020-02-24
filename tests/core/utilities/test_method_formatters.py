import pytest

from web3._utils.method_formatters import (
    get_error_formatters,
    get_revert_reason,
)
from web3._utils.rpc_abi import (
    RPC,
)
from web3.exceptions import (
    SolidityError,
)
from web3.types import (
    RPCResponse,
)

REVERT_WITH_MSG = RPCResponse({
    'jsonrpc': '2.0',
    'error': {
        'code': -32015,
        'message': 'VM execution error.',
        'data': (
            'Reverted '
            '0x08c379a'
            '00000000000000000000000000000000000000000000000000000000000000020'
            '0000000000000000000000000000000000000000000000000000000000000016'
            '6e6f7420616c6c6f77656420746f206d6f6e69746f7200000000000000000000'
        ),
    },
    'id': 2987,
})

REVERT_WITHOUT_MSG = RPCResponse({
    'jsonrpc': '2.0',
    'error': {
        'code': -32015,
        'message': 'VM execution error.',
        'data': 'Reverted 0x',
    },
    'id': 2987,
})

OTHER_ERROR = RPCResponse({
    "jsonrpc": "2.0",
    "error": {
        "code": -32601,
        "message": "Method not found",
    },
    "id": 1,
})


def test_get_revert_reason() -> None:
    assert get_revert_reason(REVERT_WITH_MSG) == 'not allowed to monitor'
    assert get_revert_reason(REVERT_WITHOUT_MSG) == ''
    assert get_revert_reason(OTHER_ERROR) is None


def test_get_error_formatters() -> None:
    formatters = get_error_formatters(RPC.eth_call)
    with pytest.raises(SolidityError, match='not allowed to monitor'):
        formatters(REVERT_WITH_MSG)
    with pytest.raises(SolidityError):
        formatters(REVERT_WITHOUT_MSG)
    assert formatters(OTHER_ERROR) == OTHER_ERROR
