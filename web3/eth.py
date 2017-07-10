from eth_utils import (
    is_address,
    is_integer,
    is_string,
    encode_hex,
    coerce_return_to_text,
)

from web3 import formatters
from web3.iban import Iban

from web3.contract import (
    Contract,
)

from web3.utils.blocks import (
    is_predefined_block_number,
)
from web3.utils.empty import (
    empty,
)
from web3.utils.encoding import (
    to_decimal,
)
from web3.utils.filters import (
    BlockFilter,
    TransactionFilter,
    LogFilter,
)
from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.utils.transactions import (
    get_buffered_gas_estimate,
)


class Eth(object):
    def __init__(self, web3):
        self.web3 = web3
        self.iban = Iban
        # self.sendIBANTransaction = lambda: raise NotImplementedError()

    defaultAccount = empty
    defaultBlock = "latest"

    def namereg(self):
        raise NotImplementedError()

    def icapNamereg(self):
        raise NotImplementedError()

    @property
    @apply_formatters_to_return(formatters.syncing_formatter)
    def syncing(self):
        return self.web3._requestManager.request_blocking("eth_syncing", [])

    def getSyncing(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    def isSyncing(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @coerce_return_to_text
    def coinbase(self):
        return self.web3._requestManager.request_blocking("eth_coinbase", [])

    @coerce_return_to_text
    def getCoinbase(self):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def mining(self):
        return self.web3._requestManager.request_blocking("eth_mining", [])

    def getMining(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(to_decimal)
    def hashrate(self):
        return self.web3._requestManager.request_blocking("eth_hashrate", [])

    def getHashrate(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(to_decimal)
    def gasPrice(self):
        return self.web3._requestManager.request_blocking("eth_gasPrice", [])

    def getGasPrice(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @coerce_return_to_text
    def accounts(self):
        return self.web3._requestManager.request_blocking("eth_accounts", [])

    def getAccounts(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(to_decimal)
    def blockNumber(self):
        return self.web3._requestManager.request_blocking("eth_blockNumber", [])

    def getBlockNumber(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @apply_formatters_to_return(to_decimal)
    def getBalance(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3._requestManager.request_blocking(
            "eth_getBalance",
            [
                account,
                formatters.input_block_identifier_formatter(block_identifier),
            ],
        )

    def getStorageAt(self, account, position, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3._requestManager.request_blocking(
            "eth_getStorageAt",
            [
                account,
                self.web3.toHex(position),
                formatters.input_block_identifier_formatter(block_identifier),
            ],
        )

    @coerce_return_to_text
    def getCode(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3._requestManager.request_blocking(
            "eth_getCode",
            [
                account,
                formatters.input_block_identifier_formatter(block_identifier),
            ],
        )

    @apply_formatters_to_return(formatters.output_block_formatter)
    def getBlock(self, block_identifier, full_transactions=False):
        """
        `eth_getBlockByHash`
        `eth_getBlockByNumber`
        """
        if is_predefined_block_number(block_identifier) or is_integer(block_identifier):
            method = 'eth_getBlockByNumber'
        else:
            method = 'eth_getBlockByHash'

        return self.web3._requestManager.request_blocking(
            method,
            [
                formatters.input_block_identifier_formatter(block_identifier),
                full_transactions,
            ],
        )

    @apply_formatters_to_return(to_decimal)
    def getBlockTransactionCount(self, block_identifier):
        """
        `eth_getBlockTransactionCountByHash`
        `eth_getBlockTransactionCountByNumber`
        """
        if is_predefined_block_number(block_identifier) or is_integer(block_identifier):
            method = 'eth_getBlockTransactionCountByNumber'
        else:
            method = 'eth_getBlockTransactionCountByHash'
        return self.web3._requestManager.request_blocking(
            method,
            [formatters.input_block_identifier_formatter(block_identifier)],
        )

    def getUncle(self, block_identifier):
        """
        `eth_getUncleCountByBlockHash`
        `eth_getUncleCountByBlockNumber`
        """
        raise NotImplementedError("TODO")

    @apply_formatters_to_return(formatters.output_transaction_formatter)
    def getTransaction(self, transaction_hash):
        return self.web3._requestManager.request_blocking(
            "eth_getTransactionByHash",
            [transaction_hash],
        )

    @apply_formatters_to_return(formatters.output_transaction_formatter)
    def getTransactionFromBlock(self, block_identifier, transaction_index):
        """
        `eth_getTransactionByBlockHashAndIndex`
        `eth_getTransactionByBlockNumberAndIndex`
        """
        if is_predefined_block_number(block_identifier) or is_integer(block_identifier):
            method = 'eth_getTransactionByBlockNumberAndIndex'
        else:
            method = 'eth_getTransactionByBlockHashAndIndex'
        return self.web3._requestManager.request_blocking(
            method,
            [
                formatters.input_block_identifier_formatter(block_identifier),
                transaction_index,
            ],
        )

    @apply_formatters_to_return(formatters.output_transaction_receipt_formatter)
    def getTransactionReceipt(self, transaction_hash):
        return self.web3._requestManager.request_blocking(
            "eth_getTransactionReceipt",
            [transaction_hash],
        )

    @apply_formatters_to_return(to_decimal)
    def getTransactionCount(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3._requestManager.request_blocking(
            "eth_getTransactionCount",
            [
                account,
                formatters.input_block_identifier_formatter(block_identifier),
            ],
        )

    @coerce_return_to_text
    def sendTransaction(self, transaction):
        formatted_transaction = formatters.input_transaction_formatter(self, transaction)
        if 'gas' not in formatted_transaction and 'data' in formatted_transaction:
            formatted_transaction['gas'] = get_buffered_gas_estimate(
                self.web3,
                transaction=formatted_transaction,
            )
        elif 'gas' not in formatted_transaction:
            formatted_transaction['gas'] = 90000

        return self.web3._requestManager.request_blocking(
            "eth_sendTransaction",
            [formatters.input_transaction_formatter(self, formatted_transaction)],
        )

    @coerce_return_to_text
    def sendRawTransaction(self, raw_transaction):
        return self.web3._requestManager.request_blocking(
            "eth_sendRawTransaction",
            [raw_transaction],
        )

    @coerce_return_to_text
    def sign(self, account, data):
        return self.web3._requestManager.request_blocking(
            "eth_sign", [account, encode_hex(data)],
        )

    def call(self, transaction, block_identifier=None):
        formatted_transaction = formatters.input_transaction_formatter(self, transaction)
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3._requestManager.request_blocking(
            "eth_call",
            [
                formatted_transaction,
                formatters.input_block_identifier_formatter(block_identifier),
            ],
        )

    @apply_formatters_to_return(to_decimal)
    def estimateGas(self, transaction):
        formatted_transaction = formatters.input_transaction_formatter(self, transaction)
        return self.web3._requestManager.request_blocking(
            "eth_estimateGas",
            [formatted_transaction],
        )

    def filter(self, filter_params):
        if is_string(filter_params):
            if filter_params == "latest":
                filter_id = self.web3._requestManager.request_blocking(
                    "eth_newBlockFilter", [],
                )
                return BlockFilter(self.web3, filter_id)
            elif filter_params == "pending":
                filter_id = self.web3._requestManager.request_blocking(
                    "eth_newPendingTransactionFilter", [],
                )
                return TransactionFilter(self.web3, filter_id)
            else:
                raise ValueError(
                    "The filter API only accepts the values of `pending` or "
                    "`latest` for string based filters"
                )
        elif isinstance(filter_params, dict):
            formatted_filter_params = formatters.input_filter_params_formatter(filter_params)
            filter_id = self.web3._requestManager.request_blocking(
                "eth_newFilter",
                [formatted_filter_params],
            )
            return LogFilter(self.web3, filter_id)
        else:
            raise ValueError("Must provide either a string or a valid filter object")

    @apply_formatters_to_return(formatters.log_array_formatter)
    def getFilterChanges(self, filter_id):
        return self.web3._requestManager.request_blocking(
            "eth_getFilterChanges", [filter_id],
        )

    @apply_formatters_to_return(formatters.log_array_formatter)
    def getFilterLogs(self, filter_id):
        return self.web3._requestManager.request_blocking(
            "eth_getFilterLogs", [filter_id],
        )

    def uninstallFilter(self, filter_id):
        return self.web3._requestManager.request_blocking(
            "eth_uninstallFilter", [filter_id],
        )

    def contract(self,
                 *args,
                 **kwargs):
        ContractFactoryClass = kwargs.pop('ContractFactoryClass', Contract)
        contract_name = kwargs.pop('contract_name', None)

        has_address = any((
            'address' in kwargs,
            len(args) >= 1 and is_address(args[0]),
            len(args) >= 2 and is_address(args[1]),
        ))

        if has_address:
            if 'address' in kwargs:
                address = kwargs.pop('address')
            elif is_address(args[0]):
                address = args[0]
            elif is_address(args[1]):
                address = args[1]
                kwargs['abi'] = args[0]

            return ContractFactoryClass.factory(self.web3, contract_name, **kwargs)(address)
        else:
            try:
                kwargs['abi'] = args[0]
            except IndexError:
                pass
            return ContractFactoryClass.factory(self.web3, contract_name, **kwargs)

    def getCompilers(self):
        return self.web3._requestManager.request_blocking("eth_getCompilers", [])

    def getWork(self):
        return self.web3._requestManager.request_blocking("eth_getWork", [])
