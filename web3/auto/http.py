from web3 import (
    HTTPProvider,
    Web3
)

def http():
    web3 =  Web3(HTTPProvider('http://localhost:8545'))
    
    if web3.isConnected():
        return web3
    else:
        return False

web3 = http()
