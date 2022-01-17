from typing import (
    Any,
    Awaitable,
    List,
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
)
from web3.types import (
    EnodeURI,
    NodeInfo,
    Peer,
    TxPoolContent,
    TxPoolInspect,
    TxPoolStatus,
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


class BaseTxPool(Module):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#txpool
    """
    _content = content
    _inspect = inspect
    _status = status


class GethTxPool(BaseTxPool):
    is_async = False

    def content(self) -> TxPoolContent:
        return self._content()

    def inspect(self) -> TxPoolInspect:
        return self._inspect()

    def status(self) -> TxPoolStatus:
        return self._status()


class AsyncGethTxPool(BaseTxPool):
    is_async = True

    async def content(self) -> Awaitable[Any]:
        return await self._content()  # type: ignore

    async def inspect(self) -> Awaitable[Any]:
        return await self._inspect()  # type: ignore

    async def status(self) -> Awaitable[Any]:
        return await self._status()  # type: ignore


class BaseGethAdmin(Module):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin
    """
    _add_peer = add_peer
    _datadir = datadir
    _node_info = node_info
    _peers = peers
    _start_rpc = start_rpc
    _start_ws = start_ws
    _stop_ws = stop_ws
    _stop_rpc = stop_rpc
    # deprecated
    _addPeer = addPeer
    _nodeInfo = nodeInfo
    _startRPC = startRPC
    _startWS = startWS
    _stopRPC = stopRPC
    _stopWS = stopWS


class GethAdmin(BaseGethAdmin):
    is_async = False

    def add_peer(self, node_url: EnodeURI) -> bool:
        return self._add_peer(node_url)

    def datadir(self) -> str:
        return self._datadir()

    def node_info(self) -> NodeInfo:
        return self._node_info()

    def peers(self) -> List[Peer]:
        return self._peers()

    def start_rpc(self,
                  host: str = "localhost",
                  port: int = 8546,
                  cors: str = "",
                  apis: str = "eth,net,web3") -> bool:
        return self._start_rpc(host, port, cors, apis)

    def start_ws(self,
                 host: str = "localhost",
                 port: int = 8546,
                 cors: str = "",
                 apis: str = "eth,net,web3") -> bool:
        return self._start_ws(host, port, cors, apis)

    def stop_rpc(self) -> bool:
        return self._stop_rpc()

    def stop_ws(self) -> bool:
        return self._stop_ws()

    def addPeer(self, node_url: EnodeURI) -> bool:
        return self._addPeer(node_url)

    def nodeInfo(self) -> NodeInfo:
        return self._nodeInfo()

    def startRPC(self,
                 host: str = "localhost",
                 port: int = 8546,
                 cors: str = "",
                 apis: str = "eth,net,web3") -> bool:
        return self._startRPC(host, port, cors, apis)

    def startWS(self,
                host: str = "localhost",
                port: int = 8546,
                cors: str = "",
                apis: str = "eth,net,web3") -> bool:
        return self._startWS(host, port, cors, apis)

    def stopRPC(self) -> bool:
        return self._stopRPC()

    def stopWS(self) -> bool:
        return self._stopWS()


class AsyncGethAdmin(BaseGethAdmin):
    is_async = True

    async def add_peer(self, node_url: EnodeURI) -> Awaitable[bool]:
        return await self._add_peer(node_url)  # type: ignore

    async def datadir(self) -> Awaitable[str]:
        return await self._datadir()  # type: ignore

    async def node_info(self) -> Awaitable[NodeInfo]:
        return await self._node_info()  # type: ignore

    async def peers(self) -> Awaitable[List[Peer]]:
        return await self._peers()  # type: ignore

    async def start_rpc(self,
                        host: str = "localhost",
                        port: int = 8546,
                        cors: str = "",
                        apis: str = "eth,net,web3") -> Awaitable[bool]:
        return await self._start_rpc(host, port, cors, apis)  # type: ignore

    async def start_ws(self,
                       host: str = "localhost",
                       port: int = 8546,
                       cors: str = "",
                       apis: str = "eth,net,web3") -> Awaitable[bool]:
        return await self._start_ws(host, port, cors, apis)  # type: ignore

    async def stop_rpc(self) -> Awaitable[bool]:
        return await self._stop_rpc()  # type: ignore

    async def stop_ws(self) -> Awaitable[bool]:
        return await self._stop_ws()  # type: ignore


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
