import pytest

from eth_utils.toolz import (
    identity,
)

from web3._utils.method_formatters import (
    raise_block_not_found,
    raise_block_not_found_for_uncle_at_index,
)
from web3.exceptions import (
    BlockNotFound,
    ContractLogicError,
)

ERROR_RESPONSE = {
    'jsonrpc': '2.0',
    'error': {
        'code': -32000,
        'message': 'Requested block number is in a range that is not available yet, '
                   'because the ancient block sync is still in progress.'
    }
}


NONE_RESPONSE = {"jsonrpc": "2.0", "id": 1, "result": None}


def raise_contract_logic_error(response):
    raise ContractLogicError


@pytest.mark.parametrize(
    'response,params,error_formatters,null_result_formatters,error',
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
            ('0x03',),
            identity,
            raise_block_not_found,
            BlockNotFound,
        ),
        (
            # Multiple params are handled with a None result
            NONE_RESPONSE,
            ('0x03', '0x01'),
            identity,
            raise_block_not_found_for_uncle_at_index,
            BlockNotFound,
        ),
        (
            # Raise function handles missing param
            NONE_RESPONSE,
            ('0x01',),
            identity,
            raise_block_not_found_for_uncle_at_index,
            BlockNotFound,
        ),
    ],
)
def test_formatted_response_raises_errors(web3,
                                          response,
                                          params,
                                          error_formatters,
                                          null_result_formatters,
                                          error):
    with pytest.raises(error):
        web3.manager.formatted_response(response,
                                        params,
                                        error_formatters,
                                        null_result_formatters)


@pytest.mark.parametrize(
    'response,params,error_formatters,null_result_formatters,error,error_message',
    [
        (
            NONE_RESPONSE,
            ('0x01',),
            identity,
            raise_block_not_found_for_uncle_at_index,
            BlockNotFound,
            "Unknown block identifier or uncle index",
        ),
        (
            NONE_RESPONSE,
            ('0x01', '0x00'),
            identity,
            raise_block_not_found_for_uncle_at_index,
            BlockNotFound,
            "Uncle at index: 0 of block with id: '0x01' not found."
        ),
    ],
)
def test_formatted_response_raises_correct_error_message(response,
                                                         web3,
                                                         params,
                                                         error_formatters,
                                                         null_result_formatters,
                                                         error,
                                                         error_message):

    with pytest.raises(error, match=error_message):
        web3.manager.formatted_response(response, params, error_formatters, null_result_formatters)


@pytest.mark.parametrize(
    'response,params,error_formatters,null_result_formatters,expected',
    [
        (
            # Response with a result of None doesn't raise if there is no null result formatter
            NONE_RESPONSE,
            ('0x03'),
            identity,
            identity,
            NONE_RESPONSE['result'],
        ),
    ],
)
def test_formatted_response(response,
                            web3,
                            params,
                            error_formatters,
                            null_result_formatters,
                            expected):

    formatted_resp = web3.manager.formatted_response(response,
                                                     params,
                                                     error_formatters,
                                                     null_result_formatters)
    assert formatted_resp == expected
