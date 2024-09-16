from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Type,
    cast,
)

from eth_typing import (
    ABI,
    ChecksumAddress,
)
from eth_utils import (
    combomethod,
)
from eth_utils.abi import (
    abi_to_signature,
    get_abi_input_names,
    get_abi_input_types,
    get_all_function_abis,
)
from eth_utils.toolz import (
    partial,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    fallback_func_abi_exists,
    get_abi_element_signature,
    get_name_from_abi_element_identifier,
    receive_func_abi_exists,
)
from web3._utils.abi_element_identifiers import (
    FallbackFn,
    ReceiveFn,
)
from web3._utils.async_transactions import (
    async_fill_transaction_defaults,
)
from web3._utils.compat import (
    Self,
)
from web3._utils.contracts import (
    async_parse_block_identifier,
    copy_contract_event,
    copy_contract_function,
)
from web3._utils.datatypes import (
    PropertyCheckingFactory,
)
from web3._utils.events import (
    AsyncEventFilterBuilder,
    get_event_data,
)
from web3._utils.filters import (
    AsyncLogFilter,
)
from web3._utils.normalizers import (
    normalize_abi,
    normalize_address_no_ens,
    normalize_bytecode,
)
from web3.contract.base_contract import (
    BaseContract,
    BaseContractCaller,
    BaseContractConstructor,
    BaseContractEvent,
    BaseContractEvents,
    BaseContractFunction,
    BaseContractFunctions,
    NonExistentFallbackFunction,
    NonExistentReceiveFunction,
)
from web3.contract.utils import (
    async_build_transaction_for_function,
    async_call_contract_function,
    async_estimate_gas_for_function,
    async_transact_with_contract_function,
    find_functions_by_identifier,
    get_function_by_identifier,
)
from web3.exceptions import (
    ABIEventNotFound,
    ABIFunctionNotFound,
    NoABIEventsFound,
    NoABIFound,
    NoABIFunctionsFound,
    Web3AttributeError,
    Web3TypeError,
    Web3ValidationError,
    Web3ValueError,
)
from web3.types import (
    BlockIdentifier,
    EventData,
    StateOverride,
    TxParams,
)
from web3.utils.abi import (
    _get_any_abi_signature_with_name,
    get_abi_element,
)

if TYPE_CHECKING:
    from ens import AsyncENS  # noqa: F401
    from web3 import AsyncWeb3  # noqa: F401


class AsyncContractEvent(BaseContractEvent):
    # mypy types
    w3: "AsyncWeb3"

    def __call__(self, *args: Any, **kwargs: Any) -> "AsyncContractEvent":
        return copy_contract_event(self, *args, **kwargs)

    @combomethod
    async def get_logs(
        self,
        argument_filters: Optional[Dict[str, Any]] = None,
        from_block: Optional[BlockIdentifier] = None,
        to_block: Optional[BlockIdentifier] = None,
        block_hash: Optional[HexBytes] = None,
    ) -> Awaitable[Iterable[EventData]]:
        """
        Get events for this contract instance using eth_getLogs API.

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

        See also: :func:`web3.middleware.filter.LocalFilterMiddleware`.

        :param argument_filters: Filter by argument values. Indexed arguments are
          filtered by the node while non-indexed arguments are filtered by the library.
        :param from_block: block number or "latest", defaults to "latest"
        :param to_block: block number or "latest". Defaults to "latest"
        :param block_hash: block hash. Cannot be set at the
          same time as ``from_block`` or ``to_block``
        :yield: Tuple of :class:`AttributeDict` instances
        """
        # validate ``argument_filters`` if present
        if argument_filters is not None:
            event_arg_names = get_abi_input_names(self.abi)
            if not all(arg in event_arg_names for arg in argument_filters.keys()):
                raise Web3ValidationError(
                    "When filtering by argument names, all argument names must be "
                    "present in the contract's event ABI."
                )

        _filter_params = self._get_event_filter_params(
            self.abi, argument_filters, from_block, to_block, block_hash
        )
        # call JSON-RPC API
        logs = await self.w3.eth.get_logs(_filter_params)

        # convert raw binary data to Python proxy objects as described by ABI:
        all_event_logs = tuple(
            get_event_data(self.w3.codec, self.abi, entry) for entry in logs
        )
        filtered_logs = self._process_get_logs_argument_filters(
            self.abi,
            all_event_logs,
            argument_filters,
        )
        return cast(Awaitable[Iterable[EventData]], filtered_logs)

    @combomethod
    async def create_filter(
        self,
        *,  # PEP 3102
        argument_filters: Optional[Dict[str, Any]] = None,
        from_block: Optional[BlockIdentifier] = None,
        to_block: BlockIdentifier = "latest",
        address: Optional[ChecksumAddress] = None,
        topics: Optional[Sequence[Any]] = None,
    ) -> AsyncLogFilter:
        """
        Create filter object that tracks logs emitted by this contract event.
        """
        filter_builder = AsyncEventFilterBuilder(self.abi, self.w3.codec)
        self._set_up_filter_builder(
            argument_filters,
            from_block,
            to_block,
            address,
            topics,
            filter_builder,
        )
        log_filter = await filter_builder.deploy(self.w3)
        log_filter.log_entry_formatter = get_event_data(self.w3.codec, self.abi)
        log_filter.builder = filter_builder

        return log_filter

    @combomethod
    def build_filter(self) -> AsyncEventFilterBuilder:
        builder = AsyncEventFilterBuilder(
            self.abi,
            self.w3.codec,
            formatter=get_event_data(self.w3.codec, self.abi),
        )
        builder.address = self.address
        return builder


