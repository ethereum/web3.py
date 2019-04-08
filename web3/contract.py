"""Interaction with smart contracts over Web3 connector.

"""
import copy
import itertools

from eth_abi import (
    decode_abi,
)
from eth_abi.exceptions import (
    DecodingError,
)
from eth_utils import (
    add_0x_prefix,
    encode_hex,
    function_abi_to_4byte_selector,
    is_list_like,
    is_text,
    to_tuple,
)
from eth_utils.toolz import (
    compose,
    partial,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    abi_to_signature,
    check_if_arguments_can_be_encoded,
    fallback_func_abi_exists,
    filter_by_type,
    get_abi_output_types,
    get_constructor_abi,
    is_array_type,
    map_abi_data,
    merge_args_and_kwargs,
)
from web3._utils.blocks import (
    is_hex_encoded_block_hash,
)
from web3._utils.contracts import (
    encode_abi,
    find_matching_event_abi,
    find_matching_fn_abi,
    get_function_info,
    prepare_transaction,
)
from web3._utils.datatypes import (
    PropertyCheckingFactory,
)
from web3._utils.decorators import (
    combomethod,
    deprecated_for,
)
from web3._utils.empty import (
    empty,
)
from web3._utils.encoding import (
    to_4byte_hex,
    to_hex,
)
from web3._utils.events import (
    EventFilterBuilder,
    get_event_data,
    is_dynamic_sized_type,
)
from web3._utils.filters import (
    construct_event_filter_params,
)
from web3._utils.function_identifiers import (
    FallbackFn,
)
from web3._utils.normalizers import (
    BASE_RETURN_NORMALIZERS,
    normalize_abi,
    normalize_address,
    normalize_bytecode,
)
from web3._utils.transactions import (
    fill_transaction_defaults,
)
from web3.exceptions import (
    BadFunctionCallOutput,
    BlockNumberOutofRange,
    FallbackNotFound,
    MismatchedABI,
    NoABIEventsFound,
    NoABIFound,
    NoABIFunctionsFound,
    ValidationError,
)

ACCEPTABLE_EMPTY_STRINGS = ["0x", b"0x", "", b""]


class ContractFunctions:
    """Class containing contract function objects
    """

    def __init__(self, abi, web3, address=None):
        self.abi = abi
        self.web3 = web3
        self.address = address

        if self.abi:
            self._functions = filter_by_type('function', self.abi)
            for func in self._functions:
                setattr(
                    self,
                    func['name'],
                    ContractFunction.factory(
                        func['name'],
                        web3=self.web3,
                        contract_abi=self.abi,
                        address=self.address,
                        function_identifier=func['name']))

    def __iter__(self):
        if not hasattr(self, '_functions') or not self._functions:
            return

        for func in self._functions:
            yield func['name']

    def __getattr__(self, function_name):
        if self.abi is None:
            raise NoABIFound(
                "There is no ABI found for this contract.",
            )
        if '_functions' not in self.__dict__:
            raise NoABIFunctionsFound(
                "The abi for this contract contains no function definitions. ",
                "Are you sure you provided the correct contract abi?"
            )
        elif function_name not in self.__dict__['_functions']:
            raise MismatchedABI(
                "The function '{}' was not found in this contract's abi. ".format(function_name),
                "Are you sure you provided the correct contract abi?"
            )
        else:
            return super().__getattribute__(function_name)

    def __getitem__(self, function_name):
        return getattr(self, function_name)


class ContractEvents:
    """Class containing contract event objects

    This is available via:

    .. code-block:: python

        >>> mycontract.events
        <web3.contract.ContractEvents object at 0x108afde10>

    To get list of all supported events in the contract ABI.
    This allows you to iterate over :class:`ContractEvent` proxy classes.

    .. code-block:: python

        >>> for e in mycontract.events: print(e)
        <class 'web3._utils.datatypes.LogAnonymous'>
        ...

    """

    def __init__(self, abi, web3, address=None):
        if abi:
            self.abi = abi
            self._events = filter_by_type('event', self.abi)
            for event in self._events:
                setattr(
                    self,
                    event['name'],
                    ContractEvent.factory(
                        event['name'],
                        web3=web3,
                        contract_abi=self.abi,
                        address=address,
                        event_name=event['name']))

    def __getattr__(self, event_name):
        if '_events' not in self.__dict__:
            raise NoABIEventsFound(
                "The abi for this contract contains no event definitions. ",
                "Are you sure you provided the correct contract abi?"
            )
        elif event_name not in self.__dict__['_events']:
            raise MismatchedABI(
                "The event '{}' was not found in this contract's abi. ".format(event_name),
                "Are you sure you provided the correct contract abi?"
            )
        else:
            return super().__getattribute__(event_name)

    def __getitem__(self, event_name):
        return getattr(self, event_name)

    def __iter__(self):
        """Iterate over supported

        :return: Iterable of :class:`ContractEvent`
        """
        for event in self._events:
            yield self[event['name']]


