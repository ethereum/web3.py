from eth_utils import (
    to_dict,
)
from eth_utils.toolz import (
    curry,
)

from web3._utils.abi import (
    map_abi_data,
)
from web3._utils.formatters import (
    apply_formatter_at_index,
)

TRANSACTION_PARAMS_ABIS = {
    'data': 'bytes',
    'from': 'address',
    'gas': 'uint',
    'gasPrice': 'uint',
    'nonce': 'uint',
    'to': 'address',
    'value': 'uint',
}

FILTER_PARAMS_ABIS = {
    'to': 'address',
    'address': 'address[]',
}

TRACE_PARAMS_ABIS = {
    'to': 'address',
    'from': 'address',
}

RPC_ABIS = {
    # eth
    'eth_call': TRANSACTION_PARAMS_ABIS,
    'eth_estimateGas': TRANSACTION_PARAMS_ABIS,
    'eth_getBalance': ['address', None],
    'eth_getBlockByHash': ['bytes32', 'bool'],
    'eth_getBlockTransactionCountByHash': ['bytes32'],
    'eth_getCode': ['address', None],
    'eth_getLogs': FILTER_PARAMS_ABIS,
    'eth_getStorageAt': ['address', 'uint', None],
    'eth_getTransactionByBlockHashAndIndex': ['bytes32', 'uint'],
    'eth_getTransactionByHash': ['bytes32'],
    'eth_getTransactionCount': ['address', None],
    'eth_getTransactionReceipt': ['bytes32'],
    'eth_getUncleCountByBlockHash': ['bytes32'],
    'eth_newFilter': FILTER_PARAMS_ABIS,
    'eth_sendRawTransaction': ['bytes'],
    'eth_sendTransaction': TRANSACTION_PARAMS_ABIS,
    'eth_signTransaction': TRANSACTION_PARAMS_ABIS,
    'eth_sign': ['address', 'bytes'],
    'eth_signTypedData': ['address', None],
    'eth_submitHashrate': ['uint', 'bytes32'],
    'eth_submitWork': ['bytes8', 'bytes32', 'bytes32'],
    # personal
    'personal_sendTransaction': TRANSACTION_PARAMS_ABIS,
    'personal_lockAccount': ['address'],
    'personal_unlockAccount': ['address', None, None],
    'personal_sign': [None, 'address', None],
    'personal_signTypedData': [None, 'address', None],
    'trace_call': TRACE_PARAMS_ABIS,
    # parity
    'parity_listStorageKeys': ['address', None, None, None],
}


@curry
def apply_abi_formatters_to_dict(normalizers, abi_dict, data):
    fields = list(set(abi_dict.keys()) & set(data.keys()))
    formatted_values = map_abi_data(
        normalizers,
        [abi_dict[field] for field in fields],
        [data[field] for field in fields],
    )
    formatted_dict = dict(zip(fields, formatted_values))
    return dict(data, **formatted_dict)


@to_dict
def abi_request_formatters(normalizers, abis):
    for method, abi_types in abis.items():
        if isinstance(abi_types, list):
            yield method, map_abi_data(normalizers, abi_types)
        elif isinstance(abi_types, dict):
            single_dict_formatter = apply_abi_formatters_to_dict(normalizers, abi_types)
            yield method, apply_formatter_at_index(single_dict_formatter, 0)
        else:
            raise TypeError("ABI definitions must be a list or dictionary, got %r" % abi_types)
