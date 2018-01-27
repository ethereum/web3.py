"""Interaction with smart contracts over Web3 connector.

"""
import functools
import itertools

from eth_abi import (
    decode_abi,
)
from eth_abi.exceptions import (
    DecodingError,
)
from eth_utils import (
    add_0x_prefix,
    coerce_return_to_text,
    encode_hex,
    function_abi_to_4byte_selector,
    to_tuple,
)
from toolz.functoolz import (
    compose,
    partial,
)

from web3.exceptions import (
    BadFunctionCallOutput,
    MismatchedABI,
)
from web3.utils.abi import (
    filter_by_type,
    get_abi_output_types,
    get_constructor_abi,
    map_abi_data,
    merge_args_and_kwargs,
)
from web3.utils.contracts import (
    encode_abi,
    find_matching_event_abi,
    find_matching_fn_abi,
    get_function_info,
    prepare_transaction,
)
from web3.utils.datatypes import (
    PropertyCheckingFactory,
)
from web3.utils.decorators import (
    combomethod,
    deprecated_for,
)
from web3.utils.empty import (
    empty,
)
from web3.utils.encoding import (
    to_hex,
)
from web3.utils.events import (
    get_event_data,
)
from web3.utils.filters import (
    construct_event_filter_params,
)
from web3.utils.normalizers import (
    BASE_RETURN_NORMALIZERS,
    normalize_abi,
    normalize_address,
    normalize_bytecode,
)
from web3.utils.transactions import (
    fill_transaction_defaults,
)

DEPRECATED_SIGNATURE_MESSAGE = (
    "The constructor signature for the `Contract` object has changed. "
    "Please update your code to reflect the updated function signature: "
    "'Contract(address)'.  To construct contract classes use the "
    "'Contract.factory(...)' class method."
)

ACCEPTABLE_EMPTY_STRINGS = ["0x", b"0x", "", b""]


class ContractFunctions(object):
    """Class containing contract function objects
    """

    _function_names = []

    def __init__(self, abi, web3, address=None):
        if abi:
            self.abi = abi
            self._functions = filter_by_type('function', self.abi)
            for function in self._functions:
                self._function_names.append(function['name'])
                setattr(
                    self,
                    function['name'],
                    ContractFunction.factory(
                        function['name'],
                        web3=web3,
                        contract_abi=self.abi,
                        address=address,
                        function_name=function['name']))


class ContractEvents(object):
    """Class containing contract event objects
    """

    _event_names = []

    def __init__(self, abi, web3, address=None):
        if abi:
            self.abi = abi
            self._events = filter_by_type('event', self.abi)
            for event in self._events:
                self._event_names.append(event['name'])
                setattr(
                    self,
                    event['name'],
                    ContractEvent.factory(
                        event['name'],
                        web3=web3,
                        contract_abi=self.abi,
                        address=address,
                        event_name=event['name']))


