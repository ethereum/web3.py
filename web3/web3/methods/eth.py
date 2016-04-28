from web3.web3.method import Method
from web3.web3.property import Property
import web3.web3.formatters as formatters
import web3.utils.config as config
import web3.utils.encoding as encoding
import web3.utils.utils as utils
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


class DefaultAccount:

    def __set__(self, v):
        config.defaultAccount = self.value

    def __get__(self):
        return config.defaultAccount


class Eth(object):

    def __init__(self, web3):
        self._requestManager = web3._requestManager

        self.defaultBlock = config.defaultBlock
        self.defaultAccount = DefaultAccount()  # config.defaultAccount

        self.iban = Iban
        # self.sendIBANTransaction = lambda: raise NotImplementedError()

        for method in methods:
            method = Method(method)
            method.attachToObject(self)
            method.setRequestManager(web3._requestManager)

        for prop in properties:
            prop = Property(prop)
            prop.attachToObject(self)
            prop.setRequestManager(web3._requestManager)

    def contract(self, abi):
        return ContractFactory(self, abi)

    def namereg(self):
        raise NotImplementedError()

    def icapNamereg(self):
        raise NotImplementedError()

    def isSyncing(self):
        raise NotImplementedError()
