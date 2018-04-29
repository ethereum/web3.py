from cytoolz import (
    compose,
    curry,
    dissoc,
)
from eth_utils.curried import (
    apply_formatter_at_index,
    apply_formatters_to_dict,
)

from web3.exceptions import (
    ValidationError,
)
from web3.middleware.formatting import (
    construct_web3_formatting_middleware,
)


@curry
def validate_chain_id(web3, chain_id):
    if chain_id == web3.net.chainId:
        return chain_id
    else:
        raise ValidationError(
            "The transaction declared chain ID %r, "
            "but the connected node is on %r" % (
                chain_id,
                "UNKNOWN",
            )
        )


def transaction_normalizer(transaction):
    return dissoc(transaction, 'chainId')


def transaction_param_validator(web3):
    transactions_params_validators = {
        'chainId': apply_formatter_if(
            # Bypass `validate_chain_id` if chainId can't be determined
            lambda _: is_not_null(web3.net.chainId),
            validate_chain_id(web3)
        ),
    }
    return apply_formatter_at_index(
        apply_formatters_to_dict(transactions_params_validators),
        0
    )


@curry
def chain_id_validator(web3):
    return compose(
        apply_formatter_at_index(transaction_normalizer, 0),
        transaction_param_validator(web3)
    )


def build_validators_with_web3(w3):
    return dict(
        request_formatters={
            'eth_sendTransaction': chain_id_validator(w3),
            'eth_estimateGas': chain_id_validator(w3),
            'eth_call': chain_id_validator(w3),
        }
    )


validation_middleware = construct_web3_formatting_middleware(build_validators_with_web3)
