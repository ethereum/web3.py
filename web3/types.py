from typing import (
    Any,
    Callable,
    Dict,
    List,
    NewType,
    Optional,
    Sequence,
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
from web3.datastructures import (
    NamedElementOnion,
)

Wei = NewType('Wei', int)
TReturn = TypeVar("TReturn")
TParams = TypeVar("TParams")
TValue = TypeVar("TValue")

Nonce = NewType("Nonce", int)

HexBytes32 = NewType("HexBytes32", HexBytes)
HexStr32 = NewType("HexStr32", HexStr)

_Hash32 = Union[Hash32, HexBytes, HexStr]

# todo: move these to eth_typing once web3 is type hinted
ABIEventParams = TypedDict("ABIEventParams", {
    "name": str,
    "type": str,
    "indexed": bool,
}, total=False)


ABIEvent = TypedDict("ABIEvent", {
    "type": Literal["event"],
    "name": str,
    "inputs": Sequence["ABIEventParams"],
    "anonymous": bool,
}, total=False)


ABIFunctionComponents = TypedDict("ABIFunctionComponents", {
    "name": str,
    "type": str,
    "components": Sequence[Any],
}, total=False)


ABIFunctionParams = TypedDict("ABIFunctionParams", {
    "name": str,
    "type": str,
    "components": Sequence["ABIFunctionComponents"],
}, total=False)


ABIFunction = TypedDict("ABIFunction", {
    "type": Literal["function", "constructor", "fallback"],
    "name": str,
    "inputs": Sequence["ABIFunctionParams"],
    "outputs": Sequence["ABIFunctionParams"],
    "stateMutability": Literal["pure", "view", "nonpayable", "payable"],
    "payable": bool,
    "constant": bool,
}, total=False)


ABIElement = Union[ABIFunction, ABIEvent]


ABI = Sequence[Union[ABIFunction, ABIEvent]]


LatestBlockParam = Literal["latest"]


BlockParams = Literal["latest", "earliest", "pending"]


BlockIdentifier = Union[BlockParams, BlockNumber, Hash32, HexStr, HexBytes]


ENS = NewType("ENS", str)


EnodeURI = NewType("EnodeURI", str)


EventData = TypedDict("EventData", {
    "args": Dict[str, Any],
    "event": str,
    "logIndex": int,
    "transactionIndex": int,
    "transactionHash": HexBytes,
    "address": ChecksumAddress,
    "blockHash": HexBytes,
    "blockNumber": int,
})


RPCError = TypedDict("RPCError", {
    "code": int,
    "message": str,
})


RPCResponse = TypedDict("RPCResponse", {
    "id": int,
    "jsonrpc": Literal["2.0"],
    "result": Any,
    "error": Union[RPCError, str],
}, total=False)


RPCEndpoint = NewType("RPCEndpoint", str)


Formatters = Dict[RPCEndpoint, Callable[..., Any]]


FormattersDict = TypedDict("FormattersDict", {
    "request_formatters": Formatters,
    "result_formatters": Formatters,
    "error_formatters": Formatters,
}, total=False)


FilterParams = TypedDict("FilterParams", {
    "fromBlock": BlockIdentifier,
    "toBlock": BlockIdentifier,
    "blockHash": HexBytes,
    "address": Union[Address, ChecksumAddress, List[ChecksumAddress]],
    "topics": Sequence[Optional[Union[_Hash32, Sequence[_Hash32]]]],
}, total=False)

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
    "nonce": int,
    "r": HexBytes,
    "s": HexBytes,
    "to": ChecksumAddress,
    "transactionIndex": int,
    "v": int,
    "value": Wei,
}, total=False)


TxParams = TypedDict("TxParams", {
    "nonce": Nonce,
    "chainId": int,
    "gasPrice": Wei,
    "gas": Wei,
    # addr or ens
    "from": Union[Address, ChecksumAddress, str],
    "to": Union[Address, ChecksumAddress, str],
    "value": Wei,
    "data": Union[bytes, HexStr],
}, total=False)

SignedTx = TypedDict("SignedTx", {
    "raw": bytes,
    "tx": TxParams,
}, total=False)

# this Any should be updated to Web3 once all type hints land
GasPriceStrategy = Callable[[Any, TxParams], Wei]
# 2 input to parent callable Any should be updated to Web3 once all type hints land
Middleware = Callable[[Callable[[RPCEndpoint, Any], RPCResponse], Any], Any]
MiddlewareOnion = NamedElementOnion[str, Middleware]


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


StorageProof = TypedDict("StorageProof", {
    'key': HexStr,
    'value': HexBytes,
    'proof': Sequence[HexStr],
})


MerkleProof = TypedDict("MerkleProof", {
    'address': ChecksumAddress,
    'accountProof': Sequence[HexStr],
    'balance': int,
    'codeHash': HexBytes,
    'nonce': int,
    'storageHash': HexBytes,
    'storageProof': Sequence[StorageProof],
})


Protocol = TypedDict("Protocol", {
    "difficulty": int,
    "head": HexStr,
    "network": int,
    "version": int,
})

NodeInfo = TypedDict("NodeInfo", {
    'enode': EnodeURI,
    'id': HexStr,
    'ip': str,
    'listenAddr': str,
    'name': str,
    'ports': Dict[str, int],
    'protocols': Dict[str, Protocol],
})


