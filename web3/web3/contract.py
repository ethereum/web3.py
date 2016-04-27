import web3.utils.utils as utils
import web3.utils.encoding as encoding
import web3.solidity.coder as coder
from web3.web3.function import SolidityFunction


def encodeConstructorParams(abi, params):
    """
    Should be called to encode constructor params
    """
    return [coder.encodeParams(json["type"], params) for json in abi
            if json["type"] == "constructor" and
            json["inputs"]["length"] == params["length"]][0] or ""


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
            options = args.pop()

        bytestring = encodeConstructorParams(self.abi, args)
        options["data"] += bytestring

        txhash = self.eth.sendTransaction(options)
        contract.transactionHash = txhash
        checkForContractAddress(contract)

        return contract

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
