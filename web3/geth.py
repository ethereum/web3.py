from typing import (
    Any,
    Awaitable,
    Dict,
    List,
    Optional,
)

from eth_typing.encoding import (
    HexStr,
)
from eth_typing.evm import (
    ChecksumAddress,
)
from hexbytes.main import (
    HexBytes,
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
    GethWallet,
    NodeInfo,
    Peer,
    TxParams,
    TxPoolContent,
    TxPoolInspect,
    TxPoolStatus,
)


class BaseGethPersonal(Module):
    """
    https://github.com/ethereum/go-ethereum/wiki/management-apis#personal
    """
    _ec_recover = ec_recover
    _import_raw_key = import_raw_key
    _list_accounts = list_accounts
    _list_wallets = list_wallets
    _lock_account = lock_account
    _new_account = new_account
    _send_transaction = send_transaction
    _sign = sign
    _sign_typed_data = sign_typed_data
    _unlock_account = unlock_account
    # deprecated
    _ecRecover = ecRecover
    _importRawKey = importRawKey
    _listAccounts = listAccounts
    _lockAccount = lockAccount
    _newAccount = newAccount
    _sendTransaction = sendTransaction
    _signTypedData = signTypedData
    _unlockAccount = unlockAccount


class GethPersonal(BaseGethPersonal):
    is_async = False

    def ec_recover(self, message: str, signature: HexStr) -> ChecksumAddress:
        return self._ec_recover(message, signature)

    def import_raw_key(self, private_key: str, passphrase: str) -> ChecksumAddress:
        return self._import_raw_key(private_key, passphrase)

    def list_accounts(self) -> List[ChecksumAddress]:
        return self._list_accounts()

    def list_wallets(self) -> List[GethWallet]:
        return self._list_wallets()

    def lock_account(self, account: ChecksumAddress) -> bool:
        return self._lock_account(account)

    def new_account(self, passphrase: str) -> ChecksumAddress:
        return self._new_account(passphrase)

    def send_transaction(self, transaction: TxParams, passphrase: str) -> HexBytes:
        return self._send_transaction(transaction, passphrase)

    def sign(self, message: str, account: ChecksumAddress, password: Optional[str]) -> HexStr:
        return self._sign(message, account, password)

    def sign_typed_data(self,
                        message: Dict[str, Any],
                        account: ChecksumAddress,
                        password: Optional[str]) -> HexStr:
        return self._sign_typed_data(message, account, password)

    def unlock_account(self,
                       account: ChecksumAddress,
                       passphrase: str,
                       duration: Optional[int] = None) -> bool:
        return self._unlock_account(account, passphrase, duration)

    def ecRecover(self, message: str, signature: HexStr) -> ChecksumAddress:
        return self._ecRecover(message, signature)

    def importRawKey(self, private_key: str, passphrase: str) -> ChecksumAddress:
        return self._importRawKey(private_key, passphrase)

    def listAccounts(self) -> List[ChecksumAddress]:
        return self._listAccounts()

    def lockAccount(self, account: ChecksumAddress) -> bool:
        return self._lockAccount(account)

    def newAccount(self, passphrase: str) -> ChecksumAddress:
        return self._newAccount(passphrase)

    def sendTransaction(self, transaction: TxParams, passphrase: str) -> HexBytes:
        return self._sendTransaction(transaction, passphrase)

    def signTypedData(self,
                      message: Dict[str, Any],
                      account: ChecksumAddress,
                      password: Optional[str] = None) -> HexStr:
        return self._signTypedData(message, account, password)

    def unlockAccount(self,
                      account: ChecksumAddress,
                      passphrase: str,
                      duration: Optional[int] = None) -> bool:
        return self._unlockAccount(account, passphrase, duration)


class AsyncGethPersonal(BaseGethPersonal):
    is_async = True

    async def ec_recover(self, message: str, signature: HexStr) -> Awaitable[ChecksumAddress]:
        return await self._ec_recover(message, signature)  # type: ignore

    async def import_raw_key(self, private_key: str, passphrase: str) -> Awaitable[ChecksumAddress]:
        return await self._import_raw_key(private_key, passphrase)  # type: ignore

    async def list_accounts(self) -> Awaitable[List[ChecksumAddress]]:
        return await self._list_accounts()  # type: ignore

    async def list_wallets(self) -> Awaitable[List[GethWallet]]:
        return await self._list_wallets()  # type: ignore

    async def lock_account(self, account: ChecksumAddress) -> Awaitable[bool]:
        return await self._lock_account(account)  # type: ignore

    async def new_account(self, passphrase: str) -> Awaitable[ChecksumAddress]:
        return await self._new_account(passphrase)  # type: ignore

    async def send_transaction(self, transaction: TxParams, passphrase: str) -> Awaitable[HexBytes]:
        return await self._send_transaction(transaction, passphrase)  # type: ignore

    async def sign(self,
                   message: str,
                   account: ChecksumAddress,
                   password: Optional[str]) -> Awaitable[HexStr]:
        return await self._sign(message, account, password)  # type: ignore

    async def sign_typed_data(self,
                              message: Dict[str, Any],
                              account: ChecksumAddress,
                              password: Optional[str]) -> Awaitable[HexStr]:
        return await self._sign_typed_data(message, account, password)  # type: ignore

    async def unlock_account(self,
                             account: ChecksumAddress,
                             passphrase: str,
                             duration: Optional[int] = None) -> Awaitable[bool]:
        return await self._unlock_account(account, passphrase, duration)  # type: ignore


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
