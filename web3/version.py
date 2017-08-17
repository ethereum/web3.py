from __future__ import absolute_import

from web3.utils.module import (
    Module,
)
<<<<<<< HEAD
from web3.utils.functional import (
    apply_formatters_to_return,
)
from web3.utils.module import (
    Module,
)
=======
>>>>>>> 2aa43e0... remove formatters.py


class Version(Module):
    @property
    def api(self):
        from web3 import __version__
        return __version__

    @property
    def node(self):
        return self.web3.manager.request_blocking("web3_clientVersion", [])

    @property
    def network(self):
        return self.web3.manager.request_blocking("net_version", [])

    @property
    def ethereum(self):
        return self.web3.manager.request_blocking("eth_protocolVersion", [])
