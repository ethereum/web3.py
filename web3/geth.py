from web3._utils import (
    shh,
)
from web3._utils.admin import (
    add_peer,
    addPeer,
    datadir,
    node_info,
    nodeInfo,
    peers,
    start_rpc,
    start_ws,
    startRPC,
    startWS,
    stop_rpc,
    stop_ws,
    stopRPC,
    stopWS,
)
from web3._utils.miner import (
    make_dag,
    makeDag,
    set_etherbase,
    set_extra,
    set_gas_price,
    setEtherbase,
    setExtra,
    setGasPrice,
    start,
    start_auto_dag,
    startAutoDag,
    stop,
    stop_auto_dag,
    stopAutoDag,
)
from web3._utils.personal import (
    ec_recover,
    ecRecover,
    import_raw_key,
    importRawKey,
    list_accounts,
    list_wallets,
    listAccounts,
    lock_account,
    lockAccount,
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
from web3._utils.txpool import (
    content,
    inspect,
    status,
)
from web3.module import (
    Module,
    ModuleV2,
)


class GethPersonal(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/management-apis#personal
    """
    ec_recover = ec_recover
    import_raw_key = import_raw_key
    list_accounts = list_accounts
    list_wallets = list_wallets
    lock_account = lock_account
    new_account = new_account
    send_transaction = send_transaction
    sign = sign
    sign_typed_data = sign_typed_data
    unlock_account = unlock_account
    # deprecated
    ecRecover = ecRecover
    importRawKey = importRawKey
    listAccounts = listAccounts
    lockAccount = lockAccount
    newAccount = newAccount
    sendTransaction = sendTransaction
    signTypedData = signTypedData
    unlockAccount = unlockAccount


class GethTxPool(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#txpool
    """
    content = content
    inspect = inspect
    status = status


class GethAdmin(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin
    """
    add_peer = add_peer
    node_info = node_info
    start_rpc = start_rpc
    start_ws = start_ws
    stop_ws = stop_ws
    stop_rpc = stop_rpc
    # deprecated
    addPeer = addPeer
    datadir = datadir
    nodeInfo = nodeInfo
    peers = peers
    startRPC = startRPC
    startWS = startWS
    stopRPC = stopRPC
    stopWS = stopWS


class GethMiner(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner
    """
    make_dag = make_dag
    set_extra = set_extra
    set_etherbase = set_etherbase
    set_gas_price = set_gas_price
    start = start
    stop = stop
    start_auto_dag = start_auto_dag
    stop_auto_dag = stop_auto_dag
    # deprecated
    makeDag = makeDag
    setExtra = setExtra
    setEtherbase = setEtherbase
    setGasPrice = setGasPrice
    startAutoDag = startAutoDag
    stopAutoDag = stopAutoDag


class GethShh(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/Whisper-v6-RPC-API
    """
    add_private_key = shh.add_private_key
    add_sym_key = shh.add_sym_key
    delete_key = shh.delete_key
    delete_key_pair = shh.delete_key_pair
    delete_message_filter = shh.delete_message_filter
    delete_sym_key = shh.delete_sym_key
    generate_sym_key_from_password = shh.generate_sym_key_from_password
    get_filter_messages = shh.get_filter_messages
    get_private_key = shh.get_private_key
    get_public_key = shh.get_public_key
    get_sym_key = shh.get_sym_key
    has_key_pair = shh.has_key_pair
    has_sym_key = shh.has_sym_key
    info = shh.info
    mark_trusted_peer = shh.mark_trusted_peer
    new_key_pair = shh.new_key_pair
    new_message_filter = shh.new_message_filter
    new_sym_key = shh.new_sym_key
    post = shh.post
    set_max_message_size = shh.set_max_message_size
    set_min_pow = shh.set_min_pow
    subscribe = shh.subscribe
    unsubscribe = shh.unsubscribe
    version = shh.version
    # Deprecated
    addPrivateKey = shh.addPrivateKey
    addSymKey = shh.addSymKey
    deleteKeyPair = shh.deleteKeyPair
    deleteMessageFilter = shh.deleteMessageFilter
    deleteSymKey = shh.deleteSymKey
    generateSymKeyFromPassword = shh.generateSymKeyFromPassword
    getMessages = shh.getFilterMessages
    getPrivateKey = shh.getPrivateKey
    getPublicKey = shh.getPublicKey
    getSymKey = shh.getSymKey
    hasKeyPair = shh.hasKeyPair
    hasSymKey = shh.hasSymKey
    markTrustedPeer = shh.markTrustedPeer
    newKeyPair = shh.newKeyPair
    newMessageFilter = shh.newMessageFilter
    newSymKey = shh.newSymKey
    setMaxMessageSize = shh.setMaxMessageSize
    setMinPoW = shh.setMinPoW


class Geth(Module):
    shh: GethShh
    personal: GethPersonal
    admin: GethAdmin
