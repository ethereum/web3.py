from typing import (
    Any,
    Callable,
    List,
    NoReturn,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
    overload,
)

from eth_account import (
    Account,
)
from eth_typing import (
    Address,
    BlockNumber,
    ChecksumAddress,
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
from web3._utils.rpc_abi import (
    RPC,
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
from web3.method import (
    Method,
    default_root_munger,
)
from web3.module import (
    Module,
    ModuleV2,
)
from web3.types import (
    ENS,
    BlockData,
    BlockIdentifier,
    FilterParams,
    GasPriceStrategy,
    LogReceipt,
    MerkleProof,
    Nonce,
    SignedTx,
    SyncStatus,
    TxData,
    TxParams,
    TxReceipt,
    Uncle,
    Wei,
    _Hash32,
)


class Eth(ModuleV2, Module):
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

    protocol_version: Method[Callable[[], str]] = Method(
        RPC.eth_protocolVersion,
        mungers=None,
    )

    @property
    def protocolVersion(self) -> str:
        return self.protocol_version()

    is_syncing: Method[Callable[[], Union[SyncStatus, bool]]] = Method(
        RPC.eth_syncing,
        mungers=None,
    )

    @property
    def syncing(self) -> Union[SyncStatus, bool]:
        return self.is_syncing()

    get_coinbase: Method[Callable[[], ChecksumAddress]] = Method(
        RPC.eth_coinbase,
        mungers=None,
    )

    @property
    def coinbase(self) -> ChecksumAddress:
        return self.get_coinbase()

    is_mining: Method[Callable[[], bool]] = Method(
        RPC.eth_mining,
        mungers=None,
    )

    @property
    def mining(self) -> bool:
        return self.is_mining()

    get_hashrate: Method[Callable[[], int]] = Method(
        RPC.eth_hashrate,
        mungers=None,
    )

    @property
    def hashrate(self) -> int:
        return self.get_hashrate()

    gas_price: Method[Callable[[], Wei]] = Method(
        RPC.eth_gasPrice,
        mungers=None,
    )

    @property
    def gasPrice(self) -> Wei:
        return self.gas_price()

    get_accounts: Method[Callable[[], Tuple[ChecksumAddress]]] = Method(
        RPC.eth_accounts,
        mungers=None,
    )

    @property
    def accounts(self) -> Tuple[ChecksumAddress]:
        return self.get_accounts()

    block_number: Method[Callable[[], BlockNumber]] = Method(
        RPC.eth_blockNumber,
        mungers=None,
    )

    @property
    def blockNumber(self) -> BlockNumber:
        return self.block_number()

    chain_id: Method[Callable[[], int]] = Method(
        RPC.eth_chainId,
        mungers=None,
    )

    @property
    def chainId(self) -> int:
        return self.web3.manager.request_blocking(RPC.eth_chainId, [])

    def getBalance(
        self, account: Union[Address, ChecksumAddress, ENS],
        block_identifier: Optional[BlockIdentifier] = None
    ) -> Wei:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            RPC.eth_getBalance,
            [account, block_identifier],
        )

    def block_identifier_munger(
        self,
        *args: Any,
        block_identifier: BlockIdentifier=None
    ) -> List[Any]:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return [*args, block_identifier]

    getStorageAt: Method[
        Callable[..., HexBytes]
    ] = Method(
        RPC.eth_getStorageAt,
        mungers=[block_identifier_munger],
    )

    getProof: Method[
        Callable[
            [Tuple[ChecksumAddress, Sequence[int], Optional[BlockIdentifier]]],
            MerkleProof
        ]
    ] = Method(
        RPC.eth_getProof,
        mungers=[block_identifier_munger],
    )

    def getCode(
        self, account: Union[Address, ChecksumAddress, ENS],
        block_identifier: Optional[BlockIdentifier] = None
    ) -> HexBytes:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            RPC.eth_getCode,
            [account, block_identifier],
        )

    def getBlock(
        self, block_identifier: BlockIdentifier, full_transactions: bool = False
    ) -> BlockData:
        """
        `eth_getBlockByHash`
        `eth_getBlockByNumber`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined=RPC.eth_getBlockByNumber,
            if_hash=RPC.eth_getBlockByHash,
            if_number=RPC.eth_getBlockByNumber,
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
            if_predefined=RPC.eth_getBlockTransactionCountByNumber,
            if_hash=RPC.eth_getBlockTransactionCountByHash,
            if_number=RPC.eth_getBlockTransactionCountByNumber,
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
            if_predefined=RPC.eth_getUncleCountByBlockNumber,
            if_hash=RPC.eth_getUncleCountByBlockHash,
            if_number=RPC.eth_getUncleCountByBlockNumber,
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
            if_predefined=RPC.eth_getUncleByBlockNumberAndIndex,
            if_hash=RPC.eth_getUncleByBlockHashAndIndex,
            if_number=RPC.eth_getUncleByBlockNumberAndIndex,
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

    def getTransaction(self, transaction_hash: _Hash32) -> TxData:
        result = self.web3.manager.request_blocking(
            RPC.eth_getTransactionByHash,
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
    ) -> TxData:
        """
        `eth_getTransactionByBlockHashAndIndex`
        `eth_getTransactionByBlockNumberAndIndex`
        """
        method = select_method_for_block_identifier(
            block_identifier,
            if_predefined=RPC.eth_getTransactionByBlockNumberAndIndex,
            if_hash=RPC.eth_getTransactionByBlockHashAndIndex,
            if_number=RPC.eth_getTransactionByBlockNumberAndIndex,
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
        self, transaction_hash: _Hash32, timeout: int=120, poll_latency: float=0.1
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

    def getTransactionReceipt(self, transaction_hash: _Hash32) -> TxReceipt:
        result = self.web3.manager.request_blocking(
            RPC.eth_getTransactionReceipt,
            [transaction_hash],
        )
        if result is None:
            raise TransactionNotFound(f"Transaction with hash: {transaction_hash} not found.")
        return result

    getTransactionCount: Method[Callable[..., Nonce]] = Method(
        RPC.eth_getTransactionCount,
        mungers=[block_identifier_munger],
    )

    def replaceTransaction(self, transaction_hash: _Hash32, new_transaction: TxParams) -> HexBytes:
        current_transaction = get_required_transaction(self.web3, transaction_hash)
        return replace_transaction(self.web3, current_transaction, new_transaction)

    # todo: Update Any to stricter kwarg checking with TxParams
    # https://github.com/python/mypy/issues/4441
    def modifyTransaction(
        self, transaction_hash: _Hash32, **transaction_params: Any
    ) -> HexBytes:
        assert_valid_transaction_params(cast(TxParams, transaction_params))
        current_transaction = get_required_transaction(self.web3, transaction_hash)
        current_transaction_params = extract_valid_transaction_params(current_transaction)
        new_transaction = merge(current_transaction_params, transaction_params)
        return replace_transaction(self.web3, current_transaction, new_transaction)

    def sendTransaction(self, transaction: TxParams) -> HexBytes:
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
            RPC.eth_sendTransaction,
            [transaction],
        )

    sendRawTransaction: Method[Callable[[Union[HexStr, bytes]], HexBytes]] = Method(
        RPC.eth_sendRawTransaction,
        mungers=[default_root_munger],
    )

    def sign_munger(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        data: Union[int, bytes]=None,
        hexstr: HexStr=None,
        text: str=None
    ) -> Tuple[Union[Address, ChecksumAddress, ENS], HexStr]:
        message_hex = to_hex(data, hexstr=hexstr, text=text)
        return (account, message_hex)

    sign: Method[Callable[..., HexStr]] = Method(
        RPC.eth_sign,
        mungers=[sign_munger],
    )

    signTransaction: Method[Callable[[TxParams], SignedTx]] = Method(
        RPC.eth_signTransaction,
        mungers=[default_root_munger],
    )

    signTypedData: Method[Callable[..., HexStr]] = Method(
        RPC.eth_signTypedData,
        mungers=[default_root_munger],
    )

    @apply_to_return_value(HexBytes)
    def call(self, transaction: TxParams,
             block_identifier: Optional[BlockIdentifier] = None) -> Sequence[Any]:
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            RPC.eth_call,
            [transaction, block_identifier],
        )

    def estimateGas(self, transaction: TxParams,
                    block_identifier: Optional[BlockIdentifier] = None) -> Wei:
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        if block_identifier is None:
            params: Sequence[Union[TxParams, BlockIdentifier]] = [transaction]
        else:
            params = [transaction, block_identifier]

        return self.web3.manager.request_blocking(
            RPC.eth_estimateGas,
            params,
        )

    def filter(
        self, filter_params: Optional[Union[str, FilterParams]] = None,
        filter_id: Optional[HexStr] = None
    ) -> Filter:
        if filter_id and filter_params:
            raise TypeError(
                "Ambiguous invocation: provide either a `filter_params` or a `filter_id` argument. "
                "Both were supplied."
            )
        if is_string(filter_params):
            if filter_params == "latest":
                filter_id = self.web3.manager.request_blocking(
                    RPC.eth_newBlockFilter, [],
                )
                return BlockFilter(self.web3, filter_id)
            elif filter_params == "pending":
                filter_id = self.web3.manager.request_blocking(
                    RPC.eth_newPendingTransactionFilter, [],
                )
                return TransactionFilter(self.web3, filter_id)
            else:
                raise ValueError(
                    "The filter API only accepts the values of `pending` or "
                    "`latest` for string based filters"
                )
        elif isinstance(filter_params, dict):
            _filter_id = self.web3.manager.request_blocking(
                RPC.eth_newFilter,
                [filter_params],
            )
            return LogFilter(self.web3, _filter_id)
        elif filter_id and not filter_params:
            return LogFilter(self.web3, filter_id)
        else:
            raise TypeError("Must provide either filter_params as a string or "
                            "a valid filter object, or a filter_id as a string "
                            "or hex.")

    def getFilterChanges(self, filter_id: HexStr) -> List[LogReceipt]:
        return self.web3.manager.request_blocking(
            RPC.eth_getFilterChanges, [filter_id],
        )

    def getFilterLogs(self, filter_id: HexStr) -> List[LogReceipt]:
        return self.web3.manager.request_blocking(
            RPC.eth_getFilterLogs, [filter_id],
        )

    def getLogs(self, filter_params: FilterParams) -> List[LogReceipt]:
        return self.web3.manager.request_blocking(
            RPC.eth_getLogs, [filter_params],
        )

    submitHashrate: Method[Callable[[int, _Hash32], bool]] = Method(
        RPC.eth_submitHashrate,
        mungers=[default_root_munger],
    )

    submitWork: Method[Callable[[int, _Hash32, _Hash32], bool]] = Method(
        RPC.eth_submitWork,
        mungers=[default_root_munger],
    )

    uninstallFilter: Method[Callable[[HexStr], bool]] = Method(
        RPC.eth_uninstallFilter,
        mungers=[default_root_munger],
    )

    @overload
    def contract(self, address: None = None, **kwargs: Any) -> Type[Contract]: ...  # noqa: E704,E501

    @overload  # noqa: F811
    def contract(self, address: Union[Address, ChecksumAddress, ENS], **kwargs: Any) -> Contract: ...  # noqa: E704,E501

    def contract(  # noqa: F811
        self, address: Optional[Union[Address, ChecksumAddress, ENS]] = None, **kwargs: Any
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

    getWork: Method[Callable[[], List[HexBytes]]] = Method(
        RPC.eth_getWork,
        mungers=None,
    )

    def generateGasPrice(self, transaction_params: Optional[TxParams] = None) -> Optional[Wei]:
        if self.gasPriceStrategy:
            return self.gasPriceStrategy(self.web3, transaction_params)
        return None

    def setGasPriceStrategy(self, gas_price_strategy: GasPriceStrategy) -> None:
        self.gasPriceStrategy = gas_price_strategy
