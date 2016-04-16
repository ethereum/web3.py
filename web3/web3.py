import web3.RequestManager
import web3.IBAN
import web3.methods.Eth
import web3.methods.Db
import web3.methods.Shh
import web3.methods.Net
import web3.Personal
import web3.Settings
import version
import utils.encoding
import utils.currency
import utils.address
import utils.sha3
import web3.extend
import web3.Batch
import web3.Property
import web3.RPCProvider
import web3.IPCProvider

class Web3:

    def __init__(self, provider):
        self._requestManager = RequestManager(provider)
        self.currentProvider = provider
        self.eth = Eth(self)
        self.db = Db(self)
        self.shh = Shh(self)
        self.net = Net(self)
        self.personal = Personal(self)
        self.settings = Settings()
        self.version = {
            "api": version.version
        }
        self.providers = {
            "RPCProvider": RPCProvider,
            "IPCProvider": IPCProvider
        }
        self._extend = extend(self)
        self._extend({
            "properties": properties()
        })

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
        self.toBigNumber = utils.toBigNumber
        self.toWei = currency.toWei
        self.fromWei = currency.fromWei
        self.isAddress = address.isAddress
        self.isChecksumAddress = address.isChecksumAddress
        self.toChecksumAddress = address.toChecksumAddress
        self.isIBAN = address.isIBAN

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

def properties():
    return [
        Property({
            "name": "version.node",
            "getter": "web3_clientVersion"
        }),
        Property({
            "name": "version.network",
            "getter": "net_version",
            "inputFormatter": utils.toDecimal
        }),
        Property({
            "name": "version.ethereum",
            "getter": "eth_protocolVersion",
            "inputFormatter": utils.toDecimal
        }),
        Property({
            "name": "version.whisper",
            "getter": "shh_version",
            "inputFormatter": utils.toDecimal
        }),
    ]