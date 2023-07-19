import codecs
import operator
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    NoReturn,
    Tuple,
    Union,
    cast,
)

from eth_typing import (
    HexStr,
)
from eth_utils.curried import (
    apply_formatter_at_index,
    apply_formatter_if,
    apply_formatter_to_array,
    apply_formatters_to_dict,
    apply_formatters_to_sequence,
    apply_one_of_formatters,
    is_0x_prefixed,
    is_address,
    is_bytes,
    is_integer,
    is_null,
    is_string,
    remove_0x_prefix,
    text_if_str,
    to_checksum_address,
    to_list,
    to_tuple,
)
from eth_utils.toolz import (
    complement,
    compose,
    curried,
    curry,
    partial,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    is_length,
)
from web3._utils.contract_error_handling import (
    raise_contract_logic_error_on_revert,
)
from web3._utils.encoding import (
    hexstr_if_str,
    to_hex,
)
from web3._utils.filters import (
    AsyncBlockFilter,
    AsyncLogFilter,
    AsyncTransactionFilter,
    BlockFilter,
    LogFilter,
    TransactionFilter,
)
from web3._utils.formatters import (
    hex_to_integer,
    integer_to_hex,
    is_array_of_dicts,
    is_array_of_strings,
    remove_key_if,
)
from web3._utils.normalizers import (
    abi_address_to_hex,
    abi_bytes_to_hex,
    abi_int_to_hex,
    abi_string_to_hex,
)
from web3._utils.rpc_abi import (
    RPC,
    RPC_ABIS,
    abi_request_formatters,
)
from web3._utils.type_conversion import (
    to_hex_if_bytes,
)
from web3._utils.utility_methods import (
    either_set_is_a_subset,
)
from web3.datastructures import (
    AttributeDict,
    ReadableAttributeDict,
)
from web3.exceptions import (
    BlockNotFound,
    TransactionNotFound,
)
from web3.types import (
    BlockIdentifier,
    CallOverrideParams,
    Formatters,
    RPCEndpoint,
    TReturn,
    TxParams,
    _Hash32,
)

if TYPE_CHECKING:
    from web3.eth import AsyncEth  # noqa: F401
    from web3.eth import Eth  # noqa: F401
    from web3.module import Module  # noqa: F401


def bytes_to_ascii(value: bytes) -> str:
    return codecs.decode(value, "ascii")


to_ascii_if_bytes = apply_formatter_if(is_bytes, bytes_to_ascii)
to_integer_if_hex = apply_formatter_if(is_string, hex_to_integer)
to_hex_if_integer = apply_formatter_if(is_integer, integer_to_hex)

is_false = partial(operator.is_, False)
is_not_false = complement(is_false)
is_not_null = complement(is_null)


@curry
def to_hexbytes(
    num_bytes: int, val: Union[str, int, bytes], variable_length: bool = False
) -> HexBytes:
    if isinstance(val, (str, int, bytes)):
        result = HexBytes(val)
    else:
        raise TypeError(f"Cannot convert {val!r} to HexBytes")

    extra_bytes = len(result) - num_bytes
    if extra_bytes == 0 or (variable_length and extra_bytes < 0):
        return result
    elif all(byte == 0 for byte in result[:extra_bytes]):
        return HexBytes(result[extra_bytes:])
    else:
        raise ValueError(
            f"The value {result!r} is {len(result)} bytes, but should be {num_bytes}"
        )


def is_attrdict(val: Any) -> bool:
    return isinstance(val, AttributeDict)


@curry
def type_aware_apply_formatters_to_dict(
    formatters: Formatters,
    value: Union[AttributeDict[str, Any], Dict[str, Any]],
) -> Union[ReadableAttributeDict[str, Any], Dict[str, Any]]:
    """
    Preserve ``AttributeDict`` types if original ``value`` was an ``AttributeDict``.
    """
    formatted_dict: Dict[str, Any] = apply_formatters_to_dict(formatters, dict(value))
    return (
        AttributeDict.recursive(formatted_dict)
        if is_attrdict(value)
        else formatted_dict
    )


def type_aware_apply_formatters_to_dict_keys_and_values(
    key_formatters: Callable[[Any], Any],
    value_formatters: Callable[[Any], Any],
    dict_like_object: Union[AttributeDict[str, Any], Dict[str, Any]],
) -> Union[ReadableAttributeDict[str, Any], Dict[str, Any]]:
    """
    Preserve ``AttributeDict`` types if original ``value`` was an ``AttributeDict``.
    """
    formatted_dict = dict(
        (key_formatters(k), value_formatters(v)) for k, v in dict_like_object.items()
    )
    return (
        AttributeDict.recursive(formatted_dict)
        if is_attrdict(dict_like_object)
        else formatted_dict
    )


