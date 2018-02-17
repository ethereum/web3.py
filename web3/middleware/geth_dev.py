"""

Middleware workaround implementation to allow for larger extraData field

For more information and a for a suggested full implementaion, see:

https://github.com/ethereum/web3.py/issues/647

"""

from eth_utils.curried import (
    apply_key_map,
)

from web3.middleware.formatting import (
    construct_formatting_middleware,
)

remap_geth_dev_fields = apply_key_map({
    'extraData': 'proofOfAuthorityData',
})

geth_dev_middleware = construct_formatting_middleware(
    result_formatters={
        'eth_getBlockByHash': remap_geth_dev_fields,
        'eth_getBlockByNumber': remap_geth_dev_fields,
    },
)

#
# A placeholder, to reserve a predefined position within a predefined middleware list
#
placeholder_middleware = construct_formatting_middleware()
