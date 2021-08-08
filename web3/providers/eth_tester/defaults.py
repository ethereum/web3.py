import operator
import random
import sys
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    List,
    NoReturn,
    Optional,
    Tuple,
    Type,
)

from eth_tester.exceptions import (
    BlockNotFound,
    FilterNotFound,
    TransactionNotFound,
    ValidationError,
)
from eth_typing import (
    HexAddress,
    HexStr,
)
from eth_utils import (
    decode_hex,
    encode_hex,
    is_null,
    keccak,
)
from eth_utils.curried import (
    apply_formatter_if,
)
from eth_utils.toolz import (
    compose,
    curry,
    excepts,
)

from web3.types import (
    LogReceipt,
    RPCResponse,
    TParams,
    TReturn,
    TValue,
    TxReceipt,
)

if TYPE_CHECKING:
    from eth_tester import (  # noqa: F401
        EthereumTester,
    )


def not_implemented(*args: Any, **kwargs: Any) -> NoReturn:
    raise NotImplementedError("RPC method not implemented")


@curry
def call_eth_tester(
    fn_name: str, eth_tester: "EthereumTester", fn_args: Any,
    fn_kwargs: Optional[Any] = None
) -> RPCResponse:
    if fn_kwargs is None:
        fn_kwargs = {}
    return getattr(eth_tester, fn_name)(*fn_args, **fn_kwargs)


def without_eth_tester(
    fn: Callable[[TParams], TReturn]
) -> Callable[["EthereumTester", TParams], TReturn]:
    # workaround for: https://github.com/pytoolz/cytoolz/issues/103
    # @functools.wraps(fn)
    def inner(eth_tester: "EthereumTester", params: TParams) -> TReturn:
        return fn(params)
    return inner


def without_params(
    fn: Callable[[TParams], TReturn]
) -> Callable[["EthereumTester", TParams], TReturn]:
    # workaround for: https://github.com/pytoolz/cytoolz/issues/103
    # @functools.wraps(fn)
    def inner(eth_tester: "EthereumTester", params: Any) -> TReturn:
        return fn(eth_tester)
    return inner


@curry
def preprocess_params(
    eth_tester: "EthereumTester", params: Any, preprocessor_fn: Callable[..., Any]
) -> Tuple["EthereumTester", Callable[..., Any]]:
    return eth_tester, preprocessor_fn(params)


def static_return(value: TValue) -> Callable[..., TValue]:
    def inner(*args: Any, **kwargs: Any) -> TValue:
        return value
    return inner


def client_version(eth_tester: "EthereumTester", params: Any) -> str:
    # TODO: account for the backend that is in use.
    from eth_tester import __version__
    return "EthereumTester/{version}/{platform}/python{v.major}.{v.minor}.{v.micro}".format(
        version=__version__,
        v=sys.version_info,
        platform=sys.platform,
    )


@curry
def null_if_excepts(
    exc_type: Type[BaseException], fn: Callable[..., TReturn]
) -> Callable[..., TReturn]:
    return excepts(
        exc_type,
        fn,
        static_return(None),
    )


null_if_block_not_found = null_if_excepts(BlockNotFound)
null_if_transaction_not_found = null_if_excepts(TransactionNotFound)
null_if_filter_not_found = null_if_excepts(FilterNotFound)
null_if_indexerror = null_if_excepts(IndexError)


@null_if_indexerror
@null_if_block_not_found
def get_transaction_by_block_hash_and_index(
    eth_tester: "EthereumTester", params: Any
) -> TxReceipt:
    block_hash, transaction_index = params
    block = eth_tester.get_block_by_hash(block_hash, full_transactions=True)
    transaction = block['transactions'][transaction_index]
    return transaction


@null_if_indexerror
@null_if_block_not_found
def get_transaction_by_block_number_and_index(
    eth_tester: "EthereumTester", params: Any
) -> TxReceipt:
    block_number, transaction_index = params
    block = eth_tester.get_block_by_number(block_number, full_transactions=True)
    transaction = block['transactions'][transaction_index]
    return transaction


def create_log_filter(eth_tester: "EthereumTester", params: Any) -> int:
    filter_params = params[0]
    filter_id = eth_tester.create_log_filter(**filter_params)
    return filter_id


def get_logs(eth_tester: "EthereumTester", params: Any) -> List[LogReceipt]:
    filter_params = params[0]
    logs = eth_tester.get_logs(**filter_params)
    return logs


