import web3.web3.formatters as formatters


# TODO: remove this list
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


class Personal(object):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal
    """
    def __init__(self, request_manager):
        self.request_manager = request_manager

    def importRawKey(self, *args, **kwargs):
        raise NotImplementedError()

    def newAccount(self, *args, **kwargs):
        raise NotImplementedError()

    @property
    def listAccounts(self):
        return self.request_manager.request_blocking("personal_listAccounts", [])

    def getListAccounts(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    def signAndSendTransaction(self, *args, **kwargs):
        raise NotImplementedError()

    def lockAccount(self, *args, **kwargs):
        raise NotImplementedError()

    def unlockAccount(self, *args, **kwargs):
        raise NotImplementedError()
