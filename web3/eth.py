from web3 import formatters
from web3.iban import Iban

from web3.utils.encoding import (
    to_decimal,
    encode_hex,
)
from web3.utils.types import (
    is_integer,
    is_string,
)
from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.utils.filters import (
    BlockFilter,
    TransactionFilter,
    LogFilter,
)
from web3.contract import construct_contract_class


class Eth(object):
    def __init__(self, web3):
        self.web3 = web3
        self.request_manager = web3._requestManager

        self.iban = Iban
        # self.sendIBANTransaction = lambda: raise NotImplementedError()

    _defaultAccount = None

    @property
    def defaultAccount(self):
        if self._defaultAccount is not None:
            return self._defaultAccount
        return self.coinbase

    @defaultAccount.setter
    def defaultAccount(self, value):
        self._defaultAccount = value

    defaultBlock = "latest"

    def namereg(self):
        raise NotImplementedError()

    def icapNamereg(self):
        raise NotImplementedError()

    @property
    @apply_formatters_to_return(formatters.syncing_formatter)
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
    @apply_formatters_to_return(to_decimal)
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

    @apply_formatters_to_return(formatters.output_transaction_formatter)
    def getTransaction(self, txn_hash):
        return self.request_manager.request_blocking(
            "eth_getTransactionByHash",
            [txn_hash],
        )

    @apply_formatters_to_return(formatters.output_transaction_formatter)
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

    @apply_formatters_to_return(formatters.output_transaction_receipt_formatter)
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
        formatted_transaction = formatters.input_transaction_formatter(self, transaction)

        return self.request_manager.request_blocking(
            "eth_sendTransaction",
            [formatted_transaction],
        )

    def sendRawTransaction(self, raw_txn):
        return self.request_manager.request_blocking(
            "eth_sendRawTransaction",
            [raw_txn],
        )

    def sign(self, account, data):
        data_hash = self.request_manager.request_blocking("web3_sha3", [encode_hex(data)])
        return self.request_manager.request_blocking("eth_sign", [account, data_hash])

    def call(self, transaction, block_identifier=None):
        formatted_transaction = formatters.input_call_formatter(self, transaction)
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.request_manager.request_blocking(
            "eth_call",
            [formatted_transaction, block_identifier],
        )

    @apply_formatters_to_return(to_decimal)
    def estimateGas(self, transaction):
        return self.request_manager.request_blocking("eth_estimateGas", [transaction])

    def filter(self, filter_params):
        if is_string(filter_params):
            if filter_params == "latest":
                filter_id = self.request_manager.request_blocking("eth_newBlockFilter", [])
                return BlockFilter(self.web3, filter_id)
            elif filter_params == "pending":
                filter_id = self.request_manager.request_blocking(
                    "eth_newPendingTransactionFilter", [],
                )
                return TransactionFilter(self.web3, filter_id)
            else:
                raise ValueError(
                    "The filter API only accepts the values of `pending` or "
                    "`latest` for string based filters"
                )
        elif isinstance(filter_params, dict):
            filter_id = self.request_manager.request_blocking("eth_newFilter", [filter_params])
            return LogFilter(self.web3, filter_id)
        else:
            raise ValueError("Must provide either a string or a valid filter object")

    def getFilterChanges(self, filter_id):
        return self.request_manager.request_blocking("eth_getFilterChanges", [filter_id])

    def getFilterLogs(self, filter_id):
        return self.request_manager.request_blocking("eth_getFilterLogs", [filter_id])

    def uninstallFilter(self, filter_id):
        return self.request_manager.request_blocking("eth_uninstallFilter", [filter_id])

    def contract(self, abi, address=None, **kwargs):
        contract_class = construct_contract_class(self.web3, abi, **kwargs)

        if address is None:
            return contract_class
        else:
            return contract_class(address=address)

    def getCompilers(self):
        return self.request_manager.request_blocking("eth_getCompilers", [])
