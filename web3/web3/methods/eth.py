import web3.web3.formatters as formatters
import web3.utils.config as config
import web3.utils.encoding as encoding
import web3.utils.utils as utils
from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.web3.contract import ContractFactory
from web3.web3.iban import Iban


def alternativeCall(a, b):
    def partial(args):
        if utils.isString(args[0]) and args[0].startswith("0x"):
            return a
        else:
            return b
    return partial

blockCall = alternativeCall("eth_getBlockByHash", "eth_getBlockByNumber")
transactionFromBlockCall = alternativeCall(
    "eth_getTransactionByBlockHashAndIndex", "eth_getTransactionByBlockNumberAndIndex")
uncleCall = alternativeCall(
    "eth_getUncleByBlockHashAndIndex", "eth_getUncleByBlockNumberAndIndex")
getBlockTransactionCountCall = alternativeCall(
    "eth_getBlockTransactionCountByHash", "eth_getBlockTransactionCountByNumber")
uncleCountCall = alternativeCall(
    "eth_getUncleCountByBlockHash", "eth_getUncleCountByBlockNumber")

methods = [
    {
        "name": "getBalance",
        "call": "eth_getBalance",
        "params": 2,
        "inputFormatter":
        [formatters.inputAddressFormatter,
            formatters.inputDefaultBlockNumberFormatter],
        "outputFormatter": encoding.toDecimal
    },
    {
        "name": "getStorageAt",
        "call": "eth_getStorageAt",
        "params": 2,
        "inputFormatter":
        [None, encoding.toHex, formatters.inputDefaultBlockNumberFormatter]
    },
    {
        "name": "getCode",
        "call": "eth_getCode",
        "params": 2,
        "inputFormatter":
        [formatters.inputAddressFormatter,
            formatters.inputDefaultBlockNumberFormatter]
    },
    {
        "name": "getBlock",
        "call": blockCall,
        "params": 2,
        "inputFormatter":
        [formatters.inputBlockNumberFormatter, lambda val: val is not None],
        "outputFormatter": formatters.outputBlockFormatter
    },
    {
        "name": "getUncle",
        "call": "eth_Uncle",
        "params": 2,
        "inputFormatter":
        [None, encoding.toHex,
            formatters.inputBlockNumberFormatter, encoding.toHex],
        "outputFormatter": formatters.outputBlockFormatter
    },
    {
        "name": "getCompilers",
        "call": "eth_getCompilers",
        "params": 0,
    },
    {
        "name": "getBlockTransactionCount",
        "call": getBlockTransactionCountCall,
        "params": 1,
        "inputFormatter": [formatters.inputBlockNumberFormatter],
        "outputFormatter": encoding.toDecimal
    },
    {
        "name": "getBlockUncleCount",
        "call": uncleCountCall,
        "params": 1,
        "inputFormatter": [formatters.inputBlockNumberFormatter],
        "outputFormatter": encoding.toDecimal
    },
    {
        "name": "getTranscation",
        "call": "eth_getTransactionByHash",
        "params": 1,
        "inputFormatter": [formatters.inputBlockNumberFormatter],
    },
    {
        "name": "getTransactionFromBlock",
        "call": transactionFromBlockCall,
        "params": 2,
        "inputFormatter": [formatters.inputBlockNumberFormatter, encoding.toHex],
        "outputFormatter": formatters.outputTransactionFormatter

    },
    {
        "name": "getTransactionReceipt",
        "call": "eth_getTransactionReceipt",
        "params": 1,
        "outputFormatter": formatters.outputTransactionReceiptFormatter
    },
    {
        "name": "getTransactionCount",
        "call": "eth_getTransactionCount",
        "params": 2,
        "inputFormatter": [None, formatters.inputDefaultBlockNumberFormatter],
        "outputFormatter": encoding.toDecimal

    },
    {
        "name": "sendRawTransaction",
        "call": "eth_sendRawTransaction",
        "params": 1,
        "inputFormatter": [None]
    },
    {
        "name": "sendTransaction",
        "call": "eth_sendTransaction",
        "params": 1,
        "inputFormatter": [formatters.inputTransactionFormatter]
    },
    {
        "name": "sign",
        "call": "eth_sign",
        "params": 2,
        "inputFormatter": [formatters.inputAddressFormatter, None]
    },
    {
        "name": "call",
        "call": "eth_call",
        "params": 2,
        "inputFormatter":
        [formatters.inputCallFormatter,
            formatters.inputDefaultBlockNumberFormatter]
    },
    {
        "name": "estimateGas",
        "call": "eth_estimateGas",
        "params": 1,
        "inputFormatter": [formatters.inputCallFormatter],
        "outputFormatter": encoding.toDecimal
    },
    # compileSolidity, compileLLL, compileSerpent deprecated
    {
        "name": "submitWork",
        "call": "eth_submitWork",
        "params": 3,
    },
    {
        "name": "getWork",
        "call": "eth_getWork",
        "params": 1,
    }
]


properties = [
    {
        "name": "coinbase",
        "getter": "eth_coinbase"
    },
    {
        "name": "mining",
        "getter": "eth_mining"
    },
    {
        "name": "hashrate",
        "getter": "eth_hashrate",
        "outputFormatter": encoding.toDecimal
    },
    {
        "name": "syncing",
        "getter": "eth_syncing",
        "outputFormatter": formatters.outputSyncingFormatter
    },
    {
        "name": "gasPrice",
        "getter": "eth_gasPrice"
        # "outputFormatter": formatters.outputNumberFormatter
    },
    {
        "name": "accounts",
        "getter": "eth_accounts",
    },
    {
        "name": "blockNumber",
        "getter": "eth_blockNumber",
        "outputFormatter": encoding.toDecimal
    }
]


