from __future__ import absolute_import

import web3.utils.encoding as encoding
from web3.utils.functional import (
    apply_formatters_to_return,
)


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
    @apply_formatters_to_return(encoding.toDecimal)
    def network(self):
        return self.request_manager.request_blocking("net_version", [])

    def getNetwork(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(encoding.toDecimal)
    def ethereum(self):
        return self.request_manager.request_blocking("eth_protocolVersion", [])

    def getEthereum(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def whisper(self):
        raise NotImplementedError("Async calling has not been implemented")

    def getWhisper(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")