class Contract(object):
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
        self.events = ContractEvents(self.abi, self.web3, self.address)

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
            normalizers=normalizers)
        setattr(contract, 'functions', ContractFunctions(contract.abi, contract.web3))
        setattr(contract, 'events', ContractEvents(contract.abi, contract.web3))

        return contract

    #
    # Contract Methods
    #
    @classmethod
    def deploy(cls, transaction=None, args=None, kwargs=None):
        """
        Deploys the contract on a blockchain.

        Example:

        .. code-block:: python

            >>> MyContract.deploy(
                transaction={
                    'from': web3.eth.accounts[1],
                    'value': 12345,
                },
                args=('DGD', 18),
            )
            '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060'

        :param transaction: Transaction parameters for the deployment
                            transaction as a dict

        :param args: The contract constructor arguments as positional arguments
        :param kwargs: The contract constructor arguments as keyword arguments

        :return: hexadecimal transaction hash of the deployment transaction
        """
        if transaction is None:
            deploy_transaction = {}
        else:
            deploy_transaction = dict(**transaction)

        if not cls.bytecode:
            raise ValueError(
                "Cannot deploy a contract that does not have 'bytecode' associated "
                "with it"
            )

        if 'data' in deploy_transaction:
            raise ValueError(
                "Cannot specify `data` for contract deployment"
            )

        if 'to' in deploy_transaction:
            raise ValueError(
                "Cannot specify `to` for contract deployment"
            )

        deploy_transaction['data'] = cls._encode_constructor_data(args, kwargs)

        # TODO: handle asynchronous contract creation
        txn_hash = cls.web3.eth.sendTransaction(deploy_transaction)
        return txn_hash

    #
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
            cls.abi, fn_name, args, kwargs,
        )

        if data is None:
            data = fn_selector

        return encode_abi(cls.web3, fn_abi, fn_arguments, data)

    @combomethod
    def eventFilter(self, event_name, filter_params={}):
        """
        Create filter object that tracks events emitted by this contract.
        :param event_name: the name of the event to track
        :param filter_params: other parameters to limit the events
        """
        filter_meta_params = dict(filter_params)
        argument_filters = filter_meta_params.pop('filter', {})

        argument_filter_names = list(argument_filters.keys())
        event_abi = self._find_matching_event_abi(
            event_name,
            argument_filter_names,
        )

        data_filter_set, event_filter_params = construct_event_filter_params(
            event_abi,
            contract_address=self.address,
            argument_filters=argument_filters,
            **filter_meta_params
        )

        log_data_extract_fn = functools.partial(get_event_data, event_abi)

        log_filter = self.web3.eth.filter(event_filter_params)

        log_filter.set_data_filters(data_filter_set)
        log_filter.log_entry_formatter = log_data_extract_fn
        log_filter.filter_params = event_filter_params

        return log_filter

    @combomethod
    @deprecated_for("contract.<functions/events>.<method name>.estimateGas")
    def estimateGas(self, transaction=None):
        """
        Estimate the gas for a call
        """
        if transaction is None:
            estimate_transaction = {}
        else:
            estimate_transaction = dict(**transaction)

        if 'data' in estimate_transaction:
            raise ValueError("Cannot set data in call transaction")
        if 'to' in estimate_transaction:
            raise ValueError("Cannot set to in call transaction")

        if self.address:
            estimate_transaction.setdefault('to', self.address)
        if self.web3.eth.defaultAccount is not empty:
            estimate_transaction.setdefault('from', self.web3.eth.defaultAccount)

        if 'to' not in estimate_transaction:
            if isinstance(self, type):
                raise ValueError(
                    "When using `Contract.estimateGas` from a contract factory "
                    "you must provide a `to` address with the transaction"
                )
            else:
                raise ValueError(
                    "Please ensure that this contract instance has an address."
                )

        contract = self

        class Caller(object):
            def __getattr__(self, function_name):
                callable_fn = functools.partial(
                    estimate_gas_for_function,
                    contract.abi,
                    contract.address,
                    contract.web3,
                    function_name,
                    estimate_transaction,
                )
                return callable_fn

        return Caller()

    @combomethod
    @deprecated_for("contract.<functions/events>.<method name>.call")
    def call(self, transaction=None):
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
                    "When using `Contract.call` from a contract factory you "
                    "must provide a `to` address with the transaction"
                )
            else:
                raise ValueError(
                    "Please ensure that this contract instance has an address."
                )

        contract = self

        class Caller(object):
            def __getattr__(self, function_name):
                callable_fn = functools.partial(
                    call_contract_function,
                    contract.abi,
                    contract.web3,
                    contract.address,
                    contract._return_data_normalizers,
                    function_name,
                    call_transaction,
                )
                return callable_fn

        return Caller()

    @combomethod
    @deprecated_for("contract.<functions/events>.<method name>.transact")
    def transact(self, transaction=None):
        """
        Execute a contract function call using the `eth_sendTransaction`
        interface.

        You should specify the account that pays the gas for this transaction
        in `transaction`. If no account is specified the coinbase account of
        web3 interface is used.

        Example:

        .. code-block:: python

            # Assume we have a Wallet contract with the following methods.
            # * Wallet.deposit()  # deposits to `msg.sender`
            # * Wallet.deposit(address to)  # deposits to the account indicated
            #   by the `to` parameter.
            # * Wallet.withdraw(address amount)

            >>> wallet = Wallet(address='0xDc3A9Db694BCdd55EBaE4A89B22aC6D12b3F0c24')
            # Deposit to the `web3.eth.coinbase` account.
            >>> wallet.functions.deposit().transact({'value': 12345})
            '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060'
            # Deposit to some other account using funds from `web3.eth.coinbase`.
            >>> wallet.functions.deposit(web3.eth.accounts[1]).transact({'value': 54321})
            '0xe122ba26d25a93911e241232d3ba7c76f5a6bfe9f8038b66b198977115fb1ddf'
            # Withdraw 12345 wei.
            >>> wallet.functions.withdraw(12345).transact()

        The new public transaction will be created.  Transaction receipt will
        be available once the transaction has been mined.

        :param transaction: Dictionary of transaction info for web3 interface.
        Variables include ``from``, ``gas``, ``value``, ``gasPrice``, ``nonce``.

        :return: ``Transactor`` object that has contract
            public functions exposed as Python methods.
            Calling these methods will execute a transaction against the contract.

        """
        if transaction is None:
            transact_transaction = {}
        else:
            transact_transaction = dict(**transaction)

        if 'data' in transact_transaction:
            raise ValueError("Cannot set data in call transaction")

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

        contract = self

        class Transactor(object):
            def __getattr__(self, function_name):
                callable_fn = functools.partial(
                    transact_with_contract_function,
                    contract.abi,
                    contract.address,
                    contract.web3,
                    function_name,
                    transact_transaction,
                )
                return callable_fn

        return Transactor()

    @combomethod
    @deprecated_for("contract.<functions/events>.<method name>.buildTransaction")
    def buildTransaction(self, transaction=None):
        """
        Build the transaction dictionary without sending
        """
        if transaction is None:
            built_transaction = {}
        else:
            built_transaction = dict(**transaction)

        if 'data' in built_transaction:
            raise ValueError("Cannot set data in call buildTransaction")

        if isinstance(self, type) and 'to' not in built_transaction:
            raise ValueError(
                "When using `Contract.buildTransaction` from a contract factory "
                "you must provide a `to` address with the transaction"
            )
        if not isinstance(self, type) and 'to' in built_transaction:
            raise ValueError("Cannot set to in call buildTransaction")

        if self.address:
            built_transaction.setdefault('to', self.address)

        if 'to' not in built_transaction:
            raise ValueError(
                "Please ensure that this contract instance has an address."
            )

        contract = self

        class Caller(object):
            def __getattr__(self, function_name):
                callable_fn = functools.partial(
                    build_transaction_for_function,
                    contract.abi,
                    contract.address,
                    contract.web3,
                    function_name,
                    built_transaction,
                )
                return callable_fn

        return Caller()

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

        return prepare_transaction(cls.abi,
                                   cls.address,
                                   cls.web3,
                                   fn_name=fn_name,
                                   fn_args=fn_args,
                                   fn_kwargs=fn_kwargs,
                                   transaction=transaction)

    @classmethod
    def _find_matching_fn_abi(cls, fn_name=None, args=None, kwargs=None):
        return find_matching_fn_abi(cls.abi,
                                    fn_name=fn_name,
                                    args=args,
                                    kwargs=kwargs)

    @classmethod
    def _find_matching_event_abi(cls, event_name=None, argument_names=None):
        return find_matching_event_abi(
            abi=cls.abi,
            event_name=event_name,
            argument_names=argument_names)

    @combomethod
    @coerce_return_to_text
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
            deploy_data = to_hex(cls.bytecode)

        return deploy_data


