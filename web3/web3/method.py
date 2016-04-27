import web3.utils.utils as utils
import web3.web3.exceptions as exceptions


class Method(object):

    def __init__(self, options):
        self.name = options.get("name")
        self.call = options.get("call")
        self.params = options.get("params", 0)
        self.inputFormatter = options.get("inputFormatter")
        self.outputFormatter = options.get("outputFormatter")
        self.requestManager = None

    def setRequestManager(self, rm):
        self.requestManager = rm

    def getCall(self, args):
        """
        Should be used to determine name of the jsonrpc method based on arguments

        @method getCall
        @param {Array} arguments
        @return {String} name of jsonrpc method
        """
        return self.call(args) if utils.isFunction(self.call) else self.call

    def validateArgs(self, args):
        """
        Should be called to check if the number of arguments is correct

        @method validateArgs
        @param {Array} arguments
        @throws {Error} if it is not
        """
        if len(args) != self.params:
            raise exceptions.InvalidNumberOfParamsException()

    def formatInput(self, args):
        """
        Should be called to format input args of method

        @method formatInput
        @param {Array}
        @return {Array}
        """
        if not self.inputFormatter:
            return args
        # print(self.name, args, self.inputFormatter)
        formatted = []
        for index, formatter in enumerate(self.inputFormatter):
            arg = args[index] if len(args) > index else None
            formatted.append(formatter(arg) if formatter else arg)
        return formatted

    def formatOutput(self, result):
        """
        Should be called to format output(result) of method

        @method formatOutput
        @param {Object}
        @return {Object}
        """
        if result and self.outputFormatter:
            return self.outputFormatter(result)
        else:
            return result

    def toPayload(self, args):
        """
        Should create payload from given input args

        @method toPayload
        @param {Array} args
        @return {Object}
        """
        call = self.getCall(args)
        params = self.formatInput(args)
        self.validateArgs(params)

        return {
            "method": call,
            "params": params,
        }

    def attachToObject(self, obj):
        func = self.buildCall()
        func.call = self.call
        name = self.name.split(".")
        # print(obj, self.name, func)
        if len(name) > 1:
            if not getattr(obj, name[0]):
                setattr(obj, name[0], object())
            setattr(getattr(obj, name[0]), name[1], func)
        else:
            setattr(obj, name[0], func)

    def buildCall(self):

        def send(*arguments, **kwargs):
            payload = self.toPayload(list(arguments))
            return self.formatOutput(self.requestManager.send(payload, *arguments, **kwargs))

        # send.request = self.request.bind(self)
        return send

    def request(self, *arguments):
        """
        Should be called to create pure JSONRPC request which can be used in batch request

        @method request
        @param {...} params
        @return {Object} jsonrpc request
        """
        payload = self.toPayload(list(arguments))
        payload["format"] = self.formatOutput
        return payload
