from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
)

from eth_utils.toolz import (
    assoc,
)

from web3._utils.method_formatters import (
    to_hex_if_integer,
)
from web3._utils.utility_methods import (
    all_in_dict,
    any_in_dict,
    none_in_dict,
)
from web3.constants import (
    DYNAMIC_FEE_TXN_PARAMS,
)
from web3.exceptions import (
    InvalidTransaction,
    TransactionTypeMismatch,
)
from web3.types import (
    AsyncMiddlewareCoroutine,
    BlockData,
    RPCEndpoint,
    RPCResponse,
    TxParams,
    Wei,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )


def validate_transaction_params(
    transaction: TxParams, latest_block: BlockData, strategy_based_gas_price: Wei
) -> TxParams:
    # gas price strategy explicitly set:
    if (
        strategy_based_gas_price is not None
        and "gasPrice" not in transaction
        and none_in_dict(DYNAMIC_FEE_TXN_PARAMS, transaction)
    ):
        transaction = assoc(
            transaction, "gasPrice", to_hex_if_integer(strategy_based_gas_price)
        )

    # legacy and dynamic fee tx variables used:
    if "gasPrice" in transaction and any_in_dict(DYNAMIC_FEE_TXN_PARAMS, transaction):
        raise TransactionTypeMismatch()
    # dynamic fee transaction - canonical case:
    elif all_in_dict(DYNAMIC_FEE_TXN_PARAMS, transaction):
        if int(str(transaction["maxFeePerGas"]), 16) < int(
            str(transaction["maxPriorityFeePerGas"]), 16
        ):
            raise InvalidTransaction("maxFeePerGas must be >= maxPriorityFeePerGas")
    # dynamic fee txn - no max fee:
    elif "maxFeePerGas" not in transaction and "maxPriorityFeePerGas" in transaction:
        base_fee = latest_block["baseFeePerGas"]
        priority_fee = int(str(transaction["maxPriorityFeePerGas"]), 16)
        max_fee_per_gas = priority_fee + 2 * base_fee
        transaction = assoc(transaction, "maxFeePerGas", hex(max_fee_per_gas))
    # dynamic fee transaction - no priority fee:
    elif "maxFeePerGas" in transaction and "maxPriorityFeePerGas" not in transaction:
        raise InvalidTransaction(
            "maxPriorityFeePerGas must be defined in a 1559 transaction."
        )

    # should be a fully formed (legacy or dynamic fee) tx
    # or no fee values were specified
    return transaction


def gas_price_strategy_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], w3: "Web3"
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    """
    - Uses a gas price strategy if one is set. This is only supported
      for legacy transactions. It is recommended to send dynamic fee
      transactions (EIP-1559) whenever possible.

    - Validates transaction params against legacy and dynamic fee txn values.
    """

    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method == "eth_sendTransaction":
            transaction = params[0]
            generated_gas_price = w3.eth.generate_gas_price(transaction)
            latest_block = w3.eth.get_block("latest")
            transaction = validate_transaction_params(
                transaction, latest_block, generated_gas_price
            )
            return make_request(method, (transaction,))
        return make_request(method, params)

    return middleware


async def async_gas_price_strategy_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], async_w3: "AsyncWeb3"
) -> AsyncMiddlewareCoroutine:
    """
    - Uses a gas price strategy if one is set. This is only supported for
      legacy transactions. It is recommended to send dynamic fee transactions
      (EIP-1559) whenever possible.

    - Validates transaction params against legacy and dynamic fee txn values.
    """

    async def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method == "eth_sendTransaction":
            transaction = params[0]
            generated_gas_price = async_w3.eth.generate_gas_price(transaction)
            latest_block = await async_w3.eth.get_block("latest")
            transaction = validate_transaction_params(
                transaction, latest_block, generated_gas_price
            )
            return await make_request(method, (transaction,))
        return await make_request(method, params)

    return middleware
