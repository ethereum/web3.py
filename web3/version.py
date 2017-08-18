from __future__ import absolute_import

from web3.utils.encoding import (
    to_decimal,
)
from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.utils.module import (
    Module,
)


class Version(Module):
    @property
    def api(self):
        from web3 import __version__
        return __version__

    @property
    def node(self):
        return self.web3.manager.request_blocking("web3_clientVersion", [])

    @property
    @apply_formatters_to_return(to_decimal)
    def network(self):
        return self.web3.manager.request_blocking("net_version", [])

    @property
    @apply_formatters_to_return(to_decimal)
    def ethereum(self):
        return self.web3.manager.request_blocking("eth_protocolVersion", [])
