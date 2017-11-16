"""Interaction with smart contracts over Web3 connector.

"""
import functools
import itertools
import json

from eth_utils import (
    function_abi_to_4byte_selector,
    encode_hex,
    add_0x_prefix,
    coerce_return_to_text,
    to_checksum_address,
)

from eth_abi import (
    encode_abi,
    decode_abi,
)
from eth_abi.exceptions import (
    EncodingError,
    DecodingError,
)

from toolz.functoolz import (
    compose,
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
    map_abi_data,
    merge_args_and_kwargs,
    check_if_arguments_can_be_encoded,
)
from web3.utils.datastructures import (
    HexBytes,
)
from web3.utils.decorators import (
    combomethod,
)
from web3.utils.empty import (
    empty,
)
from web3.utils.encoding import (
    to_hex,
)
from web3.utils.ens import (
    is_ens_name,
    validate_name_has_address,
)
from web3.utils.events import (
    get_event_data,
)
from web3.utils.filters import (
    construct_event_filter_params,
)
from web3.utils.normalizers import (
    BASE_RETURN_NORMALIZERS,
    abi_address_to_hex,
    abi_bytes_to_hex,
    abi_ens_resolver,
    abi_string_to_hex,
    hexstrs_to_bytes,
)
from web3.utils.validation import (
    validate_abi,
    validate_address,
)


DEPRECATED_SIGNATURE_MESSAGE = (
    "The constructor signature for the `Contract` object has changed. "
    "Please update your code to reflect the updated function signature: "
    "'Contract(address)'.  To construct contract classes use the "
    "'Contract.factory(...)' class methog."
)

ACCEPTABLE_EMPTY_STRINGS = ["0x", b"0x", "", b""]


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
            self.address = self.normalize_property('address', address)

        if not self.address:
            raise TypeError("The address argument is required to instantiate a contract.")

    @classmethod
    def normalize_property(cls, key, val):
        if key == 'abi':
            if isinstance(val, str):
                val = json.loads(val)
            validate_abi(val)
            return val
        elif key == 'address':
            if is_ens_name(val):
                validate_name_has_address(cls.web3.ens, val)
                return val
            else:
                validate_address(val)
                return to_checksum_address(val)
        elif key in {
            'bytecode_runtime',
            'bytecode',
        }:
            return HexBytes(val)
        else:
            return val

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
            else:
                kwargs[key] = cls.normalize_property(key, kwargs[key])

        return type(contract_name, (cls,), kwargs)

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
        fn_abi, fn_selector, fn_arguments = cls._get_function_info(
            fn_name, args, kwargs,
        )

        if data is None:
            data = fn_selector

        return cls._encode_abi(fn_abi, fn_arguments, data)

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
        functions and public variables as callable Python functions.

        Reading a public ``owner`` address variable example:

        .. code-block:: python

            ContractFactory = w3.eth.contract(
                abi=wallet_contract_definition["abi"]
            )

            # Not a real contract address
            contract = ContractFactory("0x2f70d3d26829e412A602E83FE8EeBF80255AEeA5")

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

            >>> wallet = Wallet(address='0xDc3A9Db694BCdd55EBaE4A89B22aC6D12b3F0c24')
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
                    contract,
                    function_name,
                    transact_transaction,
                )
                return callable_fn

        return Transactor()

    #
    # Private Helpers
    #
    _return_data_normalizers = tuple()

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

    @combomethod
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
            normalizers = [
                abi_ens_resolver(cls.web3),
                abi_address_to_hex,
                abi_bytes_to_hex,
                abi_string_to_hex,
                hexstrs_to_bytes,
            ]
            normalized_arguments = map_abi_data(
                normalizers,
                argument_types,
                arguments,
            )
            encoded_arguments = encode_abi(
                argument_types,
                normalized_arguments,
            )
        except EncodingError as e:
            raise TypeError(
                "One or more arguments could not be encoded to the necessary "
                "ABI type: {0}".format(str(e))
            )

        if data:
            return to_hex(HexBytes(data) + encoded_arguments)
        else:
            return encode_hex(encoded_arguments)

    @combomethod
    def _encode_transaction_data(cls, fn_name, args=None, kwargs=None):
        fn_abi, fn_selector, fn_arguments = cls._get_function_info(
            fn_name, args, kwargs,
        )
        return add_0x_prefix(cls._encode_abi(fn_abi, fn_arguments, fn_selector))

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
                cls._encode_abi(constructor_abi, arguments, data=cls.bytecode)
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

    > contract.transact({'from': eth.accounts[1], 'gas': 100000, ...}).withdraw(amount)
    '''
    def __init__(self, classic_contract):
        classic_contract._return_data_normalizers += CONCISE_NORMALIZERS
        self._classic_contract = classic_contract

    @classmethod
    def factory(cls, *args, **kwargs):
        return compose(cls, Contract.factory(*args, **kwargs))

    def __getattr__(self, attr):
        return ConciseMethod(self._classic_contract, attr)

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
    ALLOWED_MODIFIERS = set(['call', 'estimateGas', 'transact'])

    def __init__(self, contract, function):
        self.__contract = contract
        self.__function = function

    def __call__(self, *args, **kwargs):
        return self.__prepared_function(**kwargs)(*args)

    def __prepared_function(self, **kwargs):
        if not kwargs:
            modifier, modifier_dict = 'call', {}
        elif len(kwargs) == 1:
            modifier, modifier_dict = kwargs.popitem()
            if modifier not in self.ALLOWED_MODIFIERS:
                raise TypeError(
                    "The only allowed keyword arguments are: %s" % self.ALLOWED_MODIFIERS)
        else:
            raise TypeError("Use up to one keyword argument, one of: %s" % self.ALLOWED_MODIFIERS)
        contract_modifier_func = getattr(self.__contract, modifier)
        return getattr(contract_modifier_func(modifier_dict), self.__function)


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
        is_missing_code_error = (
            return_data in ACCEPTABLE_EMPTY_STRINGS and
            contract.web3.eth.getCode(contract.address) in ACCEPTABLE_EMPTY_STRINGS
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

    normalizers = itertools.chain(
        BASE_RETURN_NORMALIZERS,
        contract._return_data_normalizers,
    )
    normalized_data = map_abi_data(normalizers, output_types, output_data)

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
