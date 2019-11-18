from typing import (
    Any,
    Dict,
    List,
    NoReturn,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    overload,
)

from eth_account import (
    Account,
)
from eth_typing import (
    Address,
    BlockNumber,
    ChecksumAddress,
    Hash32,
    HexStr,
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
from web3._utils.compat import (
    Literal,
)
from web3._utils.empty import (
    empty,
)
from web3._utils.encoding import (
    to_hex,
)
from web3._utils.filters import (
    BlockFilter,
    Filter,
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
    ConciseContract,
    Contract,
    ContractCaller,
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
from web3.types import (
    ENS,
    BlockData,
    BlockIdentifier,
    FilterParams,
    GasPriceStrategy,
    LogParams,
    MerkleProof,
    SyncStatus,
    TxParams,
    TxReceipt,
    Uncle,
    Wei,
)


class Eth(Module):
    account = Account()
    defaultAccount = empty
    defaultBlock: Literal["latest"] = "latest"  # noqa: E704
    defaultContractFactory: Type[Union[Contract, ConciseContract, ContractCaller]] = Contract  # noqa: E704,E501
    iban = Iban
    gasPriceStrategy = None

    def namereg(self) -> NoReturn:
        raise NotImplementedError()

    def icapNamereg(self) -> NoReturn:
        raise NotImplementedError()

    @property
    def protocolVersion(self) -> str:
        return self.web3.manager.request_blocking("eth_protocolVersion", [])

    @property
    def syncing(self) -> Union[SyncStatus, bool]:
        return self.web3.manager.request_blocking("eth_syncing", [])

    @property
    def coinbase(self) -> ChecksumAddress:
        return self.web3.manager.request_blocking("eth_coinbase", [])

    @property
    def mining(self) -> bool:
        return self.web3.manager.request_blocking("eth_mining", [])

    @property
    def hashrate(self) -> int:
        return self.web3.manager.request_blocking("eth_hashrate", [])

    @property
    def gasPrice(self) -> Wei:
        return self.web3.manager.request_blocking("eth_gasPrice", [])

    @property
    def accounts(self) -> Tuple[ChecksumAddress]:
        return self.web3.manager.request_blocking("eth_accounts", [])

    @property
    def blockNumber(self) -> BlockNumber:
        return self.web3.manager.request_blocking("eth_blockNumber", [])

    @property
    def chainId(self) -> int:
        return self.web3.manager.request_blocking("eth_chainId", [])

    def getBalance(
        self, account: Union[Address, ChecksumAddress, ENS], block_identifier: BlockIdentifier=None
    ) -> Wei:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_getBalance",
            [account, block_identifier],
        )

    def getStorageAt(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        position: int,
        block_identifier: BlockIdentifier=None
    ) -> bytes:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_getStorageAt",
            [account, position, block_identifier]
        )

    def getProof(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        positions: Sequence[int],
        block_identifier: BlockIdentifier=None
    ) -> MerkleProof:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_getProof",
            [account, positions, block_identifier]
        )

    def getCode(
        self, account: Union[Address, ChecksumAddress, ENS], block_identifier: BlockIdentifier=None
    ) -> HexStr:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_getCode",
            [account, block_identifier],
        )

    def getBlock(
        self, block_identifier: BlockIdentifier, full_transactions: bool=False
    ) -> BlockData:
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

        result = self.web3.manager.request_blocking(
            method,
            [block_identifier, full_transactions],
        )
        if result is None:
            raise BlockNotFound(f"Block with id: {block_identifier} not found.")
        return result

    def getBlockTransactionCount(self, block_identifier: BlockIdentifier) -> int:
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
        result = self.web3.manager.request_blocking(
            method,
            [block_identifier],
        )
        if result is None:
            raise BlockNotFound(f"Block with id: {block_identifier} not found.")
        return result

    def getUncleCount(self, block_identifier: BlockIdentifier) -> int:
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
        result = self.web3.manager.request_blocking(
            method,
            [block_identifier],
        )
        if result is None:
            raise BlockNotFound(f"Block with id: {block_identifier} not found.")
        return result

    def getUncleByBlock(self, block_identifier: BlockIdentifier, uncle_index: int) -> Uncle:
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
        result = self.web3.manager.request_blocking(
            method,
            [block_identifier, uncle_index],
        )
        if result is None:
            raise BlockNotFound(
                f"Uncle at index: {uncle_index} of block with id: {block_identifier} not found."
            )
        return result

    def getTransaction(self, transaction_hash: Hash32) -> TxReceipt:
        result = self.web3.manager.request_blocking(
            "eth_getTransactionByHash",
            [transaction_hash],
        )
        if result is None:
            raise TransactionNotFound(f"Transaction with hash: {transaction_hash} not found.")
        return result

    def getTransactionFromBlock(
        self, block_identifier: BlockIdentifier, transaction_index: int
    ) -> NoReturn:
        """
        Alias for the method getTransactionByBlock
        Deprecated to maintain naming consistency with the json-rpc API
        """
        raise DeprecationWarning("This method has been deprecated as of EIP 1474.")

    def getTransactionByBlock(
        self, block_identifier: BlockIdentifier, transaction_index: int
    ) -> TxReceipt:
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

    def waitForTransactionReceipt(
        self, transaction_hash: Hash32, timeout: int=120, poll_latency: float=0.1
    ) -> TxReceipt:
        try:
            return wait_for_transaction_receipt(self.web3, transaction_hash, timeout, poll_latency)
        except Timeout:
            raise TimeExhausted(
                "Transaction {} is not in the chain, after {} seconds".format(
                    to_hex(transaction_hash),
                    timeout,
                )
            )

    def getTransactionReceipt(self, transaction_hash: Hash32) -> TxReceipt:
        result = self.web3.manager.request_blocking(
            "eth_getTransactionReceipt",
            [transaction_hash],
        )
        if result is None:
            raise TransactionNotFound(f"Transaction with hash: {transaction_hash} not found.")
        return result

    def getTransactionCount(
        self, account: Union[Address, ChecksumAddress, ENS], block_identifier: BlockIdentifier=None
    ) -> int:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "eth_getTransactionCount",
            [account, block_identifier],
        )

    def replaceTransaction(self, transaction_hash: Hash32, new_transaction: TxParams) -> Hash32:
        current_transaction = get_required_transaction(self.web3, transaction_hash)
        return replace_transaction(self.web3, current_transaction, new_transaction)

    # todo: Update Any to stricter kwarg checking with TxParams
    # https://github.com/python/mypy/issues/4441
    def modifyTransaction(self, transaction_hash: Hash32, **transaction_params: Any) -> None:
        assert_valid_transaction_params(transaction_params)
        current_transaction = get_required_transaction(self.web3, transaction_hash)
        current_transaction_params = extract_valid_transaction_params(current_transaction)
        new_transaction = merge(current_transaction_params, transaction_params)
        return replace_transaction(self.web3, current_transaction, new_transaction)

    def sendTransaction(self, transaction: TxParams) -> Hash32:
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

    def sendRawTransaction(self, raw_transaction: HexStr) -> Hash32:
        return self.web3.manager.request_blocking(
            "eth_sendRawTransaction",
            [raw_transaction],
        )

    def sign(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        data: bytes=None,
        hexstr: HexStr=None,
        text: str=None
    ) -> HexStr:
        message_hex = to_hex(data, hexstr=hexstr, text=text)
        return self.web3.manager.request_blocking(
            "eth_sign", [account, message_hex],
        )

    def signTransaction(self, transaction: TxParams) -> bytes:
        return self.web3.manager.request_blocking(
            "eth_signTransaction", [transaction],
        )

    def signTypedData(
        self, account: Union[Address, ChecksumAddress, ENS], jsonMessage: Dict[Any, Any]
    ) -> HexStr:
        return self.web3.manager.request_blocking(
            "eth_signTypedData", [account, jsonMessage],
        )

    @apply_to_return_value(HexBytes)
    def call(self, transaction: TxParams, block_identifier: BlockIdentifier=None) -> Sequence[Any]:
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

    def estimateGas(self, transaction: TxParams, block_identifier: BlockIdentifier=None) -> int:
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        if block_identifier is None:
            params = [transaction]
        else:
            params = [transaction, block_identifier]

        return self.web3.manager.request_blocking(
            "eth_estimateGas",
            params,
        )

    def filter(self, filter_params: Union[str, FilterParams]=None, filter_id: int=None) -> Filter:
        if filter_id and filter_params:
            raise TypeError(
                "Ambiguous invocation: provide either a `filter_params` or a `filter_id` argument. "
                "Both were supplied."
            )
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

    def getFilterChanges(self, filter_id: int) -> List[LogParams]:
        return self.web3.manager.request_blocking(
            "eth_getFilterChanges", [filter_id],
        )

    def getFilterLogs(self, filter_id: int) -> List[LogParams]:
        return self.web3.manager.request_blocking(
            "eth_getFilterLogs", [filter_id],
        )

    def getLogs(self, filter_params: FilterParams) -> List[LogParams]:
        return self.web3.manager.request_blocking(
            "eth_getLogs", [filter_params],
        )

    def submitHashrate(self, hashrate: int, node_id: Hash32) -> bool:
        return self.web3.manager.request_blocking(
            "eth_submitHashrate", [hashrate, node_id],
        )

    def submitWork(self, nonce: int, pow_hash: Hash32, mix_digest: Hash32) -> bool:
        return self.web3.manager.request_blocking(
            "eth_submitWork", [nonce, pow_hash, mix_digest],
        )

    def uninstallFilter(self, filter_id: int) -> bool:
        return self.web3.manager.request_blocking(
            "eth_uninstallFilter", [filter_id],
        )

    @overload
    def contract(self, address: None=None, **kwargs: Any) -> Type[Contract]: ...  # noqa: E704,E501

    @overload  # noqa: F811
    def contract(self, address: Union[Address, ChecksumAddress, ENS], **kwargs: Any) -> Contract: ...  # noqa: E704,E501

    def contract(  # noqa: F811
        self, address: Union[Address, ChecksumAddress, ENS]=None, **kwargs: Any
    ) -> Union[Type[Contract], Contract]:
        ContractFactoryClass = kwargs.pop('ContractFactoryClass', self.defaultContractFactory)

        ContractFactory = ContractFactoryClass.factory(self.web3, **kwargs)

        if address:
            return ContractFactory(address)
        else:
            return ContractFactory

    def setContractFactory(
        self, contractFactory: Type[Union[Contract, ConciseContract, ContractCaller]]
    ) -> None:
        self.defaultContractFactory = contractFactory

    def getCompilers(self) -> NoReturn:
        raise DeprecationWarning("This method has been deprecated as of EIP 1474.")

    def getWork(self) -> List[Hash32]:
        return self.web3.manager.request_blocking("eth_getWork", [])

    def generateGasPrice(self, transaction_params: TxParams=None) -> Optional[Wei]:
        if self.gasPriceStrategy:
            return self.gasPriceStrategy(self.web3, transaction_params)
        return None

    def setGasPriceStrategy(self, gas_price_strategy: GasPriceStrategy) -> None:
        self.gasPriceStrategy = gas_price_strategy