TRANSACTION_RESULT_FORMATTERS = {
    "blockHash": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "blockNumber": apply_formatter_if(is_not_null, to_integer_if_hex),
    "transactionIndex": apply_formatter_if(is_not_null, to_integer_if_hex),
    "nonce": to_integer_if_hex,
    "gas": to_integer_if_hex,
    "gasPrice": to_integer_if_hex,
    "maxFeePerGas": to_integer_if_hex,
    "maxPriorityFeePerGas": to_integer_if_hex,
    "value": to_integer_if_hex,
    "from": to_checksum_address,
    "publicKey": apply_formatter_if(is_not_null, to_hexbytes(64)),
    "r": apply_formatter_if(is_not_null, to_hexbytes(32, variable_length=True)),
    "raw": HexBytes,
    "s": apply_formatter_if(is_not_null, to_hexbytes(32, variable_length=True)),
    "to": apply_formatter_if(is_address, to_checksum_address),
    "hash": to_hexbytes(32),
    "v": apply_formatter_if(is_not_null, to_integer_if_hex),
    "standardV": apply_formatter_if(is_not_null, to_integer_if_hex),
    "type": apply_formatter_if(is_not_null, to_integer_if_hex),
    "chainId": apply_formatter_if(is_not_null, to_integer_if_hex),
    "accessList": apply_formatter_if(
        is_not_null,
        apply_formatter_to_array(
            type_aware_apply_formatters_to_dict(
                {
                    "address": to_checksum_address,
                }
            )
        ),
    ),
    "input": HexBytes,
}


transaction_result_formatter = type_aware_apply_formatters_to_dict(
    TRANSACTION_RESULT_FORMATTERS
)

WITHDRAWAL_RESULT_FORMATTERS = {
    "index": to_integer_if_hex,
    "validatorIndex": to_integer_if_hex,
    "address": to_checksum_address,
    "amount": to_integer_if_hex,
}
withdrawal_result_formatter = type_aware_apply_formatters_to_dict(
    WITHDRAWAL_RESULT_FORMATTERS
)


def apply_list_to_array_formatter(formatter: Any) -> Callable[..., Any]:
    return to_list(apply_formatter_to_array(formatter))


LOG_ENTRY_FORMATTERS = {
    "blockHash": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "blockNumber": apply_formatter_if(is_not_null, to_integer_if_hex),
    "transactionIndex": apply_formatter_if(is_not_null, to_integer_if_hex),
    "transactionHash": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "logIndex": to_integer_if_hex,
    "address": to_checksum_address,
    "topics": apply_list_to_array_formatter(to_hexbytes(32)),
    "data": HexBytes,
}


log_entry_formatter = type_aware_apply_formatters_to_dict(LOG_ENTRY_FORMATTERS)


RECEIPT_FORMATTERS = {
    "blockHash": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "blockNumber": apply_formatter_if(is_not_null, to_integer_if_hex),
    "transactionIndex": apply_formatter_if(is_not_null, to_integer_if_hex),
    "transactionHash": to_hexbytes(32),
    "cumulativeGasUsed": to_integer_if_hex,
    "status": to_integer_if_hex,
    "gasUsed": to_integer_if_hex,
    "contractAddress": apply_formatter_if(is_not_null, to_checksum_address),
    "logs": apply_list_to_array_formatter(log_entry_formatter),
    "logsBloom": to_hexbytes(256, variable_length=True),
    "from": apply_formatter_if(is_not_null, to_checksum_address),
    "to": apply_formatter_if(is_address, to_checksum_address),
    "effectiveGasPrice": to_integer_if_hex,
    "type": to_integer_if_hex,
}


receipt_formatter = type_aware_apply_formatters_to_dict(RECEIPT_FORMATTERS)

