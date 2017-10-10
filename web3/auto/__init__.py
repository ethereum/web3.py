from web3.auto import ipc
from web3.auto import http

w3 = ipc.ipc()

if not w3:
    w3 = http.http()
