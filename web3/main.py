from __future__ import absolute_import

import copy

from web3.web3.requestmanager import RequestManager
from web3.web3.methods.eth import Eth
from web3.web3.methods.db import Db
from web3.web3.methods.shh import Shh
from web3.web3.methods.net import Net
from web3.web3.methods.personal import Personal
from web3.version import Version

from web3.web3.rpcprovider import (
    RPCProvider,
    TestRPCProvider,
    is_testrpc_available,
)
from web3.web3.ipcprovider import IPCProvider

from web3.utils.encoding import (
    encode_hex,
)
import web3.utils.encoding as encoding
import web3.utils.currency as currency
import web3.utils.address as address
import web3.utils.config as config


DEFAULT_PROVIDERS = {
    "RPCProvider": RPCProvider,
    "IPCProvider": IPCProvider
}

if is_testrpc_available():
    DEFAULT_PROVIDERS['TestRPCProvider'] = TestRPCProvider


class Web3(object):
    def __init__(self, provider):
        self._requestManager = RequestManager(provider)
        self.currentProvider = provider

        self.eth = Eth(self._requestManager)
        self.db = Db(self._requestManager)
        self.shh = Shh(self._requestManager)
        self.net = Net(self._requestManager)
        self.personal = Personal(self._requestManager)
        self.version = Version(self._requestManager)

        self.providers = copy.copy(DEFAULT_PROVIDERS)

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

        # Expose providers on the class
        for class_name, klass in DEFAULT_PROVIDERS.items():
            setattr(self, class_name, klass)

        # Expose utility functions
        self.toHex = encoding.toHex
        self.toAscii = encoding.toAscii
        self.toUtf8 = encoding.toUtf8
        self.fromAscii = encoding.fromAscii
        self.fromUtf8 = encoding.fromUtf8
        self.toDecimal = encoding.toDecimal
        self.fromDecimal = encoding.fromDecimal
        self.toWei = currency.toWei
        self.fromWei = currency.fromWei
        self.isAddress = address.isAddress
        self.isChecksumAddress = address.isChecksumAddress
        self.toChecksumAddress = address.toChecksumAddress

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
        return self.currentProvider and self.currentProvider.isConnected()

    def createBatch(self):
        raise NotImplementedError("Not Implemented")

    def receive(self, requestid, timeout=0, keep=False):
        return self._requestManager.receive(requestid, timeout, keep)
