import operator
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Final,
    Optional,
    final,
)

from eth_typing import (
    ChecksumAddress,
)
from faster_eth_utils import (
    is_dict,
    is_hex,
    is_string,
)
from faster_eth_utils.curried import (
    apply_formatter_if,
    apply_formatters_to_dict,
)
from faster_eth_utils.toolz import (
    assoc,
    complement,
    compose,
    curry,
    identity,
    partial,
    pipe,
)

from faster_web3._utils.formatters import (
    apply_formatters_to_args,
    apply_key_map,
    hex_to_integer,
    integer_to_hex,
    is_array_of_dicts,
    static_return,
)
from faster_web3._utils.method_formatters import (
    apply_list_to_array_formatter,
)
from faster_web3.middleware.base import (
    Web3Middleware,
)
from faster_web3.middleware.formatting import (
    FormattingMiddlewareBuilder,
)
from faster_web3.types import (
    RPCEndpoint,
    TxParams,
)

if TYPE_CHECKING:
    from faster_web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )


def is_named_block(value: Any) -> bool:
    return value in {"latest", "earliest", "safe", "finalized"}


def is_hexstr(value: Any) -> bool:
    return is_string(value) and is_hex(value)


to_integer_if_hex: Final = apply_formatter_if(is_hexstr, hex_to_integer)
is_not_named_block: Final = complement(is_named_block)

# --- Request Mapping --- #

TRANSACTION_REQUEST_KEY_MAPPING: Final = {
    "blobVersionedHashes": "blob_versioned_hashes",
    "gasPrice": "gas_price",
    "maxFeePerBlobGas": "max_fee_per_blob_gas",
    "maxFeePerGas": "max_fee_per_gas",
    "maxPriorityFeePerGas": "max_priority_fee_per_gas",
    "accessList": "access_list",
    "authorizationList": "authorization_list",
    "chainId": "chain_id",
}
transaction_request_remapper: Final = apply_key_map(TRANSACTION_REQUEST_KEY_MAPPING)


TRANSACTION_REQUEST_FORMATTERS: Final = {
    "chainId": to_integer_if_hex,
    "gas": to_integer_if_hex,
    "gasPrice": to_integer_if_hex,
    "value": to_integer_if_hex,
    "nonce": to_integer_if_hex,
    "maxFeePerGas": to_integer_if_hex,
    "maxPriorityFeePerGas": to_integer_if_hex,
    "accessList": apply_list_to_array_formatter(
        apply_key_map({"storageKeys": "storage_keys"})
    ),
    "authorizationList": apply_list_to_array_formatter(
        compose(
            apply_formatters_to_dict(
                {
                    "chain_id": to_integer_if_hex,
                    "nonce": to_integer_if_hex,
                    "y_parity": to_integer_if_hex,
                    "r": to_integer_if_hex,
                    "s": to_integer_if_hex,
                },
            ),
            apply_key_map({"chainId": "chain_id", "yParity": "y_parity"}),
        )
    ),
}
transaction_request_formatter: Final = apply_formatters_to_dict(TRANSACTION_REQUEST_FORMATTERS)

transaction_request_transformer: Final = compose(
    transaction_request_remapper,
    transaction_request_formatter,
)

FILTER_REQUEST_KEY_MAPPING: Final = {
    "fromBlock": "from_block",
    "toBlock": "to_block",
}
filter_request_remapper: Final = apply_key_map(FILTER_REQUEST_KEY_MAPPING)


FILTER_REQUEST_FORMATTERS: Final = {
    "from_block": to_integer_if_hex,
    "to_block": to_integer_if_hex,
}
filter_request_formatter: Final = apply_formatters_to_dict(FILTER_REQUEST_FORMATTERS)

filter_request_transformer: Final = compose(
    filter_request_formatter,
    filter_request_remapper,
)


# --- Result Mapping --- #

TRANSACTION_RESULT_KEY_MAPPING: Final = {
    "access_list": "accessList",
    "authorization_list": "authorizationList",
    "blob_versioned_hashes": "blobVersionedHashes",
    "block_hash": "blockHash",
    "block_number": "blockNumber",
    "chain_id": "chainId",
    "gas_price": "gasPrice",
    "max_fee_per_blob_gas": "maxFeePerBlobGas",
    "max_fee_per_gas": "maxFeePerGas",
    "max_priority_fee_per_gas": "maxPriorityFeePerGas",
    "transaction_hash": "transactionHash",
    "transaction_index": "transactionIndex",
    "data": "input",
}
transaction_result_remapper: Final = apply_key_map(TRANSACTION_RESULT_KEY_MAPPING)


TRANSACTION_RESULT_FORMATTERS: Final = {
    "to": apply_formatter_if(partial(operator.eq, ""), static_return(None)),
    "access_list": apply_list_to_array_formatter(
        apply_key_map({"storage_keys": "storageKeys"}),
    ),
    "authorization_list": apply_list_to_array_formatter(
        apply_key_map({"chain_id": "chainId", "y_parity": "yParity"}),
    ),
}
transaction_result_formatter: Final = apply_formatters_to_dict(TRANSACTION_RESULT_FORMATTERS)


