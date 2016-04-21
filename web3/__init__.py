from __future__ import absolute_import

import pkg_resources

from .utils.crypto import (
    sha3,
)

__version__ = pkg_resources.get_distribution("web3").version

__all__ = [
    "__version__",
    "sha3",
]