class Contract:
    """Base class for Contract proxy classes.

    First you need to create your Contract classes using
    :meth:`web3.eth.Eth.contract` that takes compiled Solidity contract
    ABI definitions as input.  The created class object will be a subclass of
    this base class.

    After you have your Contract proxy class created you can interact with
    smart contracts

    * Create a Contract proxy object for an existing deployed smart contract by
      its address using :meth:`__init__`

    * Deploy a new smart contract using :py:meth:`Contract.deploy`
    """

    # set during class construction
    web3 = None

    # instance level properties
    address = None

    # class properties (overridable at instance level)
    abi = None

    asm = None
    ast = None

    bytecode = None
    bytecode_runtime = None
    clone_bin = None

    functions = None
    caller = None

    #: Instance of :class:`ContractEvents` presenting available Event ABIs
    events = None

    dev_doc = None
    interface = None
    metadata = None
    opcodes = None
    src_map = None
    src_map_runtime = None
    user_doc = None

    def __init__(self, address=None):
        """Create a new smart contract proxy object.

        :param address: Contract address as 0x hex string
        """
        if self.web3 is None:
            raise AttributeError(
                'The `Contract` class has not been initialized.  Please use the '
                '`web3.contract` interface to create your contract class.'
            )

        if address:
            self.address = normalize_address(self.web3.ens, address)

        if not self.address:
            raise TypeError("The address argument is required to instantiate a contract.")

        self.functions = ContractFunctions(self.abi, self.web3, self.address)
        self.caller = ContractCaller(self.abi, self.web3, self.address)
        self.events = ContractEvents(self.abi, self.web3, self.address)
        self.fallback = Contract.get_fallback_function(self.abi, self.web3, self.address)

    @classmethod
    def factory(cls, web3, class_name=None, **kwargs):

        kwargs['web3'] = web3

        normalizers = {
            'abi': normalize_abi,
            'address': partial(normalize_address, kwargs['web3'].ens),
            'bytecode': normalize_bytecode,
            'bytecode_runtime': normalize_bytecode,
        }

        contract = PropertyCheckingFactory(
            class_name or cls.__name__,
            (cls,),
            kwargs,
            normalizers=normalizers,
        )
        contract.functions = ContractFunctions(contract.abi, contract.web3)
        contract.caller = ContractCaller(contract.abi, contract.web3, contract.address)
        contract.events = ContractEvents(contract.abi, contract.web3)
        contract.fallback = Contract.get_fallback_function(contract.abi, contract.web3)

        return contract

    #
    # Contract Methods
    #
    @classmethod
    def constructor(cls, *args, **kwargs):
        """
        :param args: The contract constructor arguments as positional arguments
        :param kwargs: The contract constructor arguments as keyword arguments
        :return: a contract constructor object
        """
        if cls.bytecode is None:
            raise ValueError(
                "Cannot call constructor on a contract that does not have 'bytecode' associated "
                "with it"
            )

        return ContractConstructor(cls.web3,
                                   cls.abi,
                                   cls.bytecode,
                                   *args,
                                   **kwargs)

    #  Public API
    #
    @combomethod
    def encodeABI(cls, fn_name, args=None, kwargs=None, data=None):
        """
        Encodes the arguments using the Ethereum ABI for the contract function
        that matches the given name and arguments..

        :param data: defaults to function selector
        """
        fn_abi, fn_selector, fn_arguments = get_function_info(
            fn_name, contract_abi=cls.abi, args=args, kwargs=kwargs,
        )

        if data is None:
            data = fn_selector

        return encode_abi(cls.web3, fn_abi, fn_arguments, data)

    @combomethod
    def all_functions(self):
        return find_functions_by_identifier(
            self.abi, self.web3, self.address, lambda _: True
        )

    @combomethod
    def get_function_by_signature(self, signature):
        if ' ' in signature:
            raise ValueError(
                'Function signature should not contain any spaces. '
                'Found spaces in input: %s' % signature
            )

        def callable_check(fn_abi):
            return abi_to_signature(fn_abi) == signature

        fns = find_functions_by_identifier(self.abi, self.web3, self.address, callable_check)
        return get_function_by_identifier(fns, 'signature')

    @combomethod
    def find_functions_by_name(self, fn_name):
        def callable_check(fn_abi):
            return fn_abi['name'] == fn_name

        return find_functions_by_identifier(
            self.abi, self.web3, self.address, callable_check
        )

    @combomethod
    def get_function_by_name(self, fn_name):
        fns = self.find_functions_by_name(fn_name)
        return get_function_by_identifier(fns, 'name')

    @combomethod
    def get_function_by_selector(self, selector):
        def callable_check(fn_abi):
            return encode_hex(function_abi_to_4byte_selector(fn_abi)) == to_4byte_hex(selector)

        fns = find_functions_by_identifier(self.abi, self.web3, self.address, callable_check)
        return get_function_by_identifier(fns, 'selector')

    @combomethod
    def decode_function_input(self, data):
        data = HexBytes(data)
        selector, params = data[:4], data[4:]
        func = self.get_function_by_selector(selector)
        names = [x['name'] for x in func.abi['inputs']]
        types = [x['type'] for x in func.abi['inputs']]
        decoded = decode_abi(types, params)
        normalized = map_abi_data(BASE_RETURN_NORMALIZERS, types, decoded)
        return func, dict(zip(names, normalized))

    @combomethod
    def find_functions_by_args(self, *args):
        def callable_check(fn_abi):
            return check_if_arguments_can_be_encoded(fn_abi, args=args, kwargs={})

        return find_functions_by_identifier(
            self.abi, self.web3, self.address, callable_check
        )

    @combomethod
    def get_function_by_args(self, *args):
        fns = self.find_functions_by_args(*args)
        return get_function_by_identifier(fns, 'args')

    #
    # Private Helpers
    #
    _return_data_normalizers = tuple()

    @classmethod
    def _prepare_transaction(cls,
                             fn_name,
                             fn_args=None,
                             fn_kwargs=None,
                             transaction=None):

        return prepare_transaction(
            cls.address,
            cls.web3,
            fn_identifier=fn_name,
            contract_abi=cls.abi,
            transaction=transaction,
            fn_args=fn_args,
            fn_kwargs=fn_kwargs,
        )

    @classmethod
    def _find_matching_fn_abi(cls, fn_identifier=None, args=None, kwargs=None):
        return find_matching_fn_abi(cls.abi,
                                    fn_identifier=fn_identifier,
                                    args=args,
                                    kwargs=kwargs)

    @classmethod
    def _find_matching_event_abi(cls, event_name=None, argument_names=None):
        return find_matching_event_abi(
            abi=cls.abi,
            event_name=event_name,
            argument_names=argument_names)

    @staticmethod
    def get_fallback_function(abi, web3, address=None):
        if abi and fallback_func_abi_exists(abi):
            return ContractFunction.factory(
                'fallback',
                web3=web3,
                contract_abi=abi,
                address=address,
                function_identifier=FallbackFn)()

        return NonExistentFallbackFunction()

    @combomethod
    def _encode_constructor_data(cls, args=None, kwargs=None):
        constructor_abi = get_constructor_abi(cls.abi)

        if constructor_abi:
            if args is None:
                args = tuple()
            if kwargs is None:
                kwargs = {}

            arguments = merge_args_and_kwargs(constructor_abi, args, kwargs)

            deploy_data = add_0x_prefix(
                encode_abi(cls.web3, constructor_abi, arguments, data=cls.bytecode)
            )
        else:
            if args is not None or kwargs is not None:
                msg = "Constructor args were provided, but no constructor function was provided."
                raise TypeError(msg)

            deploy_data = to_hex(cls.bytecode)

        return deploy_data