class ConciseContract(object):
    '''
    An alternative Contract Factory which invokes all methods as `call()`,
    unless you add a keyword argument. The keyword argument assigns the prep method.

    This call

    > contract.withdraw(amount, transact={'from': eth.accounts[1], 'gas': 100000, ...})

    is equivalent to this call in the classic contract:

    > contract.functions.withdraw(amount).transact({'from': eth.accounts[1], 'gas': 100000, ...})
    '''
    def __init__(self, classic_contract):
        classic_contract._return_data_normalizers += CONCISE_NORMALIZERS
        self._classic_contract = classic_contract
        self.address = self._classic_contract.address

    @classmethod
    def factory(cls, *args, **kwargs):
        return compose(cls, Contract.factory(*args, **kwargs))

    def __getattr__(self, attr):
        contract_function = getattr(self._classic_contract.functions, attr)
        return ConciseMethod(contract_function, self._classic_contract._return_data_normalizers)

    @staticmethod
    def _none_addr(datatype, data):
        if datatype == 'address' and int(data, base=16) == 0:
            return (datatype, None)
        else:
            return (datatype, data)


CONCISE_NORMALIZERS = (
    ConciseContract._none_addr,
)


class ConciseMethod:
    ALLOWED_MODIFIERS = set(['call', 'estimateGas', 'transact', 'buildTransaction'])

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