class AsyncContractEvents(BaseContractEvents):
    def __init__(
        self, abi: ABI, w3: "AsyncWeb3", address: Optional[ChecksumAddress] = None
    ) -> None:
        super().__init__(abi, w3, AsyncContractEvent, address)

    def __iter__(self) -> Iterable["AsyncContractEvent"]:
        if not hasattr(self, "_events") or not self._events:
            return

        for event in self._events:
            yield self[abi_to_signature(event)]

    def __getattr__(self, event_name: str) -> "AsyncContractEvent":
        if super().__getattribute__("abi") is None:
            raise NoABIFound(
                "There is no ABI found for this contract.",
            )
        if "_events" not in self.__dict__:
            raise NoABIEventsFound(
                "The abi for this contract contains no event definitions. ",
                "Are you sure you provided the correct contract abi?",
            )
        elif get_name_from_abi_element_identifier(event_name) not in [
            get_name_from_abi_element_identifier(event["name"])
            for event in self._events
        ]:
            raise ABIEventNotFound(
                f"The event '{event_name}' was not found in this contract's abi. ",
                "Are you sure you provided the correct contract abi?",
            )
        else:
            event_abi = get_abi_element(self._events, event_name)
            argument_types = get_abi_input_types(event_abi)
            event_signature = str(get_abi_element_signature(event_name, argument_types))
            return super().__getattribute__(event_signature)

    def __getitem__(self, event_name: str) -> "AsyncContractEvent":
        return getattr(self, event_name)


