from __future__ import absolute_import

import pkg_resources

from .utils.crypto import (
    sha3,
)

from web3.main import Web3  # NOQA
from web3.web3.rpcprovider import RPCProvider  # NOQA
from web3.web3.ipcprovider import IPCProvider  # NOQA

__version__ = pkg_resources.get_distribution("web3").version

__all__ = [
    "__version__",
    "sha3",
    "web3"
]
