"""Interaction with smart contracts over Web3 connector.

"""
import copy
import itertools
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
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
    get_abi_input_types,
    get_abi_output_types,
    get_constructor_abi,
    is_array_type,
    map_abi_data,
    merge_args_and_kwargs,
    receive_func_abi_exists,
)
from web3._utils.async_transactions import (
    fill_transaction_defaults as async_fill_transaction_defaults,
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
from web3._utils.empty import (
    empty,
)
from web3._utils.encoding import (
    to_4byte_hex,
    to_hex,
)
from web3._utils.events import (
    AsyncEventFilterBuilder,
    EventFilterBuilder,
    get_event_data,
    is_dynamic_sized_type,
)
from web3._utils.filters import (
    AsyncLogFilter,
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
    normalize_address_no_ens,
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
    CallOverride,
    EventData,
    FilterParams,
    FunctionIdentifier,
    LogReceipt,
    TxParams,
    TxReceipt,
)
from web3.utils import (
    get_abi_input_names,
)

if TYPE_CHECKING:
    from ens import ENS  # noqa: F401
    from web3 import Web3  # noqa: F401

ACCEPTABLE_EMPTY_STRINGS = ["0x", b"0x", "", b""]


class BaseContractFunctions:
    """Class containing contract function objects"""

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        contract_function_class: Union[
            Type["ContractFunction"], Type["AsyncContractFunction"]
        ],
        address: Optional[ChecksumAddress] = None,
    ) -> None:

        self.abi = abi
        self.w3 = w3
        self.address = address

        if self.abi:
            self._functions = filter_by_type("function", self.abi)
            for func in self._functions:
                setattr(
                    self,
                    func["name"],
                    contract_function_class.factory(
                        func["name"],
                        w3=self.w3,
                        contract_abi=self.abi,
                        address=self.address,
                        function_identifier=func["name"],
                    ),
                )

    def __iter__(self) -> Generator[str, None, None]:
        if not hasattr(self, "_functions") or not self._functions:
            return

        for func in self._functions:
            yield func["name"]

    def __getattr__(self, function_name: str) -> "ContractFunction":
        if self.abi is None:
            raise NoABIFound(
                "There is no ABI found for this contract.",
            )
        if "_functions" not in self.__dict__:
            raise NoABIFunctionsFound(
                "The abi for this contract contains no function definitions. ",
                "Are you sure you provided the correct contract abi?",
            )
        elif function_name not in self.__dict__["_functions"]:
            raise ABIFunctionNotFound(
                f"The function '{function_name}' was not found in this contract's abi.",
                " Are you sure you provided the correct contract abi?",
            )
        else:
            return super().__getattribute__(function_name)

    def __getitem__(self, function_name: str) -> ABIFunction:
        return getattr(self, function_name)

    def __hasattr__(self, event_name: str) -> bool:
        try:
            return event_name in self.__dict__["_events"]
        except ABIFunctionNotFound:
            return False


class ContractFunctions(BaseContractFunctions):
    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: Optional[ChecksumAddress] = None,
    ) -> None:
        super().__init__(abi, w3, ContractFunction, address)


class AsyncContractFunctions(BaseContractFunctions):
    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: Optional[ChecksumAddress] = None,
    ) -> None:
        super().__init__(abi, w3, AsyncContractFunction, address)


class BaseContractEvents:
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

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        contract_event_type: Union[Type["ContractEvent"], Type["AsyncContractEvent"]],
        address: Optional[ChecksumAddress] = None,
    ) -> None:
        if abi:
            self.abi = abi
            self._events = filter_by_type("event", self.abi)
            for event in self._events:
                setattr(
                    self,
                    event["name"],
                    contract_event_type.factory(
                        event["name"],
                        w3=w3,
                        contract_abi=self.abi,
                        address=address,
                        event_name=event["name"],
                    ),
                )

    def __getattr__(self, event_name: str) -> Type["ContractEvent"]:
        if "_events" not in self.__dict__:
            raise NoABIEventsFound(
                "The abi for this contract contains no event definitions. ",
                "Are you sure you provided the correct contract abi?",
            )
        elif event_name not in self.__dict__["_events"]:
            raise ABIEventFunctionNotFound(
                f"The event '{event_name}' was not found in this contract's abi. ",
                "Are you sure you provided the correct contract abi?",
            )
        else:
            return super().__getattribute__(event_name)

    def __getitem__(self, event_name: str) -> Type["ContractEvent"]:
        return getattr(self, event_name)

    def __iter__(self) -> Iterable[Type["ContractEvent"]]:
        """Iterate over supported

        :return: Iterable of :class:`ContractEvent`
        """
        for event in self._events:
            yield self[event["name"]]

    def __hasattr__(self, event_name: str) -> bool:
        try:
            return event_name in self.__dict__["_events"]
        except ABIEventFunctionNotFound:
            return False


class ContractEvents(BaseContractEvents):
    def __init__(
        self, abi: ABI, w3: "Web3", address: Optional[ChecksumAddress] = None
    ) -> None:
        super().__init__(abi, w3, ContractEvent, address)


class AsyncContractEvents(BaseContractEvents):
    def __init__(
        self, abi: ABI, w3: "Web3", address: Optional[ChecksumAddress] = None
    ) -> None:
        super().__init__(abi, w3, AsyncContractEvent, address)


