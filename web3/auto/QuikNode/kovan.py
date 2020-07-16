from web3 import Web3
from web3.providers.auto import(
  load_provider_from_uri,
)

from .endpoints import(
  build_QuikNode_url,
)

_QuikNode_url = build_QuikNode_url("kovan")

w3 = Web3(load_provider_from_uri(_QuikNode_url))
