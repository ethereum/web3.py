from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
)

from eth_utils.curried import (
    apply_formatter_at_index,
    apply_formatter_if,
    apply_formatters_to_dict,
    is_null,
    is_string,
)
from eth_utils.toolz import (
    complement,
    compose,
    curry,
    dissoc,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.formatters import (
    hex_to_integer,
)
from web3._utils.rpc_abi import (
    RPC,
)
from web3.exceptions import (
    ExtraDataLengthError,
    ValidationError,
)
from web3.middleware.formatting import (
    construct_web3_formatting_middleware,
)
from web3.types import (
    FormattersDict,
    TxParams,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401

MAX_EXTRADATA_LENGTH = 32

is_not_null = complement(is_null)

to_integer_if_hex = apply_formatter_if(is_string, hex_to_integer)


@curry
def validate_chain_id(web3: "Web3", chain_id: int) -> int:
    if to_integer_if_hex(chain_id) == web3.eth.chainId:
        return chain_id
    else:
        raise ValidationError(
            "The transaction declared chain ID %r, "
            "but the connected node is on %r" % (
                chain_id,
                web3.eth.chainId,
            )
        )


def check_extradata_length(val: Any) -> Any:
    if not isinstance(val, (str, int, bytes)):
        return val
    result = HexBytes(val)
    if len(result) > MAX_EXTRADATA_LENGTH:
        raise ExtraDataLengthError(
            "The field extraData is %d bytes, but should be %d. "
            "It is quite likely that you are connected to a POA chain. "
            "Refer to "
            "http://web3py.readthedocs.io/en/stable/middleware.html#geth-style-proof-of-authority "
            "for more details. The full extraData is: %r" % (
                len(result), MAX_EXTRADATA_LENGTH, result
            )
        )
    return val


def transaction_normalizer(transaction: TxParams) -> TxParams:
    return dissoc(transaction, 'chainId')


def transaction_param_validator(web3: "Web3") -> Callable[..., Any]:
    transactions_params_validators = {
        "chainId": apply_formatter_if(
            # Bypass `validate_chain_id` if chainId can't be determined
            lambda _: is_not_null(web3.eth.chainId),
            validate_chain_id(web3),
        ),
    }
    return apply_formatter_at_index(
        apply_formatters_to_dict(transactions_params_validators),
        0
    )


BLOCK_VALIDATORS = {
    'extraData': check_extradata_length,
}


block_validator = apply_formatter_if(
    is_not_null,
    apply_formatters_to_dict(BLOCK_VALIDATORS)
)


@curry
def chain_id_validator(web3: "Web3") -> Callable[..., Any]:
    return compose(
        apply_formatter_at_index(transaction_normalizer, 0),
        transaction_param_validator(web3)
    )


def build_validators_with_web3(w3: "Web3") -> FormattersDict:
    return dict(
        request_formatters={
            RPC.eth_sendTransaction: chain_id_validator(w3),
            RPC.eth_estimateGas: chain_id_validator(w3),
            RPC.eth_call: chain_id_validator(w3),
        },
        result_formatters={
            RPC.eth_getBlockByHash: block_validator,
            RPC.eth_getBlockByNumber: block_validator,
        },
    )


validation_middleware = construct_web3_formatting_middleware(build_validators_with_web3)
