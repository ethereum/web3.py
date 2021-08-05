"""Interaction with smart contracts over Web3 connector.

"""
import copy
import itertools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
    Generator,
    Iterable,
    List,
    NoReturn,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)
import warnings

from eth_abi.exceptions import (
    DecodingError,
)
from eth_typing import (
    Address,
    BlockNumber,
    ChecksumAddress,
    HexStr,
)
from eth_utils import (
    add_0x_prefix,
    combomethod,
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
    get_abi_input_names,
    get_abi_input_types,
    get_abi_output_types,
    get_constructor_abi,
    is_array_type,
    map_abi_data,
    merge_args_and_kwargs,
    receive_func_abi_exists,
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
    LogFilter,
    construct_event_filter_params,
)
from web3._utils.function_identifiers import (
    FallbackFn,
    ReceiveFn,
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
from web3.datastructures import (
    AttributeDict,
    MutableAttributeDict,
)
from web3.exceptions import (
    ABIEventFunctionNotFound,
    ABIFunctionNotFound,
    BadFunctionCallOutput,
    BlockNumberOutofRange,
    FallbackNotFound,
    InvalidEventABI,
    LogTopicError,
    MismatchedABI,
    NoABIEventsFound,
    NoABIFound,
    NoABIFunctionsFound,
    ValidationError,
)
from web3.logs import (
    DISCARD,
    IGNORE,
    STRICT,
    WARN,
    EventLogErrorFlags,
)
from web3.types import (  # noqa: F401
    ABI,
    ABIEvent,
    ABIFunction,
    BlockIdentifier,
    CallOverrideParams,
    EventData,
    FunctionIdentifier,
    LogReceipt,
    TxParams,
    TxReceipt,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401

ACCEPTABLE_EMPTY_STRINGS = ["0x", b"0x", "", b""]


class ContractFunctions:
    """Class containing contract function objects
    """

    def __init__(self, abi: ABI, web3: 'Web3', address: Optional[ChecksumAddress] = None) -> None:
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

    def __iter__(self) -> Generator[str, None, None]:
        if not hasattr(self, '_functions') or not self._functions:
            return

        for func in self._functions:
            yield func['name']

    def __getattr__(self, function_name: str) -> "ContractFunction":
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
            raise ABIFunctionNotFound(
                "The function '{}' was not found in this contract's abi. ".format(function_name),
                "Are you sure you provided the correct contract abi?"
            )
        else:
            return super().__getattribute__(function_name)

    def __getitem__(self, function_name: str) -> ABIFunction:
        return getattr(self, function_name)

    def __hasattr__(self, event_name: str) -> bool:
        try:
            return event_name in self.__dict__['_events']
        except ABIFunctionNotFound:
            return False


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

    def __init__(self, abi: ABI, web3: 'Web3', address: Optional[ChecksumAddress] = None) -> None:
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

    def __getattr__(self, event_name: str) -> Type['ContractEvent']:
        if '_events' not in self.__dict__:
            raise NoABIEventsFound(
                "The abi for this contract contains no event definitions. ",
                "Are you sure you provided the correct contract abi?"
            )
        elif event_name not in self.__dict__['_events']:
            raise ABIEventFunctionNotFound(
                "The event '{}' was not found in this contract's abi. ".format(event_name),
                "Are you sure you provided the correct contract abi?"
            )
        else:
            return super().__getattribute__(event_name)

    def __getitem__(self, event_name: str) -> Type['ContractEvent']:
        return getattr(self, event_name)

    def __iter__(self) -> Iterable[Type['ContractEvent']]:
        """Iterate over supported

        :return: Iterable of :class:`ContractEvent`
        """
        for event in self._events:
            yield self[event['name']]

    def __hasattr__(self, event_name: str) -> bool:
        try:
            return event_name in self.__dict__['_events']
        except ABIEventFunctionNotFound:
            return False


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

    * Deploy a new smart contract using :py:meth:`Contract.constructor.transact()`
    """

    # set during class construction
    web3: 'Web3' = None

    # instance level properties
    address: ChecksumAddress = None

    # class properties (overridable at instance level)
    abi: ABI = None

    asm = None
    ast = None

    bytecode = None
    bytecode_runtime = None
    clone_bin = None

    functions: ContractFunctions = None
    caller: 'ContractCaller' = None

    #: Instance of :class:`ContractEvents` presenting available Event ABIs
    events: ContractEvents = None

    dev_doc = None
    interface = None
    metadata = None
    opcodes = None
    src_map = None
    src_map_runtime = None
    user_doc = None

    def __init__(self, address: Optional[ChecksumAddress] = None) -> None:
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
        self.receive = Contract.get_receive_function(self.abi, self.web3, self.address)

    @classmethod
    def factory(cls, web3: 'Web3', class_name: Optional[str] = None, **kwargs: Any) -> 'Contract':

        kwargs['web3'] = web3

        normalizers = {
            'abi': normalize_abi,
            'address': partial(normalize_address, kwargs['web3'].ens),
            'bytecode': normalize_bytecode,
            'bytecode_runtime': normalize_bytecode,
        }

        contract = cast(Contract, PropertyCheckingFactory(
            class_name or cls.__name__,
            (cls,),
            kwargs,
            normalizers=normalizers,
        ))
        contract.functions = ContractFunctions(contract.abi, contract.web3)
        contract.caller = ContractCaller(contract.abi, contract.web3, contract.address)
        contract.events = ContractEvents(contract.abi, contract.web3)
        contract.fallback = Contract.get_fallback_function(contract.abi, contract.web3)
        contract.receive = Contract.get_receive_function(contract.abi, contract.web3)

        return contract

    #
    # Contract Methods
    #
    @classmethod
    def constructor(cls, *args: Any, **kwargs: Any) -> 'ContractConstructor':
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
    def encodeABI(cls, fn_name: str, args: Optional[Any] = None,
                  kwargs: Optional[Any] = None, data: Optional[HexStr] = None) -> HexStr:
        """
        Encodes the arguments using the Ethereum ABI for the contract function
        that matches the given name and arguments..

        :param data: defaults to function selector
        """
        fn_abi, fn_selector, fn_arguments = get_function_info(
            fn_name, cls.web3.codec, contract_abi=cls.abi, args=args, kwargs=kwargs,
        )

        if data is None:
            data = fn_selector

        return encode_abi(cls.web3, fn_abi, fn_arguments, data)

    @combomethod
    def all_functions(self) -> List['ContractFunction']:
        return find_functions_by_identifier(
            self.abi, self.web3, self.address, lambda _: True
        )

    @combomethod
    def get_function_by_signature(self, signature: str) -> 'ContractFunction':
        if ' ' in signature:
            raise ValueError(
                'Function signature should not contain any spaces. '
                'Found spaces in input: %s' % signature
            )

        def callable_check(fn_abi: ABIFunction) -> bool:
            return abi_to_signature(fn_abi) == signature

        fns = find_functions_by_identifier(self.abi, self.web3, self.address, callable_check)
        return get_function_by_identifier(fns, 'signature')

    @combomethod
    def find_functions_by_name(self, fn_name: str) -> List['ContractFunction']:
        def callable_check(fn_abi: ABIFunction) -> bool:
            return fn_abi['name'] == fn_name

        return find_functions_by_identifier(
            self.abi, self.web3, self.address, callable_check
        )

    @combomethod
    def get_function_by_name(self, fn_name: str) -> 'ContractFunction':
        fns = self.find_functions_by_name(fn_name)
        return get_function_by_identifier(fns, 'name')

    @combomethod
    def get_function_by_selector(self, selector: Union[bytes, int, HexStr]) -> 'ContractFunction':
        def callable_check(fn_abi: ABIFunction) -> bool:
            # typed dict cannot be used w/ a normal Dict
            # https://github.com/python/mypy/issues/4976
            return encode_hex(function_abi_to_4byte_selector(fn_abi)) == to_4byte_hex(selector)  # type: ignore # noqa: E501

        fns = find_functions_by_identifier(self.abi, self.web3, self.address, callable_check)
        return get_function_by_identifier(fns, 'selector')

    @combomethod
    def decode_function_input(self, data: HexStr) -> Tuple['ContractFunction', Dict[str, Any]]:
        # type ignored b/c expects data arg to be HexBytes
        data = HexBytes(data)  # type: ignore
        selector, params = data[:4], data[4:]
        func = self.get_function_by_selector(selector)

        names = get_abi_input_names(func.abi)
        types = get_abi_input_types(func.abi)

        decoded = self.web3.codec.decode_abi(types, cast(HexBytes, params))
        normalized = map_abi_data(BASE_RETURN_NORMALIZERS, types, decoded)

        return func, dict(zip(names, normalized))

    @combomethod
    def find_functions_by_args(self, *args: Any) -> List['ContractFunction']:
        def callable_check(fn_abi: ABIFunction) -> bool:
            return check_if_arguments_can_be_encoded(fn_abi, self.web3.codec, args=args, kwargs={})

        return find_functions_by_identifier(
            self.abi, self.web3, self.address, callable_check
        )

    @combomethod
    def get_function_by_args(self, *args: Any) -> 'ContractFunction':
        fns = self.find_functions_by_args(*args)
        return get_function_by_identifier(fns, 'args')

    #
    # Private Helpers
    #
    _return_data_normalizers: Tuple[Callable[..., Any], ...] = tuple()

    @classmethod
    def _prepare_transaction(cls,
                             fn_name: str,
                             fn_args: Optional[Any] = None,
                             fn_kwargs: Optional[Any] = None,
                             transaction: Optional[TxParams] = None) -> TxParams:

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
    def _find_matching_fn_abi(
        cls, fn_identifier: Optional[str] = None, args: Optional[Any] = None,
        kwargs: Optional[Any] = None
    ) -> ABIFunction:
        return find_matching_fn_abi(cls.abi,
                                    cls.web3.codec,
                                    fn_identifier=fn_identifier,
                                    args=args,
                                    kwargs=kwargs)

    @classmethod
    def _find_matching_event_abi(
        cls, event_name: Optional[str] = None, argument_names: Optional[Sequence[str]] = None
    ) -> ABIEvent:
        return find_matching_event_abi(
            abi=cls.abi,
            event_name=event_name,
            argument_names=argument_names)

    @staticmethod
    def get_fallback_function(
        abi: ABI, web3: 'Web3', address: Optional[ChecksumAddress] = None
    ) -> 'ContractFunction':
        if abi and fallback_func_abi_exists(abi):
            return ContractFunction.factory(
                'fallback',
                web3=web3,
                contract_abi=abi,
                address=address,
                function_identifier=FallbackFn)()

        return cast('ContractFunction', NonExistentFallbackFunction())

    @staticmethod
    def get_receive_function(
        abi: ABI, web3: 'Web3', address: Optional[ChecksumAddress] = None
    ) -> 'ContractFunction':
        if abi and receive_func_abi_exists(abi):
            return ContractFunction.factory(
                'receive',
                web3=web3,
                contract_abi=abi,
                address=address,
                function_identifier=ReceiveFn)()

        return cast('ContractFunction', NonExistentReceiveFunction())

    @combomethod
    def _encode_constructor_data(cls, args: Optional[Any] = None,
                                 kwargs: Optional[Any] = None) -> HexStr:
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


def mk_collision_prop(fn_name: str) -> Callable[[], None]:
    def collision_fn() -> NoReturn:
        msg = "Namespace collision for function name {0} with ConciseContract API.".format(fn_name)
        raise AttributeError(msg)
    collision_fn.__name__ = fn_name
    return collision_fn


class ContractConstructor:
    """
    Class for contract constructor API.
    """
    def __init__(
        self, web3: 'Web3', abi: ABI, bytecode: HexStr, *args: Any, **kwargs: Any
    ) -> None:
        self.web3 = web3
        self.abi = abi
        self.bytecode = bytecode
        self.data_in_transaction = self._encode_data_in_transaction(*args, **kwargs)

    @combomethod
    def _encode_data_in_transaction(self, *args: Any, **kwargs: Any) -> HexStr:
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
    def estimateGas(
        self, transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None
    ) -> int:
        if transaction is None:
            estimate_gas_transaction: TxParams = {}
        else:
            estimate_gas_transaction = cast(TxParams, dict(**transaction))
            self.check_forbidden_keys_in_transaction(estimate_gas_transaction,
                                                     ["data", "to"])

        if self.web3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            estimate_gas_transaction.setdefault('from', self.web3.eth.default_account)  # type: ignore # noqa: E501

        estimate_gas_transaction['data'] = self.data_in_transaction

        return self.web3.eth.estimate_gas(
            estimate_gas_transaction, block_identifier=block_identifier
        )

    @combomethod
    def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        if transaction is None:
            transact_transaction: TxParams = {}
        else:
            transact_transaction = cast(TxParams, dict(**transaction))
            self.check_forbidden_keys_in_transaction(transact_transaction,
                                                     ["data", "to"])

        if self.web3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            transact_transaction.setdefault('from', self.web3.eth.default_account)  # type: ignore

        transact_transaction['data'] = self.data_in_transaction

        # TODO: handle asynchronous contract creation
        return self.web3.eth.send_transaction(transact_transaction)

    @combomethod
    def buildTransaction(self, transaction: Optional[TxParams] = None) -> TxParams:
        """
        Build the transaction dictionary without sending
        """

        if transaction is None:
            built_transaction: TxParams = {}
        else:
            built_transaction = cast(TxParams, dict(**transaction))
            self.check_forbidden_keys_in_transaction(built_transaction,
                                                     ["data", "to"])

        if self.web3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            built_transaction.setdefault('from', self.web3.eth.default_account)  # type: ignore

        built_transaction['data'] = self.data_in_transaction
        built_transaction['to'] = Address(b'')
        return fill_transaction_defaults(self.web3, built_transaction)

    @staticmethod
    def check_forbidden_keys_in_transaction(
        transaction: TxParams, forbidden_keys: Optional[Collection[str]] = None
    ) -> None:
        keys_found = set(transaction.keys()) & set(forbidden_keys)
        if keys_found:
            raise ValueError("Cannot set {} in transaction".format(', '.join(keys_found)))


class ConciseMethod:
    ALLOWED_MODIFIERS = {'call', 'estimateGas', 'transact', 'buildTransaction'}

    def __init__(
        self, function: 'ContractFunction',
        normalizers: Optional[Tuple[Callable[..., Any], ...]] = None
    ) -> None:
        self._function = function
        self._function._return_data_normalizers = normalizers

    def __call__(self, *args: Any, **kwargs: Any) -> 'ContractFunction':
        return self.__prepared_function(*args, **kwargs)

    def __prepared_function(self, *args: Any, **kwargs: Any) -> 'ContractFunction':
        modifier_dict: Dict[Any, Any]
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
    def __init__(
        self,
        classic_contract: Contract,
        method_class: Union[Type['ConciseMethod'], Type['ImplicitMethod']] = ConciseMethod
    ) -> None:
        classic_contract._return_data_normalizers += CONCISE_NORMALIZERS
        self._classic_contract = classic_contract
        self.address = self._classic_contract.address

        protected_fn_names = [fn for fn in dir(self) if not fn.endswith('__')]

        for fn_name in self._classic_contract.functions:

            # Override namespace collisions
            if fn_name in protected_fn_names:
                _concise_method = cast('ConciseMethod', mk_collision_prop(fn_name))

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
    def factory(cls, *args: Any, **kwargs: Any) -> Contract:
        return compose(cls, Contract.factory(*args, **kwargs))


def _none_addr(datatype: str, data: ChecksumAddress) -> Tuple[str, Optional[ChecksumAddress]]:
    if datatype == 'address' and int(data, base=16) == 0:
        return (datatype, None)
    else:
        return (datatype, data)


CONCISE_NORMALIZERS: Tuple[Callable[..., Any]] = (
    _none_addr,
)


class ImplicitMethod(ConciseMethod):
    def __call_by_default(self, args: Any) -> bool:
        function_abi = find_matching_fn_abi(self._function.contract_abi,
                                            self._function.web3.codec,
                                            fn_identifier=self._function.function_identifier,
                                            args=args)

        return function_abi['constant'] if 'constant' in function_abi.keys() else False

    @deprecated_for("classic contract syntax. Ex: contract.functions.withdraw(amount).transact({})")
    def __call__(self, *args: Any, **kwargs: Any) -> 'ContractFunction':
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
    def __init__(
        self,
        classic_contract: Contract,
        method_class: Union[Type[ImplicitMethod], Type[ConciseMethod]] = ImplicitMethod
    ) -> None:
        super().__init__(classic_contract, method_class=method_class)


class NonExistentFallbackFunction:
    @staticmethod
    def _raise_exception() -> NoReturn:
        raise FallbackNotFound("No fallback function was found in the contract ABI.")

    def __getattr__(self, attr: Any) -> Callable[[], None]:
        return self._raise_exception


class NonExistentReceiveFunction:
    @staticmethod
    def _raise_exception() -> NoReturn:
        raise FallbackNotFound("No receive function was found in the contract ABI.")

    def __getattr__(self, attr: Any) -> Callable[[], None]:
        return self._raise_exception


class ContractFunction:
    """Base class for contract functions

    A function accessed via the api contract.functions.myMethod(*args, **kwargs)
    is a subclass of this class.
    """
    address: ChecksumAddress = None
    function_identifier: FunctionIdentifier = None
    web3: 'Web3' = None
    contract_abi: ABI = None
    abi: ABIFunction = None
    transaction: TxParams = None
    arguments: Tuple[Any, ...] = None
    args: Any = None
    kwargs: Any = None

    def __init__(self, abi: Optional[ABIFunction] = None) -> None:
        self.abi = abi
        self.fn_name = type(self).__name__

    def __call__(self, *args: Any, **kwargs: Any) -> 'ContractFunction':
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

    def _set_function_info(self) -> None:
        if not self.abi:
            self.abi = find_matching_fn_abi(
                self.contract_abi,
                self.web3.codec,
                self.function_identifier,
                self.args,
                self.kwargs
            )
        if self.function_identifier is FallbackFn:
            self.selector = encode_hex(b'')
        elif self.function_identifier is ReceiveFn:
            self.selector = encode_hex(b'')
        elif is_text(self.function_identifier):
            # https://github.com/python/mypy/issues/4976
            self.selector = encode_hex(function_abi_to_4byte_selector(self.abi))  # type: ignore
        else:
            raise TypeError("Unsupported function identifier")

        self.arguments = merge_args_and_kwargs(self.abi, self.args, self.kwargs)

    def call(
        self, transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = 'latest',
        state_override: Optional[CallOverrideParams] = None,
    ) -> Any:
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
            call_transaction: TxParams = {}
        else:
            call_transaction = cast(TxParams, dict(**transaction))

        if 'data' in call_transaction:
            raise ValueError("Cannot set data in call transaction")

        if self.address:
            call_transaction.setdefault('to', self.address)
        if self.web3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            call_transaction.setdefault('from', self.web3.eth.default_account)  # type: ignore

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
            state_override,
            *self.args,
            **self.kwargs
        )

    def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        if transaction is None:
            transact_transaction: TxParams = {}
        else:
            transact_transaction = cast(TxParams, dict(**transaction))

        if 'data' in transact_transaction:
            raise ValueError("Cannot set data in transact transaction")

        if self.address is not None:
            transact_transaction.setdefault('to', self.address)
        if self.web3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            transact_transaction.setdefault('from', self.web3.eth.default_account)  # type: ignore

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

    def estimateGas(
        self, transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None
    ) -> int:
        if transaction is None:
            estimate_gas_transaction: TxParams = {}
        else:
            estimate_gas_transaction = cast(TxParams, dict(**transaction))

        if 'data' in estimate_gas_transaction:
            raise ValueError("Cannot set data in estimateGas transaction")
        if 'to' in estimate_gas_transaction:
            raise ValueError("Cannot set to in estimateGas transaction")

        if self.address:
            estimate_gas_transaction.setdefault('to', self.address)
        if self.web3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            estimate_gas_transaction.setdefault('from', self.web3.eth.default_account)  # type: ignore # noqa: E501

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
            block_identifier,
            *self.args,
            **self.kwargs
        )

    def buildTransaction(self, transaction: Optional[TxParams] = None) -> TxParams:
        """
        Build the transaction dictionary without sending
        """
        if transaction is None:
            built_transaction: TxParams = {}
        else:
            built_transaction = cast(TxParams, dict(**transaction))

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
    def _encode_transaction_data(cls) -> HexStr:
        return add_0x_prefix(encode_abi(cls.web3, cls.abi, cls.arguments, cls.selector))

    _return_data_normalizers: Optional[Tuple[Callable[..., Any], ...]] = tuple()

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> 'ContractFunction':
        return PropertyCheckingFactory(class_name, (cls,), kwargs)(kwargs.get('abi'))

    def __repr__(self) -> str:
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
    address: ChecksumAddress = None
    event_name: str = None
    web3: 'Web3' = None
    contract_abi: ABI = None
    abi: ABIEvent = None

    def __init__(self, *argument_names: Tuple[str]) -> None:

        if argument_names is None:
            # https://github.com/python/mypy/issues/6283
            self.argument_names = tuple()  # type: ignore
        else:
            self.argument_names = argument_names

        self.abi = self._get_event_abi()

    @classmethod
    def _get_event_abi(cls) -> ABIEvent:
        return find_matching_event_abi(
            cls.contract_abi,
            event_name=cls.event_name)

    @combomethod
    def processReceipt(
        self, txn_receipt: TxReceipt, errors: EventLogErrorFlags = WARN
    ) -> Iterable[EventData]:
        return self._parse_logs(txn_receipt, errors)

    @to_tuple
    def _parse_logs(
        self, txn_receipt: TxReceipt, errors: EventLogErrorFlags
    ) -> Iterable[EventData]:
        try:
            errors.name
        except AttributeError:
            raise AttributeError(f'Error flag must be one of: {EventLogErrorFlags.flag_options()}')

        for log in txn_receipt['logs']:
            try:
                rich_log = get_event_data(self.web3.codec, self.abi, log)
            except (MismatchedABI, LogTopicError, InvalidEventABI, TypeError) as e:
                if errors == DISCARD:
                    continue
                elif errors == IGNORE:
                    # type ignores b/c rich_log set on 1092 conflicts with mutated types
                    new_log = MutableAttributeDict(log)  # type: ignore
                    new_log['errors'] = e
                    rich_log = AttributeDict(new_log)  # type: ignore
                elif errors == STRICT:
                    raise e
                else:
                    warnings.warn(
                        f"The log with transaction hash: {log['transactionHash']!r} and "
                        f"logIndex: {log['logIndex']} encountered the following error "
                        f"during processing: {type(e).__name__}({e}). It has been discarded."
                    )
                    continue
            yield rich_log

    @combomethod
    def processLog(self, log: HexStr) -> EventData:
        return get_event_data(self.web3.codec, self.abi, log)

    @combomethod
    def createFilter(
            self, *,  # PEP 3102
            argument_filters: Optional[Dict[str, Any]] = None,
            fromBlock: Optional[BlockIdentifier] = None,
            toBlock: BlockIdentifier = "latest",
            address: Optional[ChecksumAddress] = None,
            topics: Optional[Sequence[Any]] = None) -> LogFilter:
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
            self.web3.codec,
            contract_address=self.address,
            argument_filters=_filters,
            fromBlock=fromBlock,
            toBlock=toBlock,
            address=address,
            topics=topics,
        )

        filter_builder = EventFilterBuilder(event_abi, self.web3.codec)
        filter_builder.address = cast(ChecksumAddress, event_filter_params.get('address'))
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
        log_filter.log_entry_formatter = get_event_data(self.web3.codec, self._get_event_abi())
        log_filter.builder = filter_builder

        return log_filter

    @combomethod
    def build_filter(self) -> EventFilterBuilder:
        builder = EventFilterBuilder(
            self._get_event_abi(),
            self.web3.codec,
            formatter=get_event_data(self.web3.codec, self._get_event_abi()))
        builder.address = self.address
        return builder

    @combomethod
    def getLogs(self,
                argument_filters: Optional[Dict[str, Any]] = None,
                fromBlock: Optional[BlockIdentifier] = None,
                toBlock: Optional[BlockIdentifier] = None,
                blockHash: Optional[HexBytes] = None) -> Iterable[EventData]:
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

            from = max(mycontract.web3.eth.block_number - 10, 1)
            to = mycontract.web3.eth.block_number

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
            self.web3.codec,
            contract_address=self.address,
            argument_filters=_filters,
            fromBlock=fromBlock,
            toBlock=toBlock,
            address=self.address,
        )

        if blockHash is not None:
            event_filter_params['blockHash'] = blockHash

        # Call JSON-RPC API
        logs = self.web3.eth.get_logs(event_filter_params)

        # Convert raw binary data to Python proxy objects as described by ABI
        return tuple(get_event_data(self.web3.codec, abi, entry) for entry in logs)

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> PropertyCheckingFactory:
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
                 abi: ABI,
                 web3: 'Web3',
                 address: ChecksumAddress,
                 transaction: Optional[TxParams] = None,
                 block_identifier: BlockIdentifier = 'latest') -> None:
        self.web3 = web3
        self.address = address
        self.abi = abi
        self._functions = None

        if self.abi:
            if transaction is None:
                transaction = {}

            self._functions = filter_by_type('function', self.abi)
            for func in self._functions:
                fn: ContractFunction = ContractFunction.factory(
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

    def __getattr__(self, function_name: str) -> Any:
        if self.abi is None:
            raise NoABIFound(
                "There is no ABI found for this contract.",
            )
        elif not self._functions or len(self._functions) == 0:
            raise NoABIFunctionsFound(
                "The ABI for this contract contains no function definitions. ",
                "Are you sure you provided the correct contract ABI?"
            )
        elif function_name not in set(fn['name'] for fn in self._functions):
            functions_available = ', '.join([fn['name'] for fn in self._functions])
            raise ABIFunctionNotFound(
                "The function '{}' was not found in this contract's ABI. ".format(function_name),
                "Here is a list of all of the function names found: ",
                "{}. ".format(functions_available),
                "Did you mean to call one of those functions?"
            )
        else:
            return super().__getattribute__(function_name)

    def __hasattr__(self, event_name: str) -> bool:
        try:
            return event_name in self.__dict__['_events']
        except ABIFunctionNotFound:
            return False

    def __call__(
        self, transaction: Optional[TxParams] = None, block_identifier: BlockIdentifier = 'latest'
    ) -> 'ContractCaller':
        if transaction is None:
            transaction = {}
        return type(self)(self.abi,
                          self.web3,
                          self.address,
                          transaction=transaction,
                          block_identifier=block_identifier)

    @staticmethod
    def call_function(
        fn: ContractFunction,
        *args: Any,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = 'latest',
        **kwargs: Any
    ) -> Any:
        if transaction is None:
            transaction = {}
        return fn(*args, **kwargs).call(transaction, block_identifier)


def check_for_forbidden_api_filter_arguments(
    event_abi: ABIEvent, _filters: Dict[str, Any]
) -> None:
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
        web3: 'Web3',
        address: ChecksumAddress,
        normalizers: Tuple[Callable[..., Any], ...],
        function_identifier: FunctionIdentifier,
        transaction: TxParams,
        block_id: Optional[BlockIdentifier] = None,
        contract_abi: Optional[ABI] = None,
        fn_abi: Optional[ABIFunction] = None,
        state_override: Optional[CallOverrideParams] = None,
        *args: Any,
        **kwargs: Any) -> Any:
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

    return_data = web3.eth.call(
        call_transaction,
        block_identifier=block_id,
        state_override=state_override,
    )

    if fn_abi is None:
        fn_abi = find_matching_fn_abi(contract_abi, web3.codec, function_identifier, args, kwargs)

    output_types = get_abi_output_types(fn_abi)

    try:
        output_data = web3.codec.decode_abi(output_types, return_data)
    except DecodingError as e:
        # Provide a more helpful error message than the one provided by
        # eth-abi-utils
        is_missing_code_error = (
            return_data in ACCEPTABLE_EMPTY_STRINGS
            and web3.eth.get_code(address) in ACCEPTABLE_EMPTY_STRINGS)
        if is_missing_code_error:
            msg = (
                "Could not transact with/call contract function, is contract "
                "deployed correctly and chain synced?"
            )
        else:
            msg = (
                f"Could not decode contract function call to {function_identifier} with "
                f"return data: {str(return_data)}, output_types: {output_types}"
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


def parse_block_identifier(web3: 'Web3', block_identifier: BlockIdentifier) -> BlockIdentifier:
    if isinstance(block_identifier, int):
        return parse_block_identifier_int(web3, block_identifier)
    elif block_identifier in ['latest', 'earliest', 'pending']:
        return block_identifier
    elif isinstance(block_identifier, bytes) or is_hex_encoded_block_hash(block_identifier):
        return web3.eth.get_block(block_identifier)['number']
    else:
        raise BlockNumberOutofRange


def parse_block_identifier_int(web3: 'Web3', block_identifier_int: int) -> BlockNumber:
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = web3.eth.get_block('latest')['number']
        block_num = last_block + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutofRange
    return BlockNumber(block_num)


def transact_with_contract_function(
        address: ChecksumAddress,
        web3: 'Web3',
        function_name: Optional[FunctionIdentifier] = None,
        transaction: Optional[TxParams] = None,
        contract_abi: Optional[ABI] = None,
        fn_abi: Optional[ABIFunction] = None,
        *args: Any,
        **kwargs: Any) -> HexBytes:
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

    txn_hash = web3.eth.send_transaction(transact_transaction)
    return txn_hash


def estimate_gas_for_function(
        address: ChecksumAddress,
        web3: 'Web3',
        fn_identifier: Optional[FunctionIdentifier] = None,
        transaction: Optional[TxParams] = None,
        contract_abi: Optional[ABI] = None,
        fn_abi: Optional[ABIFunction] = None,
        block_identifier: Optional[BlockIdentifier] = None,
        *args: Any,
        **kwargs: Any) -> int:
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

    return web3.eth.estimate_gas(estimate_transaction, block_identifier)


def build_transaction_for_function(
        address: ChecksumAddress,
        web3: 'Web3',
        function_name: Optional[FunctionIdentifier] = None,
        transaction: Optional[TxParams] = None,
        contract_abi: Optional[ABI] = None,
        fn_abi: Optional[ABIFunction] = None,
        *args: Any,
        **kwargs: Any) -> TxParams:
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


def find_functions_by_identifier(
    contract_abi: ABI, web3: 'Web3', address: ChecksumAddress, callable_check: Callable[..., Any]
) -> List[ContractFunction]:
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


def get_function_by_identifier(
    fns: Sequence[ContractFunction], identifier: str
) -> ContractFunction:
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
