from __future__ import absolute_import

import warnings

from eth_utils import (
    coerce_return_to_text,
    decode_hex,
    encode_hex,
    force_text,
    from_wei,
    is_address,
    is_checksum_address,
    to_checksum_address,
    add_0x_prefix,
    remove_0x_prefix,
    to_wei,
)

from toolz.functoolz import (
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
    hex_encode_abi_type,
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

    def __init__(self, providers, middlewares=None, modules=None):
        self.manager = RequestManager(self, providers, middlewares)

        if modules is None:
            modules = get_default_modules()

        for module_name, module_class in modules.items():
            if hasattr(self, module_name):
                raise AttributeError(
                    "Cannot set web3 module named '{0}'.  The web3 object "
                    "already has an attribute with that name".format(module_name)
                )
            setattr(self, module_name, module_class(self))

    def add_middleware(self, middleware):
        """
        Convenience API for RequestManager.add_middleware
        """
        self.manager.add_middleware(middleware)

    def clear_middlewares(self):
        """
        Convenience API for RequestManager.clear_middlewares
        """
        self.manager.clear_middlewares()

    @property
    def providers(self):
        return self.manager.providers

    def setProviders(self, providers):
        self.manager.setProvider(providers)

    def setManager(self, manager):
        warnings.warn(DeprecationWarning(
            "The `setManager` method has been deprecated.  Please update your "
            "code to directly set the `manager` property."
        ))
        self.manager = manager

    @property
    def currentProvider(self):
        warnings.warn(DeprecationWarning(
            "The `currentProvider` property has been renamed to `providers` and is now a list."
        ))
        return self.manager.providers[0]

    @coerce_return_to_text
    def sha3(self, value, encoding="hex"):
        if encoding == 'hex':
            hex_string = value
        else:
            hex_string = encode_hex(value)
        return self.manager.request_blocking('web3_sha3', [hex_string])

    def soliditySha3(self, abi_types, values):
        """
        Executes sha3 (keccak256) exactly as Solidity does.
        Takes list of abi_types as inputs -- `[uint24, int8[], bool]`
        and list of corresponding values  -- `[20, [-1, 5, 0], True]`
        """
        if len(abi_types) != len(values):
            raise ValueError(
                "Length mismatch between provided abi types and values.  Got "
                "{0} types and {1} values.".format(len(abi_types), len(values))
            )

        hex_string = add_0x_prefix(''.join(
            remove_0x_prefix(hex_encode_abi_type(abi_type, value))
            for abi_type, value
            in zip(abi_types, values)
        ))
        return self.sha3(hex_string, encoding="hex")

    def isConnected(self):
        for provider in self.providers:
            if provider.isConnected():
                return True
        else:
            return False
