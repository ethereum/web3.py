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
    makeDag,
    setEtherbase,
    setExtra,
    setGasPrice,
    start,
    startAutoDag,
    stop,
    stopAutoDag,
)
from web3._utils.personal import (
    ecRecover,
    importRawKey,
    listAccounts,
    lockAccount,
    newAccount,
    sendTransaction,
    sign,
    signTypedData,
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


class Geth(Module):
    pass


class GethPersonal(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/management-apis#personal
    """
    ecRecover = ecRecover
    importRawKey = importRawKey
    listAccounts = listAccounts
    lockAccount = lockAccount
    newAccount = newAccount
    sendTransaction = sendTransaction
    sign = sign
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
    makeDag = makeDag
    setExtra = setExtra
    setEtherbase = setEtherbase
    setGasPrice = setGasPrice
    start = start
    stop = stop
    startAutoDag = startAutoDag
    stopAutoDag = stopAutoDag


class GethShh(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/Whisper-v6-RPC-API
    """
    version = shh.version
    info = shh.info
    setMaxMessageSize = shh.setMaxMessageSize
    setMinPoW = shh.setMinPoW
    markTrustedPeer = shh.markTrustedPeer
    newKeyPair = shh.newKeyPair
    addPrivateKey = shh.addPrivateKey
    deleteKeyPair = shh.deleteKeyPair
    hasKeyPair = shh.hasKeyPair
    getPublicKey = shh.getPublicKey
    getPrivateKey = shh.getPrivateKey
    newSymKey = shh.newSymKey
    addSymKey = shh.addSymKey
    generateSymKeyFromPassword = shh.generateSymKeyFromPassword
    hasSymKey = shh.hasSymKey
    getSymKey = shh.getSymKey
    deleteSymKey = shh.deleteSymKey
    post = shh.post
    newMessageFilter = shh.newMessageFilter
    deleteMessageFilter = shh.deleteMessageFilter
    getMessages = shh.getFilterMessages
    subscribe = shh.subscribe
    unsubscribe = shh.unsubscribe