def _generate_random_private_key() -> HexStr:
    """
    WARNING: This is not a secure way to generate private keys and should only
    be used for testing purposes.
    """
    return encode_hex(bytes(bytearray((
        random.randint(0, 255)
        for _ in range(32)
    ))))


@without_params
def create_new_account(eth_tester: "EthereumTester") -> HexAddress:
    return eth_tester.add_account(_generate_random_private_key())


def personal_send_transaction(eth_tester: "EthereumTester", params: Any) -> HexStr:
    transaction, password = params

    try:
        eth_tester.unlock_account(transaction['from'], password)
        transaction_hash = eth_tester.send_transaction(transaction)
    finally:
        eth_tester.lock_account(transaction['from'])

    return transaction_hash


API_ENDPOINTS = {
    'web3': {
        'clientVersion': client_version,
        'sha3': compose(
            encode_hex,
            keccak,
            decode_hex,
            without_eth_tester(operator.itemgetter(0)),
        ),
    },
    'net': {
        'version': static_return('1'),
        'listening': static_return(False),
        'peerCount': static_return(0),
    },
    'eth': {
        'protocolVersion': static_return(63),
        'syncing': static_return(False),
        'coinbase': compose(
            operator.itemgetter(0),
            call_eth_tester('get_accounts'),
        ),
        'mining': static_return(False),
        'hashrate': static_return(0),
        'chainId': static_return('0x3d'),
        'feeHistory': not_implemented,
        'maxPriorityFeePerGas': not_implemented,
        'gasPrice': static_return(1),
        'accounts': call_eth_tester('get_accounts'),
        'blockNumber': compose(
            operator.itemgetter('number'),
            call_eth_tester('get_block_by_number', fn_kwargs={'block_number': 'latest'}),
        ),
        'getBalance': call_eth_tester('get_balance'),
        'getStorageAt': not_implemented,
        'getProof': not_implemented,
        'getTransactionCount': call_eth_tester('get_nonce'),
        'getBlockTransactionCountByHash': null_if_block_not_found(compose(
            len,
            operator.itemgetter('transactions'),
            call_eth_tester('get_block_by_hash'),
        )),
        'getBlockTransactionCountByNumber': null_if_block_not_found(compose(
            len,
            operator.itemgetter('transactions'),
            call_eth_tester('get_block_by_number'),
        )),
        'getUncleCountByBlockHash': null_if_block_not_found(compose(
            len,
            operator.itemgetter('uncles'),
            call_eth_tester('get_block_by_hash'),
        )),
        'getUncleCountByBlockNumber': null_if_block_not_found(compose(
            len,
            operator.itemgetter('uncles'),
            call_eth_tester('get_block_by_number'),
        )),
        'getCode': call_eth_tester('get_code'),
        'sign': not_implemented,
        'signTransaction': not_implemented,
        'sendTransaction': call_eth_tester('send_transaction'),
        'sendRawTransaction': call_eth_tester('send_raw_transaction'),
        'call': call_eth_tester('call'),  # TODO: untested
        'estimateGas': call_eth_tester('estimate_gas'),  # TODO: untested
        'getBlockByHash': null_if_block_not_found(call_eth_tester('get_block_by_hash')),
        'getBlockByNumber': null_if_block_not_found(call_eth_tester('get_block_by_number')),
        'getTransactionByHash': null_if_transaction_not_found(
            call_eth_tester('get_transaction_by_hash')
        ),
        'getTransactionByBlockHashAndIndex': get_transaction_by_block_hash_and_index,
        'getTransactionByBlockNumberAndIndex': get_transaction_by_block_number_and_index,
        'getTransactionReceipt': null_if_transaction_not_found(compose(
            apply_formatter_if(
                compose(is_null, operator.itemgetter('block_number')),
                static_return(None),
            ),
            call_eth_tester('get_transaction_receipt'),
        )),
        'getUncleByBlockHashAndIndex': not_implemented,
        'getUncleByBlockNumberAndIndex': not_implemented,
        'getCompilers': not_implemented,
        'compileLLL': not_implemented,
        'compileSolidity': not_implemented,
        'compileSerpent': not_implemented,
        'newFilter': create_log_filter,
        'newBlockFilter': call_eth_tester('create_block_filter'),
        'newPendingTransactionFilter': call_eth_tester('create_pending_transaction_filter'),
        'uninstallFilter': excepts(
            FilterNotFound,
            compose(
                is_null,
                call_eth_tester('delete_filter'),
            ),
            static_return(False),
        ),
        'getFilterChanges': null_if_filter_not_found(call_eth_tester('get_only_filter_changes')),
        'getFilterLogs': null_if_filter_not_found(call_eth_tester('get_all_filter_logs')),
        'getLogs': get_logs,
        'getWork': not_implemented,
        'submitWork': not_implemented,
        'submitHashrate': not_implemented,
    },
    'db': {
        'putString': not_implemented,
        'getString': not_implemented,
        'putHex': not_implemented,
        'getHex': not_implemented,
    },
    'admin': {
        'add_peer': not_implemented,
        'node_info': not_implemented,
        'start_rpc': not_implemented,
        'start_ws': not_implemented,
        'stop_rpc': not_implemented,
        'stop_ws': not_implemented,
        # deprecated
        'addPeer': not_implemented,
        'datadir': not_implemented,
        'nodeInfo': not_implemented,
        'peers': not_implemented,
        'startRPC': not_implemented,
        'startWS': not_implemented,
        'stopRPC': not_implemented,
        'stopWS': not_implemented,
    },
    'debug': {
        'backtraceAt': not_implemented,
        'blockProfile': not_implemented,
        'cpuProfile': not_implemented,
        'dumpBlock': not_implemented,
        'gtStats': not_implemented,
        'getBlockRLP': not_implemented,
        'goTrace': not_implemented,
        'memStats': not_implemented,
        'seedHashSign': not_implemented,
        'setBlockProfileRate': not_implemented,
        'setHead': not_implemented,
        'stacks': not_implemented,
        'startCPUProfile': not_implemented,
        'startGoTrace': not_implemented,
        'stopCPUProfile': not_implemented,
        'stopGoTrace': not_implemented,
        'traceBlock': not_implemented,
        'traceBlockByNumber': not_implemented,
        'traceBlockByHash': not_implemented,
        'traceBlockFromFile': not_implemented,
        'traceTransaction': not_implemented,
        'verbosity': not_implemented,
        'vmodule': not_implemented,
        'writeBlockProfile': not_implemented,
        'writeMemProfile': not_implemented,
    },
    'miner': {
        'make_dag': not_implemented,
        'set_extra': not_implemented,
        'set_gas_price': not_implemented,
        'start': not_implemented,
        'stop': not_implemented,
        'start_auto_dag': not_implemented,
        'stop_auto_dag': not_implemented,
        # deprecated
        'makeDAG': not_implemented,
        'setExtra': not_implemented,
        'setGasPrice': not_implemented,
        'startAutoDAG': not_implemented,
        'stopAutoDAG': not_implemented,
    },
    'personal': {
        'ec_recover': not_implemented,
        'import_raw_key': call_eth_tester('add_account'),
        'list_accounts': call_eth_tester('get_accounts'),
        'list_wallets': not_implemented,
        'lock_account': excepts(
            ValidationError,
            compose(static_return(True), call_eth_tester('lock_account')),
            static_return(False),
        ),
        'new_account': create_new_account,
        'unlock_account': excepts(
            ValidationError,
            compose(static_return(True), call_eth_tester('unlock_account')),
            static_return(False),
        ),
        'send_transaction': personal_send_transaction,
        'sign': not_implemented,
        # deprecated
        'ecRecover': not_implemented,
        'importRawKey': call_eth_tester('add_account'),
        'listAccounts': call_eth_tester('get_accounts'),
        'lockAccount': excepts(
            ValidationError,
            compose(static_return(True), call_eth_tester('lock_account')),
            static_return(False),
        ),
        'newAccount': create_new_account,
        'unlockAccount': excepts(
            ValidationError,
            compose(static_return(True), call_eth_tester('unlock_account')),
            static_return(False),
        ),
        'sendTransaction': personal_send_transaction,
    },
    'testing': {
        'timeTravel': call_eth_tester('time_travel'),
    },
    'txpool': {
        'content': not_implemented,
        'inspect': not_implemented,
        'status': not_implemented,
    },
    'evm': {
        'mine': call_eth_tester('mine_blocks'),
        'revert': call_eth_tester('revert_to_snapshot'),
        'snapshot': call_eth_tester('take_snapshot'),
    },
}
