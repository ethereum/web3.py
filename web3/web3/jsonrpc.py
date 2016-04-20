class Jsonrpc(object):

    def __init__(self):
        self.messageId = 0

    @staticmethod
    def getInstance():
        return Jsonrpc()

    def toPayload(self, method, params):
        """
        Should be called to valid json create payload object
        """
        if not method:
            raise Exception("jsonrpc method should be specified!")

        self.messageId += 1

        return {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": self.messageId
        }

    def isValidResponse(self, response):
        """
        Should be called to check if jsonrpc response is valid
        """
        return response is not None and not response["error"] and \
                response["jsonrpc"] == "2.0" and \
                utils.isInteger(response["id"]) and \
                response["result"] is not None

    def toBatchPayload(self, messages):
        return [self.toPayload(message["method"], message["params"]) for]