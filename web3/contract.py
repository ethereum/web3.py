"""
new web3.eth.contract(abi, address);
> {
   address: '0x123456...',
   deploy: function(options){...},
   encodeABI: function(options){...},
   // events
   on: function(event, options, callback){...},
   pastEvents:  function(event, options, callback){...},
   // methods
   estimateGas: function(options){...},
   call: function(options){...},
   transact: function(options){...}
}
"""


class _Contract(object):
    # set during class construction
    web3 = None

    _abi = None
    _code = None
    _code_runtime = None
    _source = None

    # class properties
    address = None

    def __init__(self, abi=None, address=None, code=None, code_runtime=None, source=None):
        if self.web3 is None:
            raise AttributeError('The `Contract` class has not been initialized.  Please use the `web3.contract` interface to create your contract class.')
        self._abi = abi
        self._code = code
        self._code_runtime = code_runtime
        self._source = source
        self.address = address

    @property
    def abi(self):
        if self._abi is not None:
            return self._abi
        # TODO: abi can be derived from the contract source.
        raise AttributeError("No contract abi was specified for thes contract")

    @property
    def code(self):
        if self._code is not None:
            return self._code
        # TODO: code can be derived from the contract source.
        raise AttributeError("No contract code was specified for thes contract")

    @property
    def code_runtime(self):
        if self._code_runtime is not None:
            return self._code_runtime
        # TODO: runtime can be derived from the contract source.
        raise AttributeError("No contract code_runtime was specified for thes contract")

    @property
    def source(self):
        if self._source is not None:
            return self._source
        raise AttributeError("No contract source was specified for thes contract")

    def deploy(self, transaction):
        """
        deploys the contract.
        """
        raise NotImplementedError('Not implemented')

    def encodeABI(self, method, arguments, data=None):
        """
        encodes the arguments using the Ethereum ABI.
        """
        raise NotImplementedError('Not implemented')

    def on(self, event, filters, callback):
        """
        register a callback to be triggered on the appropriate events.
        """
        raise NotImplementedError('Not implemented')

    def pastEvents(self, event, filters, callback):
        """
        register a callback to be triggered on all past events.
        """
        raise NotImplementedError('Not implemented')

    def estimateGas(self, *args, **kwargs):
        """
        Estimate the gas for a call
        """
        raise NotImplementedError('Not implemented')

    def call(self, *args, **kwargs):
        """
        Execute a contract function call using the `eth_call` interface.
        """
        raise NotImplementedError('Not implemented')

    def transact(self, *args, **kwargs):
        """
        Execute a contract function call using the `eth_sendTransaction` interface.
        """
        raise NotImplementedError('Not implemented')


def construct_contract_class(web3, abi, address=None, code=None,
                             code_runtime=None, source=None):
    _dict = {
        'web3': web3,
        'address': address,
        'abi': abi,
        'code': code,
        'code_runtime': code_runtime,
        'source', source,
    }
    return type('Contract', (_Contract,), _dict)
