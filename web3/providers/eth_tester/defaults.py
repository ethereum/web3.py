import operator
import random
import sys

from eth_tester.exceptions import (
    BlockNotFound,
    FilterNotFound,
    TransactionNotFound,
    ValidationError,
)
from eth_utils import (
    decode_hex,
    encode_hex,
    is_null,
    keccak,
)

from web3._utils.formatters import (
    apply_formatter_if,
)
from web3._utils.toolz import (
    compose,
    curry,
    excepts,
)


def not_implemented(*args, **kwargs):
    raise NotImplementedError("RPC method not implemented")


@curry
def call_eth_tester(fn_name, eth_tester, fn_args, fn_kwargs=None):
    if fn_kwargs is None:
        fn_kwargs = {}
    return getattr(eth_tester, fn_name)(*fn_args, **fn_kwargs)


def without_eth_tester(fn):
    # workaround for: https://github.com/pytoolz/cytoolz/issues/103
    # @functools.wraps(fn)
    def inner(eth_tester, params):
        return fn(params)
    return inner


def without_params(fn):
    # workaround for: https://github.com/pytoolz/cytoolz/issues/103
    # @functools.wraps(fn)
    def inner(eth_tester, params):
        return fn(eth_tester)
    return inner


@curry
def preprocess_params(eth_tester, params, preprocessor_fn):
    return eth_tester, preprocessor_fn(params)


def static_return(value):
    def inner(*args, **kwargs):
        return value
    return inner


def client_version(eth_tester, params):
    # TODO: account for the backend that is in use.
    from eth_tester import __version__
    return "EthereumTester/{version}/{platform}/python{v.major}.{v.minor}.{v.micro}".format(
        version=__version__,
        v=sys.version_info,
        platform=sys.platform,
    )


@curry
def null_if_excepts(exc_type, fn):
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
def get_transaction_by_block_hash_and_index(eth_tester, params):
    block_hash, transaction_index = params
    block = eth_tester.get_block_by_hash(block_hash, full_transactions=True)
    transaction = block['transactions'][transaction_index]
    return transaction


@null_if_indexerror
@null_if_block_not_found
def get_transaction_by_block_number_and_index(eth_tester, params):
    block_number, transaction_index = params
    block = eth_tester.get_block_by_number(block_number, full_transactions=True)
    transaction = block['transactions'][transaction_index]
    return transaction


def create_log_filter(eth_tester, params):
    filter_params = params[0]
    filter_id = eth_tester.create_log_filter(**filter_params)
    return filter_id


def get_logs(eth_tester, params):
    filter_params = params[0]
    logs = eth_tester.get_logs(**filter_params)
    return logs


def _generate_random_private_key():
    """
    WARNING: This is not a secure way to generate private keys and should only
    be used for testing purposes.
    """
    return encode_hex(bytes(bytearray((
        random.randint(0, 255)
        for _ in range(32)
    ))))


@without_params
def create_new_account(eth_tester):
    return eth_tester.add_account(_generate_random_private_key())


def personal_send_transaction(eth_tester, params):
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
        'peerCount': static_return(0),
        'listening': static_return(False),
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
        'gasPrice': static_return(1),
        'accounts': call_eth_tester('get_accounts'),
        'blockNumber': compose(
            operator.itemgetter('number'),
            call_eth_tester('get_block_by_number', fn_kwargs={'block_number': 'latest'}),
        ),
        'getBalance': call_eth_tester('get_balance'),
        'getStorageAt': not_implemented,
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
    'shh': {
        'post': not_implemented,
        'version': not_implemented,
        'newIdentity': not_implemented,
        'hasIdentity': not_implemented,
        'newGroup': not_implemented,
        'addToGroup': not_implemented,
        'newFilter': not_implemented,
        'uninstallFilter': not_implemented,
        'getFilterChanges': not_implemented,
        'getMessages': not_implemented,
    },
    'admin': {
        'addPeer': not_implemented,
        'datadir': not_implemented,
        'nodeInfo': not_implemented,
        'peers': not_implemented,
        'setSolc': not_implemented,
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
        'makeDAG': not_implemented,
        'setExtra': not_implemented,
        'setGasPrice': not_implemented,
        'start': not_implemented,
        'startAutoDAG': not_implemented,
        'stop': not_implemented,
        'stopAutoDAG': not_implemented,
    },
    'personal': {
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
        'sign': not_implemented,
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