BLOCK_FORMATTERS = {
    "baseFeePerGas": to_integer_if_hex,
    "extraData": apply_formatter_if(is_not_null, to_hexbytes(32, variable_length=True)),
    "gasLimit": to_integer_if_hex,
    "gasUsed": to_integer_if_hex,
    "size": to_integer_if_hex,
    "timestamp": to_integer_if_hex,
    "hash": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "logsBloom": apply_formatter_if(
        is_not_null, to_hexbytes(256, variable_length=True)
    ),
    "miner": apply_formatter_if(is_not_null, to_checksum_address),
    "mixHash": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "nonce": apply_formatter_if(is_not_null, to_hexbytes(8, variable_length=True)),
    "number": apply_formatter_if(is_not_null, to_integer_if_hex),
    "parentHash": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "sha3Uncles": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "uncles": apply_list_to_array_formatter(to_hexbytes(32)),
    "difficulty": to_integer_if_hex,
    "receiptsRoot": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "stateRoot": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "totalDifficulty": to_integer_if_hex,
    "transactions": apply_one_of_formatters(
        (
            (
                is_array_of_dicts,
                apply_list_to_array_formatter(transaction_result_formatter),
            ),
            (is_array_of_strings, apply_list_to_array_formatter(to_hexbytes(32))),
        )
    ),
    "transactionsRoot": apply_formatter_if(is_not_null, to_hexbytes(32)),
    "withdrawals": apply_formatter_if(
        is_not_null, apply_list_to_array_formatter(withdrawal_result_formatter)
    ),
    "withdrawalsRoot": apply_formatter_if(is_not_null, to_hexbytes(32)),
}


block_formatter = type_aware_apply_formatters_to_dict(BLOCK_FORMATTERS)


SYNCING_FORMATTERS = {
    "startingBlock": to_integer_if_hex,
    "currentBlock": to_integer_if_hex,
    "highestBlock": to_integer_if_hex,
    "knownStates": to_integer_if_hex,
    "pulledStates": to_integer_if_hex,
}
syncing_formatter = type_aware_apply_formatters_to_dict(SYNCING_FORMATTERS)

GETH_SYNCING_SUBSCRIPTION_FORMATTERS = {
    "status": SYNCING_FORMATTERS,
}

TRANSACTION_POOL_CONTENT_FORMATTERS = {
    "pending": compose(
        curried.keymap(to_ascii_if_bytes),
        curried.valmap(transaction_result_formatter),
    ),
    "queued": compose(
        curried.keymap(to_ascii_if_bytes),
        curried.valmap(transaction_result_formatter),
    ),
}


transaction_pool_content_formatter = type_aware_apply_formatters_to_dict(
    TRANSACTION_POOL_CONTENT_FORMATTERS
)


TRANSACTION_POOL_INSPECT_FORMATTERS = {
    "pending": curried.keymap(to_ascii_if_bytes),
    "queued": curried.keymap(to_ascii_if_bytes),
}


transaction_pool_inspect_formatter = type_aware_apply_formatters_to_dict(
    TRANSACTION_POOL_INSPECT_FORMATTERS
)

FEE_HISTORY_FORMATTERS = {
    "baseFeePerGas": apply_formatter_to_array(to_integer_if_hex),
    "gasUsedRatio": apply_formatter_if(is_not_null, apply_formatter_to_array(float)),
    "oldestBlock": to_integer_if_hex,
    "reward": apply_formatter_if(
        is_not_null,
        apply_formatter_to_array(apply_formatter_to_array(to_integer_if_hex)),
    ),
}

fee_history_formatter = type_aware_apply_formatters_to_dict(FEE_HISTORY_FORMATTERS)

STORAGE_PROOF_FORMATTERS = {
    "key": HexBytes,
    "value": HexBytes,
    "proof": apply_list_to_array_formatter(HexBytes),
}

ACCOUNT_PROOF_FORMATTERS = {
    "address": to_checksum_address,
    "accountProof": apply_list_to_array_formatter(HexBytes),
    "balance": to_integer_if_hex,
    "codeHash": to_hexbytes(32),
    "nonce": to_integer_if_hex,
    "storageHash": to_hexbytes(32),
    "storageProof": apply_list_to_array_formatter(
        type_aware_apply_formatters_to_dict(STORAGE_PROOF_FORMATTERS)
    ),
}

proof_formatter = type_aware_apply_formatters_to_dict(ACCOUNT_PROOF_FORMATTERS)

FILTER_PARAMS_FORMATTERS = {
    "fromBlock": apply_formatter_if(is_integer, integer_to_hex),
    "toBlock": apply_formatter_if(is_integer, integer_to_hex),
}


filter_params_formatter = type_aware_apply_formatters_to_dict(FILTER_PARAMS_FORMATTERS)


filter_result_formatter = apply_one_of_formatters(
    (
        (is_array_of_dicts, apply_list_to_array_formatter(log_entry_formatter)),
        (is_array_of_strings, apply_list_to_array_formatter(to_hexbytes(32))),
    )
)

