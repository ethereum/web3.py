from cytoolz.dicttoolz import (
    assoc,
)
from eth_account import (
    Account,
)
from eth_utils import (
    apply_to_return_value,
    is_checksum_address,
    is_string,
)
from hexbytes import (
    HexBytes,
)

from web3.contract import (
    Contract,
)
from web3.iban import (
    Iban,
)
from web3.module import (
    Module,
)
from web3.utils.blocks import (
    select_method_for_block_identifier,
)
from web3.utils.empty import (
    empty,
)
from web3.utils.encoding import (
    to_hex,
)
from web3.utils.filters import (
    BlockFilter,
    LogFilter,
    TransactionFilter,
)
from web3.utils.transactions import (
    get_buffered_gas_estimate,
)


class Eth(Module):
    account = Account()
    defaultAccount = empty
    defaultBlock = "latest"
    defaultContractFactory = Contract
    iban = Iban
    gasPriceStrategy = None

    def namereg(self):
        raise NotImplementedError()

    def icapNamereg(self):
        raise NotImplementedError()

    @property
    def protocolVersion(self):
        return self.web3.manager.request_blocking("eth_protocolVersion", [])

    @property
    def syncing(self):
        return self.web3.manager.request_blocking("eth_syncing", [])

    @property
    def coinbase(self):
        return self.web3.manager.request_blocking("eth_coinbase", [])

    @property
    def mining(self):
        return self.web3.manager.request_blocking("eth_mining", [])

    @property
    def hashrate(self):
        return self.web3.manager.request_blocking("eth_hashrate", [])

    @property
    def gasPrice(self):
        return self.web3.manager.request_blocking("eth_gasPrice", [])

    @property
    def accounts(self):
        return self.web3.manager.request_blocking("eth_accounts", [])

    @property
    def blockNumber(self):
        return self.web3.manager.request_blocking("eth_blockNumber", [])

    def getBalance(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_getBalance",
            [account, block_identifier],
        )

    def getStorageAt(self, account, position, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_getStorageAt",
            [account, position, block_identifier]
        )

    def getCode(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_getCode",
            [account, block_identifier],
        )

    def getBlock(self, block_identifier, full_transactions=False):
        """
        `eth_getBlockByHash`
        `eth_getBlockByNumber`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_getBlockByNumber',
            if_hash='eth_getBlockByHash',
            if_number='eth_getBlockByNumber',
        )

        return self.web3.manager.request_blocking(
            method,
            [block_identifier, full_transactions],
        )

    def getBlockTransactionCount(self, block_identifier):
        """
        `eth_getBlockTransactionCountByHash`
        `eth_getBlockTransactionCountByNumber`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_getBlockTransactionCountByNumber',
            if_hash='eth_getBlockTransactionCountByHash',
            if_number='eth_getBlockTransactionCountByNumber',
        )
        return self.web3.manager.request_blocking(
            method,
            [block_identifier],
        )

    def getUncleCount(self, block_identifier):
        """
        `eth_getUncleCountByBlockHash`
        `eth_getUncleCountByBlockNumber`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_getUncleCountByBlockNumber',
            if_hash='eth_getUncleCountByBlockHash',
            if_number='eth_getUncleCountByBlockNumber',
        )
        return self.web3.manager.request_blocking(
            method,
            [block_identifier],
        )

    def getTransaction(self, transaction_hash):
        return self.web3.manager.request_blocking(
            "eth_getTransactionByHash",
            [transaction_hash],
        )

    def getTransactionFromBlock(self, block_identifier, transaction_index):
        """
        `eth_getTransactionByBlockHashAndIndex`
        `eth_getTransactionByBlockNumberAndIndex`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_getTransactionByBlockNumberAndIndex',
            if_hash='eth_getTransactionByBlockHashAndIndex',
            if_number='eth_getTransactionByBlockNumberAndIndex',
        )
        return self.web3.manager.request_blocking(
            method,
            [block_identifier, transaction_index],
        )

    def getTransactionReceipt(self, transaction_hash):
        return self.web3.manager.request_blocking(
            "eth_getTransactionReceipt",
            [transaction_hash],
        )

    def getTransactionCount(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_getTransactionCount",
            [
                account,
                block_identifier,
            ],
        )

    def sendTransaction(self, transaction):
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        # TODO: move gas estimation in middleware
        if 'gas' not in transaction:
            transaction = assoc(
                transaction,
                'gas',
                get_buffered_gas_estimate(self.web3, transaction),
            )

        return self.web3.manager.request_blocking(
            "eth_sendTransaction",
            [transaction],
        )

    def sendRawTransaction(self, raw_transaction):
        return self.web3.manager.request_blocking(
            "eth_sendRawTransaction",
            [raw_transaction],
        )

    def sign(self, account, data=None, hexstr=None, text=None):
        message_hex = to_hex(data, hexstr=hexstr, text=text)
        return self.web3.manager.request_blocking(
            "eth_sign", [account, message_hex],
        )

    @apply_to_return_value(HexBytes)
    def call(self, transaction, block_identifier=None):
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.defaultBlock

        return self.web3.manager.request_blocking(
            "eth_call",
            [transaction, block_identifier],
        )

    def estimateGas(self, transaction):
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        return self.web3.manager.request_blocking(
            "eth_estimateGas",
            [transaction],
        )

    def filter(self, filter_params):
        if is_string(filter_params):
            if filter_params == "latest":
                filter_id = self.web3.manager.request_blocking(
                    "eth_newBlockFilter", [],
                )
                return BlockFilter(self.web3, filter_id)
            elif filter_params == "pending":
                filter_id = self.web3.manager.request_blocking(
                    "eth_newPendingTransactionFilter", [],
                )
                return TransactionFilter(self.web3, filter_id)
            else:
                raise ValueError(
                    "The filter API only accepts the values of `pending` or "
                    "`latest` for string based filters"
                )
        elif isinstance(filter_params, dict):
            filter_id = self.web3.manager.request_blocking(
                "eth_newFilter",
                [filter_params],
            )
            return LogFilter(self.web3, filter_id)
        else:
            raise ValueError("Must provide either a string or a valid filter object")

    def getFilterChanges(self, filter_id):
        return self.web3.manager.request_blocking(
            "eth_getFilterChanges", [filter_id],
        )

    def getFilterLogs(self, filter_id):
        return self.web3.manager.request_blocking(
            "eth_getFilterLogs", [filter_id],
        )

    def getLogs(self, filter_params):
        return self.web3.manager.request_blocking(
            "eth_getLogs", [filter_params],
        )

    def uninstallFilter(self, filter_id):
        return self.web3.manager.request_blocking(
            "eth_uninstallFilter", [filter_id],
        )

    def contract(self,
                 address=None,
                 **kwargs):
        ContractFactoryClass = kwargs.pop('ContractFactoryClass', self.defaultContractFactory)

        ContractFactory = ContractFactoryClass.factory(self.web3, **kwargs)

        if address:
            return ContractFactory(address)
        else:
            return ContractFactory

    def setContractFactory(self, contractFactory):
        self.defaultContractFactory = contractFactory

    def getCompilers(self):
        return self.web3.manager.request_blocking("eth_getCompilers", [])

    def getWork(self):
        return self.web3.manager.request_blocking("eth_getWork", [])

    def generateGasPrice(self, transaction_params=None):
        if self.gasPriceStrategy:
            return self.gasPriceStrategy(self.web3, transaction_params)

    def setGasPriceStrategy(self, gas_price_strategy):
        self.gasPriceStrategy = gas_price_strategy
