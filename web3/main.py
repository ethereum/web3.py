from __future__ import absolute_import

import warnings

from eth_utils import (
    apply_to_return_value,
    add_0x_prefix,
    decode_hex,
    encode_hex,
    force_text,
    from_wei,
    is_address,
    is_checksum_address,
    keccak,
    remove_0x_prefix,
    to_checksum_address,
    to_wei,
)

from toolz.functoolz import (
    compose,
)

from web3.admin import Admin
from web3.db import Db
from web3.eth import Eth
from web3.iban import Iban
from web3.miner import Miner
from web3.net import Net
from web3.personal import Personal
from web3.shh import Shh
from web3.testing import Testing
from web3.txpool import TxPool
from web3.version import Version

from web3.providers.ipc import (
    IPCProvider,
)
from web3.providers.rpc import (
    HTTPProvider,
    RPCProvider,
    KeepAliveRPCProvider,
)
from web3.providers.tester import (
    TestRPCProvider,
    EthereumTesterProvider,
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

    @staticmethod
    @apply_to_return_value(encode_hex)
    def sha3(primitive=None, text=None, hexstr=None, encoding=None):
        if encoding is not None:
            warnings.warn(DeprecationWarning(
                "The encoding keyword has been deprecated.  Please update your "
                "code to use sha3(text='txt'), sha3(hexstr='0x747874'), "
                "sha3(b'\\x74\\x78\\x74'), or sha3(0x747874)."
            ))
        else:
            if not isinstance(primitive, (bytes, int, type(None))):
                warnings.warn(DeprecationWarning(
                    "The first argument as a string has been deprecated. Please update your "
                    "code to use sha3(text='txt'), sha3(hexstr='0x747874'), "
                    "sha3(b'\\x74\\x78\\x74'), or sha3(0x747874)."
                ))

        if isinstance(primitive, bytes):
            if bytes == str:
                # *shakes fist at python 2*
                # fall back to deprecated functionality
                pass
            else:
                return keccak(primitive)
        elif isinstance(primitive, int):
            return keccak(decode_hex(hex(primitive)))
        elif text is not None:
            return keccak(text.encode('utf-8'))
        elif hexstr is not None:
            return keccak(decode_hex(hexstr))

        # handle deprecated cases
        if encoding in ('hex', None):
            return keccak(decode_hex(primitive))
        elif encoding == 'bytes':
            return keccak(primitive)
        elif encoding == 'utf8':
            return keccak(primitive.encode('utf8'))

        raise ValueError(
            "You called sha3 with first arg %r and keywords %r. You must call it with one of "
            "these approaches: sha3(text='txt'), sha3(hexstr='0x747874'), "
            "sha3(b'\\x74\\x78\\x74'), or sha3(0x747874)." % (
                primitive,
                {'encoding': encoding, 'text': text, 'hexstr': hexstr}
            )
        )

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
