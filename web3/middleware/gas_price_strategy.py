from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
)

from eth_utils.toolz import (
    assoc,
)

from web3.exceptions import (
    InvalidTransaction,
    TransactionTypeMismatch,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def gas_price_strategy_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], web3: "Web3"
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    """
    Includes a gas price using the gas price strategy
    """
    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method == 'eth_sendTransaction':
            transaction = params[0]

            # legacy and 1559 tx variables used:
            if "gasPrice" in transaction and (
                "maxFeePerGas" in transaction or "maxPriorityFeePerGas" in transaction
            ):
                raise TransactionTypeMismatch()
            # 1559 - canonical tx:
            elif 'maxFeePerGas' in transaction and 'maxPriorityFeePerGas' in transaction:
                if int(transaction["maxFeePerGas"], 16) < int(
                    transaction["maxPriorityFeePerGas"], 16
                ):
                    raise InvalidTransaction("maxFeePerGas must be >= maxPriorityFeePerGas")
            # 1559 - no max fee:
            elif 'maxFeePerGas' not in transaction and 'maxPriorityFeePerGas' in transaction:
                try:
                    block = web3.eth.get_block('latest')
                    base_fee = block['baseFeePerGas']
                    priority_fee = int(transaction['maxPriorityFeePerGas'], 16)
                    max_fee_per_gas = priority_fee + 2 * base_fee
                    transaction = assoc(transaction, 'maxFeePerGas', hex(max_fee_per_gas))
                    return make_request(method, [transaction])
                except Exception:
                    # If unable to calculate maxFeePerGas, allow the client to decide
                    pass
            # 1559 - no priority fee:
            elif 'maxFeePerGas' in transaction and 'maxPriorityFeePerGas' not in transaction:
                raise InvalidTransaction(
                    "maxPriorityFeePerGas must be defined in a 1559 transaction."
                )
            else:
                # fully formed (legacy or 1559) tx or no fee values specified
                pass
        return make_request(method, params)
    return middleware


async def async_gas_price_strategy_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], web3: "Web3"
) -> Callable[[RPCEndpoint, Any], Coroutine[Any, Any, RPCResponse]]:
    """
    Includes a gas price using the gas price strategy
    """
    async def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method == 'eth_sendTransaction':
            transaction = params[0]
            if 'gasPrice' not in transaction:
                generated_gas_price = await web3.eth.generate_gas_price(transaction)  # type: ignore
                if generated_gas_price is not None:
                    transaction = assoc(transaction, 'gasPrice', hex(generated_gas_price))
                    return await make_request(method, [transaction])
        return await make_request(method, params)
    return middleware
