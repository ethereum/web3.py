import web3.web3.utils.utils as utils
import web3.utils.abi as abi
import web3.solidity.coder as coder
import web3.web3.web3.formatters as formatters
from web3.utils.crypto import sha3


class SolidityEvent(object):

    def __init__(self, requestManager, json, address):
        self._requestManager = requestManager
        self._params = json["inputs"]
        self._name = abi.transformToFullname(json)
        self._address = address
        self._anonymous = json["anonymous"]

    def types(self, indexed):
        """
        Should be used to get filtered param types
        """
        return [i["type"] for i in self._params if i["indexed"] == indexed]

    def displayName(self):
        """
        Should be used to get event display name
        """
        return abi.extractDisplayName(self._name)

    def typeName(self):
        """
        Should be used to get event type name
        """
        return abi.extractTypeName(self._name)

    def signature(self):
        return sha3(self._name)

    def encode(self, indexed={}, options={}):
        """
        Should be used to encode indexed params and options to one final object
        """
        result = {}

        for f in ["fromBlock", "toBlock"]:
            if f in options:
                result[f] = formatters.inputBlockNumberFormatter(options[f])

        result["topics"] = []
        result["address"] = self._address

        if not self._anonymous:
            result["topics"].append("0x" + self.signature())

        indexedTopics = []

        for i in self._params:
            if i["indexed"]:
                value = indexed.get(i["name"])
                if value is None:
                    indexedTopics.append(None)
                    continue

                if utils.isArray(value):
                    indexedTopics.append(
                        ["0x" + coder.encodeParam(i["type", v]) for v in value])
                    continue

                indexedTopics.append(
                    "0x" + coder.encodeParam(i["type"], value))

        result["topics"] = result["topics"] + indexedTopics
        return result
