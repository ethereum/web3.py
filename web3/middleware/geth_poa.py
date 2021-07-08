from eth_utils.curried import (
    apply_formatter_if,
    apply_formatters_to_dict,
    apply_key_map,
    is_null,
)
from eth_utils.toolz import (
    complement,
    compose,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.rpc_abi import (
    RPC,
)
from web3.middleware.formatting import (
    construct_formatting_middleware,
)

is_not_null = complement(is_null)

remap_geth_poa_fields = apply_key_map({
    'extraData': 'proofOfAuthorityData',
})

pythonic_geth_poa = apply_formatters_to_dict({
    'proofOfAuthorityData': HexBytes,
})

geth_poa_cleanup = compose(pythonic_geth_poa, remap_geth_poa_fields)

geth_poa_middleware = construct_formatting_middleware(
    result_formatters={
        RPC.eth_getBlockByHash: apply_formatter_if(is_not_null, geth_poa_cleanup),
        RPC.eth_getBlockByNumber: apply_formatter_if(is_not_null, geth_poa_cleanup),
    },
)
