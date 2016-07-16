from __future__ import absolute_import

from web3.eth import Eth
from web3.db import Db
from web3.shh import Shh
from web3.net import Net
from web3.personal import Personal
from web3.version import Version

from web3.providers.rpc import (
    RPCProvider,
    TestRPCProvider,
)
from web3.providers.ipc import IPCProvider
from web3.providers.manager import RequestManager

from web3.utils.functional import (
    compose,
)
from web3.utils.string import (
    force_text,
)
from web3.utils.encoding import (
    to_hex,
    decode_hex,
    encode_hex,
    to_decimal,
    from_decimal,
)
from web3.utils.currency import (
    to_wei,
    from_wei,
)
from web3.utils.address import (
    is_address,
    is_checksum_address,
    to_checksum_address,
)
from web3.utils import config


class Web3(object):
    def __init__(self, provider):
        self._requestManager = RequestManager(provider)
        self.currentProvider = provider

        self.eth = Eth(self)
        self.db = Db(self._requestManager)
        self.shh = Shh(self._requestManager)
        self.net = Net(self._requestManager)
        self.personal = Personal(self._requestManager)
        self.version = Version(self._requestManager)

        self.providers = {
            'RPCProvider': RPCProvider,
            'IPCProvider': IPCProvider,
            'TestRPCProvider': TestRPCProvider,
        }

        self.RPCProvider = RPCProvider
        self.IPCProvider = IPCProvider
        self.TestRPCProvider = TestRPCProvider

        class Config:

            def __getattr__(self, key):
                if key == "defaultAccount":
                    return config.defaultAccount
                elif key == "defaultBlock":
                    return config.defaultBlock

            def __setattr__(self, key, value):
                if key == "defaultAccount":
                    config.defaultAccount = value
                elif key == "defaultBlock":
                    config.defaultBlock = value

        self.config = Config()

        # Encoding and Decoding
        self.toHex = to_hex
        self.toAscii = decode_hex
        self.toUtf8 = compose(decode_hex, force_text)
        self.fromAscii = encode_hex
        self.fromUtf8 = encode_hex
        self.toDecimal = to_decimal
        self.fromDecimal = from_decimal

        # Currency Utility
        self.toWei = to_wei
        self.fromWei = from_wei

        # Address Utility
        self.isAddress = is_address
        self.isChecksumAddress = is_checksum_address
        self.toChecksumAddress = to_checksum_address

    def setProvider(self, provider):
        self._requestManager.setProvider(provider)
        self.currentProvider = provider

    def reset(self, keepIsSyncing):
        self._requestManager.reset(keepIsSyncing)

    def sha3(self, value, encoding="hex"):
        if encoding == 'hex':
            hex_string = value
        else:
            hex_string = encode_hex(value)
        return self._requestManager.request_blocking('web3_sha3', [hex_string])

    def isConnected(self):
        return self.currentProvider is not None and self.currentProvider.isConnected()

    def createBatch(self):
        raise NotImplementedError("Not Implemented")

    def receive(self, requestid, timeout=0, keep=False):
        return self._requestManager.receive(requestid, timeout, keep)
