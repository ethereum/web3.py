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
import warnings

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
from web3._utils.decorators import (
    deprecated_for,
)
from web3._utils.empty import (
    Empty,
    empty,
)
from web3._utils.encoding import (
    to_hex,
)
from web3._utils.filters import (
    select_filter_method,
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
    TimeExhausted,
)
from web3.iban import (
    Iban,
)
from web3.method import (
    DeprecatedMethod,
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
    _default_account: Union[ChecksumAddress, Empty] = empty
    _default_block: BlockIdentifier = "latest"
    defaultContractFactory: Type[Union[Contract, ConciseContract, ContractCaller]] = Contract  # noqa: E704,E501
    iban = Iban
    gasPriceStrategy = None

    def namereg(self) -> NoReturn:
        raise NotImplementedError()

    def icapNamereg(self) -> NoReturn:
        raise NotImplementedError()

    _protocol_version: Method[Callable[[], str]] = Method(
        RPC.eth_protocolVersion,
        mungers=None,
    )

    @property
    def protocol_version(self) -> str:
        return self._protocol_version()

    @property
    def protocolVersion(self) -> str:
        warnings.warn(
            'protocolVersion is deprecated in favor of protocol_version',
            category=DeprecationWarning,
        )
        return self.protocol_version

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

    _gas_price: Method[Callable[[], Wei]] = Method(
        RPC.eth_gasPrice,
        mungers=None,
    )

    @property
    def gas_price(self) -> Wei:
        return self._gas_price()

    @property
    def gasPrice(self) -> Wei:
        warnings.warn(
            'gasPrice is deprecated in favor of gas_price',
            category=DeprecationWarning,
        )
        return self.gas_price

    get_accounts: Method[Callable[[], Tuple[ChecksumAddress]]] = Method(
        RPC.eth_accounts,
        mungers=None,
    )

    @property
    def accounts(self) -> Tuple[ChecksumAddress]:
        return self.get_accounts()

    _block_number: Method[Callable[[], BlockNumber]] = Method(
        RPC.eth_blockNumber,
        mungers=None,
    )

    @property
    def block_number(self) -> BlockNumber:
        return self._block_number()

    @property
    def blockNumber(self) -> BlockNumber:
        warnings.warn(
            'blockNumber is deprecated in favor of block_number',
            category=DeprecationWarning,
        )
        return self.block_number

    _chain_id: Method[Callable[[], int]] = Method(
        RPC.eth_chainId,
        mungers=None,
    )

    @property
    def chain_id(self) -> int:
        return self._chain_id()

    @property
    def chainId(self) -> int:
        warnings.warn(
            'chainId is deprecated in favor of chain_id',
            category=DeprecationWarning,
        )
        return self.chain_id

    """ property default_account """

    @property
    def default_account(self) -> Union[ChecksumAddress, Empty]:
        return self._default_account

    @default_account.setter
    def default_account(self, account: Union[ChecksumAddress, Empty]) -> None:
        self._default_account = account

    @property
    def defaultAccount(self) -> Union[ChecksumAddress, Empty]:
        warnings.warn(
            'defaultAccount is deprecated in favor of default_account',
            category=DeprecationWarning,
        )
        return self._default_account

    @defaultAccount.setter
    def defaultAccount(self, account: Union[ChecksumAddress, Empty]) -> None:
        warnings.warn(
            'defaultAccount is deprecated in favor of default_account',
            category=DeprecationWarning,
        )
        self._default_account = account

    """ property default_block """

    @property
    def default_block(self) -> BlockIdentifier:
        return self._default_block

    @default_block.setter
    def default_block(self, value: BlockIdentifier) -> None:
        self._default_block = value

    @property
    def defaultBlock(self) -> BlockIdentifier:
        warnings.warn(
            'defaultBlock is deprecated in favor of default_block',
            category=DeprecationWarning,
        )
        return self._default_block

    @defaultBlock.setter
    def defaultBlock(self, value: BlockIdentifier) -> None:
        warnings.warn(
            'defaultBlock is deprecated in favor of default_block',
            category=DeprecationWarning,
        )
        self._default_block = value

    def block_id_munger(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        block_identifier: Optional[BlockIdentifier] = None
    ) -> Tuple[Union[Address, ChecksumAddress, ENS], BlockIdentifier]:
        if block_identifier is None:
            block_identifier = self.default_block
        return (account, block_identifier)

    get_balance: Method[Callable[..., Wei]] = Method(
        RPC.eth_getBalance,
        mungers=[block_id_munger],
    )

    def get_storage_at_munger(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        position: int,
        block_identifier: Optional[BlockIdentifier] = None
    ) -> Tuple[Union[Address, ChecksumAddress, ENS], int, BlockIdentifier]:
        if block_identifier is None:
            block_identifier = self.default_block
        return (account, position, block_identifier)

    get_storage_at: Method[Callable[..., HexBytes]] = Method(
        RPC.eth_getStorageAt,
        mungers=[get_storage_at_munger],
    )

    def get_proof_munger(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        positions: Sequence[int],
        block_identifier: Optional[BlockIdentifier] = None
    ) -> Tuple[Union[Address, ChecksumAddress, ENS], Sequence[int], Optional[BlockIdentifier]]:
        if block_identifier is None:
            block_identifier = self.default_block
        return (account, positions, block_identifier)

    get_proof: Method[
        Callable[
            [Tuple[Union[Address, ChecksumAddress, ENS], Sequence[int], Optional[BlockIdentifier]]],
            MerkleProof
        ]
    ] = Method(
        RPC.eth_getProof,
        mungers=[get_proof_munger],
    )

    get_code: Method[Callable[..., HexBytes]] = Method(
        RPC.eth_getCode,
        mungers=[block_id_munger]
    )

    def get_block_munger(
        self, block_identifier: BlockIdentifier, full_transactions: bool = False
    ) -> Tuple[BlockIdentifier, bool]:
        return (block_identifier, full_transactions)

    """
    `eth_getBlockByHash`
    `eth_getBlockByNumber`
    """
    get_block: Method[Callable[..., BlockData]] = Method(
        method_choice_depends_on_args=select_method_for_block_identifier(
            if_predefined=RPC.eth_getBlockByNumber,
            if_hash=RPC.eth_getBlockByHash,
            if_number=RPC.eth_getBlockByNumber,
        ),
        mungers=[get_block_munger],
    )

    """
    `eth_getBlockTransactionCountByHash`
    `eth_getBlockTransactionCountByNumber`
    """
    get_block_transaction_count: Method[Callable[[BlockIdentifier], int]] = Method(
        method_choice_depends_on_args=select_method_for_block_identifier(
            if_predefined=RPC.eth_getBlockTransactionCountByNumber,
            if_hash=RPC.eth_getBlockTransactionCountByHash,
            if_number=RPC.eth_getBlockTransactionCountByNumber,
        ),
        mungers=[default_root_munger]
    )

    """
    `eth_getUncleCountByBlockHash`
    `eth_getUncleCountByBlockNumber`
    """
    get_uncle_count: Method[Callable[[BlockIdentifier], int]] = Method(
        method_choice_depends_on_args=select_method_for_block_identifier(
            if_predefined=RPC.eth_getUncleCountByBlockNumber,
            if_hash=RPC.eth_getUncleCountByBlockHash,
            if_number=RPC.eth_getUncleCountByBlockNumber,
        ),
        mungers=[default_root_munger]
    )

    """
    `eth_getUncleByBlockHashAndIndex`
    `eth_getUncleByBlockNumberAndIndex`
    """
    get_uncle_by_block: Method[Callable[[BlockIdentifier, int], Uncle]] = Method(
        method_choice_depends_on_args=select_method_for_block_identifier(
            if_predefined=RPC.eth_getUncleByBlockNumberAndIndex,
            if_hash=RPC.eth_getUncleByBlockHashAndIndex,
            if_number=RPC.eth_getUncleByBlockNumberAndIndex,
        ),
        mungers=[default_root_munger]
    )

    get_transaction: Method[Callable[[_Hash32], TxData]] = Method(
        RPC.eth_getTransactionByHash,
        mungers=[default_root_munger]
    )

    def getTransactionFromBlock(
        self, block_identifier: BlockIdentifier, transaction_index: int
    ) -> NoReturn:
        """
        Alias for the method getTransactionByBlock
        Deprecated to maintain naming consistency with the json-rpc API
        """
        raise DeprecationWarning("This method has been deprecated as of EIP 1474.")

    get_transaction_by_block: Method[Callable[[BlockIdentifier, int], TxData]] = Method(
        method_choice_depends_on_args=select_method_for_block_identifier(
            if_predefined=RPC.eth_getTransactionByBlockNumberAndIndex,
            if_hash=RPC.eth_getTransactionByBlockHashAndIndex,
            if_number=RPC.eth_getTransactionByBlockNumberAndIndex,
        ),
        mungers=[default_root_munger]
    )

    def waitForTransactionReceipt(
        self, transaction_hash: _Hash32, timeout: int = 120, poll_latency: float = 0.1
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

    getTransactionReceipt: Method[Callable[[_Hash32], TxReceipt]] = Method(
        RPC.eth_getTransactionReceipt,
        mungers=[default_root_munger]
    )

    get_transaction_count: Method[Callable[..., Nonce]] = Method(


        RPC.eth_getTransactionCount,
        mungers=[block_id_munger],
    )

    @deprecated_for("replace_transaction")
    def replaceTransaction(self, transaction_hash: _Hash32, new_transaction: TxParams) -> HexBytes:
        return self.replace_transaction(transaction_hash, new_transaction)

    def replace_transaction(self, transaction_hash: _Hash32, new_transaction: TxParams) -> HexBytes:
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

    def send_transaction_munger(self, transaction: TxParams) -> Tuple[TxParams]:
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.default_account):
            transaction = assoc(transaction, 'from', self.default_account)

        # TODO: move gas estimation in middleware
        if 'gas' not in transaction:
            transaction = assoc(
                transaction,
                'gas',
                get_buffered_gas_estimate(self.web3, transaction),
            )
        return (transaction,)

    send_transaction: Method[Callable[[TxParams], HexBytes]] = Method(
        RPC.eth_sendTransaction,
        mungers=[send_transaction_munger]
    )

    send_raw_transaction: Method[Callable[[Union[HexStr, bytes]], HexBytes]] = Method(
        RPC.eth_sendRawTransaction,
        mungers=[default_root_munger],
    )

    def sign_munger(
        self,
        account: Union[Address, ChecksumAddress, ENS],
        data: Union[int, bytes] = None,
        hexstr: HexStr = None,
        text: str = None
    ) -> Tuple[Union[Address, ChecksumAddress, ENS], HexStr]:
        message_hex = to_hex(data, hexstr=hexstr, text=text)
        return (account, message_hex)

    sign: Method[Callable[..., HexStr]] = Method(
        RPC.eth_sign,
        mungers=[sign_munger],
    )

    sign_transaction: Method[Callable[[TxParams], SignedTx]] = Method(
        RPC.eth_signTransaction,
        mungers=[default_root_munger],
    )

    signTypedData: Method[Callable[..., HexStr]] = Method(
        RPC.eth_signTypedData,
        mungers=[default_root_munger],
    )

    def call_munger(
        self,
        transaction: TxParams,
        block_identifier: Optional[BlockIdentifier] = None
    ) -> Tuple[TxParams, BlockIdentifier]:
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.default_account):
            transaction = assoc(transaction, 'from', self.default_account)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.default_block

        return (transaction, block_identifier)

    call: Method[Callable[..., Union[bytes, bytearray]]] = Method(
        RPC.eth_call,
        mungers=[call_munger]
    )

    def estimate_gas_munger(
        self,
        transaction: TxParams,
        block_identifier: Optional[BlockIdentifier] = None
    ) -> Sequence[Union[TxParams, BlockIdentifier]]:
        if 'from' not in transaction and is_checksum_address(self.default_account):
            transaction = assoc(transaction, 'from', self.default_account)

        if block_identifier is None:
            params: Sequence[Union[TxParams, BlockIdentifier]] = [transaction]
        else:
            params = [transaction, block_identifier]

        return params

    estimateGas: Method[Callable[..., Wei]] = Method(
        RPC.eth_estimateGas,
        mungers=[estimate_gas_munger]
    )

    def filter_munger(
        self,
        filter_params: Optional[Union[str, FilterParams]] = None,
        filter_id: Optional[HexStr] = None
    ) -> Union[List[FilterParams], List[HexStr], List[str]]:
        if filter_id and filter_params:
            raise TypeError(
                "Ambiguous invocation: provide either a `filter_params` or a `filter_id` argument. "
                "Both were supplied."
            )
        if isinstance(filter_params, dict):
            return [filter_params]
        elif is_string(filter_params):
            if filter_params in ['latest', 'pending']:
                return [filter_params]
            else:
                raise ValueError(
                    "The filter API only accepts the values of `pending` or "
                    "`latest` for string based filters"
                )
        elif filter_id and not filter_params:
            return [filter_id]
        else:
            raise TypeError("Must provide either filter_params as a string or "
                            "a valid filter object, or a filter_id as a string "
                            "or hex.")

    filter: Method[Callable[..., Any]] = Method(
        method_choice_depends_on_args=select_filter_method(
            if_new_block_filter=RPC.eth_newBlockFilter,
            if_new_pending_transaction_filter=RPC.eth_newPendingTransactionFilter,
            if_new_filter=RPC.eth_newFilter,
        ),
        mungers=[filter_munger],
    )

    getFilterChanges: Method[Callable[[HexStr], List[LogReceipt]]] = Method(
        RPC.eth_getFilterChanges,
        mungers=[default_root_munger]
    )

    getFilterLogs: Method[Callable[[HexStr], List[LogReceipt]]] = Method(
        RPC.eth_getFilterLogs,
        mungers=[default_root_munger]
    )

    getLogs: Method[Callable[[FilterParams], List[LogReceipt]]] = Method(
        RPC.eth_getLogs,
        mungers=[default_root_munger]
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

    # Deprecated Methods
    getBalance = DeprecatedMethod(get_balance, 'getBalance', 'get_balance')
    getStorageAt = DeprecatedMethod(get_storage_at, 'getStorageAt', 'get_storage_at')
    getBlock = DeprecatedMethod(get_block, 'getBlock', 'get_block')
    getBlockTransactionCount = DeprecatedMethod(get_block_transaction_count,
                                                'getBlockTransactionCount',
                                                'get_block_transaction_count')
    getCode = DeprecatedMethod(get_code, 'getCode', 'get_code')
    getProof = DeprecatedMethod(get_proof, 'getProof', 'get_proof')
    getTransaction = DeprecatedMethod(get_transaction, 'getTransaction', 'get_transaction')
    getTransactionByBlock = DeprecatedMethod(get_transaction_by_block,
                                             'getTransactionByBlock',
                                             'get_transaction_by_block')
    getTransactionCount = DeprecatedMethod(get_transaction_count,
                                           'getTransactionCount',
                                           'get_transaction_count')
    getUncleByBlock = DeprecatedMethod(get_uncle_by_block, 'getUncleByBlock', 'get_uncle_by_block')
    getUncleCount = DeprecatedMethod(get_uncle_count, 'getUncleCount', 'get_uncle_count')
    sendTransaction = DeprecatedMethod(send_transaction, 'sendTransaction', 'send_transaction')
    signTransaction = DeprecatedMethod(sign_transaction, 'signTransaction', 'sign_transaction')
    sendRawTransaction = DeprecatedMethod(send_raw_transaction,
                                          'sendRawTransaction',
                                          'send_raw_transaction')
