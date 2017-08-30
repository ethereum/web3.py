from cytoolz.functoolz import (
    compose,
    complement,
)

from eth_utils import (
    is_integer,
    is_string,
    decode_hex,
)

from web3.middleware import (
    construct_formatting_middleware,
    construct_exception_handler_middleware,
)

from web3.utils.compat import (
    make_server,
    spawn,
)
from web3.utils.formatters import (
    hex_to_integer,
    apply_formatter_if,
    apply_formatter_at_index,
    apply_formatters_to_dict,
)

from .base import BaseProvider  # noqa: E402
from .rpc import HTTPProvider  # noqa: E402


def is_testrpc_available():
    try:
        import testrpc  # noqa: F401
        return True
    except ImportError:
        return False


def static_return(value):
    def inner(*args, **kwargs):
        return value
    return inner


def static_result(value):
    def inner(*args, **kwargs):
        return {'result': value}
    return inner


to_integer_if_hex = apply_formatter_if(hex_to_integer, is_string)


TRANSACTION_FORMATTERS = {
    'to': apply_formatter_if(
        static_return(None),
        compose(complement(bool), decode_hex),
    ),
}


ethtestrpc_middleware = construct_formatting_middleware(
    request_formatters={
        'eth_uninstallFilter': apply_formatter_at_index(to_integer_if_hex, 0),
        'eth_getFilterChanges': apply_formatter_at_index(to_integer_if_hex, 0),
        'eth_getFilterLogs': apply_formatter_at_index(to_integer_if_hex, 0),
    },
    result_formatters={
        # Eth
        'eth_newFilter': apply_formatter_if(hex, is_integer),
        'eth_protocolVersion': apply_formatter_if(str, is_integer),
        'eth_getTransactionByHash': apply_formatters_to_dict(TRANSACTION_FORMATTERS),
        # Net
        'net_version': apply_formatter_if(str, is_integer),
    },
)


return_none_result = static_result(None)


ethtestrpc_exception_middleware = construct_exception_handler_middleware(
    method_handlers={
        'eth_getBlockByHash': (ValueError, return_none_result),
        'eth_getBlockByNumber': (ValueError, return_none_result),
    },
)


class EthereumTesterProvider(BaseProvider):
    middlewares = [ethtestrpc_middleware, ethtestrpc_exception_middleware]

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
    middlewares = [ethtestrpc_middleware, ethtestrpc_exception_middleware]

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
