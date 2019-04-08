from eth_utils.curried import (
    apply_formatters_to_dict,
    apply_key_map,
)
from eth_utils.toolz import (
    compose,
)
from hexbytes import (
    HexBytes,
)

from web3.middleware.formatting import (
    construct_formatting_middleware,
)

remap_geth_poa_fields = apply_key_map({
    'extraData': 'proofOfAuthorityData',
})

pythonic_geth_poa = apply_formatters_to_dict({
    'proofOfAuthorityData': HexBytes,
})

geth_poa_cleanup = compose(pythonic_geth_poa, remap_geth_poa_fields)

geth_poa_middleware = construct_formatting_middleware(
    result_formatters={
        'eth_getBlockByHash': geth_poa_cleanup,
        'eth_getBlockByNumber': geth_poa_cleanup,
    },
)
