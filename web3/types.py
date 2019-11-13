from typing import (
    Any,
    Dict,
    List,
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

from web3._utils.compat import (
    TypedDict,
)

# todo: move these to eth_typing once web3 is type hinted


ABIEventParameter = TypedDict("ABIEventParameter", {
    "name": str,
    "type": str,
    "indexed": bool,
})


ABIEvent = TypedDict("ABIEvent", {
    "type": "event",
    "name": str,
    "inputs": Sequence[ABIEventParameter],
    "anonymous": bool,
})


ABIFunctionComponents = TypedDict("ABIFunctionParameter", {
    "name": str,
    "type": str,
    "components": Optional[Sequence["ABIFunctionComponents"]],
})


ABIFunctionParameter = TypedDict("ABIFunctionParameter", {
    "name": str,
    "type": str,
    "components": Optional[Sequence[ABIFunctionComponents]],
})


# should we get more granular and define constructor / fallback individually?
ABIFunction = TypedDict("ABIFunction", {
    "type": Union["function", "constructor", "fallback"],
    "name": str,
    "inputs": Sequence[ABIFunctionParameter],
    "outputs": Optional[Sequence[ABIFunctionParameter]],
    "stateMutability": Union["pure", "view", "nonpayable", "payable"],
    "payable": bool,
    "constant": bool,
})


ABI = Sequence[Union[ABIFunction, ABIEvent]]

BlockIdentifier = Union[str, BlockNumber, Hash32]

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


TxDict = TypedDict("TxDict", {
    "nonce": int,
    "gasPrice": int,
    "gas": int,
    "from": Union[Address, ChecksumAddress, str],
    "to": Union[Address, ChecksumAddress, str],
    "value": int,
    "data": Union[bytes, str]},
    total=False
)


LogsParameter = TypedDict("LogsParameter", {
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


TxReceipt = TypedDict("TxReceipt", {
    "blockHash": Hash32,
    "blockNumber": int,
    "contractAddress": Optional[ChecksumAddress],
    "cumulativeGasUsed": int,
    "from": ChecksumAddress,
    "gasUsed": int,
    "logs": List[LogsParameter],
    "logsBloom": HexBytes,
    "root": HexStr,
    "status": int,
    "to": ChecksumAddress,
    "transactionHash": Hash32,
    "transactionIndex": int
})
