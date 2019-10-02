from eth_account import (
    Account,
)
from eth_utils import (
    apply_to_return_value,
    is_checksum_address,
    is_string,
)
from eth_utils.toolz import (
    assoc,
    merge,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.blocks import (
    select_method_for_block_identifier,
)
from web3._utils.empty import (
    empty,
)
from web3._utils.encoding import (
    to_hex,
)
from web3._utils.filters import (
    BlockFilter,
    LogFilter,
    TransactionFilter,
)
from web3._utils.threads import (
    Timeout,
)
from web3._utils.transactions import (
    assert_valid_transaction_params,
    extract_valid_transaction_params,
    get_buffered_gas_estimate,
    get_required_transaction,
    replace_transaction,
    wait_for_transaction_receipt,
)
from web3.contract import (
    Contract,
)
from web3.exceptions import (
    BlockNotFound,
    TimeExhausted,
    TransactionNotFound,
)
from web3.iban import (
    Iban,
)
from web3.module import (
    Module,
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
    def protocol_version(self):
        return self.web3.manager.request_blocking("eth_protocol_version", [])

    @property
    def protocolVersion(self):
        raise DeprecationWarning("This method has been deprecated")

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
    def hash_rate(self):
        return self.web3.manager.request_blocking("eth_hash_rate", [])

    @property
    def hashrate(self):
        raise DeprecationWarning("This method has been deprecated")

    @property
    def gas_price(self):
        return self.web3.manager.request_blocking("eth_gas_price", [])

    @property
    def gasPrice(self):
        raise DeprecationWarning("This method has been deprecated")

    @property
    def accounts(self):
        return self.web3.manager.request_blocking("eth_accounts", [])

    @property
    def block_number(self):
        return self.web3.manager.request_blocking("eth_block_number", [])

    @property
    def chainId(self):
        return self.web3.manager.request_blocking("eth_chainId", [])

    def get_balance(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_get_balance",
            [account, block_identifier],
        )

    def getBalance(self, account, block_identifier=None):
        raise DeprecationWarning("This method has been deprecated")

    def get_storage_at(self, account, position, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_get_storage_at",
            [account, position, block_identifier]
        )

    def getStorageAt(self, account, position, block_identifier=None):
        raise DeprecationWarning("This method has been deprecated")

    def get_proof(self, account, positions, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_get_proof",
            [account, positions, block_identifier]
        )

    def getProof(self, account, positions, block_identifier=None):
        raise DeprecationWarning("This method has been deprecated")

    def get_code(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_get_code",
            [account, block_identifier],
        )

    def getCode(self, account, block_identifier=None):
        raise DeprecationWarning("This method has been deprecated")

    def get_block(self, block_identifier, full_transactions=False):
        """
        `eth_get_block_by_hash`
        `eth_get_block_by_number`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_get_block_by_number',
            if_hash='eth_get_block_by_hash',
            if_number='eth_get_block_by_number',
        )

        result = self.web3.manager.request_blocking(
            method,
            [block_identifier, full_transactions],
        )
        if result is None:
            raise BlockNotFound(f"Block with id: {block_identifier} not found.")
        return result

    def get_block(self, block_identifier, full_transactions=False):
        raise DeprecationWarning("This method has been deprecated")

    def get_block_transaction_count(self, block_identifier):
        """
        `eth_get_block_transaction_count_by_hash`
        `eth_get_block_transaction_count_by_number`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_get_block_transaction_count_by_number',
            if_hash='eth_get_block_transaction_count_by_hash',
            if_number='eth_get_block_transaction_count_by_number',
        )
        result = self.web3.manager.request_blocking(
            method,
            [block_identifier],
        )
        if result is None:
            raise BlockNotFound(f"Block with id: {block_identifier} not found.")
        return result

    def getBlockTransactionCount(self, block_identifier):
        raise DeprecationWarning("This method has been deprecated")

    def get_uncle_count(self, block_identifier):
        """
        `eth_get_uncle_count_by_block_hash`
        `eth_get_uncle_count_by_block_number`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_get_uncle_count_by_block_number',
            if_hash='eth_get_uncle_count_by_block_hash',
            if_number='eth_get_uncle_count_by_block_number',
        )
        result = self.web3.manager.request_blocking(
            method,
            [block_identifier],
        )
        if result is None:
            raise BlockNotFound(f"Block with id: {block_identifier} not found.")
        return result

    def getUncleCount(self, block_identifier):
        raise DeprecationWarning("This method has been deprecated")

    def get_uncle_by_block(self, block_identifier, uncle_index):
        """
        `eth_get_uncle_by_block_hash_and_index`
        `eth_get_uncle_by_block_number_and_index`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_get_uncle_by_block_number_and_index',
            if_hash='eth_get_uncle_by_block_hash_and_index',
            if_number='eth_get_uncle_by_block_number_and_index',
        )
        result = self.web3.manager.request_blocking(
            method,
            [block_identifier, uncle_index],
        )
        if result is None:
            raise BlockNotFound(
                f"Uncle at index: {uncle_index} of block with id: {block_identifier} not found."
            )
        return result

    def getUncleByBlock(self, block_identifier, uncle_index):
        raise DeprecationWarning("This method has been deprecated")

    def get_transaction(self, transaction_hash):
        result = self.web3.manager.request_blocking(
            "eth_get_transaction_by_hash",
            [transaction_hash],
        )
        if result is None:
            raise TransactionNotFound(f"Transaction with hash: {transaction_hash} not found.")
        return result

    def get_transaction(self, transaction_hash):
        raise DeprecationWarning("This method has been deprecated")

    def get_transaction_from_block(self, block_identifier, transaction_index):
        """
        Alias for the method get_transaction_by_block
        Deprecated to maintain naming consistency with the json-rpc API
        """
        raise DeprecationWarning("This method has been deprecated as of EIP 1474.")

    def getTransactionFromBlock(self, block_identifier, transaction_index):
        """
        Alias for the method get_transaction_by_block
        Deprecated to maintain naming consistency with the json-rpc API
        """
        raise DeprecationWarning("This method has been deprecated as of EIP 1474.")

    def get_transaction_by_block(self, block_identifier, transaction_index):
        """
        `eth_get_transaction_by_block_hash_and_index`
        `eth_get_transaction_by_block_number_and_index`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_get_transaction_by_block_number_and_index',
            if_hash='eth_get_transaction_by_block_hash_and_index',
            if_number='eth_get_transaction_by_block_number_and_index',
        )
        result = self.web3.manager.request_blocking(
            method,
            [block_identifier, transaction_index],
        )
        if result is None:
            raise TransactionNotFound(
                f"Transaction index: {transaction_index} "
                f"on block id: {block_identifier} not found."
            )
        return result

    def getTransactionByBlock(self, block_identifier, transaction_index):
        raise DeprecationWarning("This method has been deprecated")

    def wait_for_transaction_receipt(self, transaction_hash, timeout=120):
        try:
            return wait_for_transaction_receipt(self.web3, transaction_hash, timeout)
        except Timeout:
            raise TimeExhausted(
                "Transaction {} is not in the chain, after {} seconds".format(
                    to_hex(transaction_hash),
                    timeout,
                )
            )

    def waitForTransactionReceipt(self, transaction_hash, timeout=120):
        raise DeprecationWarning("This method has been deprecated")

    def get_transaction_receipt(self, transaction_hash):
        result = self.web3.manager.request_blocking(
            "eth_get_transaction_receipt",
            [transaction_hash],
        )
        if result is None:
            raise TransactionNotFound(f"Transaction with hash: {transaction_hash} not found.")
        return result

    def getTransactionReceipt(self, transaction_hash):
        raise DeprecationWarning("This method has been deprecated")

    def get_transaction_count(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_get_transaction_count",
            [account, block_identifier],
        )

    def getTransactionCount(self, account, block_identifier=None):
        raise DeprecationWarning("This method has been deprecated")

    def replace_transaction(self, transaction_hash, new_transaction):
        current_transaction = get_required_transaction(self.web3, transaction_hash)
        return replace_transaction(self.web3, current_transaction, new_transaction)

    def replaceTransaction(self, transaction_hash, new_transaction):
        raise DeprecationWarning("This method has been deprecated")

    def modify_transaction(self, transaction_hash, **transaction_params):
        assert_valid_transaction_params(transaction_params)
        current_transaction = get_required_transaction(self.web3, transaction_hash)
        current_transaction_params = extract_valid_transaction_params(current_transaction)
        new_transaction = merge(current_transaction_params, transaction_params)
        return replace_transaction(self.web3, current_transaction, new_transaction)

    def modifyTransaction(self, transaction_hash, **transaction_params):
        raise DeprecationWarning("This method has been deprecated")

    def send_transaction(self, transaction):
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
            "eth_send_transaction",
            [transaction],
        )

    def sendTransaction(self, transaction):
        raise DeprecationWarning("This method has been deprecated")

    def send_raw_transaction(self, raw_transaction):
        return self.web3.manager.request_blocking(
            "eth_send_raw_transaction",
            [raw_transaction],
        )

    def sendRawTransaction(self, raw_transaction):
        raise DeprecationWarning("This method has been deprecated")

    def sign(self, account, data=None, hexstr=None, text=None):
        message_hex = to_hex(data, hexstr=hexstr, text=text)
        return self.web3.manager.request_blocking(
            "eth_sign", [account, message_hex],
        )

    def sign_transaction(self, transaction):
        return self.web3.manager.request_blocking(
            "eth_sign_transaction", [transaction],
        )

    def signTransaction(self, transaction):
        raise DeprecationWarning("This method has been deprecated")

    def sign_typed_data(self, account, jsonMessage):
        return self.web3.manager.request_blocking(
            "eth_sign_typed_data", [account, jsonMessage],
        )

    def signTypedData(self, account, jsonMessage):
        raise DeprecationWarning("This method has been deprecated")

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

    def estimate_gas(self, transaction, block_identifier=None):
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        if block_identifier is None:
            params = [transaction]
        else:
            params = [transaction, block_identifier]

        return self.web3.manager.request_blocking(
            "eth_estimate_gas",
            params,
        )

    def estimateGas(self, transaction, block_identifier=None):
        raise DeprecationWarning("This method has been deprecated")

    def filter(self, filter_params=None, filter_id=None):
        if filter_id and filter_params:
            raise TypeError(
                "Ambiguous invocation: provide either a `filter_params` or a `filter_id` argument. "
                "Both were supplied."
            )
        if is_string(filter_params):
            if filter_params == "latest":
                filter_id = self.web3.manager.request_blocking(
                    "eth_new_block_filter", [],
                )
                return BlockFilter(self.web3, filter_id)
            elif filter_params == "pending":
                filter_id = self.web3.manager.request_blocking(
                    "eth_new_pending_transaction_filter", [],
                )
                return TransactionFilter(self.web3, filter_id)
            else:
                raise ValueError(
                    "The filter API only accepts the values of `pending` or "
                    "`latest` for string based filters"
                )
        elif isinstance(filter_params, dict):
            _filter_id = self.web3.manager.request_blocking(
                "eth_newFilter",
                [filter_params],
            )
            return LogFilter(self.web3, _filter_id)
        elif filter_id and not filter_params:
            return LogFilter(self.web3, filter_id)
        else:
            raise TypeError("Must provide either filter_params as a string or "
                            "a valid filter object, or a filter_id as a string "
                            "or hex.")

    def get_filter_changes(self, filter_id):
        return self.web3.manager.request_blocking(
            "eth_get_filter_changes", [filter_id],
        )

    def getFilterChanges(self, filter_id):
        raise DeprecationWarning("This method has been deprecated")

    def get_filter_logs(self, filter_id):
        return self.web3.manager.request_blocking(
            "eth_get_filter_logs", [filter_id],
        )

    def getFilterLogs(self, filter_id):
        raise DeprecationWarning("This method has been deprecated")

    def get_logs(self, filter_params):
        return self.web3.manager.request_blocking(
            "eth_get_logs", [filter_params],
        )

    def getLogs(self, filter_params):
        raise DeprecationWarning("This method has been deprecated")

    def submit_hash_rate(self, hashrate, node_id):
        return self.web3.manager.request_blocking(
            "eth_submit_hash_rate", [hashrate, node_id],
        )

    def submitHashrate(self, hashrate, node_id):
        raise DeprecationWarning("This method has been deprecated")

    def submit_work(self, nonce, pow_hash, mix_digest):
        return self.web3.manager.request_blocking(
            "eth_submit_work", [nonce, pow_hash, mix_digest],
        )

    def submitWork(self, nonce, pow_hash, mix_digest):
        raise DeprecationWarning("This method has been deprecated")

    def uninstall_filter(self, filter_id):
        return self.web3.manager.request_blocking(
            "eth_uninstallFilter", [filter_id],
        )

    def uninstallFilter(self, filter_id):
        raise DeprecationWarning("This method has been deprecated")

    def contract(self,
                 address=None,
                 **kwargs):
        ContractFactoryClass = kwargs.pop('ContractFactoryClass', self.defaultContractFactory)

        ContractFactory = ContractFactoryClass.factory(self.web3, **kwargs)

        if address:
            return ContractFactory(address)
        else:
            return ContractFactory

    def set_contract_factory(self, contractFactory):
        self.defaultContractFactory = contractFactory

    def setContractFactory(self, contractFactory):
        raise DeprecationWarning("This method has been deprecated")

    def getCompilers(self):
        raise DeprecationWarning("This method has been deprecated as of EIP 1474.")

    def get_work(self):
        return self.web3.manager.request_blocking("eth_get_work", [])

    def getWork(self):
        raise DeprecationWarning("This method has been deprecated")

    def generate_gas_price(self, transaction_params=None):
        if self.gasPriceStrategy:
            return self.gasPriceStrategy(self.web3, transaction_params)

    def generateGasPrice(self, transaction_params=None):
        raise DeprecationWarning("This method has been deprecated")

    def set_gas_price_strategy(self, gas_price_strategy):
        self.gasPriceStrategy = gas_price_strategy

    def setGasPriceStrategy(self, gas_price_strategy):
        raise DeprecationWarning("This method has been deprecated")
