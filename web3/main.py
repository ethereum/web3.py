from __future__ import absolute_import

from eth_utils import (
    apply_to_return_value,
    add_0x_prefix,
    encode_hex,
    from_wei,
    is_address,
    is_checksum_address,
    keccak,
    remove_0x_prefix,
    to_checksum_address,
    to_wei,
)

from web3.admin import Admin
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
    to_bytes,
    to_int,
    to_hex,
    to_text,
)


def get_default_modules():
    return {
        "eth": Eth,
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
    IPCProvider = IPCProvider
    TestRPCProvider = TestRPCProvider
    EthereumTesterProvider = EthereumTesterProvider

    # Managers
    RequestManager = RequestManager

    # Iban
    Iban = Iban

    # Encoding and Decoding
    toBytes = staticmethod(to_bytes)
    toInt = staticmethod(to_int)
    toHex = staticmethod(to_hex)
    toText = staticmethod(to_text)

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
            module_class.attach(self, module_name)

    @property
    def middleware_stack(self):
        return self.manager.middleware_stack

    @property
    def providers(self):
        return self.manager.providers

    def setProviders(self, providers):
        self.manager.setProvider(providers)

    @staticmethod
    @apply_to_return_value(encode_hex)
    def sha3(primitive=None, text=None, hexstr=None):
        if isinstance(primitive, (bytes, int, type(None))):
            input_bytes = to_bytes(primitive, hexstr=hexstr, text=text)
            return keccak(input_bytes)

        raise TypeError(
            "You called sha3 with first arg %r and keywords %r. You must call it with one of "
            "these approaches: sha3(text='txt'), sha3(hexstr='0x747874'), "
            "sha3(b'\\x74\\x78\\x74'), or sha3(0x747874)." % (
                primitive,
                {'text': text, 'hexstr': hexstr}
            )
        )

    @classmethod
    def soliditySha3(cls, abi_types, values):
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
        return cls.sha3(hexstr=hex_string)

    def isConnected(self):
        for provider in self.providers:
            if provider.isConnected():
                return True
        else:
            return False