def mk_collision_prop(fn_name):
    def collision_fn():
        msg = "Namespace collision for function name {0} with ConciseContract API.".format(fn_name)
        raise AttributeError(msg)
    collision_fn.__name__ = fn_name
    return collision_fn


class ContractConstructor:
    """
    Class for contract constructor API.
    """
    def __init__(self, web3, abi, bytecode, *args, **kwargs):
        self.web3 = web3
        self.abi = abi
        self.bytecode = bytecode
        self.data_in_transaction = self._encode_data_in_transaction(*args, **kwargs)

    @combomethod
    def _encode_data_in_transaction(self, *args, **kwargs):
        constructor_abi = get_constructor_abi(self.abi)

        if constructor_abi:
            if not args:
                args = tuple()
            if not kwargs:
                kwargs = {}

            arguments = merge_args_and_kwargs(constructor_abi, args, kwargs)
            data = add_0x_prefix(
                encode_abi(self.web3, constructor_abi, arguments, data=self.bytecode)
            )
        else:
            data = to_hex(self.bytecode)

        return data

    @combomethod
    def estimateGas(self, transaction=None):
        if transaction is None:
            estimate_gas_transaction = {}
        else:
            estimate_gas_transaction = dict(**transaction)
            self.check_forbidden_keys_in_transaction(estimate_gas_transaction,
                                                     ["data", "to"])

        if self.web3.eth.defaultAccount is not empty:
            estimate_gas_transaction.setdefault('from', self.web3.eth.defaultAccount)

        estimate_gas_transaction['data'] = self.data_in_transaction

        return self.web3.eth.estimateGas(estimate_gas_transaction)

    @combomethod
    def transact(self, transaction=None):
        if transaction is None:
            transact_transaction = {}
        else:
            transact_transaction = dict(**transaction)
            self.check_forbidden_keys_in_transaction(transact_transaction,
                                                     ["data", "to"])

        if self.web3.eth.defaultAccount is not empty:
            transact_transaction.setdefault('from', self.web3.eth.defaultAccount)

        transact_transaction['data'] = self.data_in_transaction

        # TODO: handle asynchronous contract creation
        return self.web3.eth.sendTransaction(transact_transaction)

    @combomethod
    def buildTransaction(self, transaction=None):
        """
        Build the transaction dictionary without sending
        """

        if transaction is None:
            built_transaction = {}
        else:
            built_transaction = dict(**transaction)
            self.check_forbidden_keys_in_transaction(built_transaction,
                                                     ["data", "to"])

        if self.web3.eth.defaultAccount is not empty:
            built_transaction.setdefault('from', self.web3.eth.defaultAccount)

        built_transaction['data'] = self.data_in_transaction
        built_transaction['to'] = b''
        return fill_transaction_defaults(self.web3, built_transaction)

    @staticmethod
    def check_forbidden_keys_in_transaction(transaction, forbidden_keys=None):
        keys_found = set(transaction.keys()) & set(forbidden_keys)
        if keys_found:
            raise ValueError("Cannot set {} in transaction".format(', '.join(keys_found)))


