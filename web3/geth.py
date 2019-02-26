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
