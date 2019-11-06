import logging
import uuid

from eth_utils.toolz import (
    pipe,
)

from web3._utils.decorators import (
    deprecated_for,
)
from web3._utils.threads import (
    spawn,
)
from web3.datastructures import (
    NamedElementOnion,
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


def apply_error_formatters(
        error_formatters,
        response):

    if 'error' in response and error_formatters:
        formatted_response = pipe(response, error_formatters)
        return formatted_response
    else:
        return response


class RequestManager:
    logger = logging.getLogger("web3.RequestManager")

    def __init__(self, web3, provider=None, middlewares=None):
        self.web3 = web3
        self.pending_requests = {}

        if middlewares is None:
            middlewares = self.default_middlewares(web3)

        self.middleware_onion = NamedElementOnion(middlewares)

        if provider is None:
            self.provider = AutoProvider()
        else:
            self.provider = provider

    web3 = None
    _provider = None

    @property
    def provider(self):
        return self._provider

    @provider.setter
    def provider(self, provider):
        self._provider = provider

    @staticmethod
    def default_middlewares(web3):
        """
        List the default middlewares for the request manager.
        Leaving ens unspecified will prevent the middleware from resolving names.
        """
        return [
            (request_parameter_normalizer, 'request_param_normalizer'),  # Delete
            (gas_price_strategy_middleware, 'gas_price_strategy'),  # Add Async
            (name_to_address_middleware(web3), 'name_to_address'),  # Add Async
            (attrdict_middleware, 'attrdict'),  # Delete
            (pythonic_middleware, 'pythonic'),  # Delete
            (normalize_errors_middleware, 'normalize_errors'),  # Add async
            (validation_middleware, 'validation'),  # Add async
            (abi_middleware, 'abi'),  # Delete
        ]

    #
    # Provider requests and response
    #
    def _make_request(self, method, params):
        request_func = self.provider.request_func(
            self.web3,
            tuple(self.middleware_onion))
        self.logger.debug("Making request. Method: %s", method)
        return request_func(method, params)

    async def _coro_make_request(self, method, params):
        request_func = self.provider.request_func(
            self.web3,
            tuple(self.middleware_onion))
        self.logger.debug("Making request. Method: %s", method)
        return await request_func(method, params)

    def request_blocking(self, method, params, error_formatters=None):
        """
        Make a synchronous request using the provider
        """
        response = self._make_request(method, params)

        if "error" in response:
            apply_error_formatters(error_formatters, response)
            raise ValueError(response["error"])

        return response['result']

    async def coro_request(self, method, params, error_formatters=None):
        """
        Couroutine for making a request using the provider
        """
        response = await self._coro_make_request(method, params)

        if "error" in response:
            apply_error_formatters(error_formatters, response)
            raise ValueError(response["error"])

        if response['result'] is None:
            raise ValueError(f"The call to {method} did not return a value.")

        return response['result']

    @deprecated_for("coro_request")
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
