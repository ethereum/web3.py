import operator
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
)

from eth_typing import (
    ChecksumAddress,
)
from eth_utils import (
    is_dict,
    is_hex,
    is_string,
)
from eth_utils.curried import (
    apply_formatter_if,
    apply_formatters_to_dict,
)
from eth_utils.toolz import (
    assoc,
    complement,
    compose,
    curry,
    identity,
    partial,
    pipe,
)

from web3._utils.formatters import (
    apply_formatter_to_array,
    apply_formatters_to_args,
    apply_key_map,
    hex_to_integer,
    integer_to_hex,
    is_array_of_dicts,
    static_return,
)
from web3.middleware import (
    construct_formatting_middleware,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
    TxParams,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        Web3,
    )


def is_named_block(value: Any) -> bool:
    return value in {"latest", "earliest", "pending", "safe", "finalized"}


def is_hexstr(value: Any) -> bool:
    return is_string(value) and is_hex(value)


to_integer_if_hex = apply_formatter_if(is_hexstr, hex_to_integer)

is_not_named_block = complement(is_named_block)


# --- Request Mapping --- #

TRANSACTION_REQUEST_KEY_MAPPING = {
    'gasPrice': 'gas_price',
    'maxFeePerGas': 'max_fee_per_gas',
    'maxPriorityFeePerGas': 'max_priority_fee_per_gas',
    'accessList': 'access_list',
}
transaction_request_remapper = apply_key_map(TRANSACTION_REQUEST_KEY_MAPPING)


TRANSACTION_REQUEST_FORMATTERS = {
    'gas': to_integer_if_hex,
    'gasPrice': to_integer_if_hex,
    'value': to_integer_if_hex,
    'nonce': to_integer_if_hex,
    'maxFeePerGas': to_integer_if_hex,
    'maxPriorityFeePerGas': to_integer_if_hex,
    'accessList': apply_formatter_to_array(
        apply_key_map({'storageKeys': 'storage_keys'})
    ),
}
transaction_request_formatter = apply_formatters_to_dict(TRANSACTION_REQUEST_FORMATTERS)

transaction_request_transformer = compose(
    transaction_request_remapper,
    transaction_request_formatter,
)


FILTER_REQUEST_KEY_MAPPING = {
    'fromBlock': 'from_block',
    'toBlock': 'to_block',
}
filter_request_remapper = apply_key_map(FILTER_REQUEST_KEY_MAPPING)


FILTER_REQUEST_FORMATTERS = {
    'fromBlock': to_integer_if_hex,
    'toBlock': to_integer_if_hex,
}
filter_request_formatter = apply_formatters_to_dict(FILTER_REQUEST_FORMATTERS)

filter_request_transformer = compose(
    filter_request_remapper,
    filter_request_formatter,
)


# --- Result Mapping --- #

TRANSACTION_RESULT_KEY_MAPPING = {
    'access_list': 'accessList',
    'block_hash': 'blockHash',
    'block_number': 'blockNumber',
    'gas_price': 'gasPrice',
    'max_fee_per_gas': 'maxFeePerGas',
    'max_priority_fee_per_gas': 'maxPriorityFeePerGas',
    'transaction_hash': 'transactionHash',
    'transaction_index': 'transactionIndex',
}
transaction_result_remapper = apply_key_map(TRANSACTION_RESULT_KEY_MAPPING)


TRANSACTION_RESULT_FORMATTERS = {
    'to': apply_formatter_if(partial(operator.eq, ''), static_return(None)),
    'access_list': apply_formatter_to_array(
        apply_key_map({'storage_keys': 'storageKeys'}),
    ),
}
transaction_result_formatter = apply_formatters_to_dict(TRANSACTION_RESULT_FORMATTERS)


LOG_RESULT_KEY_MAPPING = {
    'log_index': 'logIndex',
    'transaction_index': 'transactionIndex',
    'transaction_hash': 'transactionHash',
    'block_hash': 'blockHash',
    'block_number': 'blockNumber',
}
log_result_remapper = apply_key_map(LOG_RESULT_KEY_MAPPING)


RECEIPT_RESULT_KEY_MAPPING = {
    'block_hash': 'blockHash',
    'block_number': 'blockNumber',
    'contract_address': 'contractAddress',
    'gas_used': 'gasUsed',
    'cumulative_gas_used': 'cumulativeGasUsed',
    'effective_gas_price': 'effectiveGasPrice',
    'transaction_hash': 'transactionHash',
    'transaction_index': 'transactionIndex',
}
receipt_result_remapper = apply_key_map(RECEIPT_RESULT_KEY_MAPPING)


BLOCK_RESULT_KEY_MAPPING = {
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
    'base_fee_per_gas': 'baseFeePerGas',
}
block_result_remapper = apply_key_map(BLOCK_RESULT_KEY_MAPPING)


RECEIPT_RESULT_FORMATTERS = {
    'logs': apply_formatter_to_array(log_result_remapper),
}
receipt_result_formatter = apply_formatters_to_dict(RECEIPT_RESULT_FORMATTERS)


