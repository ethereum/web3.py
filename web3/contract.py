"""Interaction with smart contracts over Web3 connector.

"""
import functools
import warnings
import itertools

from eth_utils import (
    is_address,
    is_list_like,
    is_dict,
    function_abi_to_4byte_selector,
    encode_hex,
    add_0x_prefix,
    remove_0x_prefix,
    compose,
    force_bytes,
    coerce_return_to_text,
    force_obj_to_bytes,
    to_normalized_address,
)

from eth_abi import (
    encode_abi,
    decode_abi,
)
from eth_abi.exceptions import (
    EncodingError,
    DecodingError,
)

from web3.exceptions import (
    BadFunctionCallOutput,
)

from web3.utils.abi import (
    filter_by_type,
    filter_by_name,
    filter_by_argument_count,
    filter_by_argument_name,
    filter_by_encodability,
    get_abi_input_types,
    get_abi_output_types,
    get_constructor_abi,
    merge_args_and_kwargs,
    normalize_return_type,
    check_if_arguments_can_be_encoded,
)
from web3.utils.decorators import (
    combomethod,
)
from web3.utils.empty import (
    empty,
)
from web3.utils.events import (
    get_event_data,
)
from web3.utils.exception import (
    raise_from,
)
from web3.utils.filters import (
    construct_event_filter_params,
    PastLogFilter,
)


DEPRECATED_SIGNATURE_MESSAGE = (
    "The constructor signature for the `Contract` object has changed. "
    "Please update your code to reflect the updated function signature: "
    "'Contract(address)'.  To construct contract classes use the "
    "'Contract.factory(...)' class methog."
)


