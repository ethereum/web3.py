from wsgiref.simple_server import (
    make_server,
)

from eth_utils import (
    decode_hex,
    is_integer,
    is_string,
    to_text,
)

from web3.middleware import (
    construct_exception_handler_middleware,
    construct_formatting_middleware,
)
from web3.utils.decorators import (
    deprecated_for,
)
from web3.utils.formatters import (
    apply_formatter_at_index,
    apply_formatter_if,
    apply_formatters_to_dict,
    hex_to_integer,
    static_result,
    static_return,
)
from web3.utils.threads import (
    spawn,
)
from web3.utils.toolz import (
    complement,
    compose,
    valmap,
)

from .base import (
    BaseProvider,
)
from .rpc import (
    HTTPProvider,
)


def is_testrpc_available():
    try:
        import testrpc  # noqa: F401
        return True
    except ImportError:
        return False


to_integer_if_hex = apply_formatter_if(is_string, hex_to_integer)


TRANSACTION_FORMATTERS = {
    'to': apply_formatter_if(
        compose(complement(bool), decode_hex),
        static_return(None),
    ),
}


def ethtestrpc_string_middleware(make_request, web3):
    def middleware(method, params):
        return valmap(to_text, make_request(method, params))
    return middleware


ethtestrpc_middleware = construct_formatting_middleware(
    request_formatters={
        'eth_uninstallFilter': apply_formatter_at_index(to_integer_if_hex, 0),
        'eth_getFilterChanges': apply_formatter_at_index(to_integer_if_hex, 0),
        'eth_getFilterLogs': apply_formatter_at_index(to_integer_if_hex, 0),
    },
    result_formatters={
        # Eth
        'eth_newFilter': apply_formatter_if(is_integer, hex),
        'eth_protocolVersion': apply_formatter_if(is_integer, str),
        'eth_getTransactionByHash': apply_formatters_to_dict(TRANSACTION_FORMATTERS),
        # Net
        'net_version': apply_formatter_if(is_integer, str),
    },
)


return_none_result = static_result(None)


ethtestrpc_exception_middleware = construct_exception_handler_middleware(
    method_handlers={
        'eth_getBlockByHash': (ValueError, static_result(None)),
        'eth_getBlockByNumber': (ValueError, static_result(None)),
    },
)


def ethereum_tester_personal_remapper_middleware(make_request, web3):
    def middleware(method, params):
        if method == 'personal_sendTransaction':
            return make_request('personal_signAndSendTransaction', params)
        else:
            return make_request(method, params)
    return middleware


class EthereumTesterProvider(BaseProvider):
    middlewares = [
        ethtestrpc_middleware,
        ethtestrpc_string_middleware,
        ethtestrpc_exception_middleware,
        ethereum_tester_personal_remapper_middleware,
    ]

    @deprecated_for("web3.providers.eth_tester.EthereumTesterProvider")
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

    @deprecated_for("web3.providers.eth_tester.EthereumTesterProvider")
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

        super().__init__(endpoint_uri, *args, **kwargs)
