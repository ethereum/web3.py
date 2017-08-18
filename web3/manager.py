import uuid
import warnings

from web3.middleware import (
    wrap_provider_request,
)

from web3.utils.compat import (
    spawn,
)


class RequestManager(object):
    def __init__(self, provider):
        self.pending_requests = {}
        self.provider = provider

    middlewares = None
    _provider = None

    @property
    def provider(self):
        return self._provider

    @provider.setter
    def provider(self, value):
        self._provider = value
        self.middlewares = tuple(
            middleware_class(value)
            for middleware_class
            in self.provider.get_middleware_classes()
        )

    def setProvider(self, provider):
        warnings.warn(DeprecationWarning(
            "The `setProvider` API has been deprecated.  You should update your "
            "code to directly set the `manager.provider` property."
        ))
        self.provider = provider

    #
    # Provider requests and response
    #
    def _get_request_id(self):
        request_id = uuid.uuid4()
        return request_id

    def _make_request(self, method, params, request_id):
        return wrap_provider_request(
            middlewares=self.middlewares,
            request_fn=self.provider.make_request,
            request_id=request_id,
        )((method, params))

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
