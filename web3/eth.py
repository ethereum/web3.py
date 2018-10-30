from eth_account import (
    Account,
)
from eth_utils import (
    is_checksum_address,
    is_string,
)
from hexbytes import (
    HexBytes,
)
from inspect import (
    iscoroutinefunction,
)

from web3._utils.async_tools import (
    sync,
)
from web3._utils.blocks import (
    select_method_for_block_identifier,
)
from web3._utils.decorators import (
    deprecated_for,
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
from web3._utils.toolz import (
    assoc,
    merge,
)
from web3._utils.transactions import (
    assert_valid_transaction_params,
    extract_valid_transaction_params,
    coro_get_buffered_gas_estimate,
    coro_get_required_transaction,
    coro_replace_transaction,
    coro_wait_for_transaction_receipt,
)
from web3.contract import (
    Contract,
)
from web3.exceptions import (
    TimeExhausted,
)
from web3.iban import (
    Iban,
)
from web3.module import (
    Module,
)


def is_coro(fn):
    if callable(fn) and fn.__name__.startswith('coro_'):
        return True
    return False


def _build_sync_methods(cls):
    coro_fns = tuple(filter(is_coro, cls.__dict__.values()))
    for coro in coro_fns:
        _add_sync_method(cls, coro)


def _add_sync_method(cls, coro):
    def method(*args, **kwargs):
        return sync(coro(*args, **kwargs))
    method.__doc__ = coro.__doc__
    method.__name__ = coro.__name__[len('coro_'):]
    if not cls.__dict__.get(method.__name__):
        setattr(cls, method.__name__, method)


class Eth(Module):
    account = Account()
    defaultAccount = empty
    defaultBlock = "latest"
    defaultContractFactory = Contract
    iban = Iban
    gasPriceStrategy = None

    @deprecated_for("doing nothing at all")
    def enable_unaudited_features(self):
        pass

    def namereg(self):
        raise NotImplementedError()

    def icapNamereg(self):
        raise NotImplementedError()

    async def coro_protocolVersion(self):
        return await self.web3.manager.request_async("eth_protocolVersion", [])

    async def coro_syncing(self):
        return await self.web3.manager.request_async("eth_syncing", [])

    async def coro_coinbase(self):
        return await self.web3.manager.request_async("eth_coinbase", [])

    async def coro_mining(self):
        return await self.web3.manager.request_async("eth_mining", [])

    async def coro_hashrate(self):
        return await self.web3.manager.request_async("eth_hashrate", [])

    async def coro_gasPrice(self):
        return await self.web3.manager.request_async("eth_gasPrice", [])

    async def coro_accounts(self):
        return await self.web3.manager.request_async("eth_accounts", [])

    async def coro_blockNumber(self):
        return await self.web3.manager.request_async("eth_blockNumber", [])

    async def coro_getBalance(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return await self.web3.manager.request_async(
            "eth_getBalance",
            [account, block_identifier],
        )

    async def coro_getStorageAt(self, account, position, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return await self.web3.manager.request_async(
            "eth_getStorageAt",
            [account, position, block_identifier]
        )

    async def coro_getCode(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return await self.web3.manager.request_async(
            "eth_getCode",
            [account, block_identifier],
        )

    async def coro_getBlock(self, block_identifier, full_transactions=False):
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

        return await self.web3.manager.request_async(
            method,
            [block_identifier, full_transactions],
        )

    async def coro_getBlockTransactionCount(self, block_identifier):
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
        return await self.web3.manager.request_async(
            method,
            [block_identifier],
        )

    async def coro_getUncleCount(self, block_identifier):
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
        return await self.web3.manager.request_async(
            method,
            [block_identifier],
        )

    async def coro_getUncleByBlock(self, block_identifier, uncle_index):
        """
        `eth_getUncleByBlockHashAndIndex`
        `eth_getUncleByBlockNumberAndIndex`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined='eth_getUncleByBlockNumberAndIndex',
            if_hash='eth_getUncleByBlockHashAndIndex',
            if_number='eth_getUncleByBlockNumberAndIndex',
        )
        return await self.web3.manager.request_async(
            method,
            [block_identifier, uncle_index],
        )

    async def coro_getTransaction(self, transaction_hash):
        return await self.web3.manager.request_async(
            "eth_getTransactionByHash",
            [transaction_hash],
        )

    @deprecated_for("w3.eth.getTransactionByBlock")
    async def coro_getTransactionFromBlock(self, block_identifier, transaction_index):
        """
        Alias for the method getTransactionByBlock
        Depreceated to maintain naming consistency with the json-rpc API
        """
        return await self.coro_getTransactionByBlock(block_identifier, transaction_index)

    async def coro_getTransactionByBlock(self, block_identifier, transaction_index):
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
        return await self.web3.manager.request_async(
            method,
            [block_identifier, transaction_index],
        )

    async def coro_waitForTransactionReceipt(self, transaction_hash, timeout=120):
        try:
            return await coro_wait_for_transaction_receipt(self.web3, transaction_hash, timeout)
        except Timeout:
            raise TimeExhausted(
                "Transaction {} is not in the chain, after {} seconds".format(
                    transaction_hash,
                    timeout,
                )
            )

    async def coro_getTransactionReceipt(self, transaction_hash):
        return await self.web3.manager.request_async(
            "eth_getTransactionReceipt",
            [transaction_hash],
        )

    async def coro_getTransactionCount(self, account, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return await self.web3.manager.request_async(
            "eth_getTransactionCount",
            [
                account,
                block_identifier,
            ],
        )

    async def coro_replaceTransaction(self, transaction_hash, new_transaction):
        current_transaction = await coro_get_required_transaction(self.web3, transaction_hash)
        return await coro_replace_transaction(self.web3, current_transaction, new_transaction)

    async def coro_modifyTransaction(self, transaction_hash, **transaction_params):
        assert_valid_transaction_params(transaction_params)
        current_transaction = await coro_get_required_transaction(self.web3, transaction_hash)
        current_transaction_params = extract_valid_transaction_params(current_transaction)
        new_transaction = merge(current_transaction_params, transaction_params)
        return await coro_replace_transaction(self.web3, current_transaction, new_transaction)

    async def coro_sendTransaction(self, transaction):
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        # TODO: move gas estimation in middleware
        if 'gas' not in transaction:
            transaction = assoc(
                transaction,
                'gas',
                await coro_get_buffered_gas_estimate(self.web3, transaction),
            )

        return await self.web3.manager.request_async(
            "eth_sendTransaction",
            [transaction],
        )

    async def coro_sendRawTransaction(self, raw_transaction):
        return await self.web3.manager.request_async(
            "eth_sendRawTransaction",
            [raw_transaction],
        )

    async def coro_sign(self, account, data=None, hexstr=None, text=None):
        message_hex = to_hex(data, hexstr=hexstr, text=text)
        return await self.web3.manager.request_async(
            "eth_sign", [account, message_hex],
        )

    async def coro_call(self, transaction, block_identifier=None):
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return HexBytes(await self.web3.manager.request_async(
            "eth_call",
            [transaction, block_identifier],
        ))

    async def coro_estimateGas(self, transaction, block_identifier=None):
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        if block_identifier is None:
            params = [transaction]
        else:
            params = [transaction, block_identifier]

        return await self.web3.manager.request_async(
            "eth_estimateGas",
            params,
        )

    async def coro_filter(self, filter_params=None, filter_id=None):
        if filter_id and filter_params:
            raise TypeError(
                "Ambiguous invocation: provide either a `filter_params` or a `filter_id` argument. "
                "Both were supplied."
            )
        if is_string(filter_params):
            if filter_params == "latest":
                filter_id = await self.web3.manager.request_async(
                    "eth_newBlockFilter", [],
                )
                return BlockFilter(self.web3, filter_id)
            elif filter_params == "pending":
                filter_id = await self.web3.manager.request_async(
                    "eth_newPendingTransactionFilter", [],
                )
                return TransactionFilter(self.web3, filter_id)
            else:
                raise ValueError(
                    "The filter API only accepts the values of `pending` or "
                    "`latest` for string based filters"
                )
        elif isinstance(filter_params, dict):
            _filter_id = await self.web3.manager.request_async(
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

    async def coro_getFilterChanges(self, filter_id):
        return await self.web3.manager.request_async(
            "eth_getFilterChanges", [filter_id],
        )

    async def coro_getFilterLogs(self, filter_id):
        return await self.web3.manager.request_async(
            "eth_getFilterLogs", [filter_id],
        )

    async def coro_getLogs(self, filter_params):
        return await self.web3.manager.request_async(
            "eth_getLogs", [filter_params],
        )

    async def coro_uninstallFilter(self, filter_id):
        return await self.web3.manager.request_async(
            "eth_uninstallFilter", [filter_id],
        )

    async def coro_contract(self, address=None, **kwargs):
        raise NotImplementedError()

    def contract(self,
                 address=None,
                 **kwargs):
        #  TODO: Async Contract
        ContractFactoryClass = kwargs.pop('ContractFactoryClass', self.defaultContractFactory)

        ContractFactory = ContractFactoryClass.factory(self.web3, **kwargs)

        if address:
            return ContractFactory(address)
        else:
            return ContractFactory

    def setContractFactory(self, contractFactory):
        self.defaultContractFactory = contractFactory

    async def coro_getCompilers(self):
        return await self.web3.manager.request_async("eth_getCompilers", [])

    async def coro_getWork(self):
        return await self.web3.manager.request_async("eth_getWork", [])

    async def coro_generateGasPrice(self, transaction_params=None):
        if self.gasPriceStrategy:
            return await self.gasPriceStrategy(self.web3, transaction_params)

    def setGasPriceStrategy(self, gas_price_strategy):
        self.gasPriceStrategy = gas_price_strategy


_build_sync_methods(Eth)
