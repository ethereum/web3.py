import json

class Jsonrpc(object):

    def toPayload(self, reqid, method, params):
        """
        Should be called to valid json create payload object
        """
        if not method:
            raise Exception("jsonrpc method should be specified!")

        return json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": reqid
        })

    def fromPayload(self, raw):
        result = json.loads(raw)
        if not Jsonrpc.isValidResponse(result):
            raise errors.InvalidResponse(result)
        return result

    def isValidResponse(self, response):
        """
        Should be called to check if jsonrpc response is valid
        """
        return response is not None and not response["error"] and \
                response["jsonrpc"] == "2.0" and \
                utils.isInteger(response["id"]) and \
                response["result"] is not None

    # def toBatchPayload(self, messages):
    #    return [self.toPayload(message["method"], message["params"]) for]