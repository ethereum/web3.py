from web3.auto import ipc
from web3.auto import http

web3 = ipc.ipc()

if not web3:
    web3 = http.http()