class AsyncContractFunction(BaseContractFunction):
    # mypy types
    w3: "AsyncWeb3"

    def __call__(self, *args: Any, **kwargs: Any) -> "AsyncContractFunction":
        return copy_contract_function(self, *args, **kwargs)

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> Self:
        return PropertyCheckingFactory(class_name, (cls,), kwargs)(kwargs.get("abi"))

    async def call(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = None,
        state_override: Optional[StateOverride] = None,
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
        :param block_identifier TODO
        :param state_override TODO
        :param ccip_read_enabled TODO
        :return: ``Caller`` object that has contract public functions
            and variables exposed as Python methods
        """
        call_transaction = self._get_call_txparams(transaction)

        block_id = await async_parse_block_identifier(self.w3, block_identifier)

        return await async_call_contract_function(
            self.w3,
            self.address,
            self._return_data_normalizers,
            self.abi_element_identifier,
            call_transaction,
            block_id,
            self.contract_abi,
            self.abi,
            state_override,
            ccip_read_enabled,
            self.decode_tuples,
            *self.args or (),
            **self.kwargs or {},
        )

    async def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        setup_transaction = self._transact(transaction)
        return await async_transact_with_contract_function(
            self.address,
            self.w3,
            self.abi_element_identifier,
            setup_transaction,
            self.contract_abi,
            self.abi,
            *self.args or (),
            **self.kwargs or {},
        )

    async def estimate_gas(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None,
        state_override: Optional[StateOverride] = None,
    ) -> int:
        setup_transaction = self._estimate_gas(transaction)
        return await async_estimate_gas_for_function(
            self.address,
            self.w3,
            self.abi_element_identifier,
            setup_transaction,
            self.contract_abi,
            self.abi,
            block_identifier,
            state_override,
            *self.args or (),
            **self.kwargs or {},
        )

    async def build_transaction(
        self, transaction: Optional[TxParams] = None
    ) -> TxParams:
        built_transaction = self._build_transaction(transaction)
        return await async_build_transaction_for_function(
            self.address,
            self.w3,
            self.abi_element_identifier,
            built_transaction,
            self.contract_abi,
            self.abi,
            *self.args or (),
            **self.kwargs or {},
        )

    @staticmethod
    def get_fallback_function(
        abi: ABI,
        async_w3: "AsyncWeb3",
        address: Optional[ChecksumAddress] = None,
    ) -> "AsyncContractFunction":
        if abi and fallback_func_abi_exists(abi):
            return AsyncContractFunction.factory(
                "fallback",
                w3=async_w3,
                contract_abi=abi,
                address=address,
                abi_element_identifier=FallbackFn,
            )()
        return cast(AsyncContractFunction, NonExistentFallbackFunction())

    @staticmethod
    def get_receive_function(
        abi: ABI,
        async_w3: "AsyncWeb3",
        address: Optional[ChecksumAddress] = None,
    ) -> "AsyncContractFunction":
        if abi and receive_func_abi_exists(abi):
            return AsyncContractFunction.factory(
                "receive",
                w3=async_w3,
                contract_abi=abi,
                address=address,
                abi_element_identifier=ReceiveFn,
            )()
        return cast(AsyncContractFunction, NonExistentReceiveFunction())


class AsyncContractFunctions(BaseContractFunctions):
    def __init__(
        self,
        abi: ABI,
        w3: "AsyncWeb3",
        address: Optional[ChecksumAddress] = None,
        decode_tuples: Optional[bool] = False,
    ) -> None:
        super().__init__(abi, w3, AsyncContractFunction, address, decode_tuples)

    def __iter__(self) -> Iterable["AsyncContractFunction"]:
        if not hasattr(self, "_functions") or not self._functions:
            return

        for func in self._functions:
            yield self[abi_to_signature(func)]

    def __getattribute__(self, function_name: str) -> "AsyncContractFunction":
        function_identifier = function_name

        # Function names can override object attributes
        if function_name in ["abi", "w3", "address"] and super().__getattribute__(
            "_functions"
        ):
            function_identifier = _get_any_abi_signature_with_name(
                function_name, super().__getattribute__("_functions")
            )

        return super().__getattribute__(function_identifier)

    def __getattr__(
        self, function_name: str
    ) -> Callable[[Any, Any], "AsyncContractFunction"]:
        if super().__getattribute__("abi") is None:
            raise NoABIFound(
                "There is no ABI found for this contract.",
            )
        elif "_functions" not in self.__dict__:
            raise NoABIFunctionsFound(
                "The abi for this contract contains no function definitions. ",
                "Are you sure you provided the correct contract abi?",
            )
        elif get_name_from_abi_element_identifier(function_name) not in [
            get_name_from_abi_element_identifier(function["name"])
            for function in self._functions
        ]:
            raise ABIFunctionNotFound(
                f"The function '{function_name}' was not found in this contract's "
                "abi. Are you sure you provided the correct contract abi?",
            )

        function_identifier = function_name

        if "(" not in function_name:
            function_identifier = _get_any_abi_signature_with_name(
                function_name, self._functions
            )

        return super().__getattribute__(
            function_identifier,
        )

    def __getitem__(self, function_name: str) -> "AsyncContractFunction":
        return getattr(self, function_name)


class AsyncContract(BaseContract):
    functions: AsyncContractFunctions = None
    caller: "AsyncContractCaller" = None

    # mypy types
    w3: "AsyncWeb3"

    #: Instance of :class:`ContractEvents` presenting available Event ABIs
    events: AsyncContractEvents = None

    def __init__(self, address: Optional[ChecksumAddress] = None) -> None:
        """
        Create a new smart contract proxy object.

        :param address: Contract address as 0x hex string
        """
        if self.w3 is None:
            raise Web3AttributeError(
                "The `Contract` class has not been initialized.  Please use the "
                "`web3.contract` interface to create your contract class."
            )

        if address:
            self.address = normalize_address_no_ens(address)

        if not self.address:
            raise Web3TypeError(
                "The address argument is required to instantiate a contract."
            )
        self.functions = AsyncContractFunctions(
            self.abi, self.w3, self.address, decode_tuples=self.decode_tuples
        )
        self.caller = AsyncContractCaller(
            self.abi, self.w3, self.address, decode_tuples=self.decode_tuples
        )
        self.events = AsyncContractEvents(self.abi, self.w3, self.address)
        self.fallback = AsyncContract.get_fallback_function(
            self.abi, self.w3, AsyncContractFunction, self.address
        )
        self.receive = AsyncContract.get_receive_function(
            self.abi, self.w3, AsyncContractFunction, self.address
        )

    @classmethod
    def factory(
        cls, w3: "AsyncWeb3", class_name: Optional[str] = None, **kwargs: Any
    ) -> Type[Self]:
        kwargs["w3"] = w3

        normalizers = {
            "abi": normalize_abi,
            "address": normalize_address_no_ens,
            "bytecode": normalize_bytecode,
            "bytecode_runtime": normalize_bytecode,
        }

        contract = cast(
            Type[Self],
            PropertyCheckingFactory(
                class_name or cls.__name__,
                (cls,),
                kwargs,
                normalizers=normalizers,
            ),
        )
        contract.functions = AsyncContractFunctions(
            contract.abi, contract.w3, decode_tuples=contract.decode_tuples
        )
        contract.caller = AsyncContractCaller(
            contract.abi,
            contract.w3,
            contract.address,
            decode_tuples=contract.decode_tuples,
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
            raise Web3ValueError(
                "Cannot call constructor on a contract that does not have "
                "'bytecode' associated with it"
            )

        return AsyncContractConstructor(cls.w3, cls.abi, cls.bytecode, *args, **kwargs)

    @combomethod
    def find_functions_by_identifier(
        cls,
        contract_abi: ABI,
        w3: "AsyncWeb3",
        address: ChecksumAddress,
        callable_check: Callable[..., Any],
    ) -> List["AsyncContractFunction"]:
        return cast(
            List[AsyncContractFunction],
            find_functions_by_identifier(
                contract_abi, w3, address, callable_check, AsyncContractFunction
            ),
        )

    @combomethod
    def get_function_by_identifier(
        cls, fns: Sequence["AsyncContractFunction"], identifier: str
    ) -> "AsyncContractFunction":
        return get_function_by_identifier(fns, identifier)


class AsyncContractCaller(BaseContractCaller):
    # mypy types
    w3: "AsyncWeb3"

    def __init__(
        self,
        abi: ABI,
        w3: "AsyncWeb3",
        address: ChecksumAddress,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = None,
        ccip_read_enabled: Optional[bool] = None,
        decode_tuples: Optional[bool] = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples=decode_tuples)

        if self.abi:
            if transaction is None:
                transaction = {}

            self._functions = get_all_function_abis(self.abi)

            for func in self._functions:
                abi_signature = abi_to_signature(func)
                fn = AsyncContractFunction.factory(
                    abi_signature,
                    w3=w3,
                    contract_abi=self.abi,
                    address=self.address,
                    decode_tuples=decode_tuples,
                )

                caller_method = partial(
                    self.call_function,
                    fn,
                    transaction=transaction,
                    block_identifier=block_identifier,
                    ccip_read_enabled=ccip_read_enabled,
                )

                setattr(self, abi_signature, caller_method)

    def __call__(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: BlockIdentifier = None,
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
            decode_tuples=self.decode_tuples,
        )


class AsyncContractConstructor(BaseContractConstructor):
    # mypy types
    w3: "AsyncWeb3"

    @combomethod
    async def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        return await self.w3.eth.send_transaction(self._get_transaction(transaction))

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

        return await self.w3.eth.estimate_gas(
            transaction, block_identifier=block_identifier
        )
