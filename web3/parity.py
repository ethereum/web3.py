from typing import (
    Callable,
    List,
    Optional,
    Tuple,
    Union,
)

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

from web3._utils.compat import (
    Literal,
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
    Method,
    default_root_munger,
)
from web3.module import (
    ModuleV2,
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


class ParityPersonal(ModuleV2):
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


class Parity(ModuleV2):
    """
    https://paritytech.github.io/wiki/JSONRPC-parity-module
    """
    defaultBlock: Literal["latest"] = "latest"  # noqa: E704
    personal: ParityPersonal

    enode: Method[Callable[[], str]] = Method(
        RPC.parity_enode,
        mungers=None,
    )

    def list_storage_keys_munger(
        self,
        address: Union[Address, ChecksumAddress, ENS, Hash32],
        quantity: int,
        hash_: Hash32,
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> Tuple[Union[Address, ChecksumAddress, ENS, Hash32], int, Hash32, BlockIdentifier]:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return (address, quantity, hash_, block_identifier)

    listStorageKeys: Method[Callable[..., List[Hash32]]] = Method(
        RPC.parity_listStorageKeys,
        mungers=[list_storage_keys_munger],
    )

    netPeers: Method[Callable[[], ParityNetPeers]] = Method(
        RPC.parity_netPeers,
        mungers=None
    )

    addReservedPeer: Method[Callable[[EnodeURI], bool]] = Method(
        RPC.parity_addReservedPeer,
        mungers=[default_root_munger],
    )

    def trace_replay_transaction_munger(
        self, block_identifier: Union[_Hash32, BlockIdentifier], mode: ParityTraceMode = ['trace']
    ) -> Tuple[Union[BlockIdentifier, _Hash32], ParityTraceMode]:
        return (block_identifier, mode)

    traceReplayTransaction: Method[Callable[..., ParityBlockTrace]] = Method(
        RPC.trace_replayTransaction,
        mungers=[trace_replay_transaction_munger],
    )

    traceReplayBlockTransactions: Method[Callable[..., List[ParityBlockTrace]]] = Method(
        RPC.trace_replayBlockTransactions,
        mungers=[trace_replay_transaction_munger]
    )

    traceBlock: Method[Callable[[BlockIdentifier], List[ParityBlockTrace]]] = Method(
        RPC.trace_block,
        mungers=[default_root_munger],
    )

    traceFilter: Method[Callable[[ParityFilterParams], List[ParityFilterTrace]]] = Method(
        RPC.trace_filter,
        mungers=[default_root_munger],
    )

    traceTransaction: Method[Callable[[_Hash32], List[ParityFilterTrace]]] = Method(
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
        if 'from' not in transaction and is_checksum_address(self.web3.eth.defaultAccount):
            transaction = assoc(transaction, 'from', self.web3.eth.defaultAccount)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.defaultBlock

        return (transaction, mode, block_identifier)

    traceCall: Method[Callable[..., ParityBlockTrace]] = Method(
        RPC.trace_call,
        mungers=[trace_call_munger],
    )

    def trace_transactions_munger(
        self, raw_transaction: HexStr, mode: ParityTraceMode = ['trace']
    ) -> Tuple[HexStr, ParityTraceMode]:
        return (raw_transaction, mode)

    traceRawTransaction: Method[Callable[..., ParityBlockTrace]] = Method(
        RPC.trace_rawTransaction,
        mungers=[trace_transactions_munger],
    )

    setMode: Method[Callable[[ParityMode], bool]] = Method(
        RPC.parity_setMode,
        mungers=[default_root_munger],
    )

    mode: Method[Callable[[], ParityMode]] = Method(
        RPC.parity_mode,
        mungers=None
    )
