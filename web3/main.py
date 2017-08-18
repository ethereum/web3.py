from __future__ import absolute_import

import warnings

from eth_utils import (
    to_wei,
    from_wei,
    is_address,
    is_checksum_address,
    to_checksum_address,
    decode_hex,
    encode_hex,
    force_text,
    coerce_return_to_text,
)

from cytoolz.functoolz import (
    compose,
)

from web3.admin import Admin
from web3.db import Db
from web3.eth import Eth
from web3.miner import Miner
from web3.net import Net
from web3.personal import Personal
from web3.shh import Shh
from web3.txpool import TxPool
from web3.version import Version
from web3.testing import Testing

from web3.iban import Iban

from web3.providers.rpc import (
    HTTPProvider,
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
from web3.manager import (
    RequestManager,
)

from web3.utils.encoding import (
    to_hex,
    to_decimal,
    from_decimal,
)


def get_default_modules():
    return {
        "eth": Eth,
        "db": Db,
        "shh": Shh,
        "net": Net,
        "personal": Personal,
        "version": Version,
        "txpool": TxPool,
        "miner": Miner,
        "admin": Admin,
        "testing": Testing,
    }


class Web3(object):
    # Providers
    HTTPProvider = HTTPProvider
    RPCProvider = RPCProvider
    KeepAliveRPCProvider = KeepAliveRPCProvider
    IPCProvider = IPCProvider
    TestRPCProvider = TestRPCProvider
    EthereumTesterProvider = EthereumTesterProvider

    # Managers
    RequestManager = RequestManager

    # Iban
    Iban = Iban

    # Encoding and Decoding
    toHex = staticmethod(to_hex)
    toAscii = staticmethod(decode_hex)
    toUtf8 = staticmethod(compose(force_text, decode_hex))
    fromAscii = staticmethod(encode_hex)
    fromUtf8 = staticmethod(encode_hex)
    toDecimal = staticmethod(to_decimal)
    fromDecimal = staticmethod(from_decimal)

    # Currency Utility
    toWei = staticmethod(to_wei)
    fromWei = staticmethod(from_wei)

    # Address Utility
    isAddress = staticmethod(is_address)
    isChecksumAddress = staticmethod(is_checksum_address)
    toChecksumAddress = staticmethod(to_checksum_address)

    def __init__(self, provider, modules=None):
        self.manager = RequestManager(provider)

        if modules is None:
            modules = get_default_modules()

        for module_name, module_class in modules.items():
            if hasattr(self, module_name):
                raise AttributeError(
                    "Cannot set web3 module named '{0}'.  The web3 object "
                    "already has an attribute with that name".format(module_name)
                )
            setattr(self, module_name, module_class(self))

    @property
    def provider(self):
        return self.manager.provider

    def setProvider(self, provider):
        self.manager.setProvider(provider)

    def setManager(self, manager):
        warnings.warn(DeprecationWarning(
            "The `setManager` method has been deprecated.  Please update your "
            "code to directly set the `manager` property."
        ))
        self.manager = manager

    @property
    def currentProvider(self):
        warnings.warn(DeprecationWarning(
            "The `currentProvider` property has been renamed to `provider`."
        ))
        return self.manager.provider

    @coerce_return_to_text
    def sha3(self, value, encoding="hex"):
        if encoding == 'hex':
            hex_string = value
        else:
            hex_string = encode_hex(value)
        return self.manager.request_blocking('web3_sha3', [hex_string])

    def isConnected(self):
        return self.provider is not None and self.provider.isConnected()
