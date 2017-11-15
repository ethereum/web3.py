from web3 import (
    HTTPProvider,
    Web3
)
import os


def connect():

    w3 = Web3(HTTPProvider(
        os.environ.get('WEB3_HTTP_PROVIDER_URI', 'http://localhost:8545')
    ))
    if w3.isConnected():
        return w3
    else:
        return False


w3 = connect()
