import logging
import uuid

from eth_utils import (
    is_list_like,
)

from web3.datastructures import (
    NamedElementOnion,
)
from web3.exceptions import (
    CannotHandleRequest,
    UnhandledRequest,
)
from web3.middleware import (
    abi_middleware,
    attrdict_middleware,
    gas_price_strategy_middleware,
    name_to_address_middleware,
    normalize_errors_middleware,
    pythonic_middleware,
    request_parameter_normalizer,
    validation_middleware,
)
from web3.providers import (
    AutoProvider,
)
from web3.utils.empty import (
    empty,
)
from web3.utils.threads import (
    spawn,
)


class RequestManager:
    logger = logging.getLogger("web3.RequestManager")

    def __init__(self, web3, providers, middlewares=None):
        self.web3 = web3
        self.pending_requests = {}

        if middlewares is None:
            middlewares = self.default_middlewares(web3)

        self.middleware_stack = NamedElementOnion(middlewares)
        if providers is empty:
            self.providers = AutoProvider()
        else:
            self.providers = providers

    web3 = None
    _providers = None

    @property
    def providers(self):
        return self._providers or tuple()

    @providers.setter
    def providers(self, value):
        if not is_list_like(value):
            providers = [value]
        else:
            providers = value
        self._providers = providers

    @staticmethod
    def default_middlewares(web3):
        '''
        List the default middlewares for the request manager.
        Leaving ens unspecified will prevent the middleware from resolving names.
        '''
        return [
            (request_parameter_normalizer, 'request_param_normalizer'),
            (gas_price_strategy_middleware, 'gas_price_strategy'),
            (name_to_address_middleware(web3), 'name_to_address'),
            (attrdict_middleware, 'attrdict'),
            (pythonic_middleware, 'pythonic'),
            (normalize_errors_middleware, 'normalize_errors'),
            (validation_middleware, 'validation'),
            (abi_middleware, 'abi'),
        ]

    #
    # Provider requests and response
    #
    def _make_request(self, method, params):
        for provider in self.providers:
            request_func = provider.request_func(self.web3, tuple(self.middleware_stack))
            self.logger.debug("Making request. Method: %s", method)
            try:
                return request_func(method, params)
            except CannotHandleRequest:
                continue
        else:
            raise UnhandledRequest(
                "No providers responded to the RPC request:\n"
                "method:{0}\n"
                "params:{1}\n".format(
                    method,
                    params,
                )
            )

    def request_blocking(self, method, params):
        """
        Make a synchronous request using the provider
        """
        response = self._make_request(method, params)

        if "error" in response:
            raise ValueError(response["error"])

        return response['result']

    def request_async(self, raw_method, raw_params):
        request_id = uuid.uuid4()
        self.pending_requests[request_id] = spawn(
            self.request_blocking,
            raw_method=raw_method,
            raw_params=raw_params,
        )
        return request_id

    def receive_blocking(self, request_id, timeout=None):
        try:
            request = self.pending_requests.pop(request_id)
        except KeyError:
            raise KeyError("Request for id:{0} not found".format(request_id))
        else:
            response = request.get(timeout=timeout)

        if "error" in response:
            raise ValueError(response["error"])

        return response['result']

    def receive_async(self, request_id, *args, **kwargs):
        raise NotImplementedError("Callback pattern not implemented")
