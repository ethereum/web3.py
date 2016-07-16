from web3 import formatters
from web3.iban import Iban

import web3.utils.config as config

from web3.utils.encoding import (
    to_decimal,
)
from web3.utils.types import (
    is_integer,
)
from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.contract import construct_contract_class


class DefaultAccount(object):
    def __set__(self, v):
        config.defaultAccount = self.value

    def __get__(self):
        return config.defaultAccount


class Eth(object):
    def __init__(self, web3):
        self.web3 = web3
        self.request_manager = web3._requestManager

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
    @apply_formatters_to_return(to_decimal)
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
    @apply_formatters_to_return(to_decimal)
    def blockNumber(self):
        return self.request_manager.request_blocking("eth_blockNumber", [])

    def getBlockNumber(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @apply_formatters_to_return(to_decimal)
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
        if is_integer(block_identifier):
            method = 'eth_getBlockByNumber'
        else:
            method = 'eth_getBlockByHash'

        return self.request_manager.request_blocking(
            method,
            [block_identifier, full_txns],
        )

    @apply_formatters_to_return(to_decimal)
    def getBlockTransactionCount(self, block_identifier):
        """
        `eth_getBlockTransactionCountByHash`
        `eth_getBlockTransactionCountByNumber`
        """
        if is_integer(block_identifier):
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
        if is_integer(block_identifier):
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

    @apply_formatters_to_return(to_decimal)
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

    @apply_formatters_to_return(to_decimal)
    def estimateGas(self, transaction):
        return self.request_manager.request_blocking("eth_estimateGas", [transaction])

    def filter(self, *args, **kwargs):
        """
        `eth_newFilter`
        `eth_newBlockFilter`
        `eth_uninstallFilter`
        """
        raise NotImplementedError("TODO")

    def contract(self, abi, address=None, **kwargs):
        contract_class = construct_contract_class(self.web3, abi, **kwargs)

        if address is None:
            return contract_class
        else:
            return contract_class(address=address)

    def getCompilers(self):
        return self.request_manager.request_blocking("eth_getCompilers", [])