class Contract(object):
    """Base class for Contract proxy classes.

    First you need to create your Contract classes using
    :func:`construct_contract_factory` that takes compiled Solidity contract
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

    dev_doc = None
    interface = None
    metadata = None
    opcodes = None
    src_map = None
    src_map_runtime = None
    user_doc = None

    def __init__(self,
                 *args,
                 **kwargs):
        """Create a new smart contract proxy object.

        :param address: Contract address as 0x hex string
        """
        code = kwargs.pop('code', empty)
        code_runtime = kwargs.pop('code_runtime', empty)
        source = kwargs.pop('source', empty)
        abi = kwargs.pop('abi', empty)
        address = kwargs.pop('address', empty)

        if self.web3 is None:
            raise AttributeError(
                'The `Contract` class has not been initialized.  Please use the '
                '`web3.contract` interface to create your contract class.'
            )

        arg_0, arg_1, arg_2, arg_3, arg_4 = tuple(itertools.chain(
            args,
            itertools.repeat(empty, 5),
        ))[:5]

        if is_list_like(arg_0):
            if abi:
                raise TypeError("The 'abi' argument was found twice")
            abi = arg_0
        elif is_address(arg_0):
            if address:
                raise TypeError("The 'address' argument was found twice")
            address = arg_0

        if arg_1 is not empty:
            if address:
                raise TypeError("The 'address' argument was found twice")
            address = arg_1

        if arg_2 is not empty:
            if code:
                raise TypeError("The 'code' argument was found twice")
            code = arg_2

        if arg_3 is not empty:
            if code_runtime:
                raise TypeError("The 'code_runtime' argument was found twice")
            code_runtime = arg_3

        if arg_4 is not empty:
            if source:
                raise TypeError("The 'source' argument was found twice")
            source = arg_4

        if any((abi, code, code_runtime, source)):
            warnings.warn(DeprecationWarning(
                "The arguments abi, code, code_runtime, and source have been "
                "deprecated and will be removed from the Contract class "
                "constructor in future releases.  Update your code to use the "
                "Contract.factory method."
            ))

        if abi is not empty:
            validate_abi(abi)
            self.abi = abi
        if code is not empty:
            self.bytecode = code
        if code_runtime is not empty:
            self.bytecode_runtime = code_runtime
        if source is not empty:
            self._source = source

        if address is not empty:
            validate_address(address)
            self.address = to_normalized_address(address)
        else:
            warnings.warn(DeprecationWarning(
                "The address argument is now required for contract class "
                "instantiation.  Please update your code to reflect this change"
            ))

    @classmethod
    def factory(cls, web3, contract_name=None, **kwargs):
        if contract_name is None:
            contract_name = cls.__name__

        kwargs['web3'] = web3

        for key in kwargs:
            if not hasattr(cls, key):
                raise AttributeError(
                    "Property {0} not found on contract class. "
                    "`Contract.factory` only accepts keyword arguments which are "
                    "present on the contract class".format(key)
                )
        return type(contract_name, (cls,), kwargs)

    #
    # deprecated properties
    #
    _source = None

    @property
    def code(self):
        warnings.warn(DeprecationWarning(
            "The `code` property has been deprecated.  You should update your "
            "code to access this value through `contract.bytecode`.  The `code` "
            "property will be removed in future releases"
        ))
        if self.bytecode is not None:
            return self.bytecode
        raise AttributeError("No contract code was specified for thes contract")

    @property
    def code_runtime(self):
        warnings.warn(DeprecationWarning(
            "The `code_runtime` property has been deprecated.  You should update your "
            "code to access this value through `contract.bytecode_runtime`.  The `code_runtime` "
            "property will be removed in future releases"
        ))
        if self.bytecode_runtime is not None:
            return self.bytecode_runtime
        raise AttributeError("No contract code_runtime was specified for thes contract")

    @property
    def source(self):
        warnings.warn(DeprecationWarning(
            "The `source` property has been deprecated and will be removed in "
            "future releases"
        ))
        if self._source is not None:
            return self._source
        raise AttributeError("No contract source was specified for thes contract")

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

        :return: hexidecimal transaction hash of the deployment
                 transaction
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
    @classmethod
    @coerce_return_to_text
    def encodeABI(cls, fn_name, args=None, kwargs=None, data=None):
        """
        encodes the arguments using the Ethereum ABI for the contract function
        that matches the given name and arguments..

        :param data: defaults to function selector
        """
        fn_abi, fn_selector, fn_arguments = cls._get_function_info(
            fn_name, args, kwargs,
        )

        if data is None:
            data = fn_selector

        return cls._encode_abi(fn_abi, fn_arguments, data)

    @combomethod
    def on(self, event_name, filter_params=None, *callbacks):
        """
        register a callback to be triggered on the appropriate events.
        """
        if filter_params is None:
            filter_params = {}

        argument_filters = filter_params.pop('filter', {})
        argument_filter_names = list(argument_filters.keys())
        event_abi = self._find_matching_event_abi(
            event_name,
            argument_filter_names,
        )

        data_filter_set, event_filter_params = construct_event_filter_params(
            event_abi,
            contract_address=self.address,
            argument_filters=argument_filters,
            **filter_params
        )

        log_data_extract_fn = functools.partial(get_event_data, event_abi)

        log_filter = self.web3.eth.filter(event_filter_params)

        log_filter.set_data_filters(data_filter_set)
        log_filter.log_entry_formatter = log_data_extract_fn
        log_filter.filter_params = event_filter_params

        if callbacks:
            log_filter.watch(*callbacks)

        return log_filter

    @combomethod
    def pastEvents(self, event_name, filter_params=None, *callbacks):
        """
        register a callback to be triggered on all past events.
        """
        if filter_params is None:
            filter_params = {}

        event_filter_params = {}
        event_filter_params.update(filter_params)
        event_filter_params.setdefault('fromBlock', 'earliest')
        event_filter_params.setdefault('toBlock', self.web3.eth.blockNumber)

        log_filter = self.on(
            event_name,
            filter_params=event_filter_params,
        )

        past_log_filter = PastLogFilter(
            web3=log_filter.web3,
            filter_id=log_filter.filter_id,
            log_entry_formatter=log_filter.log_entry_formatter,
            data_filter_set=log_filter.data_filter_set,
        )
        past_log_filter.filter_params = log_filter.filter_params

        if callbacks:
            past_log_filter.watch(*callbacks)

        return past_log_filter

    @combomethod
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
                    contract,
                    function_name,
                    estimate_transaction,
                )
                return callable_fn

        return Caller()

    @combomethod
    def call(self, transaction=None):
        """
        Execute a contract function call using the `eth_call` interface.

        This method prepares a ``Caller`` object that exposes the contract
        functions and publib variables as callable Python functions.

        Reading a public ``owner`` address variable example:

        .. code-block:: python

            ContractFactory = construct_contract_factory(
                web3=web3,
                abi=wallet_contract_definition["abi"]
            )

            # Not a real contract address
            contract = contract_class("0x2f70d3d26829e412a602e83fe8eebf80255aeea5")

            # Read "owner" public variable
            addr = contract.call().owner()

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
                    contract,
                    function_name,
                    call_transaction,
                )
                return callable_fn

        return Caller()

    @combomethod
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

            >>> wallet = Wallet(address='0xdc3a9db694bcdd55ebae4a89b22ac6d12b3f0c24')
            # Deposit to the `web3.eth.coinbase` account.
            >>> wallet.transact({'value': 12345}).deposit()
            '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060'
            # Deposit to some other account using funds from `web3.eth.coinbase`.
            >>> wallet.transact({'value': 54321}).deposit(web3.eth.accounts[1])
            '0xe122ba26d25a93911e241232d3ba7c76f5a6bfe9f8038b66b198977115fb1ddf'
            # Withdraw 12345 wei.
            >>> wallet.transact().withdraw(12345)

        The new public transaction will be created.  Transaction receipt will
        be available once the transaction has been mined.

        :param transaction: Dictionary of transaction info for web3 interface.
        Variables include ``from``, ``gas``, ``value``, ``gasPrice``.

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
                    contract,
                    function_name,
                    transact_transaction,
                )
                return callable_fn

        return Transactor()

    #
    # Private Helpers
    #
    @classmethod
    def _find_matching_fn_abi(cls, fn_name=None, args=None, kwargs=None):
        filters = []

        if fn_name:
            filters.append(functools.partial(filter_by_name, fn_name))

        if args is not None or kwargs is not None:
            if args is None:
                args = tuple()
            if kwargs is None:
                kwargs = {}

            num_arguments = len(args) + len(kwargs)
            filters.extend([
                functools.partial(filter_by_argument_count, num_arguments),
                functools.partial(filter_by_encodability, args, kwargs),
            ])

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
    def _find_matching_event_abi(cls, event_name=None, argument_names=None):
        filters = [
            functools.partial(filter_by_type, 'event'),
        ]

        if event_name is not None:
            filters.append(functools.partial(filter_by_name, event_name))

        if argument_names is not None:
            filters.append(
                functools.partial(filter_by_argument_name, argument_names)
            )

        filter_fn = compose(*filters)

        event_abi_candidates = filter_fn(cls.abi)

        if len(event_abi_candidates) == 1:
            return event_abi_candidates[0]
        elif not event_abi_candidates:
            raise ValueError("No matching functions found")
        else:
            raise ValueError("Multiple functions found")

    @classmethod
    def _get_function_info(cls, fn_name, args=None, kwargs=None):
        if args is None:
            args = tuple()
        if kwargs is None:
            kwargs = {}

        fn_abi = cls._find_matching_fn_abi(fn_name, args, kwargs)
        fn_selector = encode_hex(function_abi_to_4byte_selector(fn_abi))

        fn_arguments = merge_args_and_kwargs(fn_abi, args, kwargs)

        return fn_abi, fn_selector, fn_arguments

    @combomethod
    def _prepare_transaction(cls,
                             fn_name,
                             fn_args=None,
                             fn_kwargs=None,
                             transaction=None):
        """
        Returns a dictionary of the transaction that could be used to call this
        TODO: make this a public API
        TODO: add new prepare_deploy_transaction API
        """
        if transaction is None:
            prepared_transaction = {}
        else:
            prepared_transaction = dict(**transaction)

        if 'data' in prepared_transaction:
            raise ValueError("Transaction parameter may not contain a 'data' key")

        if cls.address:
            prepared_transaction.setdefault('to', cls.address)

        prepared_transaction['data'] = cls._encode_transaction_data(
            fn_name,
            fn_args,
            fn_kwargs,
        )
        return prepared_transaction

    @classmethod
    def _encode_abi(cls, abi, arguments, data=None):
        argument_types = get_abi_input_types(abi)

        if not check_if_arguments_can_be_encoded(abi, arguments, {}):
            raise TypeError(
                "One or more arguments could not be encoded to the necessary "
                "ABI type.  Expected types are: {0}".format(
                    ', '.join(argument_types),
                )
            )

        try:
            encoded_arguments = encode_abi(
                argument_types,
                force_obj_to_bytes(arguments),
            )
        except EncodingError as e:
            raise TypeError(
                "One or more arguments could not be encoded to the necessary "
                "ABI type: {0}".format(str(e))
            )

        if data:
            return add_0x_prefix(
                force_bytes(remove_0x_prefix(data)) +
                force_bytes(remove_0x_prefix(encode_hex(encoded_arguments)))
            )
        else:
            return encode_hex(encoded_arguments)

    @classmethod
    @coerce_return_to_text
    def _encode_transaction_data(cls, fn_name, args=None, kwargs=None):
        fn_abi, fn_selector, fn_arguments = cls._get_function_info(
            fn_name, args, kwargs,
        )
        return add_0x_prefix(cls._encode_abi(fn_abi, fn_arguments, fn_selector))

    @classmethod
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
                cls._encode_abi(constructor_abi, arguments, data=cls.bytecode)
            )
        else:
            deploy_data = add_0x_prefix(cls.bytecode)

        return deploy_data


