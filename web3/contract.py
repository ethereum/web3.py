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
    decode_abi,
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
    force_obj_to_bytes,
)
from web3.utils.abi import (
    filter_by_type,
    filter_by_name,
    filter_by_argument_count,
    filter_by_encodability,
    get_abi_input_types,
    get_abi_output_types,
    get_constructor_abi,
    check_if_arguments_can_be_encoded,
    function_abi_to_4byte_selector,
)


class _Contract(object):
    # set during class construction
    web3 = None

    # class properties (overridable at instance level)
    _abi = None
    _code = None
    _code_runtime = None
    _source = None

    # instance level properties
    address = None

    def __init__(self, abi=None, address=None, code=None, code_runtime=None, source=None):
        if self.web3 is None:
            raise AttributeError(
                'The `Contract` class has not been initialized.  Please use the '
                '`web3.contract` interface to create your contract class.'
            )
        if abi is not None:
            self._abi = abi
        if code is not None:
            self._code = code
        if code_runtime is not None:
            self._code_runtime = code_runtime
        if source is not None:
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

    @classmethod
    def deploy(cls, transaction=None, arguments=None):
        """
        deploys the contract.
        """
        if transaction is None:
            transaction = {}

        if not cls.code:
            raise ValueError(
                "Cannot deploy a contract that does not have 'code' associated with it"
            )
        if 'data' in transaction:
            raise ValueError(
                "Cannot specify `data` for contract deployment"
            )
        if 'to' in transaction:
            raise ValueError(
                "Cannot specify `to` for contract deployment"
            )

        transaction['data'] = cls.encodeConstructorData(arguments)

        # TODO: handle asynchronous contract creation
        txn_hash = cls.web3.eth.sendTransaction(transaction)
        return txn_hash

    #
    # ABI Helpers
    #
    @classmethod
    def find_matching_abi(cls, fn_name, arguments):
        filters = [
            functools.partial(filter_by_name, fn_name),
            functools.partial(filter_by_argument_count, arguments),
            functools.partial(filter_by_encodability, arguments),
        ]

        function_candidates = filter_by_type('function', cls.abi)

        for filter_fn in filters:
            function_candidates = filter_fn(function_candidates)

            if len(function_candidates) == 1:
                return function_candidates[0]
            elif not function_candidates:
                break

        if not function_candidates:
            raise ValueError("No matching functions found")
        else:
            raise ValueError("Multiple functions found")

    @classmethod
    @coerce_return_to_text
    def encodeABI(cls, fn_name, arguments, data=None):
        """
        encodes the arguments using the Ethereum ABI.
        """
        function_abi = cls.find_matching_abi(fn_name, force_obj_to_bytes(arguments))
        return cls._encodeABI(function_abi, arguments, data)

    @classmethod
    def _encodeABI(cls, abi, arguments, data=None):
        arguent_types = get_abi_input_types(abi)
        encoded_arguments = encode_abi(arguent_types, force_obj_to_bytes(arguments))
        if data:
            return add_0x_prefix(
                force_bytes(remove_0x_prefix(data)) +
                force_bytes(remove_0x_prefix(encode_hex(encoded_arguments)))
            )
        else:
            return encode_hex(encoded_arguments)

    @classmethod
    def encodeConstructorData(cls, arguments=None):
        if arguments is None:
            arguments = []

        constructor = get_constructor_abi(cls.abi)
        if constructor:
            if constructor['inputs'] and not arguments:
                raise ValueError(
                    "This contract requires {0} constructor arguments".format(
                        len(constructor['inputs']),
                    )
                )
            if arguments:
                if len(arguments) != len(constructor['inputs']):
                    raise ValueError(
                        "This contract requires {0} constructor arguments".format(
                            len(constructor['inputs']),
                        )
                    )

                is_encodable = check_if_arguments_can_be_encoded(
                    get_abi_input_types(constructor),
                    arguments,
                )
                if not is_encodable:
                    raise ValueError("Unable to encode provided arguments.")

            deploy_data = add_0x_prefix(cls._encodeABI(constructor, arguments, data=cls.code))
        else:
            deploy_data = add_0x_prefix(cls.code)

        return deploy_data

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

    def estimateGas(self, transaction=None):
        """
        Estimate the gas for a call
        """
        if transaction is None:
            transaction = {}

        if 'data' in transaction:
            raise ValueError("Cannot set data in call transaction")
        if 'to' in transaction:
            raise ValueError("Cannot set to in call transaction")

        transaction['to'] = self.address
        transaction.setdefault('from', self.web3.eth.coinbase)

        contract = self

        class Caller(object):
            def __getattr__(self, function_name):
                callable_fn = functools.partial(
                    estimate_gas_for_function,
                    contract,
                    function_name,
                    transaction,
                )
                return callable_fn

        return Caller()

    def call(self, transaction=None):
        """
        Execute a contract function call using the `eth_call` interface.
        """
        if transaction is None:
            transaction = {}

        if 'data' in transaction:
            raise ValueError("Cannot set data in call transaction")
        if 'to' in transaction:
            raise ValueError("Cannot set to in call transaction")

        transaction['to'] = self.address
        transaction.setdefault('from', self.web3.eth.coinbase)

        contract = self

        class Caller(object):
            def __getattr__(self, function_name):
                callable_fn = functools.partial(
                    call_contract_function,
                    contract,
                    function_name,
                    transaction,
                )
                return callable_fn

        return Caller()

    def transact(self, transaction=None):
        """
        Execute a contract function call using the `eth_sendTransaction` interface.
        """
        if transaction is None:
            transaction = {}

        if 'data' in transaction:
            raise ValueError("Cannot set data in call transaction")
        if 'to' in transaction:
            raise ValueError("Cannot set to in call transaction")

        transaction['to'] = self.address
        transaction.setdefault('from', self.web3.eth.coinbase)

        contract = self

        class Transactor(object):
            def __getattr__(self, function_name):
                callable_fn = functools.partial(
                    transact_with_contract_function,
                    contract,
                    function_name,
                    transaction,
                )
                return callable_fn

        return Transactor()


