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
)


class GethPersonal(Module):
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


class GethTxPool(Module):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#txpool
    """
    content = content
    inspect = inspect
    status = status


class GethAdmin(Module):
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


class GethMiner(Module):
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


class Geth(Module):
    personal: GethPersonal
    admin: GethAdmin
