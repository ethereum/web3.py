from __future__ import absolute_import

import codecs
import operator

from cytoolz.curried import (
    keymap,
    valmap,
)
from cytoolz.functoolz import (
    compose,
    complement,
    partial,
)

from eth_utils import (
    is_address,
    to_normalized_address,
    is_integer,
    is_null,
    is_dict,
    is_string,
    is_bytes,
    is_list_like,
    encode_hex,
)

from web3.utils.formatters import (
    hex_to_integer,
    integer_to_hex,
    apply_formatter_if,
    apply_formatters_to_dict,
    apply_formatter_to_array,
    apply_formatter_at_index,
    apply_one_of_formatters,
)

from .formatting import (
    construct_formatting_middleware,
)


def bytes_to_ascii(value):
    return codecs.decode(value, 'ascii')


to_ascii_if_bytes = apply_formatter_if(bytes_to_ascii, is_bytes)
to_integer_if_hex = apply_formatter_if(hex_to_integer, is_string)
block_number_formatter = apply_formatter_if(integer_to_hex, is_integer)


is_false = partial(operator.is_, False)

is_not_false = complement(is_false)
is_not_null = complement(is_null)


# TODO: decide what inputs this allows.
TRANSACTION_PARAMS_FORMATTERS = {
    'value': integer_to_hex,
    'gas': integer_to_hex,
    'gasPrice': integer_to_hex,
    'nonce': integer_to_hex,
}


transaction_params_formatter = apply_formatters_to_dict(TRANSACTION_PARAMS_FORMATTERS)


def is_array_of_strings(value):
    if not is_list_like(value):
        return False
    return all((is_string(item) for item in value))


def is_array_of_dicts(value):
    if not is_list_like(value):
        return False
    return all((is_dict(item) for item in value))


TRANSACTION_FORMATTERS = {
    'blockNumber': apply_formatter_if(to_integer_if_hex, is_not_null),
    'transactionIndex': apply_formatter_if(to_integer_if_hex, is_not_null),
    'nonce': to_integer_if_hex,
    'gas': to_integer_if_hex,
    'gasPrice': to_integer_if_hex,
    'value': to_integer_if_hex,
    'from': to_normalized_address,
    'to': apply_formatter_if(to_normalized_address, is_address),
    'hash': to_ascii_if_bytes,
}


transaction_formatter = apply_formatters_to_dict(TRANSACTION_FORMATTERS)


LOG_ENTRY_FORMATTERS = {
    'blockHash': apply_formatter_if(to_ascii_if_bytes, is_not_null),
    'blockNumber': apply_formatter_if(to_integer_if_hex, is_not_null),
    'transactionIndex': apply_formatter_if(to_integer_if_hex, is_not_null),
    'logIndex': to_integer_if_hex,
    'address': to_normalized_address,
    'topics': apply_formatter_to_array(to_ascii_if_bytes),
    'data': to_ascii_if_bytes,
}


log_entry_formatter = apply_formatters_to_dict(LOG_ENTRY_FORMATTERS)


RECEIPT_FORMATTERS = {
    'blockHash': apply_formatter_if(to_ascii_if_bytes, is_not_null),
    'blockNumber': apply_formatter_if(to_integer_if_hex, is_not_null),
    'transactionIndex': apply_formatter_if(to_integer_if_hex, is_not_null),
    'transactionHash': to_ascii_if_bytes,
    'cumulativeGasUsed': to_integer_if_hex,
    'gasUsed': to_integer_if_hex,
    'contractAddress': apply_formatter_if(to_normalized_address, is_not_null),
    'logs': apply_formatter_to_array(log_entry_formatter),
}


receipt_formatter = apply_formatters_to_dict(RECEIPT_FORMATTERS)

BLOCK_FORMATTERS = {
    'gasLimit': to_integer_if_hex,
    'gasUsed': to_integer_if_hex,
    'size': to_integer_if_hex,
    'timestamp': to_integer_if_hex,
    'hash': to_ascii_if_bytes,
    'number': apply_formatter_if(to_integer_if_hex, is_not_null),
    'difficulty': to_integer_if_hex,
    'totalDifficulty': to_integer_if_hex,
    'transactions': apply_one_of_formatters((
        (apply_formatter_to_array(transaction_formatter), is_array_of_dicts),
        (apply_formatter_to_array(to_ascii_if_bytes), is_array_of_strings),
    )),
}


block_formatter = apply_formatters_to_dict(BLOCK_FORMATTERS)


SYNCING_FORMATTERS = {
    'startingBlock': to_integer_if_hex,
    'currentBlock': to_integer_if_hex,
    'highestBlock': to_integer_if_hex,
    'knownStates': to_integer_if_hex,
    'pulledStates': to_integer_if_hex,
}


syncing_formatter = apply_formatters_to_dict(SYNCING_FORMATTERS)


TRANSACTION_POOL_CONTENT_FORMATTERS = {
    'pending': compose(
        keymap(to_ascii_if_bytes),
        valmap(transaction_formatter),
    ),
    'queued': compose(
        keymap(to_ascii_if_bytes),
        valmap(transaction_formatter),
    ),
}


transaction_pool_content_formatter = apply_formatters_to_dict(
    TRANSACTION_POOL_CONTENT_FORMATTERS
)


TRANSACTION_POOL_INSPECT_FORMATTERS = {
    'pending': keymap(to_ascii_if_bytes),
    'queued': keymap(to_ascii_if_bytes),
}


