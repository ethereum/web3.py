import web3.exceptions as exceptions
from web3.jsonrpc import Jsonrpc
import time

class RequestManager(object):

    def __init__(self, provider):
        self.provider = provider
        self.reqid = 0

    def setProvider(self, provider):
        """Should be used to set provider of request manager"""
        self.provider = provider

    def send(self, data, *args, **kwargs):
        """Should be used to synchronously send request"""

        if not "timeout" in kwargs:
            timeout = None
        else:
            timeout = kwargs["timeout"]

        requestid = self.forward(data)

        if timeout == 0:
            return requestid

        result = self.receive(requestid, timeout)
        return result["result"]

    def forward(self, data):
        """Should be used to asynchronously send request"""
        if not self.provider:
            raise errors.InvalidProvider()

        self.reqid += 1
        self.provider.requests.put(Jsonrpc.toPayload(self.reqid, data["method"], data["params"]))

        return self.reqid

    def receive(self, requestid, timeout=0):
        start = time.time()

        while True:

            if requestid in self.provider.responses:
                return Jsonrpc.fromPayload(self.provider.responses.pop(requestid))

            if timeout is not None and time.time()-start >= timeout:
                if timeout == 0:
                    return None
                else:
                    raise ValueError("Timeout waiting for {0}".format(requestid))
