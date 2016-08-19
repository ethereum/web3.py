import gevent
from gevent import monkey


monkey.patch_socket()
monkey.patch_select()


from .base import BaseProvider  # noqa: E402

import requests  # noqa: E402


class RPCProvider(BaseProvider):

    def __init__(self, host="127.0.0.1", port="8545", *args, **kwargs):
        self.host = host
        self.port = port

        super(RPCProvider, self).__init__(*args, **kwargs)

    def make_request(self, method, params):
        request = self.encode_rpc_request(method, params)
        response = requests.post(
            "http://{host}:{port}/".format(host=self.host, port=self.port),
            headers={'content-type': 'application/json'},
            data=request
        )

        return response.text


def is_testrpc_available():
    try:
        import testrpc  # noqa: F401
        return True
    except ImportError:
        return False


class TestRPCProvider(RPCProvider):
    def __init__(self, host="127.0.0.1", port=8545, *args, **kwargs):
        if not is_testrpc_available():
            raise Exception("`TestRPCProvider` requires the `eth-testrpc` package to be installed")
        from gevent.pywsgi import WSGIServer
        from testrpc.server import application
        from testrpc.testrpc import evm_reset

        evm_reset()

        self.server = WSGIServer(
            (host, port),
            application,
        )

        self.thread = gevent.spawn(self.server.serve_forever)

        super(TestRPCProvider, self).__init__(host, str(port), *args, **kwargs)