transaction_pool_inspect_formatter = apply_formatters_to_dict(
    TRANSACTION_POOL_INSPECT_FORMATTERS
)


FILTER_PARAMS_FORMATTERS = {
    'fromBlock': apply_formatter_if(integer_to_hex, is_integer),
    'toBlock': apply_formatter_if(integer_to_hex, is_integer),
}


filter_params_formatter = apply_formatters_to_dict(FILTER_PARAMS_FORMATTERS)


def is_array_of_dicts(value):
    if not is_list_like(value):
        return False
    return all((is_dict(item) for item in value))


def is_array_of_strings(value):
    if not is_list_like(value):
        return False
    return all((is_string(item) for item in value))


filter_result_formatter = apply_one_of_formatters((
    (apply_formatter_to_array(log_entry_formatter), is_array_of_dicts),
    (apply_formatter_to_array(to_ascii_if_bytes), is_array_of_strings),
))


pythonic_middleware = construct_formatting_middleware(
    request_formatters={
        # Eth
        'eth_call': apply_formatter_at_index(transaction_params_formatter, 0),
        'eth_getBalance': apply_formatter_at_index(block_number_formatter, 1),
        'eth_getBlockByNumber': apply_formatter_at_index(block_number_formatter, 0),
        'eth_getBlockTransactionCountByNumber': apply_formatter_at_index(
            block_number_formatter,
            0,
        ),
        'eth_getBlockTransactionCountByHash': apply_formatter_at_index(
            block_number_formatter,
            0,
        ),
        'eth_getCode': apply_formatter_at_index(block_number_formatter, 1),
        'eth_getStorageAt': compose(
            apply_formatter_at_index(integer_to_hex, 1),
            apply_formatter_at_index(block_number_formatter, 2),
        ),
        'eth_getTransactionByBlockNumberAndIndex': compose(
            apply_formatter_at_index(block_number_formatter, 0),
            apply_formatter_at_index(integer_to_hex, 1),
        ),
        'eth_getTransactionByBlockHashAndIndex': apply_formatter_at_index(integer_to_hex, 1),
        'eth_getTransactionCount': apply_formatter_at_index(block_number_formatter, 1),
        'eth_getUncleCountByBlockNumber': apply_formatter_at_index(block_number_formatter, 0),
        'eth_newFilter': apply_formatter_at_index(filter_params_formatter, 0),
        'eth_sendTransaction': apply_formatter_at_index(transaction_params_formatter, 0),
        'eth_estimateGas': apply_formatter_at_index(transaction_params_formatter, 0),
        # personal
        'personal_sendTransaction': apply_formatter_at_index(transaction_params_formatter, 0),
        'personal_sign': apply_formatter_at_index(encode_hex, 0),
        'personal_ecRecover': apply_formatter_at_index(encode_hex, 0),
        # Snapshot and Revert
        'evm_revert': apply_formatter_if(
            apply_formatter_at_index(to_integer_if_hex, 0),
            bool,
        )
    },
    result_formatters={
        # Eth
        'eth_accounts': apply_formatter_to_array(to_normalized_address),
        'eth_blockNumber': to_integer_if_hex,
        'eth_coinbase': to_normalized_address,
        'eth_estimateGas': to_integer_if_hex,
        'eth_gasPrice': to_integer_if_hex,
        'eth_getBalance': to_integer_if_hex,
        'eth_getBlockByHash': apply_formatter_if(block_formatter, is_not_null),
        'eth_getBlockByNumber': apply_formatter_if(block_formatter, is_not_null),
        'eth_getBlockTransactionCountByHash': to_integer_if_hex,
        'eth_getBlockTransactionCountByNumber': to_integer_if_hex,
        'eth_getCode': to_ascii_if_bytes,
        'eth_getFilterChanges': filter_result_formatter,
        'eth_getFilterLogs': filter_result_formatter,
        'eth_getTransactionByBlockHashAndIndex': apply_formatter_if(
            transaction_formatter,
            is_not_null,
        ),
        'eth_getTransactionByBlockNumberAndIndex': apply_formatter_if(
            transaction_formatter,
            is_not_null,
        ),
        'eth_getTransactionByHash': apply_formatter_if(transaction_formatter, is_not_null),
        'eth_getTransactionCount': to_integer_if_hex,
        'eth_getTransactionReceipt': apply_formatter_if(
            receipt_formatter,
            is_not_null,
        ),
        'eth_getUncleCountByBlockHash': to_integer_if_hex,
        'eth_getUncleCountByBlockNumber': to_integer_if_hex,
        'eth_hashrate': to_integer_if_hex,
        'eth_protocolVersion': compose(
            apply_formatter_if(str, is_integer),
            to_integer_if_hex,
        ),
        'eth_sendRawTransaction': to_ascii_if_bytes,
        'eth_sendTransaction': to_ascii_if_bytes,
        'eth_syncing': apply_formatter_if(syncing_formatter, is_not_false),
        # SHH
        'shh_version': to_integer_if_hex,
        # Transaction Pool
        'txpool_content': transaction_pool_content_formatter,
        'txpool_inspect': transaction_pool_inspect_formatter,
        # Snapshot and Revert
        'evm_snapshot': hex_to_integer,
        # Net
        'net_peerCount': to_integer_if_hex,
    },
)
