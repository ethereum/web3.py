from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
)

from eth_utils.toolz import (
    assoc,
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
            if 'gasPrice' not in transaction:
                generated_gas_price = web3.eth.generate_gas_price(transaction)
                if generated_gas_price is not None:
                    transaction = assoc(transaction, 'gasPrice', generated_gas_price)
                    return make_request(method, [transaction])
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
