import pytest
import re

from eth_utils.toolz import (
    identity,
)

from web3._utils.method_formatters import (
    raise_block_not_found,
    raise_block_not_found_for_uncle_at_index,
    raise_transaction_not_found,
)
from web3.exceptions import (
    BadResponseFormat,
    BlockNotFound,
    ContractLogicError,
    MethodUnavailable,
    TransactionNotFound,
)

ERROR_RESPONSE = {
    "jsonrpc": "2.0",
    "error": {
        "code": -32000,
        "message": "Requested block number is in a range that is not available yet, "
        "because the ancient block sync is still in progress.",
    },
}
ERROR_RESPONSE_WITH_NONE_ID = {
    "id": None,
    "jsonrpc": "2.0",
    "error": {
        "code": -32000,
        "message": "Requested block number is in a range that is not available yet, "
        "because the ancient block sync is still in progress.",
    },
}
ERROR_RESPONSE_WITH_VALID_ID = {
    "id": 1,
    "jsonrpc": "2.0",
    "error": {
        "code": -32000,
        "message": "Requested block number is in a range that is not available yet, "
        "because the ancient block sync is still in progress.",
    },
}
NONE_RESPONSE = {"jsonrpc": "2.0", "id": 1, "result": None}
ZERO_X_RESPONSE = {"jsonrpc": "2.0", "id": 1, "result": "0x"}
INVALID_JSONRPC_RESP_FORMAT = {
    "jsonrpc": "999",
    "error": {
        "code": -32000,
        "message": "Requested block number is in a range that is not available yet, "
        "because the ancient block sync is still in progress.",
    },
}
UNEXPECTED_RESPONSE_FORMAT = {"jsonrpc": "2.0", "id": 1}
UNEXPECTED_RESPONSE_FORMAT_NONE_ID = {"jsonrpc": "2.0", "id": None}
ANOTHER_UNEXPECTED_RESP_FORMAT = {
    "name": "LimitError",
    "message": "You cannot query logs for more than 10000 blocks at once.",
    "method": "eth_getLogs",
}
METHOD_NOT_FOUND_RESP_FORMAT = {
    "jsonrpc": "2.0",
    "error": {
        "code": -32601,
        "message": "the method eth_getTransactionByHash does not exist/is not "
        "available",
    },
}
INVALID_CODE_RESP_FORMAT = {
    "jsonrpc": "2.0",
    "error": {
        "code": "-32601",
        "message": "the method eth_getTransactionByHash does not exist/is not "
        "available",
    },
}
MISSING_CODE_RESP_FORMAT = {
    "jsonrpc": "2.0",
    "error": {
        "message": "the method eth_getTransactionByHash does not exist/is not "
        "available",
    },
}
INVALID_MESSAGE_RESP_FORMAT = {
    "jsonrpc": "2.0",
    "error": {
        "code": -32000,
        "message": {},
    },
}
ETH_TESTER_METHOD_NOT_FOUND_RESP_FORMAT = {
    "error": "the method eth_getTransactionByHash does not exist/is not available",
}


def raise_contract_logic_error(response):
    raise ContractLogicError


@pytest.mark.parametrize(
    "response,params,error_formatters,null_result_formatters,error",
    [
        (
            # Error response with no result formatters raises a ValueError
            ERROR_RESPONSE,
            (),
            identity,
            identity,
            ValueError,
        ),
        (
            # Error response with error formatters raises error in formatter
            ERROR_RESPONSE,
            (),
            raise_contract_logic_error,
            identity,
            ContractLogicError,
        ),
        (
            # Error response with no error formatters raises ValueError
            ERROR_RESPONSE,
            (),
            identity,
            raise_block_not_found,
            ValueError,
        ),
        (
            # Error response with no result formatters raises a ValueError
            ERROR_RESPONSE_WITH_NONE_ID,
            (),
            identity,
            raise_block_not_found,
            ValueError,
        ),
        (
            # Error response with no result formatters raises a ValueError
            ERROR_RESPONSE_WITH_VALID_ID,
            (),
            identity,
            raise_block_not_found,
            ValueError,
        ),
        (
            # None result raises error if there is a null_result_formatter
            NONE_RESPONSE,
            (),
            identity,
            raise_block_not_found,
            BlockNotFound,
        ),
        (
            # Params are handled with a None result
            NONE_RESPONSE,
            ("0x03",),
            identity,
            raise_block_not_found,
            BlockNotFound,
        ),
        (
            # Multiple params are handled with a None result
            NONE_RESPONSE,
            ("0x03", "0x01"),
            identity,
            raise_block_not_found_for_uncle_at_index,
            BlockNotFound,
        ),
        (
            # Raise function handles missing param
            NONE_RESPONSE,
            ("0x01",),
            identity,
            raise_block_not_found_for_uncle_at_index,
            BlockNotFound,
        ),
        (
            # 0x response gets handled the same as a None response
            ZERO_X_RESPONSE,
            ("0x03"),
            identity,
            raise_transaction_not_found,
            TransactionNotFound,
        ),
        (
            METHOD_NOT_FOUND_RESP_FORMAT,
            (),
            identity,
            identity,
            MethodUnavailable,
        ),
        (
            ETH_TESTER_METHOD_NOT_FOUND_RESP_FORMAT,
            (),
            identity,
            identity,
            ValueError,
        ),
    ],
)
def test_formatted_response_raises_errors(
    w3, response, params, error_formatters, null_result_formatters, error
):
    with pytest.raises(error):
        w3.manager.formatted_response(
            response, params, error_formatters, null_result_formatters
        )


