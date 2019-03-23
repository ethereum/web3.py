from web3 import Web3
from web3.providers.auto import (
    load_provider_from_uri,
)

from .endpoints import (
    INFURA_MAINNET_DOMAIN,
    build_http_headers,
    build_infura_url,
)

_infura_url = build_infura_url(INFURA_MAINNET_DOMAIN)
_headers = build_http_headers()

w3 = Web3(load_provider_from_uri(_infura_url, _headers))
