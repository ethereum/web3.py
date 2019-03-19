from web3.admin import (
    addPeer,
    datadir,
    nodeInfo,
    peers,
    setSolc,
    startRPC,
    startWS,
    stopRPC,
    stopWS,
)
from web3.module import (
    Module,
    ModuleV2,
)
from web3.personal import (
    ecRecover,
    importRawKey,
    listAccounts,
    lockAccount,
    newAccount,
    sendTransaction,
    sign,
    unlockAccount,
)
from web3.txpool import (
    content,
    inspect,
    status,
)


class Geth(Module):
    pass


class GethPersonal(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal
    """
    ecRecover = ecRecover()
    importRawKey = importRawKey()
    listAccounts = listAccounts()
    lockAccount = lockAccount()
    newAccount = newAccount()
    sendTransaction = sendTransaction()
    sign = sign()
    unlockAccount = unlockAccount()


class GethTxPool(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#txpool
    """
    content = content()
    inspect = inspect()
    status = status()


class GethAdmin(ModuleV2):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin
    """
    addPeer = addPeer()
    datadir = datadir()
    nodeInfo = nodeInfo()
    peers = peers()
    setSolc = setSolc()
    startRPC = startRPC()
    startWS = startWS()
    stopRPC = stopRPC()
    stopWS = stopWS()
