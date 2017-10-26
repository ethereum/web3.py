from __future__ import absolute_import

import codecs
import operator

from cytoolz import (
    curry,
)
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
    to_checksum_address,
    is_hex,
    is_integer,
    is_null,
    is_dict,
    is_string,
    is_bytes,
    is_list_like,
    encode_hex,
)

from web3.utils.abi import (
    map_abi_data,
)
from web3.utils.datastructures import (
    HexBytes,
)
from web3.utils.formatters import (
    apply_formatter_if,
    apply_formatters_to_dict,
    apply_formatter_to_array,
    apply_formatter_at_index,
    apply_one_of_formatters,
    hex_to_integer,
    integer_to_hex,
)
from web3.utils.normalizers import (
    abi_int_to_hex,
    abi_bytes_to_hex,
)

from .formatting import (
    construct_formatting_middleware,
)


def bytes_to_ascii(value):
    return codecs.decode(value, 'ascii')


to_ascii_if_bytes = apply_formatter_if(is_bytes, bytes_to_ascii)
to_integer_if_hex = apply_formatter_if(is_string, hex_to_integer)
block_number_formatter = apply_formatter_if(is_integer, integer_to_hex)


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


@curry
def to_hexbytes(num_bytes, val):
    if isinstance(val, str):
        result = HexBytes(val)
    elif isinstance(val, bytes):
        if len(val) == num_bytes:
            result = HexBytes(val)
        else:
            # some providers return values with hex as bytes, like b'0xEFFF' :(
            hexstr = val.decode('utf-8')
            if not is_hex(hexstr):
                raise ValueError("Cannot convert %r into a %d byte argument" % (hexstr, num_bytes))
            result = HexBytes(hexstr)
    else:
        raise TypeError("Cannot convert %r to HexBytes" % val)

    if len(result) != num_bytes:
        raise ValueError(
            "The value %r is %d bytes, but should be %d" % (
                result, len(result), num_bytes
            )
        )
    return result


TRANSACTION_FORMATTERS = {
    'blockNumber': apply_formatter_if(is_not_null, to_integer_if_hex),
    'transactionIndex': apply_formatter_if(is_not_null, to_integer_if_hex),
    'nonce': to_integer_if_hex,
    'gas': to_integer_if_hex,
    'gasPrice': to_integer_if_hex,
    'value': to_integer_if_hex,
    'from': to_checksum_address,
    'to': apply_formatter_if(is_address, to_checksum_address),
    'hash': to_ascii_if_bytes,
}


transaction_formatter = apply_formatters_to_dict(TRANSACTION_FORMATTERS)


LOG_ENTRY_FORMATTERS = {
    'blockHash': apply_formatter_if(is_not_null, to_ascii_if_bytes),
    'blockNumber': apply_formatter_if(is_not_null, to_integer_if_hex),
    'transactionIndex': apply_formatter_if(is_not_null, to_integer_if_hex),
    'logIndex': to_integer_if_hex,
    'address': to_checksum_address,
    'topics': apply_formatter_to_array(to_ascii_if_bytes),
    'data': to_ascii_if_bytes,
}


log_entry_formatter = apply_formatters_to_dict(LOG_ENTRY_FORMATTERS)


RECEIPT_FORMATTERS = {
    'blockHash': apply_formatter_if(is_not_null, to_ascii_if_bytes),
    'blockNumber': apply_formatter_if(is_not_null, to_integer_if_hex),
    'transactionIndex': apply_formatter_if(is_not_null, to_integer_if_hex),
    'transactionHash': to_ascii_if_bytes,
    'cumulativeGasUsed': to_integer_if_hex,
    'gasUsed': to_integer_if_hex,
    'contractAddress': apply_formatter_if(is_not_null, to_checksum_address),
    'logs': apply_formatter_to_array(log_entry_formatter),
}


receipt_formatter = apply_formatters_to_dict(RECEIPT_FORMATTERS)

