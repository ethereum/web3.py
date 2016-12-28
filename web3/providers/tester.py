import logging

import gevent

from testrpc.rpc import RPCMethods

from .base import BaseProvider  # noqa: E402
from .rpc import RPCProvider  # noqa: E402


logger = logging.getLogger(__name__)


def is_testrpc_available():
    try:
        import testrpc  # noqa: F401
        return True
    except ImportError:
        return False


class EthereumTesterProvider(BaseProvider):
    def __init__(self,
                 *args,
                 **kwargs):
        """Create a new RPC client.

        :param connection_timeout: See :class:`geventhttpclient.HTTPClient`

        :param network_timeout: See :class:`geventhttpclient.HTTPClient`
        """
        if not is_testrpc_available():
            raise Exception("`TestRPCProvider` requires the `eth-testrpc` package to be installed")
        self.rpc_methods = RPCMethods()
        super(BaseProvider, self).__init__(*args, **kwargs)

    def __str__(self):
        return "EthereumTesterProvider"

    def __repr__(self):
        return self.__str__()

    def make_request(self, method, params):
        rpc_fn = getattr(self.rpc_methods, method)
        response = rpc_fn(*params)

        return {
            'result': response,
        }

    def isConnected(self):
        return True


class TestRPCProvider(RPCProvider):
    def __init__(self, host="127.0.0.1", port=8545, *args, **kwargs):
        if not is_testrpc_available():
            raise Exception("`TestRPCProvider` requires the `eth-testrpc` package to be installed")
        from gevent.pywsgi import WSGIServer
        from testrpc.server import get_application

        try:
            logger = kwargs.pop('logger')
        except KeyError:
            logger = logging.getLogger('testrpc')

        application = get_application()

        self.server = WSGIServer(
            (host, port),
            application,
            log=logger,
            error_log=logger,
        )

        self.thread = gevent.spawn(self.server.serve_forever)

        super(TestRPCProvider, self).__init__(host, str(port), *args, **kwargs)