class ImplicitContract(ConciseContract):
    '''
    ImplicitContract class is similar to the ConciseContract class
    however it performs a transaction instead of a call if no modifier
    is given and the method is not marked 'constant' in the ABI.

    The transaction will use the default account to send the transaction.

    This call

    > contract.withdraw(amount)

    is equivalent to this call in the classic contract:

    > contract.functions.withdraw(amount).transact({})
    '''
    def __getattr__(self, attr):
        contract_function = getattr(self._classic_contract.functions, attr)
        return ImplicitMethod(contract_function, self._classic_contract._return_data_normalizers)


class ImplicitMethod(ConciseMethod):
    def __call_by_default(self, args):
        # If function is constant in ABI, then call by default, else transact
        function_abi = find_matching_fn_abi(self._function.contract_abi,
                                            fn_name=self._function.function_name,
                                            args=args)
        return function_abi['constant'] if 'constant' in function_abi.keys() else False

    def __call__(self, *args, **kwargs):
        # Modifier is not provided and method is not constant/pure do a transaction instead
        if not kwargs and not self.__call_by_default(args):
            return super().__call__(*args, transact={})
        else:
            return super().__call__(*args, **kwargs)


class ContractFunction(object):
    """Base class for contract functions

    A function accessed via the api contract.functions.myMethod(*args, **kwargs)
    is a subclass of this class.
    """
    address = None
    function_name = None
    web3 = None
    contract_abi = None
    abi = None
    transaction = None

    def __init__(self, *args, **kwargs):

        if args is None:
            self.args = tuple()
        else:
            self.args = args

        if kwargs is None:
            self.kwargs = {}
        else:
            self.kwargs = kwargs

        self.fn_name = type(self).__name__
        self._set_function_info()
        self._transaction_data = self._encode_transaction_data()

    def _set_function_info(self):
        self.abi = find_matching_fn_abi(self.contract_abi, self.fn_name, self.args, self.kwargs)
        self.selector = encode_hex(function_abi_to_4byte_selector(self.abi))
        self.arguments = merge_args_and_kwargs(self.abi, self.args, self.kwargs)

    def call(self, transaction=None):
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

        return call_contract_function(self.contract_abi,
                                      self.web3,
                                      self.address,
                                      self._return_data_normalizers,
                                      self.function_name,
                                      call_transaction,
                                      *self.args,
                                      **self.kwargs)

    def transact(self, transaction=None):
        if transaction is None:
            transact_transaction = {}
        else:
            transact_transaction = dict(**transaction)

        if 'data' in transact_transaction:
            raise ValueError("Cannot set data in call transaction")

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

        return transact_with_contract_function(self.contract_abi,
                                               self.address,
                                               self.web3,
                                               self.function_name,
                                               transact_transaction,
                                               *self.args,
                                               **self.kwargs)

    def estimateGas(self, transaction=None):
        if transaction is None:
            estimate_transaction = {}
        else:
            estimate_transaction = dict(**transaction)

        if 'data' in estimate_transaction:
            raise ValueError("Cannot set data in call transaction")
        if 'to' in estimate_transaction:
            raise ValueError("Cannot set to in call transaction")

        if self.address:
            estimate_transaction.setdefault('to', self.address)
        if self.web3.eth.defaultAccount is not empty:
            estimate_transaction.setdefault('from', self.web3.eth.defaultAccount)

        if 'to' not in estimate_transaction:
            if isinstance(self, type):
                raise ValueError(
                    "When using `Contract.estimateGas` from a contract factory "
                    "you must provide a `to` address with the transaction"
                )
            else:
                raise ValueError(
                    "Please ensure that this contract instance has an address."
                )

        return estimate_gas_for_function(self.contract_abi,
                                         self.address,
                                         self.web3,
                                         function_name=self.function_name,
                                         transaction=estimate_transaction,
                                         *self.args,
                                         **self.kwargs)

    def buildTransaction(self, transaction=None):
        """
        Build the transaction dictionary without sending
        """
        if transaction is None:
            built_transaction = {}
        else:
            built_transaction = dict(**transaction)

        if 'data' in built_transaction:
            raise ValueError("Cannot set data in call buildTransaction")

        if not self.address and 'to' not in built_transaction:
            raise ValueError(
                "When using `ContractFunction.buildTransaction` from a Contract factory"
                "you must provide a `to` address with the transaction"
            )
        if self.address and 'to' in built_transaction:
            raise ValueError("Cannot set to in contract call buildTransaction")

        if self.address:
            built_transaction.setdefault('to', self.address)

        if 'to' not in built_transaction:
            raise ValueError(
                "Please ensure that this contract instance has an address."
            )

        return build_transaction_for_function(self.contract_abi,
                                              self.address,
                                              self.web3,
                                              self.function_name,
                                              built_transaction,
                                              *self.args,
                                              **self.kwargs)

    @combomethod
    def _encode_transaction_data(cls):
        return add_0x_prefix(encode_abi(cls.web3, cls.abi, cls.arguments, cls.selector))

    _return_data_normalizers = tuple()

    @classmethod
    def factory(cls, class_name, **kwargs):
        return PropertyCheckingFactory(class_name, (cls,), kwargs)