@pytest.mark.parametrize(
    "response,params,error_formatters,null_result_formatters,error,error_message",
    [
        (
            NONE_RESPONSE,
            ("0x01",),
            identity,
            raise_block_not_found_for_uncle_at_index,
            BlockNotFound,
            "Unknown block identifier or uncle index",
        ),
        (
            NONE_RESPONSE,
            ("0x01", "0x00"),
            identity,
            raise_block_not_found_for_uncle_at_index,
            BlockNotFound,
            "Uncle at index: 0 of block with id: '0x01' not found.",
        ),
        (
            ZERO_X_RESPONSE,
            ("0x01",),
            identity,
            raise_transaction_not_found,
            TransactionNotFound,
            "Transaction with hash: '0x01' not found.",
        ),
        (
            INVALID_JSONRPC_RESP_FORMAT,
            (),
            identity,
            identity,
            BadResponseFormat,
            f"The response was in an unexpected format and unable to be parsed. "
            f'The "jsonrpc" field must be present with a value of "2.0". '
            f"The raw response is: {INVALID_JSONRPC_RESP_FORMAT}",
        ),
        (
            UNEXPECTED_RESPONSE_FORMAT,
            (),
            identity,
            identity,
            BadResponseFormat,
            f"The response was in an unexpected format and unable to be parsed. "
            f"The raw response is: {UNEXPECTED_RESPONSE_FORMAT}",
        ),
        (
            ANOTHER_UNEXPECTED_RESP_FORMAT,
            (),
            identity,
            identity,
            BadResponseFormat,
            f"The response was in an unexpected format and unable to be parsed. "
            f"The raw response is: {ANOTHER_UNEXPECTED_RESP_FORMAT}",
        ),
        (
            INVALID_CODE_RESP_FORMAT,
            (),
            identity,
            identity,
            BadResponseFormat,
            re.escape(
                f"The response was in an unexpected format and unable to be parsed. "
                f"error['code'] must be an integer. "
                f"The raw response is: {INVALID_CODE_RESP_FORMAT}"
            ),
        ),
        (
            MISSING_CODE_RESP_FORMAT,
            (),
            identity,
            identity,
            BadResponseFormat,
            re.escape(
                f"The response was in an unexpected format and unable to be parsed. "
                f"error['code'] must be an integer. "
                f"The raw response is: {MISSING_CODE_RESP_FORMAT}"
            ),
        ),
        (
            INVALID_MESSAGE_RESP_FORMAT,
            (),
            identity,
            identity,
            BadResponseFormat,
            re.escape(
                f"The response was in an unexpected format and unable to be parsed. "
                f"error['message'] must be a string. "
                f"The raw response is: {INVALID_MESSAGE_RESP_FORMAT}"
            ),
        ),
    ],
)
def test_formatted_response_raises_correct_error_message(
    response, w3, params, error_formatters, null_result_formatters, error, error_message
):
    with pytest.raises(error, match=error_message):
        w3.manager.formatted_response(
            response, params, error_formatters, null_result_formatters
        )


@pytest.mark.parametrize(
    "response,params,error_formatters,null_result_formatters,expected",
    [
        (
            # Response with a result of None doesn't raise
            # if there is no null result formatter
            NONE_RESPONSE,
            ("0x03"),
            identity,
            identity,
            NONE_RESPONSE["result"],
        ),
        (
            # Response with a result of 0x doesn't raise
            # if there is no null result formatter
            ZERO_X_RESPONSE,
            ("0x03"),
            identity,
            identity,
            ZERO_X_RESPONSE["result"],
        ),
    ],
)
def test_formatted_response(
    response, w3, params, error_formatters, null_result_formatters, expected
):
    formatted_resp = w3.manager.formatted_response(
        response, params, error_formatters, null_result_formatters
    )
    assert formatted_resp == expected