transaction_param_formatter = compose(
    remove_key_if("to", lambda txn: txn["to"] in {"", b"", None}),
    remove_key_if("gasPrice", lambda txn: txn["gasPrice"] in {"", b"", None}),
)


call_without_override: Callable[
    [Tuple[TxParams, BlockIdentifier]], Tuple[Dict[str, Any], int]
] = apply_formatters_to_sequence(
    [
        transaction_param_formatter,
        to_hex_if_integer,
    ]
)

CALL_OVERRIDE_FORMATTERS = {
    "balance": to_hex_if_integer,
    "nonce": to_hex_if_integer,
    "code": to_hex_if_bytes,
}
call_with_override: Callable[
    [Tuple[TxParams, BlockIdentifier, CallOverrideParams]],
    Tuple[Dict[str, Any], int, Dict[str, Any]],
] = apply_formatters_to_sequence(
    [
        transaction_param_formatter,
        to_hex_if_integer,
        lambda val: type_aware_apply_formatters_to_dict_keys_and_values(
            to_checksum_address,
            type_aware_apply_formatters_to_dict(CALL_OVERRIDE_FORMATTERS),
            val,
        ),
    ]
)


estimate_gas_without_block_id: Callable[[Dict[str, Any]], Dict[str, Any]]
estimate_gas_without_block_id = apply_formatter_at_index(transaction_param_formatter, 0)
estimate_gas_with_block_id: Callable[
    [Tuple[Dict[str, Any], Union[str, int]]], Tuple[Dict[str, Any], int]
]
estimate_gas_with_block_id = apply_formatters_to_sequence(
    [
        transaction_param_formatter,
        to_hex_if_integer,
    ]
)

SIGNED_TX_FORMATTER = {
    "raw": HexBytes,
    "tx": transaction_result_formatter,
}

signed_tx_formatter = type_aware_apply_formatters_to_dict(SIGNED_TX_FORMATTER)

FILTER_PARAM_NORMALIZERS = type_aware_apply_formatters_to_dict(
    {"address": apply_formatter_if(is_string, lambda x: [x])}
)


GETH_WALLET_FORMATTER = {"address": to_checksum_address}

geth_wallet_formatter = type_aware_apply_formatters_to_dict(GETH_WALLET_FORMATTER)

GETH_WALLETS_FORMATTER = {
    "accounts": apply_list_to_array_formatter(geth_wallet_formatter),
}

geth_wallets_formatter = type_aware_apply_formatters_to_dict(GETH_WALLETS_FORMATTER)

