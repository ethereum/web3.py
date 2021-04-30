from typing import (
    Callable,
    List,
    Optional,
    Tuple,
    Union,
)
import warnings

from eth_typing import (
    Address,
    ChecksumAddress,
    Hash32,
    HexStr,
)
from eth_utils import (
    is_checksum_address,
)
from eth_utils.toolz import (
    assoc,
)

from web3._utils.personal import (
    ec_recover,
    ecRecover,
    import_raw_key,
    importRawKey,
    list_accounts,
    listAccounts,
    new_account,
    newAccount,
    send_transaction,
    sendTransaction,
    sign,
    sign_typed_data,
    signTypedData,
    unlock_account,
    unlockAccount,
)
from web3._utils.rpc_abi import (
    RPC,
)
from web3.method import (
    DeprecatedMethod,
    Method,
    default_root_munger,
)
from web3.module import (
    Module,
)
from web3.types import (
    ENS,
    BlockIdentifier,
    EnodeURI,
    ParityBlockTrace,
    ParityFilterParams,
    ParityFilterTrace,
    ParityMode,
    ParityNetPeers,
    ParityTraceMode,
    TxParams,
    _Hash32,
)


class ParityPersonal(Module):
    """
    https://wiki.parity.io/JSONRPC-personal-module
    """
    ec_recover = ec_recover
    import_raw_key = import_raw_key
    list_accounts = list_accounts
    new_account = new_account
    send_transaction = send_transaction
    sign = sign
    sign_typed_data = sign_typed_data
    unlock_account = unlock_account
    # deprecated
    ecRecover = ecRecover
    importRawKey = importRawKey
    listAccounts = listAccounts
    newAccount = newAccount
    sendTransaction = sendTransaction
    signTypedData = signTypedData
    unlockAccount = unlockAccount


class Parity(Module):
    """
    https://paritytech.github.io/wiki/JSONRPC-parity-module
    """
    _default_block: BlockIdentifier = "latest"
    personal: ParityPersonal

    enode: Method[Callable[[], str]] = Method(
        RPC.parity_enode,
        mungers=None,
    )

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

    def list_storage_keys_munger(
        self,
        address: Union[Address, ChecksumAddress, ENS, Hash32],
        quantity: int,
        hash_: Hash32,
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> Tuple[Union[Address, ChecksumAddress, ENS, Hash32], int, Hash32, BlockIdentifier]:
        if block_identifier is None:
            block_identifier = self.default_block
        return (address, quantity, hash_, block_identifier)

    list_storage_keys: Method[Callable[..., List[Hash32]]] = Method(
        RPC.parity_listStorageKeys,
        mungers=[list_storage_keys_munger],
    )

    net_peers: Method[Callable[[], ParityNetPeers]] = Method(
        RPC.parity_netPeers,
        mungers=None
    )

    add_reserved_peer: Method[Callable[[EnodeURI], bool]] = Method(
        RPC.parity_addReservedPeer,
        mungers=[default_root_munger],
    )

    def trace_replay_transaction_munger(
        self, block_identifier: Union[_Hash32, BlockIdentifier], mode: ParityTraceMode = ['trace']
    ) -> Tuple[Union[BlockIdentifier, _Hash32], ParityTraceMode]:
        return (block_identifier, mode)

    trace_replay_transaction: Method[Callable[..., ParityBlockTrace]] = Method(
        RPC.trace_replayTransaction,
        mungers=[trace_replay_transaction_munger],
    )

    trace_replay_block_transactions: Method[Callable[..., List[ParityBlockTrace]]] = Method(
        RPC.trace_replayBlockTransactions,
        mungers=[trace_replay_transaction_munger]
    )

    trace_block: Method[Callable[[BlockIdentifier], List[ParityBlockTrace]]] = Method(
        RPC.trace_block,
        mungers=[default_root_munger],
    )

    trace_filter: Method[Callable[[ParityFilterParams], List[ParityFilterTrace]]] = Method(
        RPC.trace_filter,
        mungers=[default_root_munger],
    )

    trace_transaction: Method[Callable[[_Hash32], List[ParityFilterTrace]]] = Method(
        RPC.trace_transaction,
        mungers=[default_root_munger],
    )

    def trace_call_munger(
        self,
        transaction: TxParams,
        mode: ParityTraceMode = ['trace'],
        block_identifier: Optional[BlockIdentifier] = None
    ) -> Tuple[TxParams, ParityTraceMode, BlockIdentifier]:
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.web3.eth.default_account):
            transaction = assoc(transaction, 'from', self.web3.eth.default_account)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.default_block

        return (transaction, mode, block_identifier)

    trace_call: Method[Callable[..., ParityBlockTrace]] = Method(
        RPC.trace_call,
        mungers=[trace_call_munger],
    )

    def trace_transactions_munger(
        self, raw_transaction: HexStr, mode: ParityTraceMode = ['trace']
    ) -> Tuple[HexStr, ParityTraceMode]:
        return (raw_transaction, mode)

    trace_raw_transaction: Method[Callable[..., ParityBlockTrace]] = Method(
        RPC.trace_rawTransaction,
        mungers=[trace_transactions_munger],
    )

    set_mode: Method[Callable[[ParityMode], bool]] = Method(
        RPC.parity_setMode,
        mungers=[default_root_munger],
    )

    mode: Method[Callable[[], ParityMode]] = Method(
        RPC.parity_mode,
        mungers=None
    )

    # Deprecated Methods
    addReservedPeer = DeprecatedMethod(add_reserved_peer, 'addReservedPeer', 'add_reserved_peer')
    listStorageKeys = DeprecatedMethod(list_storage_keys, 'listStorageKeys', 'list_storage_keys')
    netPeers = DeprecatedMethod(net_peers, 'netPeers', 'net_peers')
    setMode = DeprecatedMethod(set_mode, 'setMode', 'set_mode')
    traceBlock = DeprecatedMethod(trace_block, 'traceBlock', 'trace_block')
    traceCall = DeprecatedMethod(trace_call, 'traceCall', 'trace_call')
    traceFilter = DeprecatedMethod(trace_filter, 'traceFilter', 'trace_filter')
    traceRawTransaction = DeprecatedMethod(trace_raw_transaction, 'traceRawTransaction',
                                           'trace_raw_transaction')
    traceReplayTransaction = DeprecatedMethod(trace_replay_transaction, 'traceReplayTransaction',
                                              'trace_replay_transaction')
    traceReplayBlockTransactions = DeprecatedMethod(trace_replay_block_transactions,
                                                    'traceReplayBlockTransactions',
                                                    'trace_replay_block_transactions')
    traceTransaction = DeprecatedMethod(trace_transaction, 'traceTransaction', 'trace_transaction')