class ConciseMethod:
    ALLOWED_MODIFIERS = {'call', 'estimateGas', 'transact', 'buildTransaction'}

    def __init__(self, function, normalizers=None):
        self._function = function
        self._function._return_data_normalizers = normalizers

    def __call__(self, *args, **kwargs):
        return self.__prepared_function(*args, **kwargs)

    def __prepared_function(self, *args, **kwargs):
        if not kwargs:
            modifier, modifier_dict = 'call', {}
        elif len(kwargs) == 1:
            modifier, modifier_dict = kwargs.popitem()
            if modifier not in self.ALLOWED_MODIFIERS:
                raise TypeError(
                    "The only allowed keyword arguments are: %s" % self.ALLOWED_MODIFIERS)
        else:
            raise TypeError("Use up to one keyword argument, one of: %s" % self.ALLOWED_MODIFIERS)

        return getattr(self._function(*args), modifier)(modifier_dict)


class ConciseContract:
    """
    An alternative Contract Factory which invokes all methods as `call()`,
    unless you add a keyword argument. The keyword argument assigns the prep method.

    This call

    > contract.withdraw(amount, transact={'from': eth.accounts[1], 'gas': 100000, ...})

    is equivalent to this call in the classic contract:

    > contract.functions.withdraw(amount).transact({'from': eth.accounts[1], 'gas': 100000, ...})
    """
    @deprecated_for(
        "contract.caller.<method name> or contract.caller({transaction_dict}).<method name>"
    )
    def __init__(self, classic_contract, method_class=ConciseMethod):

        classic_contract._return_data_normalizers += CONCISE_NORMALIZERS
        self._classic_contract = classic_contract
        self.address = self._classic_contract.address

        protected_fn_names = [fn for fn in dir(self) if not fn.endswith('__')]

        for fn_name in self._classic_contract.functions:

            # Override namespace collisions
            if fn_name in protected_fn_names:
                _concise_method = mk_collision_prop(fn_name)

            else:
                _classic_method = getattr(
                    self._classic_contract.functions,
                    fn_name)

                _concise_method = method_class(
                    _classic_method,
                    self._classic_contract._return_data_normalizers
                )

            setattr(self, fn_name, _concise_method)

    @classmethod
    def factory(cls, *args, **kwargs):
        return compose(cls, Contract.factory(*args, **kwargs))


def _none_addr(datatype, data):
    if datatype == 'address' and int(data, base=16) == 0:
        return (datatype, None)
    else:
        return (datatype, data)


CONCISE_NORMALIZERS = (
    _none_addr,
)


class ImplicitMethod(ConciseMethod):
    def __call_by_default(self, args):
        function_abi = find_matching_fn_abi(self._function.contract_abi,
                                            fn_identifier=self._function.function_identifier,
                                            args=args)

        return function_abi['constant'] if 'constant' in function_abi.keys() else False

    @deprecated_for("classic contract syntax. Ex: contract.functions.withdraw(amount).transact({})")
    def __call__(self, *args, **kwargs):
        # Modifier is not provided and method is not constant/pure do a transaction instead
        if not kwargs and not self.__call_by_default(args):
            return super().__call__(*args, transact={})
        else:
            return super().__call__(*args, **kwargs)


class ImplicitContract(ConciseContract):
    """
    ImplicitContract class is similar to the ConciseContract class
    however it performs a transaction instead of a call if no modifier
    is given and the method is not marked 'constant' in the ABI.

    The transaction will use the default account to send the transaction.

    This call

    > contract.withdraw(amount)

    is equivalent to this call in the classic contract:

    > contract.functions.withdraw(amount).transact({})
    """
    def __init__(self, classic_contract, method_class=ImplicitMethod):
        super().__init__(classic_contract, method_class=method_class)


class NonExistentFallbackFunction:
    @staticmethod
    def _raise_exception():
        raise FallbackNotFound("No fallback function was found in the contract ABI.")

    def __getattr__(self, attr):
        return NonExistentFallbackFunction._raise_exception