PYTHONIC_REQUEST_FORMATTERS: Dict[RPCEndpoint, Callable[..., Any]] = {
    # Eth
    RPC.eth_feeHistory: compose(
        apply_formatter_at_index(to_hex_if_integer, 0),
        apply_formatter_at_index(to_hex_if_integer, 1),
    ),
    RPC.eth_getBalance: apply_formatter_at_index(to_hex_if_integer, 1),
    RPC.eth_getBlockByNumber: apply_formatter_at_index(to_hex_if_integer, 0),
    RPC.eth_getBlockTransactionCountByNumber: apply_formatter_at_index(
        to_hex_if_integer,
        0,
    ),
    RPC.eth_getCode: apply_formatter_at_index(to_hex_if_integer, 1),
    RPC.eth_getStorageAt: apply_formatter_at_index(to_hex_if_integer, 2),
    RPC.eth_getTransactionByBlockNumberAndIndex: compose(
        apply_formatter_at_index(to_hex_if_integer, 0),
        apply_formatter_at_index(to_hex_if_integer, 1),
    ),
    RPC.eth_getTransactionCount: apply_formatter_at_index(to_hex_if_integer, 1),
    RPC.eth_getRawTransactionByBlockNumberAndIndex: compose(
        apply_formatter_at_index(to_hex_if_integer, 0),
        apply_formatter_at_index(to_hex_if_integer, 1),
    ),
    RPC.eth_getRawTransactionByBlockHashAndIndex: apply_formatter_at_index(
        to_hex_if_integer, 1
    ),
    RPC.eth_getUncleCountByBlockNumber: apply_formatter_at_index(to_hex_if_integer, 0),
    RPC.eth_getUncleByBlockNumberAndIndex: compose(
        apply_formatter_at_index(to_hex_if_integer, 0),
        apply_formatter_at_index(to_hex_if_integer, 1),
    ),
    RPC.eth_getUncleByBlockHashAndIndex: apply_formatter_at_index(to_hex_if_integer, 1),
    RPC.eth_newFilter: apply_formatter_at_index(filter_params_formatter, 0),
    RPC.eth_getLogs: apply_formatter_at_index(filter_params_formatter, 0),
    RPC.eth_call: apply_one_of_formatters(
        (
            (is_length(2), call_without_override),
            (is_length(3), call_with_override),
        )
    ),
    RPC.eth_estimateGas: apply_one_of_formatters(
        (
            (is_length(1), estimate_gas_without_block_id),
            (is_length(2), estimate_gas_with_block_id),
        )
    ),
    RPC.eth_sendTransaction: apply_formatter_at_index(transaction_param_formatter, 0),
    RPC.eth_signTransaction: apply_formatter_at_index(transaction_param_formatter, 0),
    RPC.eth_getProof: apply_formatter_at_index(to_hex_if_integer, 2),
    # personal
    RPC.personal_importRawKey: apply_formatter_at_index(
        compose(remove_0x_prefix, hexstr_if_str(to_hex)),
        0,
    ),
    RPC.personal_sign: apply_formatter_at_index(text_if_str(to_hex), 0),
    RPC.personal_ecRecover: apply_formatter_at_index(text_if_str(to_hex), 0),
    RPC.personal_sendTransaction: apply_formatter_at_index(
        transaction_param_formatter, 0
    ),
    # Snapshot and Revert
    RPC.evm_revert: apply_formatter_at_index(integer_to_hex, 0),
    # tracing
    RPC.trace_replayBlockTransactions: apply_formatter_at_index(to_hex_if_integer, 0),
    RPC.trace_block: apply_formatter_at_index(to_hex_if_integer, 0),
    RPC.trace_call: compose(
        apply_formatter_at_index(transaction_param_formatter, 0),
        apply_formatter_at_index(to_hex_if_integer, 2),
    ),
}

# --- Result Formatters --- #

# -- tracing -- #

# result formatters for the trace field "action"
TRACE_ACTION_FORMATTERS = apply_formatter_if(
    is_not_null,
    type_aware_apply_formatters_to_dict(
        {
            # call and create types
            "from": to_checksum_address,
            "to": to_checksum_address,
            "input": HexBytes,
            "value": to_integer_if_hex,
            "gas": to_integer_if_hex,
            # create type
            "init": HexBytes,
            # suicide type
            "address": to_checksum_address,
            "refundAddress": to_checksum_address,
            # reward type
            "author": to_checksum_address,
        }
    ),
)

# result formatters for the trace field "result"
TRACE_RESULT_FORMATTERS = apply_formatter_if(
    is_not_null,
    type_aware_apply_formatters_to_dict(
        {
            "address": to_checksum_address,
            "code": HexBytes,
            "output": HexBytes,
            "gasUsed": to_integer_if_hex,
        }
    ),
)

# result formatters for the trace field
TRACE_FORMATTERS = apply_formatter_if(
    is_not_null,
    type_aware_apply_formatters_to_dict(
        {
            "action": TRACE_ACTION_FORMATTERS,
            "result": TRACE_RESULT_FORMATTERS,
            "blockHash": HexBytes,
            "blockNumber": to_integer_if_hex,
            "transactionHash": apply_formatter_if(is_not_null, to_hexbytes(32)),
        }
    ),
)

# trace formatter for a list of traces
trace_list_result_formatter: Callable[[Formatters], Any] = apply_formatter_to_array(
    TRACE_FORMATTERS,
)

# shared formatter for common `tracing` module rpc responses
common_tracing_result_formatter = type_aware_apply_formatters_to_dict(
    {
        "trace": apply_formatter_if(is_not_null, trace_list_result_formatter),
        "output": HexBytes,
        "transactionHash": HexBytes,  # trace_replayBlockTransactions
    }
)