def call_contract_function(contract=None,
                           function_name=None,
                           transaction=None,
                           *arguments):
    if not arguments:
        arguments = []

    function_abi = contract.find_matching_abi(function_name, arguments)
    function_selector = function_abi_to_4byte_selector(function_abi)

    transaction['data'] = contract.encodeABI(
        function_name,
        arguments,
        data=function_selector,
    )

    return_data = contract.web3.eth.call(transaction)

    output_types = get_abi_output_types(function_abi)
    output_data = decode_abi(output_types, return_data)
    if len(output_data) == 1:
        return output_data[0]
    else:
        return output_data


def transact_with_contract_function(contract=None,
                                    function_name=None,
                                    transaction=None,
                                    *arguments):
    if not arguments:
        arguments = []

    function_abi = contract.find_matching_abi(function_name, arguments)
    function_selector = function_abi_to_4byte_selector(function_abi)

    transaction['data'] = contract.encodeABI(
        function_name,
        arguments,
        data=function_selector,
    )

    txn_hash = contract.web3.eth.sendTransaction(transaction)
    return txn_hash


def estimate_gas_for_function(contract=None,
                              function_name=None,
                              transaction=None,
                              *arguments):
    if not arguments:
        arguments = []

    function_abi = contract.find_matching_abi(function_name, arguments)
    function_selector = function_abi_to_4byte_selector(function_abi)

    transaction['data'] = contract.encodeABI(
        function_name,
        arguments,
        data=function_selector,
    )

    gas_estimate = contract.web3.eth.estimateGas(transaction)
    return gas_estimate


def construct_contract_class(web3, abi, code=None,
                             code_runtime=None, source=None):
    _dict = {
        'web3': web3,
        'abi': abi,
        'code': code,
        'code_runtime': code_runtime,
        'source': source,
    }
    return type('Contract', (_Contract,), _dict)
