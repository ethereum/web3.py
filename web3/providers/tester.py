from web3.utils.compat import (
    make_server,
    spawn,
)

from .base import BaseProvider  # noqa: E402
from .rpc import HTTPProvider  # noqa: E402


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
        if not is_testrpc_available():
            raise Exception("`TestRPCProvider` requires the `eth-testrpc` package to be installed")
        from testrpc.rpc import RPCMethods

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


class TestRPCProvider(HTTPProvider):
    def __init__(self, host="127.0.0.1", port=8545, *args, **kwargs):
        if not is_testrpc_available():
            raise Exception("`TestRPCProvider` requires the `eth-testrpc` package to be installed")
        from testrpc.server import get_application

        application = get_application()

        self.server = make_server(
            host,
            port,
            application,
        )

        self.thread = spawn(self.server.serve_forever)
        endpoint_uri = 'http://{0}:{1}'.format(host, port)

        super(TestRPCProvider, self).__init__(endpoint_uri, *args, **kwargs)