class ContractFunction:
    """Base class for contract functions

    A function accessed via the api contract.functions.myMethod(*args, **kwargs)
    is a subclass of this class.
    """
    address = None
    function_identifier = None
    web3 = None
    contract_abi = None
    abi = None
    transaction = None
    arguments = None

    def __init__(self, abi=None):
        self.abi = abi
        self.fn_name = type(self).__name__

    def __call__(self, *args, **kwargs):
        clone = copy.copy(self)
        if args is None:
            clone.args = tuple()
        else:
            clone.args = args

        if kwargs is None:
            clone.kwargs = {}
        else:
            clone.kwargs = kwargs
        clone._set_function_info()
        return clone

    def _set_function_info(self):
        if not self.abi:
            self.abi = find_matching_fn_abi(
                self.contract_abi,
                self.function_identifier,
                self.args,
                self.kwargs
            )
        if self.function_identifier is FallbackFn:
            self.selector = encode_hex(b'')
        elif is_text(self.function_identifier):
            self.selector = encode_hex(function_abi_to_4byte_selector(self.abi))
        else:
            raise TypeError("Unsupported function identifier")

        self.arguments = merge_args_and_kwargs(self.abi, self.args, self.kwargs)

    def call(self, transaction=None, block_identifier='latest'):
        """
        Execute a contract function call using the `eth_call` interface.

        This method prepares a ``Caller`` object that exposes the contract
        functions and public variables as callable Python functions.

        Reading a public ``owner`` address variable example:

        .. code-block:: python

            ContractFactory = w3.eth.contract(
                abi=wallet_contract_definition["abi"]
            )

            # Not a real contract address
            contract = ContractFactory("0x2f70d3d26829e412A602E83FE8EeBF80255AEeA5")

            # Read "owner" public variable
            addr = contract.functions.owner().call()

        :param transaction: Dictionary of transaction info for web3 interface
        :return: ``Caller`` object that has contract public functions
            and variables exposed as Python methods
        """
        if transaction is None:
            call_transaction = {}
        else:
            call_transaction = dict(**transaction)

        if 'data' in call_transaction:
            raise ValueError("Cannot set data in call transaction")

        if self.address:
            call_transaction.setdefault('to', self.address)
        if self.web3.eth.defaultAccount is not empty:
            call_transaction.setdefault('from', self.web3.eth.defaultAccount)

        if 'to' not in call_transaction:
            if isinstance(self, type):
                raise ValueError(
                    "When using `Contract.[methodtype].[method].call()` from"
                    " a contract factory you "
                    "must provide a `to` address with the transaction"
                )
            else:
                raise ValueError(
                    "Please ensure that this contract instance has an address."
                )

        block_id = parse_block_identifier(self.web3, block_identifier)

        return call_contract_function(
            self.web3,
            self.address,
            self._return_data_normalizers,
            self.function_identifier,
            call_transaction,
            block_id,
            self.contract_abi,
            self.abi,
            *self.args,
            **self.kwargs
        )

    def transact(self, transaction=None):
        if transaction is None:
            transact_transaction = {}
        else:
            transact_transaction = dict(**transaction)

        if 'data' in transact_transaction:
            raise ValueError("Cannot set data in transact transaction")

        if self.address is not None:
            transact_transaction.setdefault('to', self.address)
        if self.web3.eth.defaultAccount is not empty:
            transact_transaction.setdefault('from', self.web3.eth.defaultAccount)

        if 'to' not in transact_transaction:
            if isinstance(self, type):
                raise ValueError(
                    "When using `Contract.transact` from a contract factory you "
                    "must provide a `to` address with the transaction"
                )
            else:
                raise ValueError(
                    "Please ensure that this contract instance has an address."
                )

        return transact_with_contract_function(
            self.address,
            self.web3,
            self.function_identifier,
            transact_transaction,
            self.contract_abi,
            self.abi,
            *self.args,
            **self.kwargs
        )

    def estimateGas(self, transaction=None):
        if transaction is None:
            estimate_gas_transaction = {}
        else:
            estimate_gas_transaction = dict(**transaction)

        if 'data' in estimate_gas_transaction:
            raise ValueError("Cannot set data in estimateGas transaction")
        if 'to' in estimate_gas_transaction:
            raise ValueError("Cannot set to in estimateGas transaction")

        if self.address:
            estimate_gas_transaction.setdefault('to', self.address)
        if self.web3.eth.defaultAccount is not empty:
            estimate_gas_transaction.setdefault('from', self.web3.eth.defaultAccount)

        if 'to' not in estimate_gas_transaction:
            if isinstance(self, type):
                raise ValueError(
                    "When using `Contract.estimateGas` from a contract factory "
                    "you must provide a `to` address with the transaction"
                )
            else:
                raise ValueError(
                    "Please ensure that this contract instance has an address."
                )

        return estimate_gas_for_function(
            self.address,
            self.web3,
            self.function_identifier,
            estimate_gas_transaction,
            self.contract_abi,
            self.abi,
            *self.args,
            **self.kwargs
        )

    def buildTransaction(self, transaction=None):
        """
        Build the transaction dictionary without sending
        """
        if transaction is None:
            built_transaction = {}
        else:
            built_transaction = dict(**transaction)

        if 'data' in built_transaction:
            raise ValueError("Cannot set data in build transaction")

        if not self.address and 'to' not in built_transaction:
            raise ValueError(
                "When using `ContractFunction.buildTransaction` from a contract factory "
                "you must provide a `to` address with the transaction"
            )
        if self.address and 'to' in built_transaction:
            raise ValueError("Cannot set to in contract call build transaction")

        if self.address:
            built_transaction.setdefault('to', self.address)

        if 'to' not in built_transaction:
            raise ValueError(
                "Please ensure that this contract instance has an address."
            )

        return build_transaction_for_function(
            self.address,
            self.web3,
            self.function_identifier,
            built_transaction,
            self.contract_abi,
            self.abi,
            *self.args,
            **self.kwargs
        )

    @combomethod
    def _encode_transaction_data(cls):
        return add_0x_prefix(encode_abi(cls.web3, cls.abi, cls.arguments, cls.selector))

    _return_data_normalizers = tuple()

    @classmethod
    def factory(cls, class_name, **kwargs):
        return PropertyCheckingFactory(class_name, (cls,), kwargs)(kwargs.get('abi'))

    def __repr__(self):
        if self.abi:
            _repr = '<Function %s' % abi_to_signature(self.abi)
            if self.arguments is not None:
                _repr += ' bound to %r' % (self.arguments,)
            return _repr + '>'
        return '<Function %s>' % self.fn_name


