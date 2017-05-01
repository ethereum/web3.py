import json
import uuid

from eth_utils import (
    force_text,
    is_dict,
    is_string,
)

from web3.utils.compat import (
    spawn,
)


class RequestManager(object):
    def __init__(self, provider):
        self.pending_requests = {}
        self.provider = provider

    def setProvider(self, provider):
        self.provider = provider

    def request_blocking(self, method, params):
        """
        Make a synchronous request using the provider
        """
        response_raw = self.provider.make_request(method, params)

        if is_string(response_raw):
            response = json.loads(force_text(response_raw))
        elif is_dict(response_raw):
            response = response_raw

        if "error" in response:
            raise ValueError(response["error"])

        return response['result']

    def request_async(self, method, params):
        request_id = uuid.uuid4()
        self.pending_requests[request_id] = spawn(
            self.request_blocking,
            method,
            params,
        )
        return request_id

    def receive_blocking(self, request_id, timeout=None):
        try:
            request = self.pending_requests.pop(request_id)
        except KeyError:
            raise KeyError("Request for id:{0} not found".format(request_id))
        else:
            response_raw = request.get(timeout=timeout)

        response = json.loads(response_raw)

        if "error" in response:
            raise ValueError(response["error"])

        return response['result']

    def receive_async(self, request_id, *args, **kwargs):
        raise NotImplementedError("Callback pattern not implemented")
