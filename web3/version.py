from __future__ import absolute_import

from web3.utils.encoding import (
    to_decimal,
)
from web3.utils.functional import (
    apply_formatters_to_return,
)


class Version(object):
    def __init__(self, web3):
        self.web3 = web3

    @property
    def api(self):
        from web3 import __version__
        return __version__

    @property
    def node(self):
        return self.web3._requestManager.request_blocking("web3_clientVersion", [])

    def getNode(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(to_decimal)
    def network(self):
        return self.web3._requestManager.request_blocking("net_version", [])

    def getNetwork(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    @apply_formatters_to_return(to_decimal)
    def ethereum(self):
        return self.web3._requestManager.request_blocking("eth_protocolVersion", [])

    def getEthereum(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @property
    def whisper(self):
        raise NotImplementedError("Async calling has not been implemented")

    def getWhisper(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")
