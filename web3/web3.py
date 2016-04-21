from web3.requestmanager import RequestManager
from web3.iban import Iban
from web3.methods.eth import Eth
from web3.methods.db import Db
from web3.methods.shh import Shh
from web3.methods.net import Net
from web3.methods.personal import Personal
import web3.settings as settings
import version
import utils.encoding as encoding
import utils.currency as currency
import utils.address as address
import utils.utils as utils
from utils.crypto import sha3
from web3.property import Property
from web3.rpcprovider import RPCProvider
from web3.ipcprovider import IPCProvider

class Web3:

    def __init__(self, provider):
        self._requestManager = RequestManager(provider)
        self.currentProvider = provider
        self.eth = Eth(self)
        self.db = Db(self)
        self.shh = Shh(self)
        self.net = Net(self)
        self.personal = Personal(self)
        self.settings = settings
        
        class Version:
            api = version.version
        
        self.version = Version

        self.providers = {
            "RPCProvider": RPCProvider,
            "IPCProvider": IPCProvider
        }

        for prop in properties:
            prop.attachToObject(self)
            prop.setRequestManager(self._requestManager)


        # Expose providers on the class
        self.RPCProvider = RPCProvider
        self.IPCProvider = IPCProvider

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
        self.settings = Settings()

    def sha3(self, string, options):
        return "0x" + sha3.sha3(string, options)

    def isConnected():
        return self.currentProvider and self.currentProvider.isConnected()

    def createBatch():
        return Batch(self)

properties = [
    Property({
        "name": "version.node",
        "getter": "web3_clientVersion"
    }),
    Property({
        "name": "version.network",
        "getter": "net_version",
        "inputFormatter": encoding.toDecimal
    }),
    Property({
        "name": "version.ethereum",
        "getter": "eth_protocolVersion",
        "inputFormatter": encoding.toDecimal
    }),
    Property({
        "name": "version.whisper",
        "getter": "shh_version",
        "inputFormatter": encoding.toDecimal
    })
]