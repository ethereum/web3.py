import json
import web3.exceptions as exceptions
import utils.utils as utils

class Jsonrpc(object):

    @staticmethod
    def toPayload(reqid, method, params):
        """
        Should be called to valid json create payload object
        """
        if not method:
            raise Exception("jsonrpc method should be specified!")

        return (reqid, json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": reqid
        }))

    @staticmethod
    def fromPayload(raw):
        try:
            result = json.loads(raw)
        except TypeError:
            raise exceptions.InvalidResponseException("Invalid response")

        if not Jsonrpc.isValidResponse(result):
            raise exceptions.InvalidResponseException(result)
        return result

    @staticmethod
    def isValidResponse(response):
        """
        Should be called to check if jsonrpc response is valid
        """
        return response is not None and not "error" in response and \
                response["jsonrpc"] == "2.0" and \
                utils.isInteger(response["id"]) and \
                response["result"] is not None

    # def toBatchPayload(self, messages):
    #    return [self.toPayload(message["method"], message["params"]) for]