# -- eth_subscribe -- #
def subscription_formatter(value: Any) -> Union[HexBytes, HexStr, Dict[str, Any]]:
    if is_string(value):
        if len(value.replace("0x", "")) == 64:
            # transaction hash, from `newPendingTransactions` subscription w/o full_txs
            return HexBytes(value)

        # subscription id from the original subscription request
        return HexStr(value)

    response_key_set = set(value.keys())

    # handle dict subscription responses
    if either_set_is_a_subset(response_key_set, set(BLOCK_FORMATTERS.keys())):
        # block format, newHeads
        return block_formatter(value)

    elif either_set_is_a_subset(response_key_set, set(LOG_ENTRY_FORMATTERS.keys())):
        # logs
        return log_entry_formatter(value)

    elif either_set_is_a_subset(
        response_key_set, set(TRANSACTION_RESULT_FORMATTERS.keys())
    ):
        # transaction subscription type (newPendingTransactions), full transactions
        return transaction_result_formatter(value)

    elif any(_ in response_key_set for _ in {"syncing", "status"}):
        # geth syncing response
        return type_aware_apply_formatters_to_dict(GETH_SYNCING_SUBSCRIPTION_FORMATTERS)

    elif either_set_is_a_subset(response_key_set, set(SYNCING_FORMATTERS.keys())):
        # syncing response object
        return syncing_formatter

    # fallback to returning the value as-is
    return value


PYTHONIC_RESULT_FORMATTERS: Dict[RPCEndpoint, Callable[..., Any]] = {
    # Eth
    RPC.eth_accounts: apply_list_to_array_formatter(to_checksum_address),
    RPC.eth_blockNumber: to_integer_if_hex,
    RPC.eth_chainId: to_integer_if_hex,
    RPC.eth_coinbase: to_checksum_address,
    RPC.eth_call: HexBytes,
    RPC.eth_estimateGas: to_integer_if_hex,
    RPC.eth_feeHistory: fee_history_formatter,
    RPC.eth_maxPriorityFeePerGas: to_integer_if_hex,
    RPC.eth_gasPrice: to_integer_if_hex,
    RPC.eth_getBalance: to_integer_if_hex,
    RPC.eth_getBlockByHash: apply_formatter_if(is_not_null, block_formatter),
    RPC.eth_getBlockByNumber: apply_formatter_if(is_not_null, block_formatter),
    RPC.eth_getBlockTransactionCountByHash: to_integer_if_hex,
    RPC.eth_getBlockTransactionCountByNumber: to_integer_if_hex,
    RPC.eth_getCode: HexBytes,
    RPC.eth_getFilterChanges: filter_result_formatter,
    RPC.eth_getFilterLogs: filter_result_formatter,
    RPC.eth_getLogs: filter_result_formatter,
    RPC.eth_getProof: apply_formatter_if(is_not_null, proof_formatter),
    RPC.eth_getRawTransactionByBlockHashAndIndex: HexBytes,
    RPC.eth_getRawTransactionByBlockNumberAndIndex: HexBytes,
    RPC.eth_getRawTransactionByHash: HexBytes,
    RPC.eth_getStorageAt: HexBytes,
    RPC.eth_getTransactionByBlockHashAndIndex: apply_formatter_if(
        is_not_null,
        transaction_result_formatter,
    ),
    RPC.eth_getTransactionByBlockNumberAndIndex: apply_formatter_if(
        is_not_null,
        transaction_result_formatter,
    ),
    RPC.eth_getTransactionByHash: apply_formatter_if(
        is_not_null, transaction_result_formatter
    ),
    RPC.eth_getTransactionCount: to_integer_if_hex,
    RPC.eth_getTransactionReceipt: apply_formatter_if(
        is_not_null,
        receipt_formatter,
    ),
    RPC.eth_getUncleCountByBlockHash: to_integer_if_hex,
    RPC.eth_getUncleCountByBlockNumber: to_integer_if_hex,
    RPC.eth_hashrate: to_integer_if_hex,
    RPC.eth_protocolVersion: compose(
        apply_formatter_if(is_0x_prefixed, to_integer_if_hex),
        apply_formatter_if(is_integer, str),
    ),
    RPC.eth_sendRawTransaction: to_hexbytes(32),
    RPC.eth_sendTransaction: to_hexbytes(32),
    RPC.eth_sign: HexBytes,
    RPC.eth_signTransaction: apply_formatter_if(is_not_null, signed_tx_formatter),
    RPC.eth_signTypedData: HexBytes,
    RPC.eth_syncing: apply_formatter_if(is_not_false, syncing_formatter),
    # personal
    RPC.personal_importRawKey: to_checksum_address,
    RPC.personal_listAccounts: apply_list_to_array_formatter(to_checksum_address),
    RPC.personal_listWallets: apply_list_to_array_formatter(geth_wallets_formatter),
    RPC.personal_newAccount: to_checksum_address,
    RPC.personal_sendTransaction: to_hexbytes(32),
    RPC.personal_signTypedData: HexBytes,
    # Transaction Pool
    RPC.txpool_content: transaction_pool_content_formatter,
    RPC.txpool_inspect: transaction_pool_inspect_formatter,
    # Snapshot and Revert
    RPC.evm_snapshot: hex_to_integer,
    # Net
    RPC.net_peerCount: to_integer_if_hex,
    # tracing
    RPC.trace_block: trace_list_result_formatter,
    RPC.trace_call: common_tracing_result_formatter,
    RPC.trace_transaction: trace_list_result_formatter,
    RPC.trace_rawTransaction: common_tracing_result_formatter,
    RPC.trace_replayTransaction: common_tracing_result_formatter,
    RPC.trace_replayBlockTransactions: apply_formatter_to_array(
        common_tracing_result_formatter
    ),
    RPC.trace_filter: trace_list_result_formatter,
    # Subscriptions (websockets)
    RPC.eth_subscribe: apply_formatter_if(
        is_not_null,
        subscription_formatter,
    ),
}

