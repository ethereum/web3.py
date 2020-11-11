from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Sequence,
    Tuple,
)

from eth_typing import (
    TypeStr,
)
from eth_utils import (
    to_dict,
)
from eth_utils.curried import (
    apply_formatter_at_index,
)
from eth_utils.toolz import (
    curry,
)

from web3._utils.abi import (
    map_abi_data,
)
from web3.types import (
    RPCEndpoint,
)


class RPC:
    # admin
    admin_addPeer = RPCEndpoint("admin_addPeer")
    admin_datadir = RPCEndpoint("admin_datadir")
    admin_nodeInfo = RPCEndpoint("admin_nodeInfo")
    admin_peers = RPCEndpoint("admin_peers")
    admin_startRPC = RPCEndpoint("admin_startRPC")
    admin_startWS = RPCEndpoint("admin_startWS")
    admin_stopRPC = RPCEndpoint("admin_stopRPC")
    admin_stopWS = RPCEndpoint("admin_stopWS")

    # eth
    eth_accounts = RPCEndpoint("eth_accounts")
    eth_blockNumber = RPCEndpoint("eth_blockNumber")
    eth_call = RPCEndpoint("eth_call")
    eth_chainId = RPCEndpoint("eth_chainId")
    eth_coinbase = RPCEndpoint("eth_coinbase")
    eth_estimateGas = RPCEndpoint("eth_estimateGas")
    eth_gasPrice = RPCEndpoint("eth_gasPrice")
    eth_getBalance = RPCEndpoint("eth_getBalance")
    eth_getBlockByHash = RPCEndpoint("eth_getBlockByHash")
    eth_getBlockByNumber = RPCEndpoint("eth_getBlockByNumber")
    eth_getBlockTransactionCountByHash = RPCEndpoint("eth_getBlockTransactionCountByHash")
    eth_getBlockTransactionCountByNumber = RPCEndpoint("eth_getBlockTransactionCountByNumber")
    eth_getCode = RPCEndpoint("eth_getCode")
    eth_getFilterChanges = RPCEndpoint("eth_getFilterChanges")
    eth_getFilterLogs = RPCEndpoint("eth_getFilterLogs")
    eth_getLogs = RPCEndpoint("eth_getLogs")
    eth_getProof = RPCEndpoint("eth_getProof")
    eth_getStorageAt = RPCEndpoint("eth_getStorageAt")
    eth_getTransactionByBlockHashAndIndex = RPCEndpoint("eth_getTransactionByBlockHashAndIndex")
    eth_getTransactionByBlockNumberAndIndex = RPCEndpoint("eth_getTransactionByBlockNumberAndIndex")
    eth_getTransactionByHash = RPCEndpoint("eth_getTransactionByHash")
    eth_getTransactionCount = RPCEndpoint("eth_getTransactionCount")
    eth_getTransactionReceipt = RPCEndpoint("eth_getTransactionReceipt")
    eth_getUncleByBlockHashAndIndex = RPCEndpoint("eth_getUncleByBlockHashAndIndex")
    eth_getUncleByBlockNumberAndIndex = RPCEndpoint("eth_getUncleByBlockNumberAndIndex")
    eth_getUncleCountByBlockHash = RPCEndpoint("eth_getUncleCountByBlockHash")
    eth_getUncleCountByBlockNumber = RPCEndpoint("eth_getUncleCountByBlockNumber")
    eth_getWork = RPCEndpoint("eth_getWork")
    eth_hashrate = RPCEndpoint("eth_hashrate")
    eth_mining = RPCEndpoint("eth_mining")
    eth_newBlockFilter = RPCEndpoint("eth_newBlockFilter")
    eth_newFilter = RPCEndpoint("eth_newFilter")
    eth_newPendingTransactionFilter = RPCEndpoint("eth_newPendingTransactionFilter")
    eth_protocolVersion = RPCEndpoint("eth_protocolVersion")
    eth_sendRawTransaction = RPCEndpoint("eth_sendRawTransaction")
    eth_sendTransaction = RPCEndpoint("eth_sendTransaction")
    eth_sign = RPCEndpoint("eth_sign")
    eth_signTransaction = RPCEndpoint("eth_signTransaction")
    eth_signTypedData = RPCEndpoint("eth_signTypedData")
    eth_submitHashrate = RPCEndpoint("eth_submitHashrate")
    eth_submitWork = RPCEndpoint("eth_submitWork")
    eth_syncing = RPCEndpoint("eth_syncing")
    eth_uninstallFilter = RPCEndpoint("eth_uninstallFilter")

    # evm
    evm_mine = RPCEndpoint("evm_mine")
    evm_reset = RPCEndpoint("evm_reset")
    evm_revert = RPCEndpoint("evm_revert")
    evm_snapshot = RPCEndpoint("evm_snapshot")

    # miner
    miner_makeDag = RPCEndpoint("miner_makeDag")
    miner_setExtra = RPCEndpoint("miner_setExtra")
    miner_setEtherbase = RPCEndpoint("miner_setEtherbase")
    miner_setGasPrice = RPCEndpoint("miner_setGasPrice")
    miner_start = RPCEndpoint("miner_start")
    miner_stop = RPCEndpoint("miner_stop")
    miner_startAutoDag = RPCEndpoint("miner_startAutoDag")
    miner_stopAutoDag = RPCEndpoint("miner_stopAutoDag")

    # net
    net_listening = RPCEndpoint("net_listening")
    net_peerCount = RPCEndpoint("net_peerCount")
    net_version = RPCEndpoint("net_version")

    # parity
    parity_addReservedPeer = RPCEndpoint("parity_addReservedPeer")
    parity_enode = RPCEndpoint("parity_enode")
    parity_listStorageKeys = RPCEndpoint("parity_listStorageKeys")
    parity_netPeers = RPCEndpoint("parity_netPeers")
    parity_mode = RPCEndpoint("parity_mode")
    parity_setMode = RPCEndpoint("parity_setMode")

    # personal
    personal_ecRecover = RPCEndpoint("personal_ecRecover")
    personal_importRawKey = RPCEndpoint("personal_importRawKey")
    personal_listAccounts = RPCEndpoint("personal_listAccounts")
    personal_listWallets = RPCEndpoint("personal_listWallets")
    personal_lockAccount = RPCEndpoint("personal_lockAccount")
    personal_newAccount = RPCEndpoint("personal_newAccount")
    personal_sendTransaction = RPCEndpoint("personal_sendTransaction")
    personal_sign = RPCEndpoint("personal_sign")
    personal_signTypedData = RPCEndpoint("personal_signTypedData")
    personal_unlockAccount = RPCEndpoint("personal_unlockAccount")

    # testing
    testing_timeTravel = RPCEndpoint("testing_timeTravel")

    # trace
    trace_block = RPCEndpoint("trace_block")
    trace_call = RPCEndpoint("trace_call")
    trace_filter = RPCEndpoint("trace_filter")
    trace_rawTransaction = RPCEndpoint("trace_rawTransaction")
    trace_replayBlockTransactions = RPCEndpoint("trace_replayBlockTransactions")
    trace_replayTransaction = RPCEndpoint("trace_replayTransaction")
    trace_transaction = RPCEndpoint("trace_transaction")

    # txpool
    txpool_content = RPCEndpoint("txpool_content")
    txpool_inspect = RPCEndpoint("txpool_inspect")
    txpool_status = RPCEndpoint("txpool_status")

    # web3
    web3_clientVersion = RPCEndpoint("web3_clientVersion")


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
    'eth_getProof': ['address', 'uint[]', None],
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
def apply_abi_formatters_to_dict(
    normalizers: Sequence[Callable[[TypeStr, Any], Tuple[TypeStr, Any]]],
    abi_dict: Dict[str, Any],
    data: Dict[Any, Any]
) -> Dict[Any, Any]:
    fields = list(set(abi_dict.keys()) & set(data.keys()))
    formatted_values = map_abi_data(
        normalizers,
        [abi_dict[field] for field in fields],
        [data[field] for field in fields],
    )
    formatted_dict = dict(zip(fields, formatted_values))
    return dict(data, **formatted_dict)


@to_dict
def abi_request_formatters(
    normalizers: Sequence[Callable[[TypeStr, Any], Tuple[TypeStr, Any]]],
    abis: Dict[RPCEndpoint, Any],
) -> Iterable[Tuple[RPCEndpoint, Callable[..., Any]]]:
    for method, abi_types in abis.items():
        if isinstance(abi_types, list):
            yield method, map_abi_data(normalizers, abi_types)
        elif isinstance(abi_types, dict):
            single_dict_formatter = apply_abi_formatters_to_dict(normalizers, abi_types)
            yield method, apply_formatter_at_index(single_dict_formatter, 0)
        else:
            raise TypeError("ABI definitions must be a list or dictionary, got %r" % abi_types)