BLOCK_FORMATTERS = {
    'gasLimit': to_integer_if_hex,
    'gasUsed': to_integer_if_hex,
    'size': to_integer_if_hex,
    'timestamp': to_integer_if_hex,
    'hash': apply_formatter_if(is_not_null, to_hexbytes(32)),
    'number': apply_formatter_if(is_not_null, to_integer_if_hex),
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
    'fromBlock': apply_formatter_if(is_integer, integer_to_hex),
    'toBlock': apply_formatter_if(is_integer, integer_to_hex),
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


format_abi_parameters = map_abi_data([
    abi_bytes_to_hex,
    abi_int_to_hex,
])


pythonic_middleware = construct_formatting_middleware(
    request_formatters={
        # Eth
        'eth_call': apply_formatter_at_index(transaction_params_formatter, 0),
        'eth_getBalance': apply_formatter_at_index(block_number_formatter, 1),
        'eth_getBlockByHash': format_abi_parameters(['bytes32', 'bool']),
        'eth_getBlockByNumber': apply_formatter_at_index(block_number_formatter, 0),
        'eth_getBlockTransactionCountByNumber': apply_formatter_at_index(
            block_number_formatter,
            0,
        ),
        'eth_getBlockTransactionCountByHash': format_abi_parameters(['bytes32']),
        'eth_getCode': apply_formatter_at_index(block_number_formatter, 1),
        'eth_getStorageAt': compose(
            apply_formatter_at_index(integer_to_hex, 1),
            apply_formatter_at_index(block_number_formatter, 2),
        ),
        'eth_getTransactionByBlockNumberAndIndex': compose(
            apply_formatter_at_index(block_number_formatter, 0),
            apply_formatter_at_index(integer_to_hex, 1),
        ),
        'eth_getTransactionByBlockHashAndIndex': format_abi_parameters(['bytes32', 'uint']),
        'eth_getTransactionCount': apply_formatter_at_index(block_number_formatter, 1),
        'eth_getUncleCountByBlockHash': format_abi_parameters(['bytes32']),
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
            bool,
            apply_formatter_at_index(to_integer_if_hex, 0),
        )
    },
    result_formatters={
        # Eth
        'eth_accounts': apply_formatter_to_array(to_checksum_address),
        'eth_blockNumber': to_integer_if_hex,
        'eth_coinbase': to_checksum_address,
        'eth_estimateGas': to_integer_if_hex,
        'eth_gasPrice': to_integer_if_hex,
        'eth_getBalance': to_integer_if_hex,
        'eth_getBlockByHash': apply_formatter_if(is_not_null, block_formatter),
        'eth_getBlockByNumber': apply_formatter_if(is_not_null, block_formatter),
        'eth_getBlockTransactionCountByHash': to_integer_if_hex,
        'eth_getBlockTransactionCountByNumber': to_integer_if_hex,
        'eth_getCode': to_ascii_if_bytes,
        'eth_getFilterChanges': filter_result_formatter,
        'eth_getFilterLogs': filter_result_formatter,
        'eth_getTransactionByBlockHashAndIndex': apply_formatter_if(
            is_not_null,
            transaction_formatter,
        ),
        'eth_getTransactionByBlockNumberAndIndex': apply_formatter_if(
            is_not_null,
            transaction_formatter,
        ),
        'eth_getTransactionByHash': apply_formatter_if(is_not_null, transaction_formatter),
        'eth_getTransactionCount': to_integer_if_hex,
        'eth_getTransactionReceipt': apply_formatter_if(
            is_not_null,
            receipt_formatter,
        ),
        'eth_getUncleCountByBlockHash': to_integer_if_hex,
        'eth_getUncleCountByBlockNumber': to_integer_if_hex,
        'eth_hashrate': to_integer_if_hex,
        'eth_protocolVersion': compose(
            apply_formatter_if(is_integer, str),
            to_integer_if_hex,
        ),
        'eth_sendRawTransaction': to_ascii_if_bytes,
        'eth_sendTransaction': to_ascii_if_bytes,
        'eth_syncing': apply_formatter_if(is_not_false, syncing_formatter),
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
