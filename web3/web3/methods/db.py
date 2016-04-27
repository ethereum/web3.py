from web3.web3.method import Method

methods = [
    {
        "name": "putString",
        "call": "db_putString",
        "params": 3
    },
    {
        "name": "getString",
        "call": "db_getString",
        "params": 2
    },
    {
        "name": "putHex",
        "call": "db_putHex",
        "params": 3
    },
    {
        "name": "getHex",
        "call": "db_getHex",
        "params": 2
    }
]


class Db(object):

    def __init__(self, web3):
        self._requestManager = web3._requestManager

        for method in methods:
            method = Method(method)
            method.attachToObject(self)
            method.setRequestManager(web3._requestManager)
