from __future__ import absolute_import

from web3.admin import Admin
from web3.db import Db
from web3.eth import Eth
from web3.miner import Miner
from web3.net import Net
from web3.personal import Personal
from web3.shh import Shh
from web3.txpool import TxPool
from web3.version import Version

from web3.iban import Iban

from web3.providers.rpc import (
    RPCProvider,
    TestRPCProvider,
)
from web3.providers.ipc import IPCProvider
from web3.providers.manager import (
    RequestManager,
    DelegatedSigningManager,
    PrivateKeySigningManager,
)

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


class Web3(object):
    # Providers
    RPCProvider = RPCProvider
    IPCProvider = IPCProvider
    TestRPCProvider = TestRPCProvider

    # Managers
    RequestManager = RequestManager
    DelegatedSigningManager = DelegatedSigningManager
    PrivateKeySigningManager = PrivateKeySigningManager

    # Iban
    Iban = Iban

    # Encoding and Decoding
    toHex = staticmethod(to_hex)
    toAscii = staticmethod(decode_hex)
    toUtf8 = staticmethod(compose(decode_hex, force_text))
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

    def __init__(self, provider):
        self._requestManager = RequestManager(provider)

        self.eth = Eth(self)
        self.db = Db(self)
        self.shh = Shh(self)
        self.net = Net(self)
        self.personal = Personal(self)
        self.version = Version(self)
        self.txpool = TxPool(self)
        self.miner = Miner(self)
        self.admin = Admin(self)

    def setProvider(self, provider):
        self._requestManager.setProvider(provider)

    def setManager(self, manager):
        self._requestManager = manager

    @property
    def currentProvider(self):
        return self._requestManager.provider

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
