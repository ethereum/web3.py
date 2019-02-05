from web3 import Web3
from web3.middleware import (
    geth_poa_middleware,
)
from web3.providers.auto import (
    load_provider_from_uri,
)

from .endpoints import (
    INFURA_RINKEBY_DOMAIN,
    build_infura_url,
)

_infura_url = build_infura_url(INFURA_RINKEBY_DOMAIN)

w3 = Web3(load_provider_from_uri(_infura_url))
w3.middleware_stack.inject(geth_poa_middleware, layer=0)
