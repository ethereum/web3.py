import web3.web3.exceptions as exceptions
from web3.web3.jsonrpc import Jsonrpc

import uuid
import gevent




class RequestManager(object):
    def __init__(self, provider):
        self.pending_requests = {}
        self.provider = provider

    def request_blocking(self, method, params):
        """
        Make a synchronous request using the provider
        """
        return self.provider.make_request(method, params)

    def request_async(self, method, params):
        request_id = uuid.uuid4()
        self.pending_requests[request_id] = gevent.spawn(self.request_blocking, method, params)
        return request_id

    def receive_blocking(self, request_id, timeout=None):
        try:
            request = self.pending_requests.pop(request_id)
        except KeyError:
            raise KeyError("Request for id:{0} not found".format(request_id))
        else:
            if timeout is not None:
                timeout = gevent.Timeout(timeout).start()
            return request.get(timeout=timeout)

    def receive_async(self, request_id, *args, **kwargs):
        raise NotImplementedError("Callback pattern not implemented")
