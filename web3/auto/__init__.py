import importlib

for connector in ('ipc', 'http'):
    connection = importlib.import_module('web3.auto.' + connector)
    if connection.w3:
        w3 = connection.w3

        if w3.isConnected():
            break
