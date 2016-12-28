import json


class InvalidNumberOfParamsException(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid number of input parameters")


class InvalidConnectionException(Exception):
    def __init__(self, host="?"):
        Exception.__init__(self, "CONNECTION ERROR: Couldn't connect to node " + host + ".")


class InvalidProviderException(Exception):
    def __init__(self):
        Exception.__init__(self, "Provider not set or invalid")


class InvalidResponseException(Exception):
    def __init__(self, result):
        if isinstance(result, dict) and result["error"] and result["error"]["message"]:
            message = result["error"]["message"]
        else:
            message = "Invalid JSON RPC response: " + json.dumps(result)
        Exception.__init__(self, message)


class BadFunctionCallOutput(Exception):
    """We failed to decode ABI output.

    Most likely ABI mismatch.
    """