class ContractEvent:
    """Base class for contract events

    An event accessed via the api contract.events.myEvents(*args, **kwargs)
    is a subclass of this class.
    """
    address = None
    event_name = None
    web3 = None
    contract_abi = None
    abi = None

    def __init__(self, *argument_names):

        if argument_names is None:
            self.argument_names = tuple()
        else:
            self.argument_names = argument_names

        self.abi = self._get_event_abi()

    @classmethod
    def _get_event_abi(cls):
        return find_matching_event_abi(
            cls.contract_abi,
            event_name=cls.event_name)

    @combomethod
    def processReceipt(self, txn_receipt):
        return self._parse_logs(txn_receipt)

    @to_tuple
    def _parse_logs(self, txn_receipt):
        for log in txn_receipt['logs']:
            try:
                decoded_log = get_event_data(self.abi, log)
            except MismatchedABI:
                continue
            yield decoded_log

    @combomethod
    def createFilter(
            self, *,  # PEP 3102
            argument_filters=None,
            fromBlock=None,
            toBlock="latest",
            address=None,
            topics=None):
        """
        Create filter object that tracks logs emitted by this contract event.
        :param filter_params: other parameters to limit the events
        """
        if fromBlock is None:
            raise TypeError("Missing mandatory keyword argument to createFilter: fromBlock")

        if argument_filters is None:
            argument_filters = dict()

        _filters = dict(**argument_filters)

        event_abi = self._get_event_abi()

        check_for_forbidden_api_filter_arguments(event_abi, _filters)

        _, event_filter_params = construct_event_filter_params(
            self._get_event_abi(),
            contract_address=self.address,
            argument_filters=_filters,
            fromBlock=fromBlock,
            toBlock=toBlock,
            address=address,
            topics=topics,
        )

        filter_builder = EventFilterBuilder(event_abi)
        filter_builder.address = event_filter_params.get('address')
        filter_builder.fromBlock = event_filter_params.get('fromBlock')
        filter_builder.toBlock = event_filter_params.get('toBlock')
        match_any_vals = {
            arg: value for arg, value in _filters.items()
            if not is_array_type(filter_builder.args[arg].arg_type) and is_list_like(value)
        }
        for arg, value in match_any_vals.items():
            filter_builder.args[arg].match_any(*value)

        match_single_vals = {
            arg: value for arg, value in _filters.items()
            if not is_array_type(filter_builder.args[arg].arg_type) and not is_list_like(value)
        }
        for arg, value in match_single_vals.items():
            filter_builder.args[arg].match_single(value)

        log_filter = filter_builder.deploy(self.web3)
        log_filter.log_entry_formatter = get_event_data(self._get_event_abi())
        log_filter.builder = filter_builder

        return log_filter

    @combomethod
    def build_filter(self):
        builder = EventFilterBuilder(
            self._get_event_abi(),
            formatter=get_event_data(self._get_event_abi()))
        builder.address = self.address
        return builder

    @combomethod
    def getLogs(self,
                argument_filters=None,
                fromBlock=None,
                toBlock=None,
                blockHash=None):
        """Get events for this contract instance using eth_getLogs API.

        This is a stateless method, as opposed to createFilter.
        It can be safely called against nodes which do not provide
        eth_newFilter API, like Infura nodes.

        If there are many events,
        like ``Transfer`` events for a popular token,
        the Ethereum node might be overloaded and timeout
        on the underlying JSON-RPC call.

        Example - how to get all ERC-20 token transactions
        for the latest 10 blocks:

        .. code-block:: python

            from = max(mycontract.web3.eth.blockNumber - 10, 1)
            to = mycontract.web3.eth.blockNumber

            events = mycontract.events.Transfer.getLogs(fromBlock=from, toBlock=to)

            for e in events:
                print(e["args"]["from"],
                    e["args"]["to"],
                    e["args"]["value"])

        The returned processed log values will look like:

        .. code-block:: python

            (
                AttributeDict({
                 'args': AttributeDict({}),
                 'event': 'LogNoArguments',
                 'logIndex': 0,
                 'transactionIndex': 0,
                 'transactionHash': HexBytes('...'),
                 'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
                 'blockHash': HexBytes('...'),
                 'blockNumber': 3
                }),
                AttributeDict(...),
                ...
            )

        See also: :func:`web3.middleware.filter.local_filter_middleware`.

        :param argument_filters:
        :param fromBlock: block number or "latest", defaults to "latest"
        :param toBlock: block number or "latest". Defaults to "latest"
        :param blockHash: block hash. blockHash cannot be set at the
          same time as fromBlock or toBlock
        :yield: Tuple of :class:`AttributeDict` instances
        """

        if not self.address:
            raise TypeError("This method can be only called on "
                            "an instated contract with an address")

        abi = self._get_event_abi()

        if argument_filters is None:
            argument_filters = dict()

        _filters = dict(**argument_filters)

        blkhash_set = blockHash is not None
        blknum_set = fromBlock is not None or toBlock is not None
        if blkhash_set and blknum_set:
            raise ValidationError(
                'blockHash cannot be set at the same'
                ' time as fromBlock or toBlock')

        # Construct JSON-RPC raw filter presentation based on human readable Python descriptions
        # Namely, convert event names to their keccak signatures
        data_filter_set, event_filter_params = construct_event_filter_params(
            abi,
            contract_address=self.address,
            argument_filters=_filters,
            fromBlock=fromBlock,
            toBlock=toBlock,
            address=self.address,
        )

        if blockHash is not None:
            event_filter_params['blockHash'] = blockHash

        # Call JSON-RPC API
        logs = self.web3.eth.getLogs(event_filter_params)

        # Convert raw binary data to Python proxy objects as described by ABI
        return tuple(get_event_data(abi, entry) for entry in logs)

    @classmethod
    def factory(cls, class_name, **kwargs):
        return PropertyCheckingFactory(class_name, (cls,), kwargs)