def call_contract_function(contract,
                           function_name,
                           transaction,
                           *args,
                           **kwargs):
    """
    Helper function for interacting with a contract function using the
    `eth_call` API.
    """
    call_transaction = contract._prepare_transaction(
        fn_name=function_name,
        fn_args=args,
        fn_kwargs=kwargs,
        transaction=transaction,
    )

    return_data = contract.web3.eth.call(call_transaction)

    function_abi = contract._find_matching_fn_abi(function_name, args, kwargs)

    output_types = get_abi_output_types(function_abi)

    try:
        output_data = decode_abi(output_types, return_data)
    except DecodingError as e:
        # Provide a more helpful error message than the one provided by
        # eth-abi-utils
        msg = (
            "Could not decode contract function call {} return data {} for "
            "output_types {}".format(
                function_name,
                return_data,
                output_types
            )
        )
        raise_from(BadFunctionCallOutput(msg), e)

    normalized_data = [
        normalize_return_type(data_type, data_value)
        for data_type, data_value
        in zip(output_types, output_data)
    ]

    if len(normalized_data) == 1:
        return normalized_data[0]
    else:
        return normalized_data


def transact_with_contract_function(contract=None,
                                    function_name=None,
                                    transaction=None,
                                    *args,
                                    **kwargs):
    """
    Helper function for interacting with a contract function by sending a
    transaction.
    """
    transact_transaction = contract._prepare_transaction(
        fn_name=function_name,
        fn_args=args,
        fn_kwargs=kwargs,
        transaction=transaction,
    )

    txn_hash = contract.web3.eth.sendTransaction(transact_transaction)
    return txn_hash


