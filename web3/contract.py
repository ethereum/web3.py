"""Interaction with smart contracts over Web3 connector.

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
from web3.utils.functional import (
    compose,
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
    check_if_arguments_can_be_encoded,
    function_abi_to_4byte_selector,
)
from web3.utils.transactions import (
    get_block_gas_limit,
)
from web3.utils.filters import (
    construct_event_filter_params,
)


class Contract(object):
    """Base class for Contract proxy classes.

    First you need to create your Contract classes using :func:`construct_contract_class`
    that takes compiled Solidity contract ABI definitions as input.
    The created class object will be a subclass of this base class.

    After you have your Contract proxy class created you can interact with smart contracts

    * Create a Contract proxy object for an existing deployed smart contract by its address
      using :meth:`__init__`

    * Deploy a new smart contract using :py:meth:`Contract.deploy`
    """

    # set during class construction
    web3 = None

    # class properties (overridable at instance level)
    _abi = None
    _code = None
    _code_runtime = None
    _source = None

    # instance level properties
    address = None

    # extra gas to include when auto-computing transaction gas.
    gas_buffer = 100000

    def __init__(self, abi=None, address=None, code=None, code_runtime=None, source=None):
        """Create a new smart contract proxy object.

        :param address: Contract address as 0x hex string
        :param abi: Override class level definition
        :param code: Override class level definition
        :param code_runtime: Override class level definition
        :param source: Override class level definition
        """
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
        Deploys the contract on a blockchain.

        Example:

        .. code-block:: python

            from typing import Optional, Tuple

            from gevent import Timeout
            from web3 import Web3
            from web3.contract import Contract, construct_contract_class

            from populus.utils.transactions import (
                get_contract_address_from_txn,
                wait_for_transaction_receipt
            )


            def deploy_contract(
                    web3: Web3,
                    contract_definition: dict,
                    gas=1500000,
                    timeout=60.0,
                    constructor_arguments: Optional[list]=None,
                    from_account=None) -> Tuple[Contract, str]:
                '''Deploys a single contract using Web3 client.

                :param web3: Web3 client instance

                :param contract_definition: Dictionary of describing the contract interface,
                    as read from ``contracts.json`` Contains

                :param gas: Max gas

                :param timeout: How many seconds to wait the transaction to
                    confirm to get the contract address.

                :param constructor_arguments: Arguments passed to the smart contract
                    constructor. Automatically encoded through ABI signature.

                :param from_account: Geth account that's balance is used for deployment.
                    By default, the gas is spent from Web3 coinbase account.
                    Account must be unlocked.

                :return: Tuple containing Contract proxy object and the
                    transaction hash where it was deployed

                :raise gevent.timeout.Timeout: If we can't get our contract
                    in a block within given timeout
                '''

                # Check we are passed valid contract definition
                assert "abi" in contract_definition, \
                    "Please pass a valid contract definition dictionary, got {}".
                        format(contract_definition)

                contract_class = construct_contract_class(
                    web3=web3,
                    abi=contract_definition["abi"],
                    code=contract_definition["code"],
                    code_runtime=contract_definition["code_runtime"],
                    source=contract_definition["source"],
                        )

                if not from_account:
                    from_account = web3.eth.coinbase

                # Set transaction parameters
                transaction = {
                    "gas": gas,
                    "from": from_account,
                }

                # Call web3 to deploy the contract
                txn_hash = contract_class.deploy(transaction, constructor_arguments)

                # Wait until we get confirmation and address
                address = get_contract_address_from_txn(web3, txn_hash, timeout=timeout)

                # Create Contract proxy object
                contract = contract_class(address=address)

                return contract, txn_hash

        :param transaction: Transaction parameters for the deployment transaction as a dict

        :param arguments: The contract constructor arguments

        :return: 0x string formatted transaction hash of the deployment transaction
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

        if 'gas' not in transaction:
            transaction['gas'] = cls.getBufferedGasEstimate(transaction)

        # TODO: handle asynchronous contract creation
        txn_hash = cls.web3.eth.sendTransaction(transaction)
        return txn_hash

    @classmethod
    def getBufferedGasEstimate(cls, transaction):
        gas_estimate_transaction = dict(**transaction)

        gas_estimate = cls.web3.eth.estimateGas(gas_estimate_transaction)

        gas_limit = get_block_gas_limit(cls.web3)

        if gas_estimate > gas_limit:
            raise ValueError(
                "Contract does not appear to be delpoyable within the "
                "current network gas limits"
            )

        return min(gas_limit, gas_estimate + cls.gas_buffer)

    #
    # ABI Helpers
    #
    @classmethod
    def find_matching_fn_abi(cls, fn_name, arguments):
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
    def find_matching_event_abi(cls, event_name, argument_names):
        filter_fn = compose(
            functools.partial(filter_by_type, 'event'),
            functools.partial(filter_by_name, event_name),
            functools.partial(filter_by_argument_name, argument_names),
        )

        event_abi_candidates = filter_fn(cls.abi)

        if len(event_abi_candidates) == 1:
            return event_abi_candidates[0]
        elif not event_abi_candidates:
            raise ValueError("No matching functions found")
        else:
            raise ValueError("Multiple functions found")

    @classmethod
    @coerce_return_to_text
    def encodeABI(cls, fn_name, arguments, data=None):
        """
        encodes the arguments using the Ethereum ABI.
        """
        function_abi = cls.find_matching_fn_abi(fn_name, force_obj_to_bytes(arguments))
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
    @coerce_return_to_text
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

    def on(self, event_name, default_filter_params=None, *callbacks):
        """
        register a callback to be triggered on the appropriate events.
        """
        if default_filter_params is None:
            default_filter_params = {}

        argument_filters = default_filter_params.pop('filter', {})
        argument_filter_names = list(argument_filters.keys())
        event_abi = self.find_matching_event_abi(event_name, argument_filter_names)

        data_filter_set, filter_params = construct_event_filter_params(
            event_abi,
            contract_address=self.address,
            argument_filters=argument_filters,
            **default_filter_params
        )

        log_filter = self.web3.eth.filter(filter_params)
        log_filter.set_data_filters(data_filter_set)

        if callbacks:
            log_filter.watch(*callbacks)

        log_filter.filter_params = filter_params
        return log_filter

    def pastEvents(self, event_name, default_filter_params=None, *callbacks):
        """
        register a callback to be triggered on all past events.
        """
        if default_filter_params is None:
            default_filter_params = {}

        if 'fromBlock' in default_filter_params or 'toBlock' in default_filter_params:
            raise ValueError("Cannot provide `fromBlock` or `toBlock` in `pastEvents` calls")

        argument_filters = default_filter_params.pop('filter', {})
        argument_filter_names = list(argument_filters.keys())
        event_abi = self.find_matching_event_abi(event_name, argument_filter_names)

        data_filter_set, filter_params = construct_event_filter_params(
            event_abi,
            contract_address=self.address,
            argument_filters=argument_filters,
            fromBlock="earliest",
            toBlock=self.web3.eth.blockNumber,
            **default_filter_params
        )

        log_filter = self.web3.eth.filter(filter_params)
        log_filter.set_data_filters(data_filter_set)

        if callbacks:
            log_filter.watch(*callbacks)

        return log_filter

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

        This method prepares a ``Caller`` object that exposes the contract
        functions and publib variables as callable Python functions.

        Reading a public ``owner`` address variable example:

        .. code-block:: python

            contract_class = construct_contract_class(
                web3=web3,
                abi=wallet_contract_definition["abi"]

            # Not a real contract address
            contract = contract_class("0x2f70d3d26829e412a602e83fe8eebf80255aeea5")

            # Read "owner" public variable
            bin_addr = contract.call().owner()

            # Convert address to 0x format
            address = "0x" + bin_addr.decode("ascii")

        :param transaction: Dictionary of transaction info for web3 interface
        :return: ``Caller`` object that has contract public functions
            and variables exposed as Python methods
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

        You should specify the account that pays the gas for this
        transaction in `transaction`. If no account is specified the coinbase
        account of web3 interface is used.

        Example:

        .. code-block:: python

            # Assumes self.contract points to a Contract instance having withdraw() function

            def withdraw(self,
                    to_address: str,
                    amount_in_eth: Decimal,
                    from_account=None, max_gas=50000) -> str:
                '''Withdraw funds from a hosted wallet contract.

                :param amount_in_eth: How much as ETH
                :param to_address: Destination address we are withdrawing to
                :param from_account: Which Geth account pays the gas
                :return: Transaction hash as 0x string
                '''

                assert isinstance(amount_in_eth, Decimal)  # Don't let floats slip through

                wei = to_wei(amount_in_eth)

                if not from_account:
                    # Default to coinbase for transaction fees
                    from_account = self.contract.web3.eth.coinbase

                tx_info = {
                    # The Ethereum account that pays the gas for this operation
                    "from": from_account,
                    "gas": max_gas,
                }

                # Interact with underlying wrapped contract
                txid = self.contract.transact(tx_info).withdraw(to_address, wei)
                return txid

        The transaction is created in the Ethereum node memory pool.
        Transaction receipt is not available until the transaction has been mined.
        See :func:`populus.transaction.wait_for_transaction_receipt`.

        :param transaction: Dictionary of transaction info for web3 interface.
            Variables include ``from``, ``gas``.

        :return: ``Transactor`` object that has contract
            public functions exposed as Python methods.
            Calling these methods will execute a transaction against the contract.

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


@coerce_return_to_text
def call_contract_function(contract=None,
                           function_name=None,
                           transaction=None,
                           *arguments):
    """Calls a contract constant or function.

    The function must not have state changing effects.
    For those see :func:`transact_with_contract_function`

    For usual cases, you do not want to call this directly,
    but interact with your contract through :meth:`Contract.call` method.

    :param contract: :class:`web3.contract.Contract` object instance
    :param function_name: Contract function name to call
    :param transaction: Transaction parameters to pass to underlying ``web3.eth.call``
    :param *arguments: Arguments to be passed to contract function. Automatically encoded
    :return: Function call results, encoded to Python object
    """
    if not arguments:
        arguments = []

    function_abi = contract.find_matching_fn_abi(function_name, arguments)
    function_selector = function_abi_to_4byte_selector(function_abi)

    transaction['data'] = contract.encodeABI(
        function_name,
        arguments,
        data=function_selector,
    )

    return_data = contract.web3.eth.call(transaction)

    output_types = get_abi_output_types(function_abi)
    output_data = decode_abi(output_types, return_data)

    normalized_data = [
        add_0x_prefix(data_value) if data_type == 'address' else data_value
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
                                    *arguments):
    """Transacts with a contract.

    Sends in a transaction that interacts with the contract.
    You should specify the account that pays the gas for this
    transaction in `transaction`.

    Example:

    .. code-block:: python

        def withdraw(self,
                     to_address: str,
                     amount_in_eth: Decimal,
                     from_account=None,
                     max_gas=50000) -> str:
            '''Withdraw funds from a wallet contract.

            :param amount_in_eth: How much as ETH
            :param to_address: Destination address we are withdrawing to
            :param from_account: Which Geth accout pays the gas
            :return: Transaction hash
            '''

            assert isinstance(amount_in_eth, Decimal)  # Don't let floats slip through

            wei = to_wei(amount_in_eth)

            if not from_account:
                # Default to coinbase for transaction fees
                from_account = self.contract.web3.eth.coinbase

            tx_info = {
                # The Ethereum account that pays the gas for this operation
                "from": from_account,
                "gas": max_gas,
            }

            # Interact with underlying wrapped contract
            txid = transact_with_contract_function(
                self.contract, "withdraw", tx_info, to_address, wei,
            )
            return txid

    The transaction is created in the Ethereum node memory pool.
    Transaction receipt is not available until the transaction has been mined.
    See :func:`populus.utils.transactions.wait_for_transaction`.

    Usually there is no reason to call directly. Instead
    use :meth:`Contract.transact` interface.

    :param contract: :class:`web3.contract.Contract` object instance
    :param function_name: Contract function name to call
    :param transaction: Dictionary of transaction parameters to pass to
                        underlying ``web3.eth.sendTransaction``
    :param *arguments: Arguments to be passed to contract function. Automatically encoded
    :return: String, 0x formatted transaction hash.
    """

    if not arguments:
        arguments = []

    function_abi = contract.find_matching_fn_abi(function_name, arguments)
    function_selector = function_abi_to_4byte_selector(function_abi)

    transaction['data'] = contract.encodeABI(
        function_name,
        arguments,
        data=function_selector,
    )

    if 'gas' not in transaction:
        transaction['gas'] = contract.getBufferedGasEstimate(transaction)

    txn_hash = contract.web3.eth.sendTransaction(transaction)
    return txn_hash


def estimate_gas_for_function(contract=None,
                              function_name=None,
                              transaction=None,
                              *arguments):
    """Estimates gas cost a function call would take.

    Don't call this directly, instead use :meth:`Contract.estimateGas`
    on your contract instance.
    """
    if not arguments:
        arguments = []

    function_abi = contract.find_matching_fn_abi(function_name, arguments)
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

        # Assume we have a contract called Token from token.sol, as
        # previously build by Populus command line client
        contract_abis = json.load(open("build/contracts.json", "rt"))
        contract_definition = contract_abis["Token"]

        # contract_class is now Python "Token" class
        contract_class = construct_contract_class(
            web3=web3,
            abi=contract_definition["abi"],
            code=contract_definition["code"],
            code_runtime=contract_definition["code_runtime"],
            source=contract_definition["source"],
                )

        # Create Contract proxy object based on a given
        # smart contract address in block chain
        contract = contract_class(
            address=address,
            abi=contract_definition["abi"],
            code=contract_definition["code"],
            code_runtime=contract_definition["code_runtime"],
            source=contract_definition["source"])


    :param web3: Web3 connection
    :param abi: As given by solc compiler
    :param code: As given by solc compiler
    :param code_runtime: As given by solc compiler
    :param source: As given by solc compiler
    :return: Contract class (not instance)
    """
    _dict = {
        'web3': web3,
        'abi': abi,
        'code': code,
        'code_runtime': code_runtime,
        'source': source,
    }
    return type('Contract', (Contract,), _dict)