class ContractCaller:
    """
    An alternative Contract API.

    This call:

    > contract.caller({'from': eth.accounts[1], 'gas': 100000, ...}).add(2, 3)
    is equivalent to this call in the classic contract:
    > contract.functions.add(2, 3).call({'from': eth.accounts[1], 'gas': 100000, ...})

    Other options for invoking this class include:

    > contract.caller.add(2, 3)

    or

    > contract.caller().add(2, 3)

    or

    > contract.caller(transaction={'from': eth.accounts[1], 'gas': 100000, ...}).add(2, 3)
    """
    def __init__(self,
                 abi,
                 web3,
                 address,
                 transaction=None,
                 block_identifier='latest'):
        self.web3 = web3
        self.address = address
        self.abi = abi
        self._functions = None

        if self.abi:
            if transaction is None:
                transaction = {}

            self._functions = filter_by_type('function', self.abi)
            for func in self._functions:
                fn = ContractFunction.factory(
                    func['name'],
                    web3=self.web3,
                    contract_abi=self.abi,
                    address=self.address,
                    function_identifier=func['name'])

                block_id = parse_block_identifier(self.web3, block_identifier)
                caller_method = partial(self.call_function,
                                        fn,
                                        transaction=transaction,
                                        block_identifier=block_id)

                setattr(self, func['name'], caller_method)

    def __getattr__(self, function_name):
        if self.abi is None:
            raise NoABIFound(
                "There is no ABI found for this contract.",
            )
        elif not self._functions or len(self._functions) == 0:
            raise NoABIFunctionsFound(
                "The ABI for this contract contains no function definitions. ",
                "Are you sure you provided the correct contract ABI?"
            )
        elif function_name not in self._functions:
            functions_available = ', '.join([fn['name'] for fn in self._functions])
            raise MismatchedABI(
                "The function '{}' was not found in this contract's ABI. ".format(function_name),
                "Here is a list of all of the function names found: ",
                "{}. ".format(functions_available),
                "Did you mean to call one of those functions?"
            )
        else:
            return super().__getattribute__(function_name)

    def __call__(self, transaction=None, block_identifier='latest'):
        if transaction is None:
            transaction = {}
        return type(self)(self.abi,
                          self.web3,
                          self.address,
                          transaction=transaction,
                          block_identifier=block_identifier)

    @staticmethod
    def call_function(fn, *args, transaction=None, block_identifier='latest', **kwargs):
        if transaction is None:
            transaction = {}
        return fn(*args, **kwargs).call(transaction, block_identifier)


