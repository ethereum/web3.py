from __future__ import absolute_import

import pkg_resources

from web3.main import Web3
from web3.providers.rpc import (
    RPCProvider,
    KeepAliveRPCProvider,
)
from web3.providers.tester import (
    TestRPCProvider,
    EthereumTesterProvider,
)
from web3.providers.ipc import (
    IPCProvider,
)

__version__ = pkg_resources.get_distribution("web3").version

__all__ = [
    "__version__",
    "Web3",
    "RPCProvider",
    "KeepAliveRPCProvider",
    "IPCProvider",
    "TestRPCProvider",
    "EthereumTesterProvider",
]
