"""Interaction with smart contracts over Web3 connector.

See https://github.com/ethereum/wiki/wiki/JavaScript-API for more details.
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
    """Base class for Contract proxy classes.

    See :func:`construct_contract_class` for creating your own Contract instances.
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
    """Calls a contract constant or function.

    The function must not have state changing effects.
    For those see :func:`transact_with_contract_function`


    Example:

    .. code-block:: python

            call_contract_function(my_token_address, "balanceOf", {})

    :param contract: :class:`web3.contract.Contract` object instance
    :param function_name: Contract function name to call
    :param transaction: Transaction parameters to pass to underlying ``web3.eth.call``
    :param *arguments: Arguments to be passed to contract function. Automatically encoded
    :return: Function call results, encoded to Python object
    """
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
    """Transacts with a contract.

    Sends in a transaction that interacts with the contract.
    You should specify the account that pays the gas for this
    transaction in `transaction`.

    Example:

    .. code-block:: python

        def withdraw(self, to_address: str, amount_in_eth: Decimal, from_account=None, max_gas=50000) -> str:
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
            txid = transact_with_contract_function(self.contract, "withdraw", tx_info, to_address, wei)
            return txid

    The transaction is created in the Ethereum node memory pool.
    Transaction receipt is not available until the transaction has been mined.
    See :func:`populus.transaction.wait_for_transaction_receipt`.

    :param contract: :class:`web3.contract.Contract` object instance
    :param function_name: Contract function name to call
    :param transaction: Dictionary of transaction parameters to pass to underlying ``web3.eth.sendTransaction``
    :param *arguments: Arguments to be passed to contract function. Automatically encoded
    :return: String, 0x formatted transaction hash.
    """


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
    return type('Contract', (_Contract,), _dict)
