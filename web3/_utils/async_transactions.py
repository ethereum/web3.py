from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Optional,
    cast,
)

from eth_abi import (
    abi,
)
from eth_typing import (
    URI,
)
from eth_utils.toolz import (
    curry,
    merge,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.request import (
    async_get_json_from_client_response,
    async_get_response_from_get_request,
    async_get_response_from_post_request,
)
from web3._utils.transactions import (
    prepare_replacement_transaction,
)
from web3._utils.type_conversion import (
    to_bytes_if_hex,
    to_hex_if_bytes,
)
from web3._utils.utility_methods import (
    any_in_dict,
)
from web3.constants import (
    DYNAMIC_FEE_TXN_PARAMS,
)
from web3.exceptions import (
    Web3ValidationError,
)
from web3.types import (
    BlockIdentifier,
    TxData,
    TxParams,
    Wei,
    _Hash32,
)

if TYPE_CHECKING:
    from web3.eth import AsyncEth  # noqa: F401
    from web3.main import (  # noqa: F401
        AsyncWeb3,
    )


async def _estimate_gas(async_w3: "AsyncWeb3", tx: TxParams) -> int:
    return await async_w3.eth.estimate_gas(tx)


async def _max_fee_per_gas(async_w3: "AsyncWeb3", _tx: TxParams) -> Wei:
    block = await async_w3.eth.get_block("latest")
    max_priority_fee = await async_w3.eth.max_priority_fee
    return Wei(max_priority_fee + (2 * block["baseFeePerGas"]))


async def _max_priority_fee_gas(async_w3: "AsyncWeb3", _tx: TxParams) -> Wei:
    return await async_w3.eth.max_priority_fee


async def _chain_id(async_w3: "AsyncWeb3", _tx: TxParams) -> int:
    return await async_w3.eth.chain_id


TRANSACTION_DEFAULTS = {
    "value": 0,
    "data": b"",
    "gas": _estimate_gas,
    "gasPrice": lambda w3, tx: w3.eth.generate_gas_price(tx),
    "maxFeePerGas": _max_fee_per_gas,
    "maxPriorityFeePerGas": _max_priority_fee_gas,
    "chainId": _chain_id,
}


async def get_block_gas_limit(
    web3_eth: "AsyncEth", block_identifier: Optional[BlockIdentifier] = None
) -> int:
    if block_identifier is None:
        block_identifier = await web3_eth.block_number
    block = await web3_eth.get_block(block_identifier)
    return block["gasLimit"]


async def get_buffered_gas_estimate(
    async_w3: "AsyncWeb3", transaction: TxParams, gas_buffer: int = 100000
) -> int:
    gas_estimate_transaction = cast(TxParams, dict(**transaction))

    gas_estimate = await async_w3.eth.estimate_gas(gas_estimate_transaction)

    gas_limit = await get_block_gas_limit(async_w3.eth)

    if gas_estimate > gas_limit:
        raise ValueError(
            "Contract does not appear to be deployable within the "
            f"current network gas limits.  Estimated: {gas_estimate}. "
            f"Current gas limit: {gas_limit}"
        )

    return min(gas_limit, gas_estimate + gas_buffer)


@curry
async def fill_transaction_defaults(
    async_w3: "AsyncWeb3", transaction: TxParams
) -> TxParams:
    """
    if w3 is None, fill as much as possible while offline
    """
    strategy_based_gas_price = async_w3.eth.generate_gas_price(transaction)

    is_dynamic_fee_transaction = strategy_based_gas_price is None and (
        "gasPrice" not in transaction  # default to dynamic fee transaction
        or any_in_dict(DYNAMIC_FEE_TXN_PARAMS, transaction)
    )

    defaults = {}
    for key, default_getter in TRANSACTION_DEFAULTS.items():
        if key not in transaction:
            if (
                is_dynamic_fee_transaction
                and key == "gasPrice"
                or not is_dynamic_fee_transaction
                and key in DYNAMIC_FEE_TXN_PARAMS
            ):
                # do not set default max fees if legacy txn or
                # gas price if dynamic fee txn
                continue

            if callable(default_getter):
                if async_w3 is None:
                    raise ValueError(
                        f"You must specify a '{key}' value in the transaction"
                    )
                if key == "gasPrice":
                    # `generate_gas_price()` is on the `BaseEth` class and does not
                    # need to be awaited
                    default_val = default_getter(async_w3, transaction)
                else:
                    default_val = await default_getter(async_w3, transaction)
            else:
                default_val = default_getter

            defaults[key] = default_val
    return merge(defaults, transaction)


async def async_handle_offchain_lookup(
    offchain_lookup_payload: Dict[str, Any],
    transaction: TxParams,
) -> bytes:
    formatted_sender = to_hex_if_bytes(offchain_lookup_payload["sender"]).lower()
    formatted_data = to_hex_if_bytes(offchain_lookup_payload["callData"]).lower()

    if formatted_sender != to_hex_if_bytes(transaction["to"]).lower():
        raise Web3ValidationError(
            "Cannot handle OffchainLookup raised inside nested call. Returned `sender` "
            "value does not equal `to` address in transaction."
        )

    for url in offchain_lookup_payload["urls"]:
        formatted_url = URI(
            str(url)
            .replace("{sender}", str(formatted_sender))
            .replace("{data}", str(formatted_data))
        )

        try:
            if "{data}" in url and "{sender}" in url:
                response = await async_get_response_from_get_request(formatted_url)
            elif "{sender}" in url:
                response = await async_get_response_from_post_request(
                    formatted_url,
                    data={"data": formatted_data, "sender": formatted_sender},
                )
            else:
                raise Web3ValidationError("url not formatted properly.")
        except Exception:
            continue  # try next url if timeout or issues making the request

        if (
            400 <= response.status <= 499
        ):  # if request returns 400 error, raise exception
            response.raise_for_status()
        if not 200 <= response.status <= 299:  # if not 400 error, try next url
            continue

        result = await async_get_json_from_client_response(response)

        if "data" not in result.keys():
            raise Web3ValidationError(
                "Improperly formatted response for offchain lookup HTTP request "
                "- missing 'data' field."
            )

        encoded_data_with_function_selector = b"".join(
            [
                # 4-byte callback function selector
                to_bytes_if_hex(offchain_lookup_payload["callbackFunction"]),
                # encode the `data` from the result and the `extraData` as bytes
                abi.encode(
                    ["bytes", "bytes"],
                    [
                        to_bytes_if_hex(result["data"]),
                        to_bytes_if_hex(offchain_lookup_payload["extraData"]),
                    ],
                ),
            ]
        )

        return encoded_data_with_function_selector
    raise Exception("Offchain lookup failed for supplied urls.")


async def async_get_required_transaction(
    async_w3: "AsyncWeb3", transaction_hash: _Hash32
) -> TxData:
    current_transaction = await async_w3.eth.get_transaction(transaction_hash)
    if not current_transaction:
        raise ValueError(
            f"Supplied transaction with hash {transaction_hash!r} does not exist"
        )
    return current_transaction


async def async_replace_transaction(
    async_w3: "AsyncWeb3", current_transaction: TxData, new_transaction: TxParams
) -> HexBytes:
    new_transaction = prepare_replacement_transaction(
        async_w3, current_transaction, new_transaction
    )
    return await async_w3.eth.send_transaction(new_transaction)