METHOD_NORMALIZERS: Dict[RPCEndpoint, Callable[..., Any]] = {
    RPC.eth_getLogs: apply_formatter_at_index(FILTER_PARAM_NORMALIZERS, 0),
    RPC.eth_newFilter: apply_formatter_at_index(FILTER_PARAM_NORMALIZERS, 0),
}

STANDARD_NORMALIZERS = [
    abi_bytes_to_hex,
    abi_int_to_hex,
    abi_string_to_hex,
    abi_address_to_hex,
]


ABI_REQUEST_FORMATTERS: Formatters = abi_request_formatters(
    STANDARD_NORMALIZERS, RPC_ABIS
)


ERROR_FORMATTERS: Dict[RPCEndpoint, Callable[..., Any]] = {
    RPC.eth_estimateGas: raise_contract_logic_error_on_revert,
    RPC.eth_call: raise_contract_logic_error_on_revert,
}


@to_tuple
def combine_formatters(
    formatter_maps: Collection[Dict[RPCEndpoint, Callable[..., TReturn]]],
    method_name: RPCEndpoint,
) -> Iterable[Callable[..., TReturn]]:
    for formatter_map in formatter_maps:
        if method_name in formatter_map:
            yield formatter_map[method_name]


def get_request_formatters(
    method_name: Union[RPCEndpoint, Callable[..., RPCEndpoint]]
) -> Dict[str, Callable[..., Any]]:
    request_formatter_maps = (
        ABI_REQUEST_FORMATTERS,
        # METHOD_NORMALIZERS needs to be after ABI_REQUEST_FORMATTERS
        # so that eth_getLogs's apply_formatter_at_index formatter
        # is applied to the whole address
        # rather than on the first byte of the address
        METHOD_NORMALIZERS,
        PYTHONIC_REQUEST_FORMATTERS,
    )
    formatters = combine_formatters(request_formatter_maps, method_name)
    return compose(*formatters)


def raise_block_not_found(params: Tuple[BlockIdentifier, bool]) -> NoReturn:
    try:
        block_identifier = params[0]
        message = f"Block with id: {block_identifier!r} not found."
    except IndexError:
        message = "Unknown block identifier"

    raise BlockNotFound(message)


def raise_block_not_found_for_uncle_at_index(
    params: Tuple[BlockIdentifier, Union[HexStr, int]]
) -> NoReturn:
    try:
        block_identifier = params[0]
        uncle_index = to_integer_if_hex(params[1])
        message = (
            f"Uncle at index: {uncle_index} of block with id: "
            f"{block_identifier!r} not found."
        )
    except IndexError:
        message = "Unknown block identifier or uncle index"

    raise BlockNotFound(message)


def raise_transaction_not_found(params: Tuple[_Hash32]) -> NoReturn:
    try:
        transaction_hash = params[0]
        message = f"Transaction with hash: {transaction_hash!r} not found."
    except IndexError:
        message = "Unknown transaction hash"

    raise TransactionNotFound(message)


def raise_transaction_not_found_with_index(
    params: Tuple[BlockIdentifier, int]
) -> NoReturn:
    try:
        block_identifier = params[0]
        transaction_index = to_integer_if_hex(params[1])
        message = (
            f"Transaction index: {transaction_index} "
            f"on block id: {block_identifier!r} not found."
        )
    except IndexError:
        message = "Unknown transaction index or block identifier"

    raise TransactionNotFound(message)


