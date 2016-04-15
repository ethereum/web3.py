from __future__ import absolute_import

import pkg_resources

from . import (
    eth,
    web3,
)

__version__ = pkg_resources.get_distribution("web3.py").version

__all__ = [
    "__version__",
    "eth",
    "web3",
]
