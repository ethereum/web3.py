from typing import (
    List,
    Optional,
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

from web3._utils import (
    shh,
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
from web3.module import (
    Module,
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


class ParityShh(ModuleV2):
    """
    https://wiki.parity.io/JSONRPC-shh-module
    """
    info = shh.info
    new_key_pair = shh.new_key_pair
    add_private_key = shh.add_private_key
    new_sym_key = shh.new_sym_key
    add_sym_key = shh.add_sym_key
    get_public_key = shh.get_public_key
    get_private_key = shh.get_private_key
    get_sym_key = shh.get_sym_key
    post = shh.post
    new_message_filter = shh.new_message_filter
    delete_message_filter = shh.delete_message_filter
    get_filter_messages = shh.get_filter_messages
    delete_key = shh.delete_key
    subscribe = shh.subscribe
    unsubscribe = shh.unsubscribe
    # Deprecated
    newKeyPair = shh.new_key_pair
    addPrivateKey = shh.add_private_key
    newSymKey = shh.new_sym_key
    addSymKey = shh.add_sym_key
    getPublicKey = shh.get_public_key
    getPrivateKey = shh.get_private_key
    getSymKey = shh.get_sym_key
    newMessageFilter = shh.new_message_filter
    deleteMessageFilter = shh.delete_message_filter
    getFilterMessages = shh.get_filter_messages
    deleteKey = shh.delete_key


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


class Parity(Module):
    """
    https://paritytech.github.io/wiki/JSONRPC-parity-module
    """
    defaultBlock: Literal["latest"] = "latest"  # noqa: E704
    shh: ParityShh
    personal: ParityPersonal

    def enode(self) -> EnodeURI:
        return self.web3.manager.request_blocking(
            RPC.parity_enode,
            [],
        )

    def listStorageKeys(
        self,
        address: Union[Address, ChecksumAddress, ENS],
        quantity: int,
        hash_: Hash32,
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> List[Hash32]:
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            RPC.parity_listStorageKeys,
            [address, quantity, hash_, block_identifier],
        )

    def netPeers(self) -> ParityNetPeers:
        return self.web3.manager.request_blocking(
            RPC.parity_netPeers,
            [],
        )

    def addReservedPeer(self, url: EnodeURI) -> bool:
        return self.web3.manager.request_blocking(
            RPC.parity_addReservedPeer,
            [url],
        )

    def traceReplayTransaction(
        self, transaction_hash: _Hash32, mode: ParityTraceMode = ['trace']
    ) -> ParityBlockTrace:
        return self.web3.manager.request_blocking(
            RPC.trace_replayTransaction,
            [transaction_hash, mode],
        )

    def traceReplayBlockTransactions(
        self, block_identifier: BlockIdentifier, mode: ParityTraceMode = ['trace']
    ) -> List[ParityBlockTrace]:
        return self.web3.manager.request_blocking(
            RPC.trace_replayBlockTransactions,
            [block_identifier, mode]
        )

    def traceBlock(self, block_identifier: BlockIdentifier) -> List[ParityBlockTrace]:
        return self.web3.manager.request_blocking(
            RPC.trace_block,
            [block_identifier]
        )

    def traceFilter(self, params: ParityFilterParams) -> List[ParityFilterTrace]:
        return self.web3.manager.request_blocking(
            RPC.trace_filter,
            [params]
        )

    def traceTransaction(self, transaction_hash: _Hash32) -> List[ParityFilterTrace]:
        return self.web3.manager.request_blocking(
            RPC.trace_transaction,
            [transaction_hash]
        )

    def traceCall(
        self,
        transaction: TxParams,
        mode: ParityTraceMode = ['trace'],
        block_identifier: Optional[BlockIdentifier] = None
    ) -> ParityBlockTrace:
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.web3.eth.defaultAccount):
            transaction = assoc(transaction, 'from', self.web3.eth.defaultAccount)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            RPC.trace_call,
            [transaction, mode, block_identifier],
        )

    def traceRawTransaction(
        self, raw_transaction: HexStr, mode: ParityTraceMode = ['trace']
    ) -> ParityBlockTrace:
        return self.web3.manager.request_blocking(
            RPC.trace_rawTransaction,
            [raw_transaction, mode],
        )

    def setMode(self, mode: ParityMode) -> bool:
        return self.web3.manager.request_blocking(
            RPC.parity_setMode,
            [mode]
        )

    def mode(self) -> ParityMode:
        return self.web3.manager.request_blocking(
            RPC.parity_mode,
            []
        )