def check_for_forbidden_api_filter_arguments(event_abi, _filters):
    name_indexed_inputs = {_input['name']: _input for _input in event_abi['inputs']}

    for filter_name, filter_value in _filters.items():
        _input = name_indexed_inputs[filter_name]
        if is_array_type(_input['type']):
            raise TypeError(
                "createFilter no longer supports array type filter arguments. "
                "see the build_filter method for filtering array type filters.")
        if is_list_like(filter_value) and is_dynamic_sized_type(_input['type']):
            raise TypeError(
                "createFilter no longer supports setting filter argument options for dynamic sized "
                "types. See the build_filter method for setting filters with the match_any "
                "method.")


def call_contract_function(
        web3,
        address,
        normalizers,
        function_identifier,
        transaction,
        block_id=None,
        contract_abi=None,
        fn_abi=None,
        *args,
        **kwargs):
    """
    Helper function for interacting with a contract function using the
    `eth_call` API.
    """
    call_transaction = prepare_transaction(
        address,
        web3,
        fn_identifier=function_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    if block_id is None:
        return_data = web3.eth.call(call_transaction)
    else:
        return_data = web3.eth.call(call_transaction, block_identifier=block_id)

    if fn_abi is None:
        fn_abi = find_matching_fn_abi(contract_abi, function_identifier, args, kwargs)

    output_types = get_abi_output_types(fn_abi)

    try:
        output_data = decode_abi(output_types, return_data)
    except DecodingError as e:
        # Provide a more helpful error message than the one provided by
        # eth-abi-utils
        is_missing_code_error = (
            return_data in ACCEPTABLE_EMPTY_STRINGS and
            web3.eth.getCode(address) in ACCEPTABLE_EMPTY_STRINGS
        )
        if is_missing_code_error:
            msg = (
                "Could not transact with/call contract function, is contract "
                "deployed correctly and chain synced?"
            )
        else:
            msg = (
                "Could not decode contract function call {} return data {} for "
                "output_types {}".format(
                    function_identifier,
                    return_data,
                    output_types
                )
            )
        raise BadFunctionCallOutput(msg) from e

    _normalizers = itertools.chain(
        BASE_RETURN_NORMALIZERS,
        normalizers,
    )
    normalized_data = map_abi_data(_normalizers, output_types, output_data)

    if len(normalized_data) == 1:
        return normalized_data[0]
    else:
        return normalized_data


def parse_block_identifier(web3, block_identifier):
    if isinstance(block_identifier, int):
        return parse_block_identifier_int(web3, block_identifier)
    elif block_identifier in ['latest', 'earliest', 'pending']:
        return block_identifier
    elif isinstance(block_identifier, bytes) or is_hex_encoded_block_hash(block_identifier):
        return web3.eth.getBlock(block_identifier)['number']
    else:
        raise BlockNumberOutofRange


def parse_block_identifier_int(web3, block_identifier_int):
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = web3.eth.getBlock('latest')['number']
        block_num = last_block + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutofRange
    return block_num


def transact_with_contract_function(
        address,
        web3,
        function_name=None,
        transaction=None,
        contract_abi=None,
        fn_abi=None,
        *args,
        **kwargs):
    """
    Helper function for interacting with a contract function by sending a
    transaction.
    """
    transact_transaction = prepare_transaction(
        address,
        web3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        transaction=transaction,
        fn_abi=fn_abi,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    txn_hash = web3.eth.sendTransaction(transact_transaction)
    return txn_hash


def estimate_gas_for_function(
        address,
        web3,
        fn_identifier=None,
        transaction=None,
        contract_abi=None,
        fn_abi=None,
        *args,
        **kwargs):
    """Estimates gas cost a function call would take.

    Don't call this directly, instead use :meth:`Contract.estimateGas`
    on your contract instance.
    """
    estimate_transaction = prepare_transaction(
        address,
        web3,
        fn_identifier=fn_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    gas_estimate = web3.eth.estimateGas(estimate_transaction)
    return gas_estimate


def build_transaction_for_function(
        address,
        web3,
        function_name=None,
        transaction=None,
        contract_abi=None,
        fn_abi=None,
        *args,
        **kwargs):
    """Builds a dictionary with the fields required to make the given transaction

    Don't call this directly, instead use :meth:`Contract.buildTransaction`
    on your contract instance.
    """
    prepared_transaction = prepare_transaction(
        address,
        web3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    prepared_transaction = fill_transaction_defaults(web3, prepared_transaction)

    return prepared_transaction


def find_functions_by_identifier(contract_abi, web3, address, callable_check):
    fns_abi = filter_by_type('function', contract_abi)
    return [
        ContractFunction.factory(
            fn_abi['name'],
            web3=web3,
            contract_abi=contract_abi,
            address=address,
            function_identifier=fn_abi['name'],
            abi=fn_abi
        )
        for fn_abi in fns_abi
        if callable_check(fn_abi)
    ]


def get_function_by_identifier(fns, identifier):
    if len(fns) > 1:
        raise ValueError(
            'Found multiple functions with matching {0}. '
            'Found: {1!r}'.format(identifier, fns)
        )
    elif len(fns) == 0:
        raise ValueError(
            'Could not find any function with matching {0}'.format(identifier)
        )
    return fns[0]
