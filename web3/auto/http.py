from web3 import (
    HTTPProvider,
    Web3
)


def http():

    w3 = Web3(HTTPProvider('http://localhost:8545'))
    if w3.isConnected():
        return w3
    else:
        return False


w3 = http()