def estimate_gas_for_function(contract=None,
                              function_name=None,
                              transaction=None,
                              *args,
                              **kwargs):
    """Estimates gas cost a function call would take.

    Don't call this directly, instead use :meth:`Contract.estimateGas`
    on your contract instance.
    """
    estimate_transaction = contract._prepare_transaction(
        fn_name=function_name,
        fn_args=args,
        fn_kwargs=kwargs,
        transaction=transaction,
    )

    gas_estimate = contract.web3.eth.estimateGas(estimate_transaction)
    return gas_estimate


def construct_contract_factory(web3,
                               abi,
                               code=None,
                               code_runtime=None,
                               source=None,
                               contract_name='Contract',
                               base_contract_factory_class=Contract):
    """Creates a new Contract class.

    Contract lass is a Python proxy class to interact with smart contracts.

    ``abi`` and other contract definition fields are coming from
    ``solc`` compiler or ``build/contracts.json`` in the
    case of Populus framework.

    After contract has been instiated you can interact with it
    using :meth:`transact_with_contract_function` and
     :meth:`call_contract_function`.

    Example:

    .. code-block:: python

        # Assume we have a Token contract
        token_contract_data = {
            'abi': [...],
            'code': '0x...',
            'code_runtime': '0x...',
            'source': 'contract Token {.....}',
        }

        # contract_factory is a python class that can be used to interact with
        # or deploy the "Token" contract.
        token_contract_factory = construct_contract_factory(
            web3=web3,
            abi=token_contract_data["abi"],
            code=token_contract_data["code"],
            code_runtime=token_contract_data["code_runtime"],
            source=token_contract_data["source"],
                )

        # Create Contract instance to interact with a deployed smart contract.
        token_contract = token_contract_factory(
            address=address,
            abi=token_contract_data["abi"],
            code=token_contract_data["code"],
            code_runtime=token_contract_data["code_runtime"],
            source=token_contract_data["source"])


    :param web3: Web3 connection
    :param abi: As given by solc compiler
    :param code: As given by solc compiler
    :param code_runtime: As given by solc compiler
    :param source: As given by solc compiler
    :return: Contract class (not instance)
    """
    warnings.warn(DeprecationWarning(
        "This function has been deprecated.  Please use the `Contract.factory` "
        "method as this function will be removed in future releases"
    ))

    _dict = {
        'web3': web3,
        'abi': abi,
        'code': code,
        'code_runtime': code_runtime,
        'source': source,
    }
    return type(contract_name, (base_contract_factory_class,), _dict)


def validate_abi(abi):
    """
    Helper function for validating an ABI
    """
    if not is_list_like(abi):
        raise TypeError("'abi' is not a list")
    for e in abi:
        if not is_dict(e):
            raise TypeError("The elements of 'abi' are not all dictionaries")


def validate_address(address):
    """
    Helper function for validating an address
    """
    if not is_address(address):
        raise TypeError("The 'address' argument is not an address")
