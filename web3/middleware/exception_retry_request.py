from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Type,
)

from requests.exceptions import (
    ConnectionError,
    HTTPError,
    Timeout,
    TooManyRedirects,
)

from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401

whitelist = [
    "admin",
    "miner",
    "net",
    "txpool",
    "testing",
    "evm",
    "eth_protocolVersion",
    "eth_syncing",
    "eth_coinbase",
    "eth_mining",
    "eth_hashrate",
    "eth_chainId",
    "eth_gasPrice",
    "eth_accounts",
    "eth_blockNumber",
    "eth_getBalance",
    "eth_getStorageAt",
    "eth_getProof",
    "eth_getCode",
    "eth_getBlockByNumber",
    "eth_getBlockByHash",
    "eth_getBlockTransactionCountByNumber",
    "eth_getBlockTransactionCountByHash",
    "eth_getUncleCountByBlockNumber",
    "eth_getUncleCountByBlockHash",
    "eth_getTransactionByHash",
    "eth_getTransactionByBlockHashAndIndex",
    "eth_getTransactionByBlockNumberAndIndex",
    "eth_getTransactionReceipt",
    "eth_getTransactionCount",
    "eth_getRawTransactionByHash",
    "eth_call",
    "eth_estimateGas",
    "eth_newBlockFilter",
    "eth_newPendingTransactionFilter",
    "eth_newFilter",
    "eth_getFilterChanges",
    "eth_getFilterLogs",
    "eth_getLogs",
    "eth_uninstallFilter",
    "eth_getCompilers",
    "eth_getWork",
    "eth_sign",
    "eth_signTypedData",
    "eth_sendRawTransaction",
    "personal_importRawKey",
    "personal_newAccount",
    "personal_listAccounts",
    "personal_listWallets",
    "personal_lockAccount",
    "personal_unlockAccount",
    "personal_ecRecover",
    "personal_sign",
    "personal_signTypedData",
]


def check_if_retry_on_failure(method: RPCEndpoint) -> bool:
    root = method.split("_")[0]
    if root in whitelist:
        return True
    elif method in whitelist:
        return True
    else:
        return False


def exception_retry_middleware(
    make_request: Callable[[RPCEndpoint, Any], RPCResponse],
    w3: "Web3",
    errors: Collection[Type[BaseException]],
    retries: int = 5,
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    """
    Creates middleware that retries failed HTTP requests. Is a default
    middleware for HTTPProvider.
    """

    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if check_if_retry_on_failure(method):
            for i in range(retries):
                try:
                    return make_request(method, params)
                # https://github.com/python/mypy/issues/5349
                except errors:  # type: ignore
                    if i < retries - 1:
                        continue
                    else:
                        raise
            return None
        else:
            return make_request(method, params)

    return middleware


def http_retry_request_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], w3: "Web3"
) -> Callable[[RPCEndpoint, Any], Any]:
    return exception_retry_middleware(
        make_request, w3, (ConnectionError, HTTPError, Timeout, TooManyRedirects)
    )