class BaseContract:
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
    w3: "Web3" = None

    # instance level properties
    address: ChecksumAddress = None

    # class properties (overridable at instance level)
    abi: ABI = None

    asm = None
    ast = None

    bytecode = None
    bytecode_runtime = None
    clone_bin = None

    dev_doc = None
    interface = None
    metadata = None
    opcodes = None
    src_map = None
    src_map_runtime = None
    user_doc = None

    #  Public API
    #
    @combomethod
    def encodeABI(
        cls,
        fn_name: str,
        args: Optional[Any] = None,
        kwargs: Optional[Any] = None,
        data: Optional[HexStr] = None,
    ) -> HexStr:
        """
        Encodes the arguments using the Ethereum ABI for the contract function
        that matches the given name and arguments..

        :param data: defaults to function selector
        """
        fn_abi, fn_selector, fn_arguments = get_function_info(
            fn_name,
            cls.w3.codec,
            contract_abi=cls.abi,
            args=args,
            kwargs=kwargs,
        )

        if data is None:
            data = fn_selector

        return encode_abi(cls.w3, fn_abi, fn_arguments, data)

    @combomethod
    def all_functions(
        self,
    ) -> Union[List["ContractFunction"], List["AsyncContractFunction"]]:
        return self.find_functions_by_identifier(
            self.abi, self.w3, self.address, lambda _: True
        )

    @combomethod
    def get_function_by_signature(
        self, signature: str
    ) -> Union["ContractFunction", "AsyncContractFunction"]:
        if " " in signature:
            raise ValueError(
                "Function signature should not contain any spaces. "
                f"Found spaces in input: {signature}"
            )

        def callable_check(fn_abi: ABIFunction) -> bool:
            return abi_to_signature(fn_abi) == signature

        fns = self.find_functions_by_identifier(
            self.abi, self.w3, self.address, callable_check
        )
        return get_function_by_identifier(fns, "signature")

    @combomethod
    def find_functions_by_name(
        self, fn_name: str
    ) -> Union[List["ContractFunction"], List["AsyncContractFunction"]]:
        def callable_check(fn_abi: ABIFunction) -> bool:
            return fn_abi["name"] == fn_name

        return self.find_functions_by_identifier(
            self.abi, self.w3, self.address, callable_check
        )

    @combomethod
    def get_function_by_name(
        self, fn_name: str
    ) -> Union["ContractFunction", "AsyncContractFunction"]:
        fns = self.find_functions_by_name(fn_name)
        return get_function_by_identifier(fns, "name")

    @combomethod
    def get_function_by_selector(
        self, selector: Union[bytes, int, HexStr]
    ) -> Union["ContractFunction", "AsyncContractFunction"]:
        def callable_check(fn_abi: ABIFunction) -> bool:
            # typed dict cannot be used w/ a normal Dict
            # https://github.com/python/mypy/issues/4976
            return encode_hex(function_abi_to_4byte_selector(fn_abi)) == to_4byte_hex(selector)  # type: ignore # noqa: E501

        fns = self.find_functions_by_identifier(
            self.abi, self.w3, self.address, callable_check
        )
        return get_function_by_identifier(fns, "selector")

    @combomethod
    def decode_function_input(
        self, data: HexStr
    ) -> Union[
        Tuple["ContractFunction", Dict[str, Any]],
        Tuple["AsyncContractFunction", Dict[str, Any]],
    ]:
        # type ignored b/c expects data arg to be HexBytes
        data = HexBytes(data)  # type: ignore
        selector, params = data[:4], data[4:]
        func = self.get_function_by_selector(selector)

        names = get_abi_input_names(func.abi)
        types = get_abi_input_types(func.abi)

        decoded = self.w3.codec.decode(types, cast(HexBytes, params))
        normalized = map_abi_data(BASE_RETURN_NORMALIZERS, types, decoded)

        return func, dict(zip(names, normalized))

    @combomethod
    def find_functions_by_args(
        self, *args: Any
    ) -> Union[List["ContractFunction"], List["AsyncContractFunction"]]:
        def callable_check(fn_abi: ABIFunction) -> bool:
            return check_if_arguments_can_be_encoded(
                fn_abi, self.w3.codec, args=args, kwargs={}
            )

        return self.find_functions_by_identifier(
            self.abi, self.w3, self.address, callable_check
        )

    @combomethod
    def get_function_by_args(
        self, *args: Any
    ) -> Union["ContractFunction", "AsyncContractFunction"]:
        fns = self.find_functions_by_args(*args)
        return get_function_by_identifier(fns, "args")

    #
    # Private Helpers
    #
    _return_data_normalizers: Tuple[Callable[..., Any], ...] = tuple()

    @classmethod
    def _prepare_transaction(
        cls,
        fn_name: str,
        fn_args: Optional[Any] = None,
        fn_kwargs: Optional[Any] = None,
        transaction: Optional[TxParams] = None,
    ) -> TxParams:

        return prepare_transaction(
            cls.address,
            cls.w3,
            fn_identifier=fn_name,
            contract_abi=cls.abi,
            transaction=transaction,
            fn_args=fn_args,
            fn_kwargs=fn_kwargs,
        )

    @classmethod
    def _find_matching_fn_abi(
        cls,
        fn_identifier: Optional[str] = None,
        args: Optional[Any] = None,
        kwargs: Optional[Any] = None,
    ) -> ABIFunction:
        return find_matching_fn_abi(
            cls.abi, cls.w3.codec, fn_identifier=fn_identifier, args=args, kwargs=kwargs
        )

    @classmethod
    def _find_matching_event_abi(
        cls,
        event_name: Optional[str] = None,
        argument_names: Optional[Sequence[str]] = None,
    ) -> ABIEvent:
        return find_matching_event_abi(
            abi=cls.abi, event_name=event_name, argument_names=argument_names
        )

    @combomethod
    def _encode_constructor_data(
        cls, args: Optional[Any] = None, kwargs: Optional[Any] = None
    ) -> HexStr:
        constructor_abi = get_constructor_abi(cls.abi)

        if constructor_abi:
            if args is None:
                args = tuple()
            if kwargs is None:
                kwargs = {}

            arguments = merge_args_and_kwargs(constructor_abi, args, kwargs)

            deploy_data = add_0x_prefix(
                encode_abi(cls.w3, constructor_abi, arguments, data=cls.bytecode)
            )
        else:
            if args is not None or kwargs is not None:
                msg = "Constructor args were provided, but no constructor function was provided."  # noqa: E501
                raise TypeError(msg)

            deploy_data = to_hex(cls.bytecode)

        return deploy_data

    @combomethod
    def find_functions_by_identifier(
        cls,
        contract_abi: ABI,
        w3: "Web3",
        address: ChecksumAddress,
        callable_check: Callable[..., Any],
    ) -> List[Any]:
        raise NotImplementedError(
            "This method should be implemented in the inherited class"
        )

    @staticmethod
    def get_fallback_function(
        abi: ABI,
        w3: "Web3",
        function_type: Union[Type["ContractFunction"], Type["AsyncContractFunction"]],
        address: Optional[ChecksumAddress] = None,
    ) -> Union["ContractFunction", "AsyncContractFunction"]:
        if abi and fallback_func_abi_exists(abi):
            return function_type.factory(
                "fallback",
                w3=w3,
                contract_abi=abi,
                address=address,
                function_identifier=FallbackFn,
            )()

        return cast(function_type, NonExistentFallbackFunction())  # type: ignore

    @staticmethod
    def get_receive_function(
        abi: ABI,
        w3: "Web3",
        function_type: Union[Type["ContractFunction"], Type["AsyncContractFunction"]],
        address: Optional[ChecksumAddress] = None,
    ) -> Union["ContractFunction", "AsyncContractFunction"]:
        if abi and receive_func_abi_exists(abi):
            return function_type.factory(
                "receive",
                w3=w3,
                contract_abi=abi,
                address=address,
                function_identifier=ReceiveFn,
            )()

        return cast(function_type, NonExistentReceiveFunction())  # type: ignore


