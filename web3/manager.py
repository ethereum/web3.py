import uuid
import warnings

from eth_utils import (
    is_list_like,
)

from web3.exceptions import (
    CannotHandleRequest,
    UnhandledRequest,
)
from web3.middleware import (
    wrap_provider_request,
    pythonic_middleware,
)

from web3.utils.compat import (
    spawn,
)


class RequestManager(object):
    def __init__(self, web3, providers, middlewares=None):
        self.web3 = web3
        self.pending_requests = {}
        self.providers = providers

        if middlewares is None:
            middlewares = [pythonic_middleware]

        self.middlewares = middlewares

    web3 = None
    middlewares = None
    _provider = None

    @property
    def providers(self):
        return self._provider

    @providers.setter
    def providers(self, value):
        if not is_list_like(value):
            providers = [value]
        else:
            providers = value
        self._provider = providers

    def setProvider(self, providers):
        warnings.warn(DeprecationWarning(
            "The `setProvider` API has been deprecated.  You should update your "
            "code to directly set the `manager.provider` property."
        ))
        self.providers = providers

    #
    # Provider requests and response
    #
    def _get_request_id(self):
        request_id = uuid.uuid4()
        return request_id

    def _make_request(self, method, params, request_id):
        for provider in self.providers:
            try:
                return wrap_provider_request(
                    middlewares=self.middlewares,
                    web3=self.web3,
                    make_request_fn=provider.make_request,
                    request_id=request_id,
                )(method, params)
            except CannotHandleRequest:
                continue
        else:
            raise UnhandledRequest(
                "No providers responded to the RPC request:\n"
                "method:{0}\n"
                "params:{1}\n"
                "request_id: {2}".format(
                    method,
                    params,
                    request_id
                )
            )

    def request_blocking(self, method, params, request_id=None):
        """
        Make a synchronous request using the provider
        """
        if request_id is None:
            request_id = self._get_request_id()

        response = self._make_request(method, params, request_id)

        if "error" in response:
            raise ValueError(response["error"])

        return response['result']

    def request_async(self, raw_method, raw_params):
        request_id = self._get_request_id()
        self.pending_requests[request_id] = spawn(
            self.request_blocking,
            raw_method=raw_method,
            raw_params=raw_params,
            request_id=request_id,
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
