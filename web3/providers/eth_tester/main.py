from web3.providers import (
    BaseProvider,
)

from .middleware import (
    default_transaction_fields_middleware,
    ethereum_tester_middleware,
)


class AsyncEthereumTesterProvider(BaseProvider):
    """This is a placeholder.

    For now its purpose is to provide an awaitable request function
    for testing the async api execution.
    """
    def __init__(self):
        self.eth_tester = EthereumTesterProvider()

    async def make_request(self, method, params):
        return self.eth_tester.make_request(method, params)


class EthereumTesterProvider(BaseProvider):
    middlewares = [
        default_transaction_fields_middleware,
        ethereum_tester_middleware,
    ]
    ethereum_tester = None
    api_endpoints = None

    def __init__(self, ethereum_tester=None, api_endpoints=None):
        # do not import eth_tester until runtime, it is not a default dependency
        from eth_tester import EthereumTester
        from eth_tester.backends.base import BaseChainBackend
        if ethereum_tester is None:
            self.ethereum_tester = EthereumTester()
        elif isinstance(ethereum_tester, EthereumTester):
            self.ethereum_tester = ethereum_tester
        elif isinstance(ethereum_tester, BaseChainBackend):
            self.ethereum_tester = EthereumTester(ethereum_tester)
        else:
            raise TypeError(
                "Expected ethereum_tester to be of type `eth_tester.EthereumTester` or "
                "a subclass of `eth_tester.backends.base.BaseChainBackend`, "
                f"instead received {type(ethereum_tester)}. "
                "If you would like a custom eth-tester instance to test with, see the "
                "eth-tester documentation. https://github.com/ethereum/eth-tester."
            )

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
