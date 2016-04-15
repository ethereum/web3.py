from __future__ import absolute_import

import pkg_resources

__version__ = pkg_resources.get_distribution("web3.py").version


from web3.utils.crypto import (
    sha3
)
