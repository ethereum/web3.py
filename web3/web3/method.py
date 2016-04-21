import utils.utils
import errors


class Method(object):

    def __init__(self, options):
        self.name = options["name"]
        self.call = options["call"]
        self.params = options["params"] if "params" in options else 0
        self.inputFormatter = options["inputFormatter"]
        self.outputFormatter = options["outputFormatter"]
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

    def extractCallback(self, args):
        """
        Should be used to extract callback from array of arguments. Modifies input param

        @method extractCallback
        @param {Array} arguments
        @return {Function|Null} callback, if exists
        """
        if utils.isFunction(args[-1]):
            return args[:-1]

    def validateArgs(self, args):
        """
        Should be called to check if the number of arguments is correct

        @method validateArgs
        @param {Array} arguments
        @throws {Error} if it is not
        """
        if len(args) != self.params:
            raise errors.InvalidNumberOfParams()

    def formatInput(self, args):
        """
        Should be called to format input args of method

        @method formatInput
        @param {Array}
        @return {Array}
        """
        if not self.inputFormatter:
            return args

        return self.inputFormatter.map(lambda formatter, index:
                formatter(args[index]) if formatter else args[index])

    def formatOutput(self, result):
        """
        Should be called to format output(result) of method

        @method formatOutput
        @param {Object}
        @return {Object}
        """
        return self.outputFormatter and self.outputFormatter(result) if result else result

    def toPayload(self, args):
        """
        Should create payload from given input args

        @method toPayload
        @param {Array} args
        @return {Object}
        """
        call = self.getCall(args)
        callback = self.extractCallback(args)
        params = self.formatInput(args)
        self.validateArgs(params)

        return {
            "method": call,
            "params": params,
            "callback": callback
        }

    def attachToObject(self, obj):
        func = self.buildCall()
        func.call = self.call
        name = self.name.split(".")
        if len(name) > 1:
            obj[name[0]] = obj[name[0]] if name[0] in obj else {}
            obj[name[0]][name[1]] = func
        else:
            obj[name[0]] = func

    def buildCall(self):
        method = self

        def send(*arguments):
            payload = method.toPayload(list(arguments))
            if "callback" in payload:
                return method.requestManager.sendAsync(payload,
                        lambda err, result: payload.callback(err, method.formatOutput(result)))

            return method.formatOutput(method.requestManager.send(payload))

        send.request = self.request.bind(self)
        return send

    def request(self, *arguments):
        """
        Should be called to create pure JSONRPC request which can be used in batch request

        @method request
        @param {...} params
        @return {Object} jsonrpc request
        """
        payload = self.toPayload(list(arguments))
        payload.format = self.formatOutput.bind(self)
        return payload
