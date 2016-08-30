class Admin(object):
    def __init__(self, request_manager):
        self.request_manager = request_manager

    def addPeer(self, node_url):
        return self.request_manager.request_blocking("admin_addPeer", [node_url])

    @property
    def datadir(self):
        return self.request_manager.request_blocking("admin_datadir", [])

    @property
    def nodeInfo(self):
        return self.request_manager.request_blocking("admin_nodeInfo", [])

    @property
    def peers(self):
        return self.request_manager.request_blocking("admin_peers", [])

    def setSolc(self, solc_path):
        return self.request_manager.request_blocking("admin_setSolc", [solc_path])

    def startRPC(self, host='localhost', port='8545', cors="", apis="eth,net,web3"):
        return self.request_manager.request_blocking(
            "admin_startRPC",
            [host, port, cors, apis],
        )

    def startWS(self, host='localhost', port='8546', cors="", apis="eth,net,web3"):
        return self.request_manager.request_blocking(
            "admin_startWS",
            [host, port, cors, apis],
        )

    def stopRPC(self):
        return self.request_manager.request_blocking("admin_stopRPC", [])

    def stopWS(self):
        return self.request_manager.request_blocking("admin_stopWS", [])
