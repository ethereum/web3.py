import web3.solidity.coder
import web3.utils.utils as utils
import web3.formatters as formatters
from web3.utils.crypto import sha3

class SolidityFunction(object):

    def __init__(self, eth, json, address):
        self._eth = eth
        self._inputTypes = [i.type for i in json["inputs"]]
        self._outputTypes = [o.type for o in json["outputs"]]
        self._constant = json["constant"]
        self._name = utils.transformToFullName(json)
        self._address = address 

    def extractDefaultBlock(self, args):
        if (len(args) > len(self._inputTypes) and utils.isObject(args[-1])):
            return formatters.inputDefaultBlockNumberFormatter(args.pop())

    def toPayload(self, args):
        """
        Should be used to create payload from arguments
        """
        options = {}
        if len(args) > self._inputTypes and utils.isObject(args[-1]):
            options = args[-1]
        options["to"] = self._address
        options["data"] = "0x" + self.signature() + coder.encodeParams(self._inputTypes, args)
        return options

    def signature(self):
        """
        Should be used to get function signature
        """
        return sha3(self._name)[:8]

    def unpackOutput(self, output):
        if not output:
            return

        if len(output) >= 2:
            output = output[2:]

        result = coder.decodeParams(self._outputTypes, output)

        if len(result) == 1:
            return result[0]

        return result

    def call(self, *arguments):
        """
        Calls a contract function.
        """
        args = [a for a in arguments if a]
        defaultBlock = self.extractDefaultBlock(args)
        payload = self.toPayload(args)

        output = self._eth.call(payload, defaultBlock)
        return self.unpackOutput(output)

    def sendTransaction(self, *arguments):
        """
        Should be used to sendTransaction to solidity function
        """
        args = [a for a in arguments if a]
        payload = self.toPayload(args)

        return self._eth.sendTransaction(payload)

    def estimateGas(self, *arguments):
        """
        Should be used to estimateGas of solidity function
        """
        args = [a for a in arguments if a]
        payload = self.toPayload(args)

        return self._eth.estimateGas(payload)

    def getData(self, *arguments):
        """
        Return the encoded data of the call
        """
        args = [a for a in arguments if a]
        payload = self.toPayload(args)

        return payload["data"]

    def displayName(self):
        """
        Should be used to get function display name
        """
        return utils.extractDisplayName(self._name)

    def typeName(self):
        """
        Should be used to get function type name
        """
        return utils.extractTypeName(self._name)

    def request(self, *arguments):
        """
        Should be called to get rpc requests from solidity function
        """
        return {
            "method": "eth_call" if self._constant else "eth_sendTransaction"
            "params": [self.toPayload(arguments)],
            "format": self.unpackOutput
        }

    def execute(self, *arguments):
        transaction = not self._constant

        if transaction:
            return self.sendTransaction(arguments)
        else:
            return self.call(arguments)

    def attachToContract(self, contract):
        displayName = self.displayName()
        # still missing arguments here
        if not getattr(contract, displayName):
            setattr(contract, displayName, execute)
        setattr(getattr(contract, displayName), self.typeName(), execute)