class Contract(BaseContract):

    functions: ContractFunctions = None
    caller: "ContractCaller" = None

    #: Instance of :class:`ContractEvents` presenting available Event ABIs
    events: ContractEvents = None

    def __init__(self, address: Optional[ChecksumAddress] = None) -> None:
        """Create a new smart contract proxy object.

        :param address: Contract address as 0x hex string"""

        _w3 = self.w3
        if _w3 is None:
            raise AttributeError(
                "The `Contract` class has not been initialized.  Please use the "
                "`web3.contract` interface to create your contract class."
            )

        if address:
            _ens = cast("ENS", _w3.ens)
            self.address = normalize_address(_ens, address)

        if not self.address:
            raise TypeError(
                "The address argument is required to instantiate a contract."
            )

        self.functions = ContractFunctions(self.abi, _w3, self.address)
        self.caller = ContractCaller(self.abi, _w3, self.address)
        self.events = ContractEvents(self.abi, _w3, self.address)
        self.fallback = Contract.get_fallback_function(
            self.abi,
            _w3,
            ContractFunction,
            self.address,
        )
        self.receive = Contract.get_receive_function(
            self.abi,
            _w3,
            ContractFunction,
            self.address,
        )

    @classmethod
    def factory(
        cls, w3: "Web3", class_name: Optional[str] = None, **kwargs: Any
    ) -> "Contract":
        kwargs["w3"] = w3

        normalizers = {
            "abi": normalize_abi,
            "address": partial(normalize_address, kwargs["w3"].ens),
            "bytecode": normalize_bytecode,
            "bytecode_runtime": normalize_bytecode,
        }

        contract = cast(
            Contract,
            PropertyCheckingFactory(
                class_name or cls.__name__,
                (cls,),
                kwargs,
                normalizers=normalizers,
            ),
        )
        contract.functions = ContractFunctions(contract.abi, contract.w3)
        contract.caller = ContractCaller(contract.abi, contract.w3, contract.address)
        contract.events = ContractEvents(contract.abi, contract.w3)
        contract.fallback = Contract.get_fallback_function(
            contract.abi,
            contract.w3,
            ContractFunction,
        )
        contract.receive = Contract.get_receive_function(
            contract.abi,
            contract.w3,
            ContractFunction,
        )

        return contract

    @classmethod
    def constructor(cls, *args: Any, **kwargs: Any) -> "ContractConstructor":
        """
        :param args: The contract constructor arguments as positional arguments
        :param kwargs: The contract constructor arguments as keyword arguments
        :return: a contract constructor object
        """
        if cls.bytecode is None:
            raise ValueError(
                "Cannot call constructor on a contract that does not have "
                "'bytecode' associated with it"
            )

        return ContractConstructor(cls.w3, cls.abi, cls.bytecode, *args, **kwargs)

    @combomethod
    def find_functions_by_identifier(
        cls,
        contract_abi: ABI,
        w3: "Web3",
        address: ChecksumAddress,
        callable_check: Callable[..., Any],
    ) -> List["ContractFunction"]:
        return find_functions_by_identifier(  # type: ignore
            contract_abi, w3, address, callable_check, ContractFunction
        )


class AsyncContract(BaseContract):

    functions: AsyncContractFunctions = None
    caller: "AsyncContractCaller" = None

    #: Instance of :class:`ContractEvents` presenting available Event ABIs
    events: AsyncContractEvents = None

    def __init__(self, address: Optional[ChecksumAddress] = None) -> None:
        """Create a new smart contract proxy object.

        :param address: Contract address as 0x hex string"""

        if self.w3 is None:
            raise AttributeError(
                "The `Contract` class has not been initialized.  Please use the "
                "`web3.contract` interface to create your contract class."
            )

        if address:
            self.address = normalize_address_no_ens(address)

        if not self.address:
            raise TypeError(
                "The address argument is required to instantiate a contract."
            )
        self.functions = AsyncContractFunctions(self.abi, self.w3, self.address)
        self.caller = AsyncContractCaller(self.abi, self.w3, self.address)
        self.events = AsyncContractEvents(self.abi, self.w3, self.address)
        self.fallback = AsyncContract.get_fallback_function(
            self.abi, self.w3, AsyncContractFunction, self.address
        )
        self.receive = AsyncContract.get_receive_function(
            self.abi, self.w3, AsyncContractFunction, self.address
        )

    @classmethod
    def factory(
        cls, w3: "Web3", class_name: Optional[str] = None, **kwargs: Any
    ) -> "AsyncContract":
        kwargs["w3"] = w3

        normalizers = {
            "abi": normalize_abi,
            "address": normalize_address_no_ens,
            "bytecode": normalize_bytecode,
            "bytecode_runtime": normalize_bytecode,
        }

        contract = cast(
            AsyncContract,
            PropertyCheckingFactory(
                class_name or cls.__name__,
                (cls,),
                kwargs,
                normalizers=normalizers,
            ),
        )
        contract.functions = AsyncContractFunctions(contract.abi, contract.w3)
        contract.caller = AsyncContractCaller(
            contract.abi, contract.w3, contract.address
        )
        contract.events = AsyncContractEvents(contract.abi, contract.w3)
        contract.fallback = AsyncContract.get_fallback_function(
            contract.abi,
            contract.w3,
            AsyncContractFunction,
        )
        contract.receive = AsyncContract.get_receive_function(
            contract.abi,
            contract.w3,
            AsyncContractFunction,
        )
        return contract

    @classmethod
    def constructor(cls, *args: Any, **kwargs: Any) -> "AsyncContractConstructor":
        """
        :param args: The contract constructor arguments as positional arguments
        :param kwargs: The contract constructor arguments as keyword arguments
        :return: a contract constructor object
        """
        if cls.bytecode is None:
            raise ValueError(
                "Cannot call constructor on a contract that does not have "
                "'bytecode' associated with it"
            )

        return AsyncContractConstructor(cls.w3, cls.abi, cls.bytecode, *args, **kwargs)

    @combomethod
    def find_functions_by_identifier(
        cls,
        contract_abi: ABI,
        w3: "Web3",
        address: ChecksumAddress,
        callable_check: Callable[..., Any],
    ) -> List["AsyncContractFunction"]:
        return find_functions_by_identifier(  # type: ignore
            contract_abi, w3, address, callable_check, AsyncContractFunction
        )


