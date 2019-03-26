from web3 import Web3
from web3.providers.auto import (
    load_provider_from_uri,
)

from .endpoints import (
    build_nodesmith_url,
)

_nodesmith_url = build_nodesmith_url("mainnet")

w3 = Web3(load_provider_from_uri(_nodesmith_url))