ethereum_tester_middleware = construct_formatting_middleware(
    request_formatters={
        # Eth
        RPCEndpoint('eth_getBlockByNumber'): apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
        ),
        RPCEndpoint('eth_getFilterChanges'): apply_formatters_to_args(hex_to_integer),
        RPCEndpoint('eth_getFilterLogs'): apply_formatters_to_args(hex_to_integer),
        RPCEndpoint('eth_getBlockTransactionCountByNumber'): apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
        ),
        RPCEndpoint('eth_getUncleCountByBlockNumber'): apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
        ),
        RPCEndpoint('eth_getTransactionByBlockHashAndIndex'): apply_formatters_to_args(
            identity,
            to_integer_if_hex,
        ),
        RPCEndpoint('eth_getTransactionByBlockNumberAndIndex'): apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
            to_integer_if_hex,
        ),
        RPCEndpoint('eth_getUncleByBlockNumberAndIndex'): apply_formatters_to_args(
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
            to_integer_if_hex,
        ),
        RPCEndpoint('eth_newFilter'): apply_formatters_to_args(
            filter_request_transformer,
        ),
        RPCEndpoint('eth_getLogs'): apply_formatters_to_args(
            filter_request_transformer,
        ),
        RPCEndpoint('eth_sendTransaction'): apply_formatters_to_args(
            transaction_request_transformer,
        ),
        RPCEndpoint('eth_estimateGas'): apply_formatters_to_args(
            transaction_request_transformer,
        ),
        RPCEndpoint('eth_call'): apply_formatters_to_args(
            transaction_request_transformer,
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
        ),
        RPCEndpoint('eth_uninstallFilter'): apply_formatters_to_args(hex_to_integer),
        RPCEndpoint('eth_getCode'): apply_formatters_to_args(
            identity,
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
        ),
        RPCEndpoint('eth_getBalance'): apply_formatters_to_args(
            identity,
            apply_formatter_if(is_not_named_block, to_integer_if_hex),
        ),
        # EVM
        RPCEndpoint('evm_revert'): apply_formatters_to_args(hex_to_integer),
        # Personal
        RPCEndpoint('personal_sendTransaction'): apply_formatters_to_args(
            transaction_request_transformer,
            identity,
        ),
    },
    result_formatters={
        RPCEndpoint('eth_getBlockByHash'): apply_formatter_if(
            is_dict,
            block_result_remapper,
        ),
        RPCEndpoint('eth_getBlockByNumber'): apply_formatter_if(
            is_dict,
            block_result_remapper,
        ),
        RPCEndpoint('eth_getBlockTransactionCountByHash'): apply_formatter_if(
            is_dict,
            transaction_result_remapper,
        ),
        RPCEndpoint('eth_getBlockTransactionCountByNumber'): apply_formatter_if(
            is_dict,
            transaction_result_remapper,
        ),
        RPCEndpoint('eth_getTransactionByHash'): apply_formatter_if(
            is_dict,
            compose(transaction_result_remapper, transaction_result_formatter),
        ),
        RPCEndpoint('eth_getTransactionReceipt'): apply_formatter_if(
            is_dict,
            compose(receipt_result_remapper, receipt_result_formatter),
        ),
        RPCEndpoint('eth_newFilter'): integer_to_hex,
        RPCEndpoint('eth_newBlockFilter'): integer_to_hex,
        RPCEndpoint('eth_newPendingTransactionFilter'): integer_to_hex,
        RPCEndpoint('eth_getLogs'): apply_formatter_if(
            is_array_of_dicts,
            apply_formatter_to_array(log_result_remapper),
        ),
        RPCEndpoint('eth_getFilterChanges'): apply_formatter_if(
            is_array_of_dicts,
            apply_formatter_to_array(log_result_remapper),
        ),
        RPCEndpoint('eth_getFilterLogs'): apply_formatter_if(
            is_array_of_dicts,
            apply_formatter_to_array(log_result_remapper),
        ),
        # EVM
        RPCEndpoint('evm_snapshot'): integer_to_hex,
    },
)


def guess_from(web3: "Web3", _: TxParams) -> ChecksumAddress:
    coinbase = web3.eth.coinbase
    if coinbase is not None:
        return coinbase

    try:
        return web3.eth.accounts[0]
    except KeyError:
        # no accounts available to pre-fill, carry on
        pass

    return None


@curry
def fill_default(
    field: str, guess_func: Callable[..., Any], web3: "Web3", transaction: TxParams
) -> TxParams:
    # type ignored b/c TxParams keys must be string literal types
    if field in transaction and transaction[field] is not None:  # type: ignore
        return transaction
    else:
        guess_val = guess_func(web3, transaction)
        return assoc(transaction, field, guess_val)


def default_transaction_fields_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], web3: "Web3"
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    fill_default_from = fill_default('from', guess_from, web3)

    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method in (
            'eth_call',
            'eth_estimateGas',
            'eth_sendTransaction',
        ):
            filled_transaction = pipe(
                params[0],
                fill_default_from,
            )
            return make_request(method, [filled_transaction] + list(params)[1:])
        else:
            return make_request(method, params)
    return middleware