Peer = TypedDict("Peer", {
    'caps': Sequence[str],
    'id': HexStr,
    'name': str,
    'network': Dict[str, str],
    'protocols': Dict[str, Protocol],
}, total=False)


SyncStatus = TypedDict("SyncStatus", {
    'currentBlock': int,
    'highestBlock': int,
    'knownStates': int,
    'pulledStates': int,
    'startingBlock': int,
})


Timestamp = NewType("Timestamp", int)


TxReceipt = TypedDict("TxReceipt", {
    "blockHash": HexBytes,
    "blockNumber": int,
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


BlockData = TypedDict("BlockData", {
    'difficulty': int,
    'extraData': HexBytes,
    'gasLimit': Wei,
    'gasUsed': Wei,
    'hash': HexBytes,
    'logsBloom': HexBytes,
    'miner': ChecksumAddress,
    'mixHash': HexBytes,
    'nonce': HexBytes,
    'number': BlockNumber,
    'parentHash': HexBytes,
    'receiptRoot': HexBytes,
    'sha3Uncles': HexBytes,
    'size': int,
    'stateRoot': HexBytes,
    'timestamp': Timestamp,
    'totalDifficulty': int,
    # list of tx hashes or of txdatas
    'transactions': Union[Sequence[HexBytes], Sequence[TxData]],
    'transactionsRoot': HexBytes,
    'uncles': Sequence[HexBytes],
}, total=False)


Uncle = TypedDict("Uncle", {
    'author': ChecksumAddress,
    'difficulty': HexStr,
    'extraData': HexStr,
    'gasLimit': HexStr,
    'gasUsed': HexStr,
    'hash': HexBytes,
    'logsBloom': HexStr,
    'miner': HexBytes,
    'mixHash': HexBytes,
    'nonce': HexStr,
    'number': HexStr,
    'parentHash': HexBytes,
    'receiptsRoot': HexBytes,
    'sealFields': Sequence[HexStr],
    'sha3Uncles': HexBytes,
    'size': int,
    'stateRoot': HexBytes,
    'timestamp': Timestamp,
    'totalDifficulty': HexStr,
    'transactions': Sequence[HexBytes],
    'transactionsRoot': HexBytes,
    'uncles': Sequence[HexBytes]
})

# shh

ShhID = NewType("ShhID", HexStr)
ShhFilterID = NewType("ShhFilterID", HexStr)
ShhSubscriptionID = NewType("ShhSubscriptionID", HexStr)

ShhMessageFilter = TypedDict("ShhMessageFilter", {
    "symKeyID": ShhID,
    "decryptWith": ShhID,
    "from": HexStr,
    "privateKeyID": ShhID,
    "sig": str,
    "minPoW": float,
    "topics": List[HexStr],
    "allowP2P": bool,
}, total=False)


ShhMessage = TypedDict("ShhMessage", {
    "from": bytes,
    "hash": HexBytes,
    "recipient": bytes,
    "ttl": int,
    "topic": HexBytes,
    "timestamp": int,
    "payload": HexBytes,
    "padding": HexBytes,
    "pow": float,
    "recipientPublicKey": ShhID,
}, total=False)


ShhMessageParams = TypedDict("ShhMessageParams", {
    "symKeyID": ShhID,
    "from": ShhID,
    "to": Dict[str, HexStr],
    "pubKey": HexStr,
    "ttl": int,
    "sig": str,
    "topics": List[HexStr],
    "topic": HexStr,
    "payload": str,
    "padding": str,
    "powTime": int,
    "powTarget": float,
    "priority": int,
    "targetPeer": ShhID,
}, total=False)

ShhStats = TypedDict("ShhStats", {
    "maxMessageSize": int,
    "memory": int,
    "messages": int,
    "minPow": float,
    "targetMemory": int,
}, total=False)

# txpool types
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


TxPoolContent = TypedDict("TxPoolContent", {
    "pending": Dict[ChecksumAddress, Dict[Nonce, List[PendingTx]]],
    "queued": Dict[ChecksumAddress, Dict[Nonce, List[PendingTx]]],
}, total=False)


TxPoolInspect = TypedDict("TxPoolInspect", {
    "pending": Dict[ChecksumAddress, Dict[Nonce, str]],
    "queued": Dict[ChecksumAddress, Dict[Nonce, str]],
}, total=False)


TxPoolStatus = TypedDict("TxPoolStatus", {
    "pending": int,
    "queued": int,
}, total=False)


# web3.parity types
ParityBlockTrace = NewType("ParityBlockTrace", Dict[str, Any])
ParityFilterTrace = NewType("ParityFilterTrace", Dict[str, Any])
ParityMode = Literal["active", "passive", "dark", "offline"]
ParityTraceMode = Sequence[Literal["trace", "vmTrace", "stateDiff"]]
ParityNetPeers = TypedDict("ParityNetPeers", {
    "active": int,
    "connected": int,
    "max": int,
    "peers": List[Dict[Any, Any]],
})
ParityFilterParams = TypedDict("ParityFilterParams", {
    "fromBlock": BlockIdentifier,
    "toBlock": BlockIdentifier,
    "fromAddress": Sequence[Union[Address, ChecksumAddress, ENS]],
    "toAddress": Sequence[Union[Address, ChecksumAddress, ENS]],
    "after": int,
    "count": int,
}, total=False)