LOG_RESULT_KEY_MAPPING: Final = {
    "log_index": "logIndex",
    "transaction_index": "transactionIndex",
    "transaction_hash": "transactionHash",
    "block_hash": "blockHash",
    "block_number": "blockNumber",
}
log_result_remapper = apply_key_map(LOG_RESULT_KEY_MAPPING)


RECEIPT_RESULT_KEY_MAPPING: Final = {
    "block_hash": "blockHash",
    "block_number": "blockNumber",
    "contract_address": "contractAddress",
    "gas_used": "gasUsed",
    "cumulative_gas_used": "cumulativeGasUsed",
    "effective_gas_price": "effectiveGasPrice",
    "transaction_hash": "transactionHash",
    "transaction_index": "transactionIndex",
    "blob_gas_used": "blobGasUsed",
    "blob_gas_price": "blobGasPrice",
}
receipt_result_remapper: Final = apply_key_map(RECEIPT_RESULT_KEY_MAPPING)


BLOCK_RESULT_KEY_MAPPING: Final = {
    "gas_limit": "gasLimit",
    "sha3_uncles": "sha3Uncles",
    "transactions_root": "transactionsRoot",
    "parent_hash": "parentHash",
    "logs_bloom": "logsBloom",
    "state_root": "stateRoot",
    "receipts_root": "receiptsRoot",
    "total_difficulty": "totalDifficulty",
    "extra_data": "extraData",
    "gas_used": "gasUsed",
    "base_fee_per_gas": "baseFeePerGas",
    "mix_hash": "mixHash",
    # eth-tester changed the miner key to coinbase since
    # there is no longer any mining happening, but the current
    # JSON-RPC spec still says miner
    "coinbase": "miner",
    "withdrawals_root": "withdrawalsRoot",
    "parent_beacon_block_root": "parentBeaconBlockRoot",
    "blob_gas_used": "blobGasUsed",
    "excess_blob_gas": "excessBlobGas",
    "requests_hash": "requestsHash",
}
block_result_remapper: Final = apply_key_map(BLOCK_RESULT_KEY_MAPPING)

BLOCK_RESULT_FORMATTERS: Final = {
    "withdrawals": apply_list_to_array_formatter(
        apply_key_map({"validator_index": "validatorIndex"}),
    ),
}
block_result_formatter: Final = apply_formatters_to_dict(BLOCK_RESULT_FORMATTERS)


RECEIPT_RESULT_FORMATTERS: Final = {
    "logs": apply_list_to_array_formatter(log_result_remapper),
}
receipt_result_formatter: Final = apply_formatters_to_dict(RECEIPT_RESULT_FORMATTERS)


fee_history_result_remapper: Final = apply_key_map(
    {
        "oldest_block": "oldestBlock",
        "base_fee_per_gas": "baseFeePerGas",
        "gas_used_ratio": "gasUsedRatio",
    }
)


request_formatters: Final = {
    # Eth
    RPCEndpoint("eth_getBlockByNumber"): apply_formatters_to_args(
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
    ),
    RPCEndpoint("eth_getFilterChanges"): apply_formatters_to_args(hex_to_integer),
    RPCEndpoint("eth_getFilterLogs"): apply_formatters_to_args(hex_to_integer),
    RPCEndpoint("eth_getTransactionCount"): apply_formatters_to_args(
        identity,
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
    ),
    RPCEndpoint("eth_getBlockTransactionCountByNumber"): apply_formatters_to_args(
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
    ),
    RPCEndpoint("eth_getUncleCountByBlockNumber"): apply_formatters_to_args(
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
    ),
    RPCEndpoint("eth_getTransactionByBlockHashAndIndex"): apply_formatters_to_args(
        identity,
        to_integer_if_hex,
    ),
    RPCEndpoint("eth_getTransactionByBlockNumberAndIndex"): apply_formatters_to_args(
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
        to_integer_if_hex,
    ),
    RPCEndpoint("eth_getUncleByBlockNumberAndIndex"): apply_formatters_to_args(
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
        to_integer_if_hex,
    ),
    RPCEndpoint("eth_newFilter"): apply_formatters_to_args(
        filter_request_transformer,
    ),
    RPCEndpoint("eth_getLogs"): apply_formatters_to_args(
        filter_request_transformer,
    ),
    RPCEndpoint("eth_sendTransaction"): apply_formatters_to_args(
        transaction_request_transformer,
    ),
    RPCEndpoint("eth_estimateGas"): apply_formatters_to_args(
        transaction_request_transformer,
    ),
    RPCEndpoint("eth_call"): apply_formatters_to_args(
        transaction_request_transformer,
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
    ),
    RPCEndpoint("eth_createAccessList"): apply_formatters_to_args(
        transaction_request_transformer,
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
    ),
    RPCEndpoint("eth_uninstallFilter"): apply_formatters_to_args(hex_to_integer),
    RPCEndpoint("eth_getCode"): apply_formatters_to_args(
        identity,
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
    ),
    RPCEndpoint("eth_getBalance"): apply_formatters_to_args(
        identity,
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
    ),
    RPCEndpoint("eth_feeHistory"): apply_formatters_to_args(
        to_integer_if_hex,
        apply_formatter_if(is_not_named_block, to_integer_if_hex),
    ),
    # EVM
    RPCEndpoint("evm_revert"): apply_formatters_to_args(hex_to_integer),
}

