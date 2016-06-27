from __future__ import absolute_import


class Version(object):
    def __init__(self, request_manager):
        self.request_manager = request_manager

    @property
    def api(self):
        from web3 import __version__
        return __version__

    @property
    def node(self):
        return self.request_manager.request_blocking("web3_clientVersion", [])

    def getNode(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def network(self):
        return self.request_manager.request_blocking("net_version", [])

    def getNetwork(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")
