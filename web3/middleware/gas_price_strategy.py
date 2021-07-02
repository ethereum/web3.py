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
    BlockData,
    RPCEndpoint,
    RPCResponse,
    TxParams,
    Wei,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def validate_transaction_params(
    transaction: TxParams, latest_block: BlockData, generated_gas_price: Wei
) -> TxParams:
    # gas price strategy explicitly set:
    if generated_gas_price is not None and 'gasPrice' not in transaction:
        transaction = assoc(transaction, 'gasPrice', hex(generated_gas_price))

    # legacy and 1559 tx variables used:
    if "gasPrice" in transaction and (
        "maxFeePerGas" in transaction or "maxPriorityFeePerGas" in transaction
    ):
        raise TransactionTypeMismatch()
    # 1559 - canonical tx:
    elif 'maxFeePerGas' in transaction and 'maxPriorityFeePerGas' in transaction:
        if int(str(transaction["maxFeePerGas"]), 16) < int(
            str(transaction["maxPriorityFeePerGas"]), 16
        ):
            raise InvalidTransaction("maxFeePerGas must be >= maxPriorityFeePerGas")
    # 1559 - no max fee:
    elif 'maxFeePerGas' not in transaction and 'maxPriorityFeePerGas' in transaction:
        base_fee = latest_block['baseFeePerGas']
        priority_fee = int(str(transaction['maxPriorityFeePerGas']), 16)
        max_fee_per_gas = priority_fee + 2 * base_fee
        transaction = assoc(transaction, 'maxFeePerGas', hex(max_fee_per_gas))
    # 1559 - no priority fee:
    elif 'maxFeePerGas' in transaction and 'maxPriorityFeePerGas' not in transaction:
        raise InvalidTransaction(
            "maxPriorityFeePerGas must be defined in a 1559 transaction."
        )

    # should be a fully formed (legacy or 1559) tx or no fee values were specified
    return transaction


def gas_price_strategy_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], web3: "Web3"
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    """
    - Uses a gas price strategy if one is set. This is only supported for legacy transactions.
      It is recommended to send 1559 transactions whenever possible.

    - Validates transaction params against legacy and 1559 values.
    """
    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method == 'eth_sendTransaction':
            transaction = params[0]
            generated_gas_price = web3.eth.generate_gas_price(transaction)
            latest_block = web3.eth.get_block('latest')
            transaction = validate_transaction_params(
                transaction, latest_block, generated_gas_price
            )
            return make_request(method, (transaction,))
        return make_request(method, params)

    return middleware


async def async_gas_price_strategy_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], web3: "Web3"
) -> Callable[[RPCEndpoint, Any], Coroutine[Any, Any, RPCResponse]]:
    """
    - Uses a gas price strategy if one is set. This is only supported for legacy transactions.
      It is recommended to send 1559 transactions whenever possible.

    - Validates transaction params against legacy and 1559 values.
    """
    async def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method == 'eth_sendTransaction':
            transaction = params[0]
            generated_gas_price = await web3.eth.generate_gas_price(transaction)  # type: ignore
            latest_block = await web3.eth.get_block('latest')  # type: ignore
            transaction = validate_transaction_params(
                transaction, latest_block, generated_gas_price
            )
            return await make_request(method, (transaction,))
        return await make_request(method, params)

    return middleware
