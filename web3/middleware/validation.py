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


@curry
def validate_chain_id(web3, chain_id):
    if chain_id == web3.version.network:
        return None
    else:
        raise ValidationError(
            "The transaction declared chain ID %r, "
            "but the connected node is on %r" % (
                chain_id,
                web3.version.network,
            )
        )


def transaction_normalizer(transaction):
    return dissoc(transaction, 'chainId')


def validation_middleware(make_request, web3):
    transaction_validator = apply_formatters_to_dict({
        'chainId': validate_chain_id(web3),
    })

    transaction_sanitizer = compose(transaction_normalizer, transaction_validator)

    def middleware(method, params):
        if method in ('eth_sendTransaction', 'eth_estimateGas', 'eth_call'):
            post_validated_params = apply_formatter_at_index(transaction_sanitizer, 0, params)
            return make_request(method, post_validated_params)
        else:
            return make_request(method, params)
    return middleware