class BaseContractConstructor:
    """
    Class for contract constructor API.
    """

    def __init__(
        self, w3: "Web3", abi: ABI, bytecode: HexStr, *args: Any, **kwargs: Any
    ) -> None:
        self.w3 = w3
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
                encode_abi(self.w3, constructor_abi, arguments, data=self.bytecode)
            )
        else:
            data = to_hex(self.bytecode)

        return data

    @combomethod
    def _estimate_gas(self, transaction: Optional[TxParams] = None) -> TxParams:
        if transaction is None:
            estimate_gas_transaction: TxParams = {}
        else:
            estimate_gas_transaction = cast(TxParams, dict(**transaction))
            self.check_forbidden_keys_in_transaction(
                estimate_gas_transaction, ["data", "to"]
            )

        if self.w3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            estimate_gas_transaction.setdefault(
                "from", self.w3.eth.default_account  # type: ignore
            )

        estimate_gas_transaction["data"] = self.data_in_transaction

        return estimate_gas_transaction

    def _get_transaction(self, transaction: Optional[TxParams] = None) -> TxParams:
        if transaction is None:
            transact_transaction: TxParams = {}
        else:
            transact_transaction = cast(TxParams, dict(**transaction))
            self.check_forbidden_keys_in_transaction(
                transact_transaction, ["data", "to"]
            )

        if self.w3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            transact_transaction.setdefault(
                "from", self.w3.eth.default_account  # type: ignore
            )

        transact_transaction["data"] = self.data_in_transaction

        return transact_transaction

    @combomethod
    def _build_transaction(self, transaction: Optional[TxParams] = None) -> TxParams:
        built_transaction = self._get_transaction(transaction)
        built_transaction["to"] = Address(b"")
        return built_transaction

    @staticmethod
    def check_forbidden_keys_in_transaction(
        transaction: TxParams, forbidden_keys: Optional[Collection[str]] = None
    ) -> None:
        keys_found = transaction.keys() & forbidden_keys
        if keys_found:
            raise ValueError(
                f"Cannot set '{', '.join(keys_found)}' field(s) in transaction"
            )


