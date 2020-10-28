from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    NewType,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
)

from eth_typing import (
    Address,
    BlockNumber,
    ChecksumAddress,
    Hash32,
    HexStr,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.compat import (
    Literal,
    TypedDict,
)
from web3._utils.function_identifiers import (
    FallbackFn,
    ReceiveFn,
)
from web3.datastructures import (
    NamedElementOnion,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


TReturn = TypeVar("TReturn")
TParams = TypeVar("TParams")
TValue = TypeVar("TValue")

BlockParams = Literal["latest", "earliest", "pending"]
BlockIdentifier = Union[BlockParams, BlockNumber, Hash32, HexStr, HexBytes, int]
LatestBlockParam = Literal["latest"]

FunctionIdentifier = Union[str, Type[FallbackFn], Type[ReceiveFn]]

# bytes, hexbytes, or hexstr representing a 32 byte hash
_Hash32 = Union[Hash32, HexBytes, HexStr]
EnodeURI = NewType("EnodeURI", str)
ENS = NewType("ENS", str)
Nonce = NewType("Nonce", int)
RPCEndpoint = NewType("RPCEndpoint", str)
Timestamp = NewType("Timestamp", int)
Wei = NewType('Wei', int)
Formatters = Dict[RPCEndpoint, Callable[..., Any]]


# todo: move these to eth_typing once web3 is type hinted
class ABIEventParams(TypedDict, total=False):
    indexed: bool
    name: str
    type: str


class ABIEvent(TypedDict, total=False):
    anonymous: bool
    inputs: Sequence["ABIEventParams"]
    name: str
    type: Literal["event"]


class ABIFunctionComponents(TypedDict, total=False):
    # better typed as Sequence['ABIFunctionComponents'], but recursion isnt possible yet
    # https://github.com/python/mypy/issues/731
    components: Sequence[Any]
    name: str
    type: str


class ABIFunctionParams(TypedDict, total=False):
    components: Sequence["ABIFunctionComponents"]
    name: str
    type: str


class ABIFunction(TypedDict, total=False):
    constant: bool
    inputs: Sequence["ABIFunctionParams"]
    name: str
    outputs: Sequence["ABIFunctionParams"]
    payable: bool
    stateMutability: Literal["pure", "view", "nonpayable", "payable"]
    type: Literal["function", "constructor", "fallback", "receive"]


ABIElement = Union[ABIFunction, ABIEvent]
ABI = Sequence[Union[ABIFunction, ABIEvent]]


class EventData(TypedDict):
    address: ChecksumAddress
    args: Dict[str, Any]
    blockHash: HexBytes
    blockNumber: int
    event: str
    logIndex: int
    transactionHash: HexBytes
    transactionIndex: int


class RPCError(TypedDict):
    code: int
    message: str
    data: Optional[str]


class RPCResponse(TypedDict, total=False):
    error: Union[RPCError, str]
    id: int
    jsonrpc: Literal["2.0"]
    result: Any


Middleware = Callable[[Callable[[RPCEndpoint, Any], RPCResponse], "Web3"], Any]
MiddlewareOnion = NamedElementOnion[str, Middleware]


class FormattersDict(TypedDict, total=False):
    error_formatters: Formatters
    request_formatters: Formatters
    result_formatters: Formatters


class FilterParams(TypedDict, total=False):
    address: Union[Address, ChecksumAddress, List[Address], List[ChecksumAddress]]
    blockHash: HexBytes
    fromBlock: BlockIdentifier
    toBlock: BlockIdentifier
    topics: Sequence[Optional[Union[_Hash32, Sequence[_Hash32]]]]


class LogReceipt(TypedDict):
    address: ChecksumAddress
    blockHash: HexBytes
    blockNumber: BlockNumber
    data: HexStr
    logIndex: int
    payload: HexBytes
    removed: bool
    topic: HexBytes
    topics: Sequence[HexBytes]
    transactionHash: HexBytes
    transactionIndex: int


# syntax b/c "from" keyword not allowed w/ class construction
TxData = TypedDict("TxData", {
    "blockHash": HexBytes,
    "blockNumber": BlockNumber,
    "chainId": int,
    "data": Union[bytes, HexStr],
    "from": ChecksumAddress,
    "gas": Wei,
    "gasPrice": Wei,
    "hash": HexBytes,
    "input": HexStr,
    "nonce": Nonce,
    "r": HexBytes,
    "s": HexBytes,
    "to": ChecksumAddress,
    "transactionIndex": int,
    "v": int,
    "value": Wei,
}, total=False)


# syntax b/c "from" keyword not allowed w/ class construction
TxParams = TypedDict("TxParams", {
    "chainId": int,
    "data": Union[bytes, HexStr],
    # addr or ens
    "from": Union[Address, ChecksumAddress, str],
    "gas": Wei,
    "gasPrice": Wei,
    "nonce": Nonce,
    # addr or ens
    "to": Union[Address, ChecksumAddress, str],
    "value": Wei,
}, total=False)

GasPriceStrategy = Callable[["Web3", TxParams], Wei]


# syntax b/c "from" keyword not allowed w/ class construction
TxReceipt = TypedDict("TxReceipt", {
    "blockHash": HexBytes,
    "blockNumber": BlockNumber,
    "contractAddress": Optional[ChecksumAddress],
    "cumulativeGasUsed": int,
    "gasUsed": Wei,
    "from": ChecksumAddress,
    "logs": List[LogReceipt],
    "logsBloom": HexBytes,
    "root": HexStr,
    "status": int,
    "to": ChecksumAddress,
    "transactionHash": HexBytes,
    "transactionIndex": int,
})


class SignedTx(TypedDict, total=False):
    raw: bytes
    tx: TxParams


class StorageProof(TypedDict):
    key: HexStr
    proof: Sequence[HexStr]
    value: HexBytes


class MerkleProof(TypedDict):
    address: ChecksumAddress
    accountProof: Sequence[HexStr]
    balance: int
    codeHash: HexBytes
    nonce: Nonce
    storageHash: HexBytes
    storageProof: Sequence[StorageProof]


class Protocol(TypedDict):
    difficulty: int
    head: HexStr
    network: int
    version: int


class NodeInfo(TypedDict):
    enode: EnodeURI
    id: HexStr
    ip: str
    listenAddr: str
    name: str
    ports: Dict[str, int]
    protocols: Dict[str, Protocol]


class Peer(TypedDict, total=False):
    caps: Sequence[str]
    id: HexStr
    name: str
    network: Dict[str, str]
    protocols: Dict[str, Protocol]


class SyncStatus(TypedDict):
    currentBlock: int
    highestBlock: int
    knownStates: int
    pulledStates: int
    startingBlock: int


class BlockData(TypedDict, total=False):
    difficulty: int
    extraData: HexBytes
    gasLimit: Wei
    gasUsed: Wei
    hash: HexBytes
    logsBloom: HexBytes
    miner: ChecksumAddress
    mixHash: HexBytes
    nonce: HexBytes
    number: BlockNumber
    parentHash: HexBytes
    receiptRoot: HexBytes
    sha3Uncles: HexBytes
    size: int
    stateRoot: HexBytes
    timestamp: Timestamp
    totalDifficulty: int
    # list of tx hashes or of txdatas
    transactions: Union[Sequence[HexBytes], Sequence[TxData]]
    transactionsRoot: HexBytes
    uncles: Sequence[HexBytes]


class Uncle(TypedDict):
    author: ChecksumAddress
    difficulty: HexStr
    extraData: HexStr
    gasLimit: HexStr
    gasUsed: HexStr
    hash: HexBytes
    logsBloom: HexStr
    miner: HexBytes
    mixHash: HexBytes
    nonce: HexStr
    number: HexStr
    parentHash: HexBytes
    receiptsRoot: HexBytes
    sealFields: Sequence[HexStr]
    sha3Uncles: HexBytes
    size: int
    stateRoot: HexBytes
    timestamp: Timestamp
    totalDifficulty: HexStr
    transactions: Sequence[HexBytes]
    transactionsRoot: HexBytes
    uncles: Sequence[HexBytes]


#
# shh
#

ShhID = NewType("ShhID", HexStr)
ShhFilterID = NewType("ShhFilterID", HexStr)
ShhSubscriptionID = NewType("ShhSubscriptionID", HexStr)


# syntax b/c "from" keyword not allowed w/ class construction
ShhMessageFilter = TypedDict("ShhMessageFilter", {
    "allowP2P": bool,
    "decryptWith": ShhID,
    "from": HexStr,
    "minPoW": float,
    "privateKeyID": ShhID,
    "sig": str,
    "symKeyID": ShhID,
    "topics": List[HexStr],
}, total=False)


# syntax b/c "from" keyword not allowed w/ class construction
ShhMessage = TypedDict("ShhMessage", {
    "from": bytes,
    "hash": HexBytes,
    "padding": HexBytes,
    "payload": HexBytes,
    "pow": float,
    "recipient": bytes,
    "recipientPublicKey": ShhID,
    "timestamp": int,
    "topic": HexBytes,
    "ttl": int,
}, total=False)


# syntax b/c "from" keyword not allowed w/ class construction
ShhMessageParams = TypedDict("ShhMessageParams", {
    "from": ShhID,
    "padding": str,
    "payload": str,
    "powTarget": float,
    "powTime": int,
    "priority": int,
    "pubKey": HexStr,
    "sig": str,
    "symKeyID": ShhID,
    "targetPeer": ShhID,
    "to": Dict[str, HexStr],
    "topic": HexStr,
    "topics": List[HexStr],
    "ttl": int,
}, total=False)


class ShhStats(TypedDict, total=False):
    maxMessageSize: int
    memory: int
    messages: int
    minPow: float
    targetMemory: int


#
# txpool types
#

# syntax b/c "from" keyword not allowed w/ class construction
PendingTx = TypedDict("PendingTx", {
    "blockHash": HexBytes,
    "blockNumber": None,
    "from": ChecksumAddress,
    "gas": HexBytes,
    "gasPrice": HexBytes,
    "hash": HexBytes,
    "input": HexBytes,
    "nonce": HexBytes,
    "to": ChecksumAddress,
    "transactionIndex": None,
    "value": HexBytes,
}, total=False)


class TxPoolContent(TypedDict, total=False):
    pending: Dict[ChecksumAddress, Dict[Nonce, List[PendingTx]]]
    queued: Dict[ChecksumAddress, Dict[Nonce, List[PendingTx]]]


class TxPoolInspect(TypedDict, total=False):
    pending: Dict[ChecksumAddress, Dict[Nonce, str]]
    queued: Dict[ChecksumAddress, Dict[Nonce, str]]


class TxPoolStatus(TypedDict, total=False):
    pending: int
    queued: int


#
# web3.geth types
#


class GethWallet(TypedDict):
    accounts: Sequence[Dict[str, str]]
    status: str
    url: str


#
# web3.parity types
#

ParityBlockTrace = NewType("ParityBlockTrace", Dict[str, Any])
ParityFilterTrace = NewType("ParityFilterTrace", Dict[str, Any])
ParityMode = Literal["active", "passive", "dark", "offline"]
ParityTraceMode = Sequence[Literal["trace", "vmTrace", "stateDiff"]]


class ParityNetPeers(TypedDict):
    active: int
    connected: int
    max: int
    peers: List[Dict[Any, Any]]


class ParityFilterParams(TypedDict, total=False):
    after: int
    count: int
    fromAddress: Sequence[Union[Address, ChecksumAddress, ENS]]
    fromBlock: BlockIdentifier
    toAddress: Sequence[Union[Address, ChecksumAddress, ENS]]
    toBlock: BlockIdentifier
