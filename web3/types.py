from typing import (
    Any,
    Callable,
    Dict,
    List,
    NewType,
    Optional,
    Sequence,
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
from typing_extensions import (
    Literal,
)

from web3._utils.compat import (
    TypedDict,
)

Wei = NewType('Wei', int)


# todo: move these to eth_typing once web3 is type hinted
ABIEventParams = TypedDict("ABIEventParams", {
    "name": str,
    "type": str,
    "indexed": bool,
})

ENS = NewType("ENS", str)

ABIEvent = TypedDict("ABIEvent", {
    "type": "event",
    "name": str,
    "inputs": Sequence[ABIEventParams],
    "anonymous": bool,
})


ABIFunctionComponents = TypedDict("ABIFunctionParams", {
    "name": str,
    "type": str,
    "components": Sequence["ABIFunctionComponents"],
}, total=False)


ABIFunctionParams = TypedDict("ABIFunctionParams", {
    "name": str,
    "type": str,
    "components": Sequence[ABIFunctionComponents],
}, total=False)


ABIFunction = TypedDict("ABIFunction", {
    "type": Union["function", "constructor", "fallback"],
    "name": str,
    "inputs": Sequence[ABIFunctionParams],
    "outputs": Sequence[ABIFunctionParams],
    "stateMutability": Union["pure", "view", "nonpayable", "payable"],
    "payable": bool,
    "constant": bool,
}, total=False)


ABI = Sequence[Union[ABIFunction, ABIEvent]]


BlockParams = Literal["latest", "earliest", "pending"]

BlockIdentifier = Union[BlockParams, BlockNumber, Hash32, HexStr]


ENS = NewType("ENS", str)


EventData = TypedDict("EventData", {
    "args": Dict[str, Any],
    "event": str,
    "logIndex": int,
    "transactionIndex": int,
    "transactionHash": Hash32,
    "address": ChecksumAddress,
    "blockHash": Hash32,
    "blockNumber": int,
})

JsonRpcResponse = Dict[str, Any]

Middleware = Callable[[Any, Any], Any]

JsonRpcError = TypedDict("JsonRpcError", {
    "code": int,
    "message": str,
})


JsonRpcResponse = TypedDict("JsonRpcResponse", {
    "id": int,
    "jsonrpc": Literal["2.0"],
    "result": Any,
    "error": JsonRpcError,
}, total=False)


FilterParams = TypedDict("FilterParams", {
    "from": Union["earliest", "pending", "latest", BlockNumber],
    "to": Union["earliest", "pending", "latest", BlockNumber],
    "address": Union[Address, ChecksumAddress, List[Union[Address, ChecksumAddress]]],
    "topics": List[Optional[Union[Hash32, List[Hash32]]]],
}, total=False)


TxParams = TypedDict("TxParams", {
    "nonce": int,
    "gasPrice": int,
    "gas": int,
    "from": Union[Address, ChecksumAddress, str],
    "to": Union[Address, ChecksumAddress, str],
    "value": int,
    "data": Union[bytes, str],
}, total=False)


# this Any should be updated to Web3 once all type hints land
GasPriceStrategy = Callable[[Any, TxParams], Wei]


LogParams = TypedDict("LogParams", {
    "address": ChecksumAddress,
    "blockHash": Hash32,
    "blockNumber": int,
    "data": HexStr,
    "logIndex": int,
    "removed": bool,
    "topics": List[Hash32],
    "transactionHash": Hash32,
    "transactionIndex": int,
})


StorageProof = TypedDict("StorageProof", {
    'key': HexStr,
    'value': Hash32,
    'proof': Sequence[HexStr],
})


MerkleProof = TypedDict("MerkleProof", {
    'address': ChecksumAddress,
    'accountProof': Sequence[HexStr],
    'balance': int,
    'codeHash': Hash32,
    'nonce': int,
    'storageHash': Hash32,
    'storageProof': Sequence[StorageProof],
})


SyncStatus = TypedDict("SyncStatus", {
    'currentBlock': int,
    'highestBlock': int,
    'knownStates': int,
    'pulledStates': int,
    'startingBlock': int,
})


Timestamp = NewType("Timestamp", int)


TxReceipt = TypedDict("TxReceipt", {
    "blockHash": Hash32,
    "blockNumber": int,
    "contractAddress": Optional[ChecksumAddress],
    "cumulativeGasUsed": int,
    "gasUsed": int,
    "from": ChecksumAddress,
    "logs": List[LogParams],
    "logsBloom": HexBytes,
    "root": HexStr,
    "status": int,
    "to": ChecksumAddress,
    "transactionHash": Hash32,
    "transactionIndex": int,
})


BlockData = TypedDict("BlockData", {
    'difficulty': int,
    'extraData': HexStr,
    'gasLimit': int,
    'gasUsed': int,
    'hash': Hash32,
    'logsBloom': HexStr,
    'miner': ChecksumAddress,
    'nonce': HexStr,
    'number': int,
    'parentHash': Hash32,
    'receiptRoot': Hash32,
    'sha3Uncles': Hash32,
    'size': int,
    'stateRoot': Hash32,
    'timestamp': Timestamp,
    'totalDifficulty': int,
    'transactions': Union[Sequence[Hash32], Sequence[TxReceipt]],
    'transactionsRoot': Hash32,
    'uncles': Sequence[Hash32],
})


Uncle = TypedDict("Uncle", {
    'author': ChecksumAddress,
    'difficulty': HexStr,
    'extraData': HexStr,
    'gasLimit': HexStr,
    'gasUsed': HexStr,
    'hash': Hash32,
    'logsBloom': HexStr,
    'miner': Hash32,
    'mixHash': Hash32,
    'nonce': HexStr,
    'number': HexStr,
    'parentHash': Hash32,
    'receiptsRoot': Hash32,
    'sealFields': Sequence[HexStr],
    'sha3Uncles': Hash32,
    'size': int,
    'stateRoot': Hash32,
    'timestamp': Timestamp,
    'totalDifficulty': HexStr,
    'transactions': Sequence[Hash32],
    'transactionsRoot': Hash32,
    'uncles': Sequence[Hash32]
})


# web3.parity types
ParityBlockTrace = NewType("ParityBlockTrace", Dict[str, Any])
ParityFilterTrace = NewType("ParityFilterTrace", Dict[str, Any])
ParityEnodeURI = NewType("ParityEnodeURI", str)
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