class ContractConstructor(BaseContractConstructor):
    @combomethod
    def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        return self.w3.eth.send_transaction(self._get_transaction(transaction))

    @combomethod
    def build_transaction(self, transaction: Optional[TxParams] = None) -> TxParams:
        """
        Build the transaction dictionary without sending
        """
        built_transaction = self._build_transaction(transaction)
        return fill_transaction_defaults(self.w3, built_transaction)

    @combomethod
    def estimate_gas(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> int:
        transaction = self._estimate_gas(transaction)

        return self.w3.eth.estimate_gas(transaction, block_identifier=block_identifier)


class AsyncContractConstructor(BaseContractConstructor):
    @combomethod
    async def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        return await self.w3.eth.send_transaction(  # type: ignore
            self._get_transaction(transaction)
        )

    @combomethod
    async def build_transaction(
        self, transaction: Optional[TxParams] = None
    ) -> TxParams:
        """
        Build the transaction dictionary without sending
        """
        built_transaction = self._build_transaction(transaction)
        return await async_fill_transaction_defaults(self.w3, built_transaction)

    @combomethod
    async def estimate_gas(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> int:
        transaction = self._estimate_gas(transaction)

        return await self.w3.eth.estimate_gas(  # type: ignore
            transaction, block_identifier=block_identifier
        )


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


class BaseContractFunction:
    """Base class for contract functions

    A function accessed via the api contract.functions.myMethod(*args, **kwargs)
    is a subclass of this class.
    """

    address: ChecksumAddress = None
    function_identifier: FunctionIdentifier = None
    w3: "Web3" = None
    contract_abi: ABI = None
    abi: ABIFunction = None
    transaction: TxParams = None
    arguments: Tuple[Any, ...] = None
    args: Any = None
    kwargs: Any = None

    def __init__(self, abi: Optional[ABIFunction] = None) -> None:
        self.abi = abi
        self.fn_name = type(self).__name__

    def _set_function_info(self) -> None:
        if not self.abi:
            self.abi = find_matching_fn_abi(
                self.contract_abi,
                self.w3.codec,
                self.function_identifier,
                self.args,
                self.kwargs,
            )
        if self.function_identifier in [FallbackFn, ReceiveFn]:
            self.selector = encode_hex(b"")
        elif is_text(self.function_identifier):
            # https://github.com/python/mypy/issues/4976
            self.selector = encode_hex(
                function_abi_to_4byte_selector(self.abi)  # type: ignore
            )
        else:
            raise TypeError("Unsupported function identifier")

        self.arguments = merge_args_and_kwargs(self.abi, self.args, self.kwargs)

    def _get_call_txparams(self, transaction: Optional[TxParams] = None) -> TxParams:

        if transaction is None:
            call_transaction: TxParams = {}
        else:
            call_transaction = cast(TxParams, dict(**transaction))

        if "data" in call_transaction:
            raise ValueError("Cannot set 'data' field in call transaction")

        if self.address:
            call_transaction.setdefault("to", self.address)
        if self.w3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            call_transaction.setdefault(
                "from", self.w3.eth.default_account  # type: ignore
            )

        if "to" not in call_transaction:
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

        return call_transaction

    def _transact(self, transaction: Optional[TxParams] = None) -> TxParams:
        if transaction is None:
            transact_transaction: TxParams = {}
        else:
            transact_transaction = cast(TxParams, dict(**transaction))

        if "data" in transact_transaction:
            raise ValueError("Cannot set 'data' field in transact transaction")

        if self.address is not None:
            transact_transaction.setdefault("to", self.address)
        if self.w3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            transact_transaction.setdefault(
                "from", self.w3.eth.default_account  # type: ignore
            )

        if "to" not in transact_transaction:
            if isinstance(self, type):
                raise ValueError(
                    "When using `Contract.transact` from a contract factory you "
                    "must provide a `to` address with the transaction"
                )
            else:
                raise ValueError(
                    "Please ensure that this contract instance has an address."
                )
        return transact_transaction

    def _estimate_gas(self, transaction: Optional[TxParams] = None) -> TxParams:
        if transaction is None:
            estimate_gas_transaction: TxParams = {}
        else:
            estimate_gas_transaction = cast(TxParams, dict(**transaction))

        if "data" in estimate_gas_transaction:
            raise ValueError("Cannot set 'data' field in estimate_gas transaction")
        if "to" in estimate_gas_transaction:
            raise ValueError("Cannot set to in estimate_gas transaction")

        if self.address:
            estimate_gas_transaction.setdefault("to", self.address)
        if self.w3.eth.default_account is not empty:
            # type ignored b/c check prevents an empty default_account
            estimate_gas_transaction.setdefault(
                "from", self.w3.eth.default_account  # type: ignore
            )

        if "to" not in estimate_gas_transaction:
            if isinstance(self, type):
                raise ValueError(
                    "When using `Contract.estimate_gas` from a contract factory "
                    "you must provide a `to` address with the transaction"
                )
            else:
                raise ValueError(
                    "Please ensure that this contract instance has an address."
                )
        return estimate_gas_transaction

    def _build_transaction(self, transaction: Optional[TxParams] = None) -> TxParams:
        if transaction is None:
            built_transaction: TxParams = {}
        else:
            built_transaction = cast(TxParams, dict(**transaction))

        if "data" in built_transaction:
            raise ValueError("Cannot set 'data' field in build transaction")

        if not self.address and "to" not in built_transaction:
            raise ValueError(
                "When using `ContractFunction.build_transaction` from a contract "
                "factory you must provide a `to` address with the transaction"
            )
        if self.address and "to" in built_transaction:
            raise ValueError("Cannot set 'to' field in contract call build transaction")

        if self.address:
            built_transaction.setdefault("to", self.address)

        if "to" not in built_transaction:
            raise ValueError(
                "Please ensure that this contract instance has an address."
            )

        return built_transaction

    @combomethod
    def _encode_transaction_data(cls) -> HexStr:
        return add_0x_prefix(encode_abi(cls.w3, cls.abi, cls.arguments, cls.selector))

    _return_data_normalizers: Optional[Tuple[Callable[..., Any], ...]] = tuple()

    def __repr__(self) -> str:
        if self.abi:
            _repr = f"<Function {abi_to_signature(self.abi)}"
            if self.arguments is not None:
                _repr += f" bound to {self.arguments!r}"
            return _repr + ">"
        return f"<Function {self.fn_name}>"

    @classmethod
    def factory(
        cls, class_name: str, **kwargs: Any
    ) -> Union["AsyncContractFunction", "ContractFunction"]:
        return PropertyCheckingFactory(class_name, (cls,), kwargs)(kwargs.get("abi"))


class ContractFunction(BaseContractFunction):
    def __call__(self, *args: Any, **kwargs: Any) -> "ContractFunction":
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

    def call(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: Optional[CallOverride] = None,
        ccip_read_enabled: Optional[bool] = None,
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
        call_transaction = self._get_call_txparams(transaction)

        block_id = parse_block_identifier(self.w3, block_identifier)

        return call_contract_function(
            self.w3,
            self.address,
            self._return_data_normalizers,
            self.function_identifier,
            call_transaction,
            block_id,
            self.contract_abi,
            self.abi,
            state_override,
            ccip_read_enabled,
            *self.args,
            **self.kwargs,
        )

    def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        setup_transaction = self._transact(transaction)
        return transact_with_contract_function(
            self.address,
            self.w3,
            self.function_identifier,
            setup_transaction,
            self.contract_abi,
            self.abi,
            *self.args,
            **self.kwargs,
        )

    def estimate_gas(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> int:
        setup_transaction = self._estimate_gas(transaction)
        return estimate_gas_for_function(
            self.address,
            self.w3,
            self.function_identifier,
            setup_transaction,
            self.contract_abi,
            self.abi,
            block_identifier,
            *self.args,
            **self.kwargs,
        )

    def build_transaction(self, transaction: Optional[TxParams] = None) -> TxParams:

        built_transaction = self._build_transaction(transaction)
        return build_transaction_for_function(
            self.address,
            self.w3,
            self.function_identifier,
            built_transaction,
            self.contract_abi,
            self.abi,
            *self.args,
            **self.kwargs,
        )


class AsyncContractFunction(BaseContractFunction):
    def __call__(self, *args: Any, **kwargs: Any) -> "AsyncContractFunction":
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

    async def call(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: Optional[CallOverride] = None,
        ccip_read_enabled: Optional[bool] = None,
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
        call_transaction = self._get_call_txparams(transaction)

        block_id = await async_parse_block_identifier(self.w3, block_identifier)

        return await async_call_contract_function(
            self.w3,
            self.address,
            self._return_data_normalizers,
            self.function_identifier,
            call_transaction,
            # BlockIdentifier does have an Awaitable type in types.py
            block_id,  # type: ignore
            self.contract_abi,
            self.abi,
            state_override,
            ccip_read_enabled,
            *self.args,
            **self.kwargs,
        )

    async def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        setup_transaction = self._transact(transaction)
        return await async_transact_with_contract_function(
            self.address,
            self.w3,
            self.function_identifier,
            setup_transaction,
            self.contract_abi,
            self.abi,
            *self.args,
            **self.kwargs,
        )

    async def estimate_gas(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> int:
        setup_transaction = self._estimate_gas(transaction)
        return await async_estimate_gas_for_function(
            self.address,
            self.w3,
            self.function_identifier,
            setup_transaction,
            self.contract_abi,
            self.abi,
            block_identifier,
            *self.args,
            **self.kwargs,
        )

    async def build_transaction(
        self, transaction: Optional[TxParams] = None
    ) -> TxParams:

        built_transaction = self._build_transaction(transaction)
        return await async_build_transaction_for_function(
            self.address,
            self.w3,
            self.function_identifier,
            built_transaction,
            self.contract_abi,
            self.abi,
            *self.args,
            **self.kwargs,
        )


class BaseContractEvent:
    """Base class for contract events

    An event accessed via the api contract.events.myEvents(*args, **kwargs)
    is a subclass of this class.
    """

    address: ChecksumAddress = None
    event_name: str = None
    w3: "Web3" = None
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
        return find_matching_event_abi(cls.contract_abi, event_name=cls.event_name)

    @combomethod
    def process_receipt(
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
            raise AttributeError(
                f"Error flag must be one of: {EventLogErrorFlags.flag_options()}"
            )

        for log in txn_receipt["logs"]:
            try:
                rich_log = get_event_data(self.w3.codec, self.abi, log)
            except (MismatchedABI, LogTopicError, InvalidEventABI, TypeError) as e:
                if errors == DISCARD:
                    continue
                elif errors == IGNORE:
                    # type ignores b/c rich_log set on 1092 conflicts with mutated types
                    new_log = MutableAttributeDict(log)  # type: ignore
                    new_log["errors"] = e
                    rich_log = AttributeDict(new_log)  # type: ignore
                elif errors == STRICT:
                    raise e
                else:
                    warnings.warn(
                        f"The log with transaction hash: {log['transactionHash']!r} "
                        f"and logIndex: {log['logIndex']} encountered the following "
                        f"error during processing: {type(e).__name__}({e}). It has "
                        "been discarded."
                    )
                    continue
            yield rich_log

    @combomethod
    def process_log(self, log: HexStr) -> EventData:
        return get_event_data(self.w3.codec, self.abi, log)

    @combomethod
    def _get_event_filter_params(
        self,
        abi: ABIEvent,
        argument_filters: Optional[Dict[str, Any]] = None,
        fromBlock: Optional[BlockIdentifier] = None,
        toBlock: Optional[BlockIdentifier] = None,
        blockHash: Optional[HexBytes] = None,
    ) -> FilterParams:

        if not self.address:
            raise TypeError(
                "This method can be only called on "
                "an instantiated contract with an address"
            )

        if argument_filters is None:
            argument_filters = dict()

        _filters = dict(**argument_filters)

        blkhash_set = blockHash is not None
        blknum_set = fromBlock is not None or toBlock is not None
        if blkhash_set and blknum_set:
            raise ValidationError(
                "blockHash cannot be set at the same time as fromBlock or toBlock"
            )

        # Construct JSON-RPC raw filter presentation based on human readable
        # Python descriptions. Namely, convert event names to their keccak signatures
        data_filter_set, event_filter_params = construct_event_filter_params(
            abi,
            self.w3.codec,
            contract_address=self.address,
            argument_filters=_filters,
            fromBlock=fromBlock,
            toBlock=toBlock,
            address=self.address,
        )

        if blockHash is not None:
            event_filter_params["blockHash"] = blockHash

        return event_filter_params

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> PropertyCheckingFactory:
        return PropertyCheckingFactory(class_name, (cls,), kwargs)

    @combomethod
    def _set_up_filter_builder(
        self,
        argument_filters: Optional[Dict[str, Any]] = None,
        fromBlock: Optional[BlockIdentifier] = None,
        toBlock: BlockIdentifier = "latest",
        address: Optional[ChecksumAddress] = None,
        topics: Optional[Sequence[Any]] = None,
        filter_builder: Union[EventFilterBuilder, AsyncEventFilterBuilder] = None,
    ) -> None:
        if fromBlock is None:
            raise TypeError(
                "Missing mandatory keyword argument to create_filter: fromBlock"
            )

        if argument_filters is None:
            argument_filters = dict()

        _filters = dict(**argument_filters)

        event_abi = self._get_event_abi()

        check_for_forbidden_api_filter_arguments(event_abi, _filters)

        _, event_filter_params = construct_event_filter_params(
            self._get_event_abi(),
            self.w3.codec,
            contract_address=self.address,
            argument_filters=_filters,
            fromBlock=fromBlock,
            toBlock=toBlock,
            address=address,
            topics=topics,
        )

        filter_builder.address = cast(
            ChecksumAddress, event_filter_params.get("address")
        )
        filter_builder.fromBlock = event_filter_params.get("fromBlock")
        filter_builder.toBlock = event_filter_params.get("toBlock")
        match_any_vals = {
            arg: value
            for arg, value in _filters.items()
            if not is_array_type(filter_builder.args[arg].arg_type)
            and is_list_like(value)
        }
        for arg, value in match_any_vals.items():
            filter_builder.args[arg].match_any(*value)

        match_single_vals = {
            arg: value
            for arg, value in _filters.items()
            if not is_array_type(filter_builder.args[arg].arg_type)
            and not is_list_like(value)
        }
        for arg, value in match_single_vals.items():
            filter_builder.args[arg].match_single(value)


class ContractEvent(BaseContractEvent):
    @combomethod
    def get_logs(
        self,
        argument_filters: Optional[Dict[str, Any]] = None,
        from_block: Optional[BlockIdentifier] = None,
        to_block: Optional[BlockIdentifier] = None,
        block_hash: Optional[HexBytes] = None,
    ) -> Iterable[EventData]:
        """Get events for this contract instance using eth_getLogs API.

        This is a stateless method, as opposed to create_filter.
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

            events = mycontract.events.Transfer.get_logs(from_block=from, to_block=to)

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
        :param from_block: block number or "latest", defaults to "latest"
        :param to_block: block number or "latest". Defaults to "latest"
        :param block_hash: block hash. block_hash cannot be set at the
          same time as from_block or to_block
        :yield: Tuple of :class:`AttributeDict` instances
        """
        abi = self._get_event_abi()
        # Call JSON-RPC API
        logs = self.w3.eth.get_logs(
            self._get_event_filter_params(
                abi, argument_filters, from_block, to_block, block_hash
            )
        )

        # Convert raw binary data to Python proxy objects as described by ABI
        return tuple(get_event_data(self.w3.codec, abi, entry) for entry in logs)

    @combomethod
    def create_filter(
        self,
        *,  # PEP 3102
        argument_filters: Optional[Dict[str, Any]] = None,
        fromBlock: Optional[BlockIdentifier] = None,
        toBlock: BlockIdentifier = "latest",
        address: Optional[ChecksumAddress] = None,
        topics: Optional[Sequence[Any]] = None,
    ) -> LogFilter:
        """
        Create filter object that tracks logs emitted by this contract event.
        """
        filter_builder = EventFilterBuilder(self._get_event_abi(), self.w3.codec)
        self._set_up_filter_builder(
            argument_filters,
            fromBlock,
            toBlock,
            address,
            topics,
            filter_builder,
        )
        log_filter = filter_builder.deploy(self.w3)
        log_filter.log_entry_formatter = get_event_data(
            self.w3.codec, self._get_event_abi()
        )
        log_filter.builder = filter_builder

        return log_filter

    @combomethod
    def build_filter(self) -> EventFilterBuilder:
        builder = EventFilterBuilder(
            self._get_event_abi(),
            self.w3.codec,
            formatter=get_event_data(self.w3.codec, self._get_event_abi()),
        )
        builder.address = self.address
        return builder


class AsyncContractEvent(BaseContractEvent):
    @combomethod
    async def get_logs(
        self,
        argument_filters: Optional[Dict[str, Any]] = None,
        from_block: Optional[BlockIdentifier] = None,
        to_block: Optional[BlockIdentifier] = None,
        block_hash: Optional[HexBytes] = None,
    ) -> Awaitable[Iterable[EventData]]:
        """Get events for this contract instance using eth_getLogs API.

        This is a stateless method, as opposed to create_filter.
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

            events = mycontract.events.Transfer.get_logs(from_block=from, to_block=to)

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
        :param from_block: block number or "latest", defaults to "latest"
        :param to_block: block number or "latest". Defaults to "latest"
        :param block_hash: block hash. block_hash cannot be set at the
          same time as from_block or to_block
        :yield: Tuple of :class:`AttributeDict` instances
        """
        abi = self._get_event_abi()
        # Call JSON-RPC API
        logs = await self.w3.eth.get_logs(
            self._get_event_filter_params(
                abi, argument_filters, from_block, to_block, block_hash  # type: ignore
            )
        )

        # Convert raw binary data to Python proxy objects as described by ABI
        return tuple(
            get_event_data(self.w3.codec, abi, entry) for entry in logs  # type: ignore
        )

    @combomethod
    async def create_filter(
        self,
        *,  # PEP 3102
        argument_filters: Optional[Dict[str, Any]] = None,
        fromBlock: Optional[BlockIdentifier] = None,
        toBlock: BlockIdentifier = "latest",
        address: Optional[ChecksumAddress] = None,
        topics: Optional[Sequence[Any]] = None,
    ) -> AsyncLogFilter:
        """
        Create filter object that tracks logs emitted by this contract event.
        """
        filter_builder = AsyncEventFilterBuilder(self._get_event_abi(), self.w3.codec)
        self._set_up_filter_builder(
            argument_filters,
            fromBlock,
            toBlock,
            address,
            topics,
            filter_builder,
        )
        log_filter = await filter_builder.deploy(self.w3)
        log_filter.log_entry_formatter = get_event_data(
            self.w3.codec, self._get_event_abi()
        )
        log_filter.builder = filter_builder

        return log_filter

    @combomethod
    def build_filter(self) -> AsyncEventFilterBuilder:
        builder = AsyncEventFilterBuilder(
            self._get_event_abi(),
            self.w3.codec,
            formatter=get_event_data(self.w3.codec, self._get_event_abi()),
        )
        builder.address = self.address
        return builder


class BaseContractCaller:
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

    > contract.caller(transaction={'from': eth.accounts[1], 'gas': 100000, ...}).add(2, 3)  # noqa: E501
    """

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = "latest",
        ccip_read_enabled: Optional[bool] = None,
        contract_function_class: Optional[
            Union[Type[ContractFunction], Type[AsyncContractFunction]]
        ] = ContractFunction,  # noqa: E501
    ) -> None:
        self.w3 = w3
        self.address = address
        self.abi = abi
        self._functions = None

        if self.abi:
            if transaction is None:
                transaction = {}

            self._functions = filter_by_type("function", self.abi)
            for func in self._functions:
                fn: BaseContractFunction = contract_function_class.factory(
                    func["name"],
                    w3=self.w3,
                    contract_abi=self.abi,
                    address=self.address,
                    function_identifier=func["name"],
                )

                block_id = parse_block_identifier(self.w3, block_identifier)
                caller_method = partial(
                    self.call_function,
                    fn,
                    transaction=transaction,
                    block_identifier=block_id,
                    ccip_read_enabled=ccip_read_enabled,
                )

                setattr(self, func["name"], caller_method)

    def __getattr__(self, function_name: str) -> Any:
        if self.abi is None:
            raise NoABIFound(
                "There is no ABI found for this contract.",
            )
        elif not self._functions or len(self._functions) == 0:
            raise NoABIFunctionsFound(
                "The ABI for this contract contains no function definitions. ",
                "Are you sure you provided the correct contract ABI?",
            )
        elif function_name not in {fn["name"] for fn in self._functions}:
            functions_available = ", ".join([fn["name"] for fn in self._functions])
            raise ABIFunctionNotFound(
                f"The function '{function_name}' was not found in this contract's ABI.",
                " Here is a list of all of the function names found: ",
                f"{functions_available}. ",
                "Did you mean to call one of those functions?",
            )
        else:
            return super().__getattribute__(function_name)

    def __hasattr__(self, event_name: str) -> bool:
        try:
            return event_name in self.__dict__["_events"]
        except ABIFunctionNotFound:
            return False

    @staticmethod
    def call_function(
        fn: ContractFunction,
        *args: Any,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = "latest",
        ccip_read_enabled: Optional[bool] = None,
        **kwargs: Any,
    ) -> Any:
        if transaction is None:
            transaction = {}
        return fn(*args, **kwargs).call(
            transaction=transaction,
            block_identifier=block_identifier,
            ccip_read_enabled=ccip_read_enabled,
        )


class ContractCaller(BaseContractCaller):
    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = "latest",
        ccip_read_enabled: Optional[bool] = None,
    ) -> None:
        super().__init__(
            abi=abi,
            w3=w3,
            address=address,
            transaction=transaction,
            block_identifier=block_identifier,
            ccip_read_enabled=ccip_read_enabled,
            contract_function_class=ContractFunction,
        )

    def __call__(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: Optional[CallOverride] = None,
        ccip_read_enabled: Optional[bool] = None,
    ) -> "ContractCaller":
        if transaction is None:
            transaction = {}
        return type(self)(
            self.abi,
            self.w3,
            self.address,
            transaction=transaction,
            block_identifier=block_identifier,
            ccip_read_enabled=ccip_read_enabled,
        )


class AsyncContractCaller(BaseContractCaller):
    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = "latest",
        ccip_read_enabled: Optional[bool] = None,
    ) -> None:
        super().__init__(
            abi=abi,
            w3=w3,
            address=address,
            transaction=transaction,
            block_identifier=block_identifier,
            ccip_read_enabled=ccip_read_enabled,
            contract_function_class=AsyncContractFunction,
        )

    def __call__(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = "latest",
        ccip_read_enabled: Optional[bool] = None,
    ) -> "AsyncContractCaller":
        if transaction is None:
            transaction = {}
        return type(self)(
            self.abi,
            self.w3,
            self.address,
            transaction=transaction,
            block_identifier=block_identifier,
            ccip_read_enabled=ccip_read_enabled,
        )


def check_for_forbidden_api_filter_arguments(
    event_abi: ABIEvent, _filters: Dict[str, Any]
) -> None:
    name_indexed_inputs = {_input["name"]: _input for _input in event_abi["inputs"]}

    for filter_name, filter_value in _filters.items():
        _input = name_indexed_inputs[filter_name]
        if is_array_type(_input["type"]):
            raise TypeError(
                "create_filter no longer supports array type filter arguments. "
                "see the build_filter method for filtering array type filters."
            )
        if is_list_like(filter_value) and is_dynamic_sized_type(_input["type"]):
            raise TypeError(
                "create_filter no longer supports setting filter argument options for "
                "dynamic sized types. See the build_filter method for setting "
                "filters with the match_any method."
            )


def call_contract_function(
    w3: "Web3",
    address: ChecksumAddress,
    normalizers: Tuple[Callable[..., Any], ...],
    function_identifier: FunctionIdentifier,
    transaction: TxParams,
    block_id: Optional[BlockIdentifier] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    state_override: Optional[CallOverride] = None,
    ccip_read_enabled: Optional[bool] = None,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    Helper function for interacting with a contract function using the
    `eth_call` API.
    """
    call_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return_data = w3.eth.call(
        call_transaction,
        block_identifier=block_id,
        state_override=state_override,
        ccip_read_enabled=ccip_read_enabled,
    )

    if fn_abi is None:
        fn_abi = find_matching_fn_abi(
            contract_abi, w3.codec, function_identifier, args, kwargs
        )

    output_types = get_abi_output_types(fn_abi)

    try:
        output_data = w3.codec.decode(output_types, return_data)
    except DecodingError as e:
        # Provide a more helpful error message than the one provided by
        # eth-abi-utils
        is_missing_code_error = (
            return_data in ACCEPTABLE_EMPTY_STRINGS
            and w3.eth.get_code(address) in ACCEPTABLE_EMPTY_STRINGS
        )
        if is_missing_code_error:
            msg = (
                "Could not transact with/call contract function, is contract "
                "deployed correctly and chain synced?"
            )
        else:
            msg = (
                f"Could not decode contract function call to {function_identifier} "
                f"with return data: {str(return_data)}, output_types: {output_types}"
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


async def async_call_contract_function(
    async_w3: "Web3",
    address: ChecksumAddress,
    normalizers: Tuple[Callable[..., Any], ...],
    function_identifier: FunctionIdentifier,
    transaction: TxParams,
    block_id: Optional[BlockIdentifier] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    state_override: Optional[CallOverride] = None,
    ccip_read_enabled: Optional[bool] = None,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    Helper function for interacting with a contract function using the
    `eth_call` API.
    """
    call_transaction = prepare_transaction(
        address,
        async_w3,
        fn_identifier=function_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return_data = await async_w3.eth.call(  # type: ignore
        call_transaction,
        block_identifier=block_id,
        state_override=state_override,
        ccip_read_enabled=ccip_read_enabled,
    )

    if fn_abi is None:
        fn_abi = find_matching_fn_abi(
            contract_abi, async_w3.codec, function_identifier, args, kwargs
        )

    output_types = get_abi_output_types(fn_abi)

    try:
        output_data = async_w3.codec.decode(output_types, return_data)
    except DecodingError as e:
        # Provide a more helpful error message than the one provided by
        # eth-abi-utils
        is_missing_code_error = (
            return_data in ACCEPTABLE_EMPTY_STRINGS
            and await async_w3.eth.get_code(address) in ACCEPTABLE_EMPTY_STRINGS  # type: ignore  # noqa: E501
        )
        if is_missing_code_error:
            msg = (
                "Could not transact with/call contract function, is contract "
                "deployed correctly and chain synced?"
            )
        else:
            msg = (
                f"Could not decode contract function call to {function_identifier} "
                f"with return data: {str(return_data)}, output_types: {output_types}"
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


def parse_block_identifier(
    w3: "Web3", block_identifier: BlockIdentifier
) -> BlockIdentifier:
    if isinstance(block_identifier, int):
        return parse_block_identifier_int(w3, block_identifier)
    elif block_identifier in {"latest", "earliest", "pending", "safe", "finalized"}:
        return block_identifier
    elif isinstance(block_identifier, bytes) or is_hex_encoded_block_hash(
        block_identifier
    ):
        return w3.eth.get_block(block_identifier)["number"]
    else:
        raise BlockNumberOutofRange


async def async_parse_block_identifier(
    w3: "Web3", block_identifier: BlockIdentifier
) -> Awaitable[BlockIdentifier]:
    if isinstance(block_identifier, int):
        return await async_parse_block_identifier_int(w3, block_identifier)
    elif block_identifier in {"latest", "earliest", "pending", "safe", "finalized"}:
        return block_identifier  # type: ignore
    elif isinstance(block_identifier, bytes) or is_hex_encoded_block_hash(
        block_identifier
    ):
        requested_block = await w3.eth.get_block(block_identifier)  # type: ignore
        return requested_block["number"]
    else:
        raise BlockNumberOutofRange


def parse_block_identifier_int(w3: "Web3", block_identifier_int: int) -> BlockNumber:
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = w3.eth.get_block("latest")["number"]
        block_num = last_block + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutofRange
    return BlockNumber(block_num)


async def async_parse_block_identifier_int(
    w3: "Web3", block_identifier_int: int
) -> Awaitable[BlockNumber]:
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = await w3.eth.get_block("latest")  # type: ignore
        last_block_num = last_block.number
        block_num = last_block_num + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutofRange
    return BlockNumber(block_num)  # type: ignore


def transact_with_contract_function(
    address: ChecksumAddress,
    w3: "Web3",
    function_name: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    *args: Any,
    **kwargs: Any,
) -> HexBytes:
    """
    Helper function for interacting with a contract function by sending a
    transaction.
    """
    transact_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        transaction=transaction,
        fn_abi=fn_abi,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    txn_hash = w3.eth.send_transaction(transact_transaction)
    return txn_hash


async def async_transact_with_contract_function(
    address: ChecksumAddress,
    w3: "Web3",
    function_name: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    *args: Any,
    **kwargs: Any,
) -> HexBytes:
    """
    Helper function for interacting with a contract function by sending a
    transaction.
    """
    transact_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        transaction=transaction,
        fn_abi=fn_abi,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    txn_hash = await w3.eth.send_transaction(transact_transaction)  # type: ignore
    return txn_hash


def estimate_gas_for_function(
    address: ChecksumAddress,
    w3: "Web3",
    fn_identifier: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    block_identifier: Optional[BlockIdentifier] = None,
    *args: Any,
    **kwargs: Any,
) -> int:
    """Estimates gas cost a function call would take.

    Don't call this directly, instead use :meth:`Contract.estimate_gas`
    on your contract instance.
    """
    estimate_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=fn_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return w3.eth.estimate_gas(estimate_transaction, block_identifier)


async def async_estimate_gas_for_function(
    address: ChecksumAddress,
    w3: "Web3",
    fn_identifier: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    block_identifier: Optional[BlockIdentifier] = None,
    *args: Any,
    **kwargs: Any,
) -> int:
    """Estimates gas cost a function call would take.

    Don't call this directly, instead use :meth:`Contract.estimate_gas`
    on your contract instance.
    """
    estimate_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=fn_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return await w3.eth.estimate_gas(  # type: ignore
        estimate_transaction, block_identifier
    )


def build_transaction_for_function(
    address: ChecksumAddress,
    w3: "Web3",
    function_name: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    *args: Any,
    **kwargs: Any,
) -> TxParams:
    """Builds a dictionary with the fields required to make the given transaction

    Don't call this directly, instead use :meth:`Contract.build_transaction`
    on your contract instance.
    """
    prepared_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    prepared_transaction = fill_transaction_defaults(w3, prepared_transaction)

    return prepared_transaction


async def async_build_transaction_for_function(
    address: ChecksumAddress,
    w3: "Web3",
    function_name: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    *args: Any,
    **kwargs: Any,
) -> TxParams:
    """Builds a dictionary with the fields required to make the given transaction

    Don't call this directly, instead use :meth:`Contract.build_transaction`
    on your contract instance.
    """
    prepared_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return await async_fill_transaction_defaults(w3, prepared_transaction)


def find_functions_by_identifier(
    contract_abi: ABI,
    w3: "Web3",
    address: ChecksumAddress,
    callable_check: Callable[..., Any],
    function_type: Union[Type[ContractFunction], Type[AsyncContractFunction]],
) -> List[Union[ContractFunction, AsyncContractFunction]]:
    fns_abi = filter_by_type("function", contract_abi)
    return [
        function_type.factory(
            fn_abi["name"],
            w3=w3,
            contract_abi=contract_abi,
            address=address,
            function_identifier=fn_abi["name"],
            abi=fn_abi,
        )
        for fn_abi in fns_abi
        if callable_check(fn_abi)
    ]


def get_function_by_identifier(
    fns: Sequence[ContractFunction], identifier: str
) -> Union[ContractFunction, AsyncContractFunction]:
    if len(fns) > 1:
        raise ValueError(
            f"Found multiple functions with matching {identifier}. " f"Found: {fns!r}"
        )
    elif len(fns) == 0:
        raise ValueError(f"Could not find any function with matching {identifier}")
    return fns[0]
