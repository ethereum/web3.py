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
import functools

from eth_abi import (
    encode_abi,
)

from web3.utils.encoding import (
    encode_hex,
)
from web3.utils.formatting import (
    add_0x_prefix,
    remove_0x_prefix,
)
from web3.utils.string import (
    force_bytes,
    coerce_return_to_text,
)
from web3.utils.functional import (
    compose,
)
from web3.utils.abi import (
    filter_by_type,
    filter_by_name,
    filter_by_encodability,
    get_abi_types,
)


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

    #
    # ABI Helpers
    #
    @classmethod
    def find_matching_abi(cls, fn_name, arguments):
        filter_fn = compose(
            functools.partial(filter_by_type, 'function'),
            functools.partial(filter_by_name, fn_name),
            functools.partial(filter_by_encodability, arguments),
        )
        matches = filter_fn(cls.abi)
        if len(matches) == 1:
            return matches[0]
        elif len(matches) == 0:
            raise ValueError("No matching functions found")
        else:
            raise ValueError("Multiple functions found")

    @classmethod
    @coerce_return_to_text
    def encodeABI(cls, fn_name, arguments, data=None):
        """
        encodes the arguments using the Ethereum ABI.
        """
        function_abi = cls.find_matching_abi(fn_name, arguments)
        function_types = get_abi_types(function_abi)
        encoded_arguments = encode_abi(function_types, arguments)
        if data:
            return add_0x_prefix(
                force_bytes(remove_0x_prefix(data)) +
                force_bytes(remove_0x_prefix(encode_hex(encoded_arguments)))
            )
        else:
            return encode_hex(encoded_arguments)

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
        'source': source,
    }
    return type('Contract', (_Contract,), _dict)
