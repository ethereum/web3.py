from web3.providers import (
    BaseProvider,
)

from .middleware import (
    default_transaction_fields_middleware,
    ethereum_tester_fixture_middleware,
    ethereum_tester_middleware,
)


class EthereumTesterProvider(BaseProvider):
    middlewares = [
        default_transaction_fields_middleware,
        ethereum_tester_fixture_middleware,
        ethereum_tester_middleware,
    ]
    ethereum_tester = None
    api_endpoints = None

    def __init__(self, ethereum_tester=None, api_endpoints=None):
        if ethereum_tester is None:
            # do not import eth_tester until runtime, it is not a default dependency
            from eth_tester import EthereumTester
            self.ethereum_tester = EthereumTester()
        else:
            self.ethereum_tester = ethereum_tester

        if api_endpoints is None:
            # do not import eth_tester derivatives until runtime, it is not a default dependency
            from .defaults import API_ENDPOINTS
            self.api_endpoints = API_ENDPOINTS
        else:
            self.api_endpoints = api_endpoints

    def make_request(self, method, params):
        namespace, _, endpoint = method.partition('_')
        try:
            delegator = self.api_endpoints[namespace][endpoint]
        except KeyError:
            return {
                "error": "Unknown RPC Endpoint: {0}".format(method),
            }

        try:
            response = delegator(self.ethereum_tester, params)
        except NotImplementedError:
            return {
                "error": "RPC Endpoint has not been implemented: {0}".format(method),
            }
        else:
            return {
                'result': response,
            }

    def isConnected(self):
        return True
