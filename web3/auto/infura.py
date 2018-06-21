from web3 import (
    HTTPProvider,
    Web3,
)

INFURA_MAINNET_HTTP_URL = 'https://mainnet.infura.io'

w3 = Web3(HTTPProvider(INFURA_MAINNET_HTTP_URL))
