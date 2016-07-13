import json
import web3.web3.exceptions as exceptions
import web3.utils.utils as utils
import six


class Jsonrpc(object):

    @staticmethod
    def toPayload(reqid, method, params):
        """
        Should be called to valid json create payload object
        """
        if not method:
            raise Exception("jsonrpc method should be specified!")

        rawrequest = json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": reqid
        })

        if six.PY3:
            rawrequest = rawrequest.encode("utf8")
        return (reqid, rawrequest)

    @staticmethod
    def fromPayload(raw):
        try:
            result = json.loads(raw)
        except IndexError:
            raise exceptions.InvalidResponseException("Invalid response")

        if not Jsonrpc.isValidResponse(result):
            raise exceptions.InvalidResponseException(result)
        return result

    @staticmethod
    def isValidResponse(response):
        """
        Should be called to check if jsonrpc response is valid
        """
        return response is not None and "error" not in response and \
            response["jsonrpc"] == "2.0" and \
            utils.isInteger(response["id"]) and \
            response["result"] is not None

    # def toBatchPayload(self, messages):
    #    return [self.toPayload(message["method"], message["params"]) for]
