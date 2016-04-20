import web3.web3.errors as errors
from web3.web3.jsonrpc import Jsonrpc
import time

class RequestManager(object):

    def __init__(self, provider):
        self.provider = provider

    def setProvider(self, provider):
        """Should be used to set provider of request manager"""
        self.provider = provider

    def send(self, data):
        """Should be used to synchronously send request"""
        requestid = self.sendAsync(payload)
        result = self.receiveAsync(requestid, timeout=None)

        if not Jsonrpc.isValidResponse(result):
            raise errors.InvalidResponse(result)

        return result["result"]

    def sendAsync(self, data):
        """Should be used to asynchronously send request"""
        if not self.provider:
            raise errors.InvalidProvider()

        payload = Jsonrpc.toPayload(data["method"], data["params"])
        requestid = payload["messageId"]
        self.provider.requests.put(payload)

        return requestid

    def receiveAsync(self, requestid, timeout=0):
        start = time.time()

        while True:

            if requestid in self.provider.responses:
                return self.provider.pop(requestid)

            if timeout is not None and time.time()-start >= timeout:
                if timeout == 0:
                    return None
                else:
                    raise ValueError("Timeout waiting for {0}".format(requestid))
