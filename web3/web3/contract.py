import web3.utils.utils as utils
import web3.utils.encoding as encoding
from web3.solidity.coder import coder
from web3.web3.function import SolidityFunction


def encodeConstructorParams(abi, params):
    """
    Should be called to encode constructor params
    """
    for json in abi:
        if json["type"] == "constructor" and len(json["inputs"]) == len(params):
                types = tuple(inp["type"] for inp in json["inputs"])
                return coder.encodeParams(types, params)
    return ""


def addFunctionsToContract(contract):
    """
    Should be called to add functions to contract object
    """
    for json in contract.abi:
        if json["type"] == "function":
            f = SolidityFunction(contract._eth, json, contract.address)
            f.attachToContract(contract)


'''
def addEventsToContract(contract):
    """
    Should be called to add events to contract object
    """
    events = [json for json in contract.abi if json["type"] == "event"]

    All = AllEvents(contract._eth._requestManager, events, contract.address)
    All.attachToContract(contract)

    for json in events:
        evt = SolidityEvent(
            contract._eth._requestManager, json, contract.address)
        evt.attachToContract(contract)
'''


def checkForContractAddress(contract):
    """
    Should be called to check if the contract gets properly deployed on the blockchain.
    """
    raise NotImplementedError()


class ContractFactory(object):
    def __init__(self, eth, abi):
        self.eth = eth

        if utils.isString(abi):
            abi = encoding.abiToJson(abi)
        self.abi = abi

    def new(self, *args):
        """
        Should be called to create new contract on a blockchain
        """
        contract = Contract(self.eth, self.abi)

        options = {}

        if utils.isObject(args[-1]) and not utils.isArray(args[-1]):
            options = args[-1]

        bytestring = encodeConstructorParams(self.abi, args[:-1])
        options["data"] += bytestring

        txhash = self.eth.sendTransaction(options)
        contract.transactionHash = txhash
        # TODO: Implement check for contract address.
        # checkForContractAddress(contract)

        return txhash

    def at(self, address):
        contract = Contract(self.eth, self.abi, address)

        addFunctionsToContract(contract)
        # addEventsToContract(contract)

        return contract


class Contract(object):
    def __init__(self, eth, abi, address=None):
        self._eth = eth
        self.transactionhash = None
        self.address = address
        self.abi = abi