NULL_RESULT_FORMATTERS: Dict[RPCEndpoint, Callable[..., Any]] = {
    RPC.eth_getBlockByHash: raise_block_not_found,
    RPC.eth_getBlockByNumber: raise_block_not_found,
    RPC.eth_getBlockTransactionCountByHash: raise_block_not_found,
    RPC.eth_getBlockTransactionCountByNumber: raise_block_not_found,
    RPC.eth_getUncleCountByBlockHash: raise_block_not_found,
    RPC.eth_getUncleCountByBlockNumber: raise_block_not_found,
    RPC.eth_getUncleByBlockHashAndIndex: raise_block_not_found_for_uncle_at_index,
    RPC.eth_getUncleByBlockNumberAndIndex: raise_block_not_found_for_uncle_at_index,
    RPC.eth_getTransactionByHash: raise_transaction_not_found,
    RPC.eth_getTransactionByBlockHashAndIndex: raise_transaction_not_found_with_index,
    RPC.eth_getTransactionByBlockNumberAndIndex: raise_transaction_not_found_with_index,
    RPC.eth_getTransactionReceipt: raise_transaction_not_found,
    RPC.eth_getRawTransactionByBlockHashAndIndex: raise_transaction_not_found_with_index,  # noqa: E501
    RPC.eth_getRawTransactionByBlockNumberAndIndex: raise_transaction_not_found_with_index,  # noqa: E501
    RPC.eth_getRawTransactionByHash: raise_transaction_not_found,
}


def filter_wrapper(
    module: Union["AsyncEth", "Eth"],
    method: RPCEndpoint,
    filter_id: HexStr,
) -> Union[
    AsyncBlockFilter,
    AsyncTransactionFilter,
    AsyncLogFilter,
    BlockFilter,
    TransactionFilter,
    LogFilter,
]:
    if method == RPC.eth_newBlockFilter:
        if module.is_async:
            return AsyncBlockFilter(filter_id, eth_module=cast("AsyncEth", module))
        else:
            return BlockFilter(filter_id, eth_module=cast("Eth", module))
    elif method == RPC.eth_newPendingTransactionFilter:
        if module.is_async:
            return AsyncTransactionFilter(
                filter_id, eth_module=cast("AsyncEth", module)
            )
        else:
            return TransactionFilter(filter_id, eth_module=cast("Eth", module))
    elif method == RPC.eth_newFilter:
        if module.is_async:
            return AsyncLogFilter(filter_id, eth_module=cast("AsyncEth", module))
        else:
            return LogFilter(filter_id, eth_module=cast("Eth", module))
    else:
        raise NotImplementedError(
            "Filter wrapper needs to be used with either "
            f"{RPC.eth_newBlockFilter}, {RPC.eth_newPendingTransactionFilter}"
            f" or {RPC.eth_newFilter}"
        )


FILTER_RESULT_FORMATTERS: Dict[RPCEndpoint, Callable[..., Any]] = {
    RPC.eth_newPendingTransactionFilter: filter_wrapper,
    RPC.eth_newBlockFilter: filter_wrapper,
    RPC.eth_newFilter: filter_wrapper,
}


@to_tuple
def apply_module_to_formatters(
    formatters: Tuple[Callable[..., TReturn]],
    module: "Module",
    method_name: Union[RPCEndpoint, Callable[..., RPCEndpoint]],
) -> Iterable[Callable[..., TReturn]]:
    for f in formatters:
        yield partial(f, module, method_name)


def get_result_formatters(
    method_name: Union[RPCEndpoint, Callable[..., RPCEndpoint]],
    module: "Module",
) -> Dict[str, Callable[..., Any]]:
    formatters = combine_formatters((PYTHONIC_RESULT_FORMATTERS,), method_name)
    formatters_requiring_module = combine_formatters(
        (FILTER_RESULT_FORMATTERS,), method_name
    )
    partial_formatters = apply_module_to_formatters(
        formatters_requiring_module, module, method_name
    )
    return compose(*partial_formatters, *formatters)


def get_error_formatters(
    method_name: Union[RPCEndpoint, Callable[..., RPCEndpoint]]
) -> Callable[..., Any]:
    #  Note error formatters work on the full response dict
    error_formatter_maps = (ERROR_FORMATTERS,)
    formatters = combine_formatters(error_formatter_maps, method_name)

    return compose(*formatters)


def get_null_result_formatters(
    method_name: Union[RPCEndpoint, Callable[..., RPCEndpoint]]
) -> Callable[..., Any]:
    formatters = combine_formatters((NULL_RESULT_FORMATTERS,), method_name)

    return compose(*formatters)