class DefaultAccount(object):
    def __set__(self, v):
        config.defaultAccount = self.value

    def __get__(self):
        return config.defaultAccount


class Eth(object):
    def __init__(self, request_manager):
        self.request_manager = request_manager

        self.defaultBlock = config.defaultBlock
        self.defaultAccount = DefaultAccount()  # config.defaultAccount

        self.iban = Iban
        # self.sendIBANTransaction = lambda: raise NotImplementedError()

    def namereg(self):
        raise NotImplementedError()

    def icapNamereg(self):
        raise NotImplementedError()

    @property
    def syncing(self):
        return self.request_manager.request_blocking("eth_syncing", [])

    def getSyncing(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    def isSyncing(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def coinbase(self):
        return self.request_manager.request_blocking("eth_coinbase", [])

    def getCoinbase(self):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def mining(self):
        return self.request_manager.request_blocking("eth_mining", [])

    def getMining(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def hashrate(self):
        return self.request_manager.request_blocking("eth_hashrate", [])

    def getHashrate(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(encoding.toDecimal)
    def gasPrice(self):
        return self.request_manager.request_blocking("eth_gasPrice", [])

    def getGasPrice(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def accounts(self):
        return self.request_manager.request_blocking("eth_accounts", [])

    def getAccounts(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(encoding.toDecimal)
    def blockNumber(self):
        return self.request_manager.request_blocking("eth_blockNumber", [])

    def getBlockNumber(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @apply_formatters_to_return(encoding.toDecimal)
    def getBalance(self, account, block_number=None):
        if block_number is None:
            block_number = self.defaultBlock
        return self.request_manager.request_blocking(
            "eth_getBalance",
            [account, block_number],
        )

    def getStorageAt(self, account, position, block_number=None):
        if block_number is None:
            block_number = self.defaultBlock
        return self.request_manager.request_blocking(
            "eth_getStorageAt",
            [account, position, block_number],
        )

    def getCode(self, account, block_number=None):
        if block_number is None:
            block_number = self.defaultBlock
        return self.request_manager.request_blocking(
            "eth_getCode",
            [account, block_number],
        )

    @apply_formatters_to_return(formatters.outputBlockFormatter)
    def getBlock(self, block_identifier, full_txns=False):
        """
        `eth_getBlockByHash`
        `eth_getBlockByNumber`
        """
        if encoding.is_integer(block_identifier):
            method = 'eth_getBlockByNumber'
        else:
            method = 'eth_getBlockByHash'

        return self.request_manager.request_blocking(
            method,
            [block_identifier, full_txns],
        )

    @apply_formatters_to_return(encoding.toDecimal)
    def getBlockTransactionCount(self, block_identifier):
        """
        `eth_getBlockTransactionCountByHash`
        `eth_getBlockTransactionCountByNumber`
        """
        if encoding.is_integer(block_identifier):
            method = 'eth_getBlockTransactionCountByNumber'
        else:
            method = 'eth_getBlockTransactionCountByHash'
        return self.request_manager.request_blocking(method, [block_identifier])

    def getUncle(self, block_identifier):
        """
        `eth_getUncleCountByBlockHash`
        `eth_getUncleCountByBlockNumber`
        """
        raise NotImplementedError("TODO")

    @apply_formatters_to_return(formatters.outputTransactionFormatter)
    def getTransaction(self, txn_hash):
        return self.request_manager.request_blocking(
            "eth_getTransactionByHash",
            [txn_hash],
        )

    @apply_formatters_to_return(formatters.outputTransactionFormatter)
    def getTransactionFromBlock(self, block_identifier, txn_index):
        """
        `eth_getTransactionByBlockHashAndIndex`
        `eth_getTransactionByBlockNumberAndIndex`
        """
        if encoding.is_integer(block_identifier):
            method = 'eth_getTransactionByBlockNumberAndIndex'
        else:
            method = 'eth_getTransactionByBlockHashAndIndex'
        return self.request_manager.request_blocking(
            method,
            [block_identifier, txn_index],
        )

    @apply_formatters_to_return(formatters.outputTransactionReceiptFormatter)
    def getTransactionReceipt(self, txn_hash):
        return self.request_manager.request_blocking(
            "eth_getTransactionReceipt",
            [txn_hash],
        )

    @apply_formatters_to_return(encoding.toDecimal)
    def getTransactionCount(self, account, block_number=None):
        if block_number is None:
            block_number = self.defaultBlock
        return self.request_manager.request_blocking(
            "eth_getTransactionCount",
            [account, block_number],
        )

    def sendTransaction(self, transaction):
        return self.request_manager.request_blocking(
            "eth_sendTransaction",
            [transaction],
        )

    def sendRawTransaction(self, raw_txn):
        return self.request_manager.request_blocking(
            "eth_sendRawTransaction",
            [raw_txn],
        )

    def sign(self, account, data):
        data_hash = self.request_manager.request_blocking("web3_sha3", [data])
        return self.request_manager.request_blocking("eth_sign", [account, data_hash])

    def call(self, transaction, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.request_manager.request_blocking("eth_call", [transaction, block_identifier])

    def estimateGas(self, *args, **kwargs):
        raise NotImplementedError("TODO")

    def filter(self, *args, **kwargs):
        """
        `eth_newFilter`
        `eth_newBlockFilter`
        `eth_uninstallFilter`
        """
        raise NotImplementedError("TODO")

    def contract(self, abi):
        return ContractFactory(self, abi)

    def getCompilers(self):
        return self.request_manager.request_blocking("eth_getCompilers", [])
