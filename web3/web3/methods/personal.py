from web3.web3.method import Method
from web3.web3.property import Property
import web3.web3.formatters as formatters

methods = [
    {
        "name": "newAccount",
        "call": "personal_newAccount",
        "params": 1,
        "inputFormatter": [None]
    },
    {
        "name": "unlockAccount",
        "call": "personal_unlockAccount",
        "params": 3,
        "inputFormatter": [formatters.inputAddressFormatter, None, None]
    },
    {
        "name": "lockAccount",
        "call": "personal_lockAccount",
        "params": 1,
        "inputFormatter": [formatters.inputAddressFormatter]
    }
]


properties = [
    {
        "name": "listAccounts",
        "getter": "personal_listAccounts",
    }
]


class Personal(object):

    def __init__(self, web3):
        self._requestManager = web3._requestManager

        for method in methods:
            method = Method(method)
            method.attachToObject(self)
            method.setRequestManager(web3._requestManager)

        for prop in properties:
            prop = Property(prop)
            prop.attachToObject(self)
            prop.setRequestManager(web3._requestManager)
