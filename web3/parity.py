from eth_utils import (
    is_checksum_address,
)
from eth_utils.toolz import (
    assoc,
)

from web3._utils import (
    shh,
)
from web3._utils.personal import (
    ecRecover,
    importRawKey,
    listAccounts,
    newAccount,
    sendTransaction,
    sign,
    signTypedData,
    unlockAccount,
)
from web3.module import (
    Module,
    ModuleV2,
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
    ecRecover = ecRecover
    importRawKey = importRawKey
    listAccounts = listAccounts
    newAccount = newAccount
    sendTransaction = sendTransaction
    sign = sign
    signTypedData = signTypedData
    unlockAccount = unlockAccount


class Parity(Module):
    """
    https://paritytech.github.io/wiki/JSONRPC-parity-module
    """
    defaultBlock = "latest"

    def enode(self):
        return self.web3.manager.request_blocking(
            "parity_enode",
            [],
        )

    def listStorageKeys(self, address, quantity, hash_, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "parity_listStorageKeys",
            [address, quantity, hash_, block_identifier],
        )

    def netPeers(self):
        return self.web3.manager.request_blocking(
            "parity_netPeers",
            [],
        )

    def addReservedPeer(self, url):
        return self.web3.manager.request_blocking(
            "parity_addReservedPeer",
            [url],
        )

    def traceReplayTransaction(self, transaction_hash, mode=['trace']):
        return self.web3.manager.request_blocking(
            "trace_replayTransaction",
            [transaction_hash, mode],
        )

    def traceReplayBlockTransactions(self, block_identifier, mode=['trace']):
        return self.web3.manager.request_blocking(
            "trace_replayBlockTransactions",
            [block_identifier, mode]
        )

    def traceBlock(self, block_identifier):
        return self.web3.manager.request_blocking(
            "trace_block",
            [block_identifier]
        )

    def traceFilter(self, params):
        return self.web3.manager.request_blocking(
            "trace_filter",
            [params]
        )

    def traceTransaction(self, transaction_hash):
        return self.web3.manager.request_blocking(
            "trace_transaction",
            [transaction_hash]
        )

    def traceCall(self, transaction, mode=['trace'], block_identifier=None):
        # TODO: move to middleware
        if 'from' not in transaction and is_checksum_address(self.defaultAccount):
            transaction = assoc(transaction, 'from', self.defaultAccount)

        # TODO: move to middleware
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "trace_call",
            [transaction, mode, block_identifier],
        )

    def traceRawTransaction(self, raw_transaction, mode=['trace']):
        return self.web3.manager.request_blocking(
            "trace_rawTransaction",
            [raw_transaction, mode],
        )

    def setMode(self, mode):
        return self.web3.manager.request_blocking(
            "parity_setMode",
            [mode]
        )

    def mode(self):
        return self.web3.manager.request_blocking(
            "parity_mode",
            []
        )
