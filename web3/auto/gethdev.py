from web3 import (
    IPCProvider,
    Web3,
)
from web3.middleware import (
    ExtradataToPOAMiddleware,
)
from web3.providers.ipc import (
    get_dev_ipc_path,
)

w3 = Web3(IPCProvider(get_dev_ipc_path()))
w3.middleware_onion.inject(ExtradataToPOAMiddleware, layer=0)