result_formatters: Final[Dict[RPCEndpoint, Callable[..., Any]]] = {
    RPCEndpoint("eth_getBlockByHash"): apply_formatter_if(
        is_dict, compose(block_result_remapper, block_result_formatter)
    ),
    RPCEndpoint("eth_getBlockByNumber"): apply_formatter_if(
        is_dict, compose(block_result_remapper, block_result_formatter)
    ),
    RPCEndpoint("eth_getBlockTransactionCountByHash"): apply_formatter_if(
        is_dict,
        transaction_result_remapper,
    ),
    RPCEndpoint("eth_getBlockTransactionCountByNumber"): apply_formatter_if(
        is_dict,
        transaction_result_remapper,
    ),
    RPCEndpoint("eth_getTransactionByHash"): apply_formatter_if(
        is_dict,
        compose(transaction_result_remapper, transaction_result_formatter),
    ),
    RPCEndpoint("eth_getTransactionReceipt"): apply_formatter_if(
        is_dict,
        compose(receipt_result_remapper, receipt_result_formatter),
    ),
    RPCEndpoint("eth_newFilter"): integer_to_hex,
    RPCEndpoint("eth_newBlockFilter"): integer_to_hex,
    RPCEndpoint("eth_newPendingTransactionFilter"): integer_to_hex,
    RPCEndpoint("eth_getLogs"): apply_formatter_if(
        is_array_of_dicts,
        apply_list_to_array_formatter(log_result_remapper),
    ),
    RPCEndpoint("eth_getFilterChanges"): apply_formatter_if(
        is_array_of_dicts,
        apply_list_to_array_formatter(log_result_remapper),
    ),
    RPCEndpoint("eth_getFilterLogs"): apply_formatter_if(
        is_array_of_dicts,
        apply_list_to_array_formatter(log_result_remapper),
    ),
    RPCEndpoint("eth_feeHistory"): apply_formatter_if(
        is_dict, fee_history_result_remapper
    ),
    # EVM
    RPCEndpoint("evm_snapshot"): integer_to_hex,
}


def guess_from(w3: "Web3", _: TxParams) -> ChecksumAddress:
    accounts = w3.eth.accounts
    return accounts[0] if len(accounts) > 0 else None


@curry
def fill_default(
    field: str, guess_func: Callable[..., Any], w3: "Web3", transaction: TxParams
) -> TxParams:
    # type ignored b/c TxParams keys must be string literal types
    if field in transaction and transaction[field] is not None:  # type: ignore
        return transaction
    else:
        guess_val = guess_func(w3, transaction)
        return assoc(transaction, field, guess_val)


# --- async --- #


async def async_guess_from(
    async_w3: "AsyncWeb3", _: TxParams
) -> Optional[ChecksumAddress]:
    accounts = await async_w3.eth.accounts
    if accounts is not None and len(accounts) > 0:
        return accounts[0]
    return None


@curry
async def async_fill_default(
    field: str,
    guess_func: Callable[..., Any],
    async_w3: "AsyncWeb3",
    transaction: TxParams,
) -> TxParams:
    # type ignored b/c TxParams keys must be string literal types
    if field in transaction and transaction[field] is not None:  # type: ignore
        return transaction
    else:
        guess_val = await guess_func(async_w3, transaction)
        return assoc(transaction, field, guess_val)


# --- define middleware --- #


@final
class DefaultTransactionFieldsMiddleware(Web3Middleware):
    def request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        if method in {
            "eth_call",
            "eth_estimateGas",
            "eth_sendTransaction",
            "eth_createAccessList",
        }:
            fill_default_from = fill_default("from", guess_from, self._w3)
            filled_transaction = pipe(
                params[0],
                fill_default_from,
            )
            params = [filled_transaction] + list(params)[1:]
        return method, params

    # --- async --- #

    async def async_request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        if method in {
            "eth_call",
            "eth_estimateGas",
            "eth_sendTransaction",
            "eth_createAccessList",
        }:
            filled_transaction = await async_fill_default(
                "from", async_guess_from, self._w3, params[0]
            )
            params = [filled_transaction] + list(params)[1:]

        return method, params


ethereum_tester_middleware: Final = FormattingMiddlewareBuilder.build(
    request_formatters=request_formatters, result_formatters=result_formatters
)
default_transaction_fields_middleware: Final = DefaultTransactionFieldsMiddleware
