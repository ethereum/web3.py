import operator

from cytoolz.functoolz import (
    complement,
    compose,
    partial,
    identity,
)

from eth_utils import (
    is_dict,
    is_string,
)

from web3.middleware import (
    construct_formatting_middleware,
    construct_fixture_middleware,
)

from web3.utils.formatters import (
    apply_formatter_if,
    apply_formatters_to_args,
    apply_formatter_to_array,
    apply_formatters_to_dict,
    apply_key_map,
    hex_to_integer,
    integer_to_hex,
    static_return,
)


def is_named_block(value):
    return value in {"latest", "earliest", "pending"}


to_integer_if_hex = apply_formatter_if(is_string, hex_to_integer)


is_not_named_block = complement(is_named_block)


TRANSACTION_KEY_MAPPINGS = {
    'block_hash': 'blockHash',
    'block_number': 'blockNumber',
    'gas_price': 'gasPrice',
    'transaction_hash': 'transactionHash',
    'transaction_index': 'transactionIndex',
}

transaction_key_remapper = apply_key_map(TRANSACTION_KEY_MAPPINGS)


LOG_KEY_MAPPINGS = {
    'log_index': 'logIndex',
    'transaction_index': 'transactionIndex',
    'transaction_hash': 'transactionHash',
    'block_hash': 'blockHash',
    'block_number': 'blockNumber',
}


log_key_remapper = apply_key_map(LOG_KEY_MAPPINGS)


RECEIPT_KEY_MAPPINGS = {
    'block_hash': 'blockHash',
    'block_number': 'blockNumber',
    'contract_address': 'contractAddress',
    'gas_used': 'gasUsed',
    'cumulative_gas_used': 'cumulativeGasUsed',
    'transaction_hash': 'transactionHash',
    'transaction_index': 'transactionIndex',
}


receipt_key_remapper = apply_key_map(RECEIPT_KEY_MAPPINGS)


BLOCK_KEY_MAPPINGS = {
    'gas_limit': 'gasLimit',
    'sha3_uncles': 'sha3Uncles',
    'transactions_root': 'transactionsRoot',
    'parent_hash': 'parentHash',
    'bloom': 'logsBloom',
    'state_root': 'stateRoot',
    'receipt_root': 'receiptsRoot',
    'total_difficulty': 'totalDifficulty',
    'extra_data': 'extraData',
    'gas_used': 'gasUsed',
}


block_key_remapper = apply_key_map(BLOCK_KEY_MAPPINGS)


TRANSACTION_PARAMS_MAPPING = {
    'gasPrice': 'gas_price',
}


transaction_params_remapper = apply_key_map(TRANSACTION_PARAMS_MAPPING)


TRANSACTION_PARAMS_FORMATTERS = {
    'gas': to_integer_if_hex,
    'gasPrice': to_integer_if_hex,
    'value': to_integer_if_hex,
}


transaction_params_formatter = apply_formatters_to_dict(TRANSACTION_PARAMS_FORMATTERS)


TRANSACTION_FORMATTERS = {
    'to': apply_formatter_if(partial(operator.eq, b''), static_return(None)),
}


transaction_formatter = apply_formatters_to_dict(TRANSACTION_FORMATTERS)


RECEIPT_FORMATTERS = {
    'logs': apply_formatter_to_array(log_key_remapper),
}


receipt_formatter = apply_formatters_to_dict(RECEIPT_FORMATTERS)


ethereum_tester_middleware = construct_formatting_middleware(
    request_formatters={
        # Eth
        'eth_getBlockByNumber': apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
        ),
        'eth_getFilterChanges': apply_formatters_to_args(hex_to_integer),
        'eth_getFilterLogs': apply_formatters_to_args(hex_to_integer),
        'eth_getBlockTransactionCountByNumber': apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
        ),
        'eth_getUncleCountByBlockNumber': apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
        ),
        'eth_getTransactionByBlockHashAndIndex': apply_formatters_to_args(
            identity,
            to_integer_if_hex,
        ),
        'eth_getTransactionByBlockNumberAndIndex': apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
            to_integer_if_hex,
        ),
        'eth_getUncleByBlockNumberAndIndex': apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
            to_integer_if_hex,
        ),
        'eth_sendTransaction': apply_formatters_to_args(
            transaction_params_formatter,
        ),
        'eth_estimateGas': apply_formatters_to_args(
            transaction_params_formatter,
        ),
        'eth_call': apply_formatters_to_args(
            transaction_params_formatter,
        ),
        'eth_uninstallFilter': apply_formatters_to_args(hex_to_integer),
        # Personal
        'personal_sendTransaction': apply_formatters_to_args(
            compose(transaction_params_remapper, transaction_params_formatter),
            identity,
        ),
    },
    result_formatters={
        'eth_getBlockByHash': apply_formatter_if(
            is_dict,
            block_key_remapper,
        ),
        'eth_getBlockByNumber': apply_formatter_if(
            is_dict,
            block_key_remapper,
        ),
        'eth_getBlockTransactionCountByHash': apply_formatter_if(
            is_dict,
            transaction_key_remapper,
        ),
        'eth_getBlockTransactionCountByNumber': apply_formatter_if(
            is_dict,
            transaction_key_remapper,
        ),
        'eth_getTransactionByHash': apply_formatter_if(
            is_dict,
            compose(transaction_key_remapper, transaction_formatter),
        ),
        'eth_getTransactionReceipt': apply_formatter_if(
            is_dict,
            compose(receipt_key_remapper, receipt_formatter),
        ),
        'eth_newFilter': integer_to_hex,
        'eth_newBlockFilter': integer_to_hex,
        'eth_newPendingTransactionFilter': integer_to_hex,
    },
)


ethereum_tester_fixture_middleware = construct_fixture_middleware({
    # Eth
    'eth_protocolVersion': '63',
    'eth_hashrate': 0,
    'eth_gasPrice': 1,
    'eth_syncing': False,
    'eth_mining': False,
    # Net
    'net_version': '12345',
    'net_listening': False,
    'net_peerCount': 0,
})