class ContractEvent(object):
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

    @classmethod
    def factory(cls, class_name, **kwargs):
        return PropertyCheckingFactory(class_name, (cls,), kwargs)


def call_contract_function(abi,
                           web3,
                           address,
                           normalizers,
                           function_name,
                           transaction,
                           *args,
                           **kwargs):
    """
    Helper function for interacting with a contract function using the
    `eth_call` API.
    """
    call_transaction = prepare_transaction(
        abi,
        address,
        web3,
        fn_name=function_name,
        fn_args=args,
        fn_kwargs=kwargs,
        transaction=transaction,
    )

    return_data = web3.eth.call(call_transaction)

    function_abi = find_matching_fn_abi(abi, function_name, args, kwargs)

    output_types = get_abi_output_types(function_abi)

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
                    function_name,
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


def transact_with_contract_function(abi,
                                    address,
                                    web3,
                                    function_name=None,
                                    transaction=None,
                                    *args,
                                    **kwargs):
    """
    Helper function for interacting with a contract function by sending a
    transaction.
    """
    transact_transaction = prepare_transaction(
        abi,
        address,
        web3,
        fn_name=function_name,
        fn_args=args,
        fn_kwargs=kwargs,
        transaction=transaction,
    )

    txn_hash = web3.eth.sendTransaction(transact_transaction)
    return txn_hash


def estimate_gas_for_function(abi,
                              address,
                              web3,
                              function_name=None,
                              transaction=None,
                              *args,
                              **kwargs):
    """Estimates gas cost a function call would take.

    Don't call this directly, instead use :meth:`Contract.estimateGas`
    on your contract instance.
    """
    estimate_transaction = prepare_transaction(
        abi,
        address,
        web3,
        fn_name=function_name,
        fn_args=args,
        fn_kwargs=kwargs,
        transaction=transaction,
    )

    gas_estimate = web3.eth.estimateGas(estimate_transaction)
    return gas_estimate


def build_transaction_for_function(abi,
                                   address,
                                   web3,
                                   function_name=None,
                                   transaction=None,
                                   *args,
                                   **kwargs):
    """Builds a dictionary with the fields required to make the given transaction

    Don't call this directly, instead use :meth:`Contract.buildTransaction`
    on your contract instance.
    """
    prepared_transaction = prepare_transaction(
        abi,
        address,
        web3,
        fn_name=function_name,
        fn_args=args,
        fn_kwargs=kwargs,
        transaction=transaction,
    )

    prepared_transaction = fill_transaction_defaults(web3, prepared_transaction)

    return prepared_transaction
