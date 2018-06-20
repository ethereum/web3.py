from web3 import (
    HTTPProvider,
    Web3,
)
from web3.providers.auto import (
    INFURA_MAINNET_HTTP_URL,
)

w3 = Web3(HTTPProvider(INFURA_MAINNET_HTTP_URL))
