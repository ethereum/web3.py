.. _contracts:

Contracts
=========

.. py:module:: web3.contract

It is worth taking your time to understand all about contracts. To get started,
check out this example:

.. _contract_example:

Contract Deployment Example
----------------------------------------------

To run this example, you will need to install a few extra features:

- The sandbox node provided by eth-tester. You can install it with ``pip install -U web3[tester]``.
- The ``solc`` solidity compiler. See `Installing the Solidity Compiler
  <http://solidity.readthedocs.io/en/latest/installing-solidity.html#binary-packages>`_

.. code-block:: python

    >>> import json

    >>> from web3 import Web3
    >>> from solc import compile_standard

    # Solidity source code
    >>> compiled_sol = compile_standard({
    ...     "language": "Solidity",
    ...     "sources": {
    ...         "Greeter.sol": {
    ...             "content": '''
    ...                 pragma solidity ^0.5.0;
    ...
    ...                 contract Greeter {
    ...                   string public greeting;
    ...
    ...                   constructor() public {
    ...                       greeting = 'Hello';
    ...                   }
    ...
    ...                   function setGreeting(string memory _greeting) public {
    ...                       greeting = _greeting;
    ...                   }
    ...
    ...                   function greet() view public returns (string memory) {
    ...                       return greeting;
    ...                   }
    ...                 }
    ...               '''
    ...         }
    ...     },
    ...     "settings":
    ...         {
    ...             "outputSelection": {
    ...                 "*": {
    ...                     "*": [
    ...                         "metadata", "evm.bytecode"
    ...                         , "evm.bytecode.sourceMap"
    ...                     ]
    ...                 }
    ...             }
    ...         }
    ... })

    # web3.py instance
    >>> w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    >>> w3.eth.defaultAccount = w3.eth.accounts[0]

    # get bytecode
    >>> bytecode = compiled_sol['contracts']['Greeter.sol']['Greeter']['evm']['bytecode']['object']

    # get abi
    >>> abi = json.loads(compiled_sol['contracts']['Greeter.sol']['Greeter']['metadata'])['output']['abi']

    >>> Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Submit the transaction that deploys the contract
    >>> tx_hash = Greeter.constructor().transact()

    # Wait for the transaction to be mined, and get the transaction receipt
    >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    >>> greeter = w3.eth.contract(
    ...     address=tx_receipt.contractAddress,
    ...     abi=abi
    ... )

    >>> greeter.functions.greet().call()
    'Hello'

    >>> tx_hash = greeter.functions.setGreeting('Nihao').transact()
    >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    >>> greeter.functions.greet().call()
    'Nihao'


Contract Factories
------------------

These factories are not intended to be initialized directly.
Instead, create contract objects using the :meth:`w3.eth.contract() <web3.eth.Eth.contract>`
method. By default, the contract factory is :class:`Contract`. See the
example in :class:`ConciseContract` for specifying an alternate factory.

.. py:class:: Contract(address)

    Contract provides a default interface for deploying and interacting with
    Ethereum smart contracts.

    The address parameter can be a hex address or an ENS name, like ``mycontract.eth``.

.. py:class:: ConciseContract(Contract())

    .. warning:: Deprecated: This method is deprecated in favor of the :class:`~ContractCaller` API
      or the verbose syntax

    This variation of :class:`Contract` is designed for more succinct read access,
    without making write access more wordy. This comes at a cost of losing
    access to features like ``deploy()`` and properties like ``address``. It is
    recommended to use the classic ``Contract`` for those use cases.
    Just to be be clear, `ConciseContract` only exposes contract functions and all
    other `Contract` class methods and properties are not available with the `ConciseContract`
    API. This includes but is not limited to ``contract.address``, ``contract.abi``, and
    ``contract.deploy()``.

    Create this type of contract by passing a :py:class:`Contract` instance to
    :class:`ConciseContract`:


    .. code-block:: python

        >>> concise = ConciseContract(myContract)


    This variation invokes all methods as a call, so if the classic contract had a method like
    ``contract.functions.owner().call()``, you could call it with ``concise.owner()`` instead.

    For access to send a transaction or estimate gas, you can add a keyword argument like so:


    .. code-block:: python

        >>> concise.withdraw(amount, transact={'from': eth.accounts[1], 'gas': 100000, ...})

        >>>  # which is equivalent to this transaction in the classic contract:

        >>> contract.functions.withdraw(amount).transact({'from': eth.accounts[1], 'gas': 100000, ...})

.. py:class:: ImplicitContract(Contract())

   .. warning:: Deprecated: This method is deprecated in favor of the verbose syntax

   This variation mirrors :py:class:`ConciseContract`, but it invokes all methods as a
   transaction rather than a call, so if the classic contract had a method like
   ``contract.functions.owner.transact()``, you could call it with ``implicit.owner()`` instead.

    Create this type of contract by passing a :py:class:`Contract` instance to
    :class:`ImplicitContract`:


    .. code-block:: python

        >>> concise = ImplicitContract(myContract)


Properties
----------

Each Contract Factory exposes the following properties.


.. py:attribute:: Contract.address

    The hexadecimal encoded 20-byte address of the contract, or an ENS name.
    May be ``None`` if not provided during factory creation.


.. py:attribute:: Contract.abi

    The contract ABI array.


.. py:attribute:: Contract.bytecode

    The contract bytecode string.  May be ``None`` if not provided during
    factory creation.


.. py:attribute:: Contract.bytecode_runtime

    The runtime part of the contract bytecode string.  May be ``None`` if not
    provided during factory creation.

.. py:attribute:: Contract.functions

    This provides access to contract functions as attributes.  For example:
    ``myContract.functions.MyMethod()``.  The exposed contract functions are classes of the
    type :py:class:`ContractFunction`.

.. py:attribute:: Contract.events

    This provides access to contract events as attributes.  For example:
    ``myContract.events.MyEvent()``.  The exposed contract events are classes of the
    type :py:class:`ContractEvent`.

Methods
-------

Each Contract Factory exposes the following methods.

.. py:classmethod:: Contract.constructor(*args, **kwargs).transact(transaction=None)

    Construct and deploy a contract by sending a new public transaction.

    If provided ``transaction`` should be a dictionary conforming to the
    ``web3.eth.sendTransaction(transaction)`` method.  This value may not
    contain the keys ``data`` or ``to``.

    If the contract takes constructor parameters they should be provided as
    positional arguments or keyword arguments.

    If any of the arguments specified in the ABI are an ``address`` type, they
    will accept ENS names.

    If a ``gas`` value is not provided, then the ``gas`` value for the
    deployment transaction will be created using the ``web3.eth.estimateGas()``
    method.

    Returns the transaction hash for the deploy transaction.

    .. code-block:: python

        >>> deploy_txn = token_contract.constructor(web3.eth.coinbase, 12345).transact()
        >>> txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
        >>> txn_receipt['contractAddress']
        '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'

.. py:classmethod:: Contract.constructor(*args, **kwargs).estimateGas(transaction=None)

    Estimate gas for constructing and deploying the contract.

    This method behaves the same as the
    :py:meth:`Contract.constructor(*args, **kwargs).transact` method,
    with transaction details being passed into the end portion of the
    function call, and function arguments being passed into the first portion.

    Returns the amount of gas consumed which can be used as a gas estimate for
    executing this transaction publicly.

    Returns the gas needed to deploy the contract.

    .. code-block:: python

        >>> token_contract.constructor(web3.eth.coinbase, 12345).estimateGas()
        12563

.. py:classmethod:: Contract.constructor(*args, **kwargs).buildTransaction(transaction=None)

    Construct the contract deploy transaction bytecode data.

    If the contract takes constructor parameters they should be provided as
    positional arguments or keyword arguments.

    If any of the ``args`` specified in the ABI are an ``address`` type, they
    will accept ENS names.

    Returns the transaction dictionary that you can pass to sendTransaction method.

    .. code-block:: python

        >>> transaction = {
        'gasPrice': w3.eth.gasPrice,
        'chainId': None
        }
        >>> contract_data = token_contract.constructor(web3.eth.coinbase, 12345).buildTransaction(transaction)
        >>> web3.eth.sendTransaction(contract_data)

.. _contract_createFilter:

.. py:classmethod:: Contract.events.<event name>.createFilter(fromBlock=block, toBlock=block, \
                    argument_filters={"arg1": "value"}, topics=[])

    Creates a new event filter, an instance of :py:class:`web3.utils.filters.LogFilter`.

    - ``fromBlock`` is a mandatory field. Defines the starting block (exclusive) filter block range. It can be either the starting block number, or 'latest' for the last mined block, or 'pending' for unmined transactions. In the case of ``fromBlock``, 'latest' and 'pending' set the 'latest' or 'pending' block as a static value for the starting filter block.
    - ``toBlock`` optional. Defaults to 'latest'. Defines the ending block (inclusive) in the filter block range.  Special values 'latest' and 'pending' set a dynamic range that always includes the 'latest' or 'pending' blocks for the filter's upper block range.
    - ``address`` optional. Defaults to the contract address. The filter matches the event logs emanating from ``address``.
    - ``argument_filters``, optional. Expects a dictionary of argument names and values. When provided event logs are filtered for the event argument values. Event arguments can be both indexed or unindexed. Indexed values with be translated to their corresponding topic arguments. Unindexed arguments will be filtered using a regular expression.
    - ``topics`` optional, accepts the standard JSON-RPC topics argument.  See the JSON-RPC documentation for `eth_newFilter <https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newfilter>`_ more information on the ``topics`` parameters.

.. _contract_build_filter:

.. py:classmethod:: Contract.events.<event name>.build_filter()

    Creates a EventFilterBuilder instance with the event abi, and the contract address if called from a deployed contract instance.  The EventFilterBuilder provides a convenient way to construct the filter parameters with value checking against the event abi. It allows for defining multiple match values or of single values through the match_any and match_single methods.

    .. code-block:: python

        filter_builder = myContract.events.myEvent.build_filter()
        filter_builder.fromBlock = "latest"
        filter_builder.args.clientID.match_any(1, 2, 3, 4)
        filter_builder.args.region.match_single("UK")
        filter_instance = filter_builder.deploy()

    The ``deploy`` method returns a :py:class:`web3.utils.filters.LogFilter` instance from the filter parameters generated by the filter builder. Defining multiple match values for array arguments can be accomplished easily with the filter builder:

    .. code-block:: python

        filter_builder = myContract.events.myEvent.build_filter()
        filter_builder.args.clientGroups.match_any((1, 3, 5,), (2, 3, 5), (1, 2, 3))

    The filter builder blocks already defined filter parameters from being changed.

    .. code-block:: python

        filter_builder = myContract.events.myEvent.build_filter()
        filter_builder.fromBlock = "latest"
        filter_builder.fromBlock = 0  # raises a ValueError


.. py:classmethod:: Contract.deploy(transaction=None, args=None)

    .. warning:: Deprecated: this method is deprecated in favor of
      :meth:`~Contract.constructor`, which provides more flexibility.

    Construct and send a transaction to deploy the contract.

    If provided ``transaction`` should be a dictionary conforming to the
    ``web3.eth.sendTransaction(transaction)`` method.  This value may not
    contain the keys ``data`` or ``to``.

    If the contract takes constructor arguments they should be provided as a
    list via the ``args`` parameter.

    If any of the ``args`` specified in the ABI are an ``address`` type, they
    will accept ENS names.

    If a ``gas`` value is not provided, then the ``gas`` value for the
    deployment transaction will be created using the ``web3.eth.estimateGas()``
    method.

    Returns the transaction hash for the deploy transaction.


.. py:classmethod:: Contract.encodeABI(fn_name, args=None, kwargs=None, data=None)

   Encodes the arguments using the Ethereum ABI for the contract function that
   matches the given `fn_name` and arguements `args`. The `data` parameter
   defaults to the function selector.

   .. code-block:: python

      >>> contract.encodeABI(fn_name="register", args=["rainbows", 10])
      "0xea87152b0000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000000000087261696e626f7773000000000000000000000000000000000000000000000000"

.. py:classmethod:: Contract.all_functions()

    Returns a list of all the functions present in a Contract where every function is
    an instance of :py:class:`ContractFunction`.

    .. code-block:: python

        >>> contract.all_functions()
        [<Function identity(uint256,bool)>, <Function identity(int256,bool)>]


.. py:classmethod:: Contract.get_function_by_signature(signature)

    Searches for a distinct function with matching signature. Returns an instance of
    :py:class:`ContractFunction` upon finding a match. Raises `ValueError` if no
    match is found.

    .. code-block:: python

        >>> contract.get_function_by_signature('identity(uint256,bool)')
        <Function identity(uint256,bool)>


.. py:classmethod:: Contract.find_functions_by_name(name)

    Searches for all function with matching name. Returns a list of matching functions
    where every function is an instance of :py:class:`ContractFunction`. Returns an empty
    list when no match is found.

    .. code-block:: python

        >>> contract.find_functions_by_name('identity')
        [<Function identity(uint256,bool)>, <Function identity(int256,bool)>]


.. py:classmethod:: Contract.get_function_by_name(name)

    Searches for a distinct function with matching name. Returns an instance of
    :py:class:`ContractFunction` upon finding a match. Raises `ValueError` if no
    match is found or if multiple matches are found.

    .. code-block:: python

        >>> contract.get_function_by_name('unique_name')
        <Function unique_name(uint256)>


.. py:classmethod:: Contract.get_function_by_selector(selector)

    Searches for a distinct function with matching selector.
    The selector can be a hexadecimal string, bytes or int.
    Returns an instance of :py:class:`ContractFunction` upon finding a match.
    Raises `ValueError` if no match is found.

    .. code-block:: python

        >>> contract.get_function_by_selector('0xac37eebb')
        <Function identity(uint256)'>
        >>> contract.get_function_by_selector(b'\xac7\xee\xbb')
        <Function identity(uint256)'>
        >>> contract.get_function_by_selector(0xac37eebb)
        <Function identity(uint256)'>


.. py:classmethod:: Contract.find_functions_by_args(*args)

    Searches for all function with matching args. Returns a list of matching functions
    where every function is an instance of :py:class:`ContractFunction`. Returns an empty
    list when no match is found.

    .. code-block:: python

        >>> contract.find_functions_by_args(1, True)
        [<Function identity(uint256,bool)>, <Function identity(int256,bool)>]


.. py:classmethod:: Contract.get_function_by_args(*args)

    Searches for a distinct function with matching args. Returns an instance of
    :py:class:`ContractFunction` upon finding a match. Raises `ValueError` if no
    match is found or if multiple matches are found.

    .. code-block:: python

        >>> contract.get_function_by_args(1)
        <Function unique_func_with_args(uint256)>


.. note::
    `Contract` methods `all_functions`, `get_function_by_signature`, `find_functions_by_name`,
    `get_function_by_name`, `get_function_by_selector`, `find_functions_by_args` and
    `get_function_by_args` can only be used when abi is provided to the contract.


.. note::
    `Web3.py` rejects the initialization of contracts that have more than one function
    with the same selector or signature.
    eg. `blockHashAddendsInexpansible(uint256)` and `blockHashAskewLimitary(uint256)` have the
    same selector value equal to `0x00000000`. A contract containing both of these functions
    will be rejected.


.. _ambiguous-contract-functions:

Invoke Ambiguous Contract Functions Example
-------------------------------------------

Below is an example of a contract that has multiple functions of the same name,
and the arguments are ambiguous.

.. code-block:: python

        >>> contract_source_code = """
        pragma solidity ^0.4.21;
        contract AmbiguousDuo {
          function identity(uint256 input, bool uselessFlag) returns (uint256) {
            return input;
          }
          function identity(int256 input, bool uselessFlag) returns (int256) {
            return input;
          }
        }
        """
        # fast forward all the steps of compiling and deploying the contract.
        >>> ambiguous_contract.functions.identity(1, True) # raises ValidationError

        >>> identity_func = ambiguous_contract.get_function_by_signature('identity(uint256,bool)')
        >>> identity_func(1, True)
        <Function identity(uint256,bool) bound to (1, True)>
        >>> identity_func(1, True).call()
        1


Contract Functions
------------------

.. py:class:: ContractFunction

The named functions exposed through the :py:attr:`Contract.functions` property are
of the ContractFunction type. This class is not to be used directly,
but instead through :py:attr:`Contract.functions`.

For example:

    .. code-block:: python

        myContract = web3.eth.contract(address=contract_address, abi=contract_abi)
        twentyone = myContract.functions.multiply7(3).call()

If you have the function name in a variable, you might prefer this alternative:

    .. code-block:: python

        func_to_call = 'multiply7'
        contract_func = myContract.functions[func_to_call]
        twentyone = contract_func(3).call()

:py:class:`ContractFunction` provides methods to interact with contract functions.
Positional and keyword arguments supplied to the contract function subclass
will be used to find the contract function by signature,
and forwarded to the contract function when applicable.

Methods
~~~~~~~~~~

.. py:method:: ContractFunction.transact(transaction)

    Execute the specified function by sending a new public transaction.

    Refer to the following invocation:

    .. code-block:: python

        myContract.functions.myMethod(*args, **kwargs).transact(transaction)

    The first portion of the function call ``myMethod(*args, **kwargs)``
    selects the appropriate contract function based on the name and provided
    argument.  Arguments can be provided as positional arguments, keyword
    arguments, or a mix of the two.

    The end portion of this function call ``transact(transaction)`` takes a
    single parameter which should be a python dictionary conforming to
    the same format as the ``web3.eth.sendTransaction(transaction)`` method.
    This dictionary may not contain the keys ``data``.

    If any of the ``args`` or ``kwargs`` specified in the ABI are an ``address`` type, they
    will accept ENS names.

    If a ``gas`` value is not provided, then the ``gas`` value for the
    method transaction will be created using the ``web3.eth.estimateGas()``
    method.

    Returns the transaction hash.

    .. code-block:: python

        >>> token_contract.functions.transfer(web3.eth.accounts[1], 12345).transact()
        "0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd"


.. py:method:: ContractFunction.call(transaction, block_identifier='latest')

    Call a contract function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

    Refer to the following invocation:

    .. code-block:: python

        myContract.functions.myMethod(*args, **kwargs).call(transaction)

    This method behaves the same as the :py:meth:`ContractFunction.transact` method,
    with transaction details being passed into the end portion of the
    function call, and function arguments being passed into the first portion.

    Returns the return value of the executed function.

    .. code-block:: python

        >>> my_contract.functions.multiply7(3).call()
        21
        >>> token_contract.functions.myBalance().call({'from': web3.eth.coinbase})
        12345  # the token balance for `web3.eth.coinbase`
        >>> token_contract.functions.myBalance().call({'from': web3.eth.accounts[1]})
        54321  # the token balance for the account `web3.eth.accounts[1]`

    You can call the method at a historical block using ``block_identifier``. Some examples:

    .. code-block:: python

        # You can call your contract method at a block number:
        >>> token_contract.functions.myBalance().call(block_identifier=10)

        # or a number of blocks back from pending,
        # in this case, the block just before the latest block:
        >>> token_contract.functions.myBalance().call(block_identifier=-2)

        # or a block hash:
        >>> token_contract.functions.myBalance().call(block_identifier='0x4ff4a38b278ab49f7739d3a4ed4e12714386a9fdf72192f2e8f7da7822f10b4d')
        >>> token_contract.functions.myBalance().call(block_identifier=b'O\xf4\xa3\x8b\'\x8a\xb4\x9fw9\xd3\xa4\xedN\x12qC\x86\xa9\xfd\xf7!\x92\xf2\xe8\xf7\xdax"\xf1\x0bM')

        # Latest is the default, so this is redundant:
        >>> token_contract.functions.myBalance().call(block_identifier='latest')

        # You can check the state after your pending transactions (if supported by your node):
        >>> token_contract.functions.myBalance().call(block_identifier='pending')

.. py:method:: ContractFunction.estimateGas(transaction)

    Call a contract function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

    Refer to the following invocation:

    .. code-block:: python

        myContract.functions.myMethod(*args, **kwargs).estimateGas(transaction)

    This method behaves the same as the :py:meth:`ContractFunction.transact` method,
    with transaction details being passed into the end portion of the
    function call, and function arguments being passed into the first portion.

    Returns the amount of gas consumed which can be used as a gas estimate for
    executing this transaction publicly.

    .. code-block:: python

        >>> my_contract.functions.multiply7(3).estimateGas()
        42650

.. py:method:: ContractFunction.buildTransaction(transaction)

    Builds a transaction dictionary based on the contract function call specified.

    Refer to the following invocation:

    .. code-block:: python

        myContract.functions.myMethod(*args, **kwargs).buildTransaction(transaction)

    This method behaves the same as the :py:meth:`Contract.transact` method,
    with transaction details being passed into the end portion of the
    function call, and function arguments being passed into the first portion.

    .. note::
        `nonce` is not returned as part of the transaction dictionary unless it is
        specified in the first portion of the function call:

        .. code-block:: python

            >>> math_contract.functions.increment(5).buildTransaction({'nonce': 10})

        You may use :meth:`~web3.eth.Eth.getTransactionCount` to get the current nonce
        for an account. Therefore a shortcut for producing a transaction dictionary with
        nonce included looks like:

        .. code-block:: python

            >>> math_contract.functions.increment(5).buildTransaction({'nonce': web3.eth.getTransactionCount('0xF5...')})

    Returns a transaction dictionary. This transaction dictionary can then be sent using
    :meth:`~web3.eth.Eth.sendTransaction`.

    Additionally, the dictionary may be used for offline transaction signing using
    :meth:`~web3.eth.account.Account.signTransaction`.

    .. code-block:: python

        >>> math_contract.functions.increment(5).buildTransaction({'gasPrice': 21000000000})
        {
            'to': '0x6Bc272FCFcf89C14cebFC57B8f1543F5137F97dE',
            'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',
            'value': 0,
            'gas': 43242,
            'gasPrice': 21000000000,
            'chainId': 1
        }

.. _fallback-function:

Fallback Function
~~~~~~~~~~~~~~~~~

    The Contract Factory also offers an API to interact with the fallback function, which supports four methods like
    normal functions:

.. py:method:: Contract.fallback.call(transaction)

    Call fallback function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

.. py:method:: Contract.fallback.estimateGas(transaction)

    Call fallback function and return the gas estimation.

.. py:method:: Contract.fallback.transact(transaction)

    Execute fallback function by sending a new public transaction.

.. py:method:: Contract.fallback.buildTransaction(transaction)

    Builds a transaction dictionary based on the contract fallback function call.

Events
------

.. py:class:: ContractEvents

The named events exposed through the :py:attr:`Contract.events` property are of the ContractEvents type. This class is not to be used directly, but instead through :py:attr:`Contract.events`.

For example:

    .. code-block:: python

        myContract = web3.eth.contract(address=contract_address, abi=contract_abi)
        tx_hash = myContract.functions.myFunction().transact()
        receipt = web3.eth.getTransactionReceipt(tx_hash)
        myContract.events.myEvent().processReceipt(receipt)

:py:class:`ContractEvent` provides methods to interact with contract events. Positional and keyword arguments supplied to the contract event subclass will be used to find the contract event by signature.

.. _processReceipt:

.. py:method:: ContractEvents.myEvent(*args, **kwargs).processReceipt(transaction_receipt, errors=WARN)

   Extracts the pertinent logs from a transaction receipt.

   If there are no errors, ``processReceipt`` returns a tuple of :ref:`Event Log Objects <event-log-object>`, emitted from the event (e.g. ``myEvent``),
   with decoded ouput.

   .. code-block:: python

       >>> tx_hash = contract.functions.myFunction(12345).transact({'to':contract_address})
       >>> tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       >>> rich_logs = contract.events.myEvent().processReceipt(tx_receipt)
       >>> rich_logs[0]['args']
       {'myArg': 12345}

   If there are errors, the logs will be handled differently depending on the flag that is passed in:

     - ``WARN`` (default) - logs a warning to the console for the log that has an error, and discards the log. Returns any logs that are able to be processed.
     - ``STRICT`` - stops all processing and raises the error encountered.
     - ``IGNORE`` - returns any raw logs that raised an error with an added "errors" field, along with any other logs were able to be processed.
     - ``DISCARD`` - silently discards any logs that have errors, and returns processed logs that don't have errors.

   An event log error flag needs to be imported from ``web3/logs.py``.

   .. code-block:: python

       >>> tx_hash = contract.functions.myFunction(12345).transact({'to':contract_address})
       >>> tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       >>> processed_logs = contract.events.myEvent().processReceipt(tx_receipt)
       >>> processed_logs
       (
          AttributeDict({
              'args': AttributeDict({}),
              'event': 'myEvent',
              'logIndex': 0,
              'transactionIndex': 0,
              'transactionHash': HexBytes('0xfb95ccb6ab39e19821fb339dee33e7afe2545527725b61c64490a5613f8d11fa'),
              'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
              'blockHash': HexBytes('0xd74c3e8bdb19337987b987aee0fa48ed43f8f2318edfc84e3a8643e009592a68'),
              'blockNumber': 3
          })
       )


       # Or, if there were errors encountered during processing:
       >>> from web3.logs import STRICT, IGNORE, DISCARD, WARN
       >>> processed_logs = contract.events.myEvent().processReceipt(tx_receipt, errors=IGNORE)
       >>> processed_logs
       (
           AttributeDict({
               'type': 'mined',
               'logIndex': 0,
               'transactionIndex': 0,
               'transactionHash': HexBytes('0x01682095d5abb0270d11a31139b9a1f410b363c84add467004e728ec831bd529'),
               'blockHash': HexBytes('0x92abf9325a3959a911a2581e9ea36cba3060d8b293b50e5738ff959feb95258a'),
               'blockNumber': 5,
               'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
               'data': '0x0000000000000000000000000000000000000000000000000000000000003039',
               'topics': [
                   HexBytes('0xf70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb15')l
               ],
               'errors': LogTopicError('Expected 1 log topics.  Got 0')})
          })
       )
       >>> processed_logs = contract.events.myEvent().processReceipt(tx_receipt, errors=DISCARD)
       >>> assert processed_logs == ()
       True

.. py:method:: ContractEvents.myEvent(*args, **kwargs).processLog(log)

   Similar to processReceipt_, but only processes one log at a time, instead of a whole transaction receipt.
   Will return a single :ref:`Event Log Object <event-log-object>` if there are no errors encountered during processing. If an error is encountered during processing, it will be raised.

   .. code-block:: python

       >>> tx_hash = contract.functions.myFunction(12345).transact({'to':contract_address})
       >>> tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       >>> log_to_process = tx_receipt['logs'][0]
       >>> processed_log = contract.events.myEvent().processLog(log_to_process)
       >>> processed_log
       AttributeDict({
           'args': AttributeDict({}),
           'event': 'myEvent',
           'logIndex': 0,
           'transactionIndex': 0,
           'transactionHash': HexBytes('0xfb95ccb6ab39e19821fb339dee33e7afe2545527725b61c64490a5613f8d11fa'),
           'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
           'blockHash': HexBytes('0xd74c3e8bdb19337987b987aee0fa48ed43f8f2318edfc84e3a8643e009592a68'),
           'blockNumber': 3
       })


.. _event-log-object:

Event Log Object
~~~~~~~~~~~~~~~~

    The Event Log Object is a python dictionary with the following keys:

    * ``args``: Dictionary - The arguments coming from the event.
    * ``event``: String - The event name.
    * ``logIndex``: Number - integer of the log index position in the block.
    * ``transactionIndex``: Number - integer of the transactions index position
      log was created from.
    * ``transactionHash``: String, 32 Bytes - hash of the transactions this log
      was created from.
    * ``address``: String, 32 Bytes - address from which this log originated.
    * ``blockHash``: String, 32 Bytes - hash of the block where this log was
      in. null when it's pending.
    * ``blockNumber``: Number - the block number where this log was in. null
      when it's pending.


    .. code-block:: python

        >>> transfer_filter = my_token_contract.eventFilter('Transfer', {'filter': {'_from': '0xDc3A9Db694BCdd55EBaE4A89B22aC6D12b3F0c24'}})
        >>> transfer_filter.get_new_entries()
        [...]  # array of Event Log Objects that match the filter.
        # wait a while...
        >>> transfer_filter.get_new_entries()
        [...]  # new events since the last call
        >>> transfer_filter.get_all_entries()
        [...]  # all events that match the filter.


Utils
-----

.. py:classmethod:: Contract.decode_function_input(data)

    Decodes the transaction data used to invoke a smart contract function, and returns
    :py:class:`ContractFunction` and decoded parameters as :py:class:`dict`.

    .. code-block:: python

        >>> transaction = w3.eth.getTransaction('0x5798fbc45e3b63832abc4984b0f3574a13545f415dd672cd8540cd71f735db56')
        >>> transaction.input
        '0x612e45a3000000000000000000000000b656b2a9c3b2416437a811e07466ca712f5a5b5a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000093a80000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000116c6f6e656c792c20736f206c6f6e656c7900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        >>> contract.decode_function_input(transaction.input)
        (<Function newProposal(address,uint256,string,bytes,uint256,bool)>,
         {'_recipient': '0xB656b2a9c3b2416437A811e07466cA712F5a5b5a',
          '_amount': 0,
          '_description': b'lonely, so lonely',
          '_transactionData': b'',
          '_debatingPeriod': 604800,
          '_newCurator': True})

ContractCaller
--------------

.. py:class:: ContractCaller

The ``ContractCaller`` class provides an API to call functions in a contract. This class
is not to be used directly, but instead through ``Contract.caller``.

There are a number of different ways to invoke the ``ContractCaller``.

For example:

.. testsetup:: contractcaller

   import json
   from web3 import Web3
   w3 = Web3(Web3.EthereumTesterProvider())
   bytecode = "0x606060405261022e806100126000396000f360606040523615610074576000357c01000000000000000000000000000000000000000000000000000000009004806316216f391461007657806361bc221a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d578063dcf537b11461014057610074565b005b610083600480505061016c565b6040518082815260200191505060405180910390f35b6100a6600480505061017f565b6040518082815260200191505060405180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b6040518082815260200191505060405180910390f35b6101566004808035906020019091905050610217565b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90565b60006000505481565b6000816000600082828250540192505081905550600060005054905080507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b60006007820290508050809050610229565b91905056"
   ABI = json.loads('[{"constant":false,"inputs":[],"name":"return13","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":true,"inputs":[],"name":"counter","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"amt","type":"uint256"}],"name":"increment","outputs":[{"name":"result","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"},{"name":"b","type":"int256"}],"name":"add","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":false,"inputs":[],"name":"increment","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"}],"name":"multiply7","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"Increased","type":"event"}]')
   contract = w3.eth.contract(abi=ABI, bytecode=bytecode)
   deploy_txn = contract.constructor().transact()
   deploy_receipt = w3.eth.waitForTransactionReceipt(deploy_txn)
   address = deploy_receipt.contractAddress

.. doctest:: contractcaller

   >>> myContract = w3.eth.contract(address=address, abi=ABI)
   >>> twentyone = myContract.caller.multiply7(3)
   >>> twentyone
   21

It can also be invoked using parentheses:

.. doctest:: contractcaller

   >>> twentyone = myContract.caller().multiply7(3)
   >>> twentyone
   21

And a transaction dictionary, with or without the ``transaction`` keyword.
You can also optionally include a block identifier. For example:

.. doctest:: contractcaller

   >>> from_address = w3.eth.accounts[1]
   >>> twentyone = myContract.caller({'from': from_address}).multiply7(3)
   >>> twentyone
   21
   >>> twentyone = myContract.caller(transaction={'from': from_address}).multiply7(3)
   >>> twentyone
   21
   >>> twentyone = myContract.caller(block_identifier='latest').multiply7(3)
   >>> twentyone
   21

Like :py:class:`ContractFunction`, :py:class:`ContractCaller`
provides methods to interact with contract functions.
Positional and keyword arguments supplied to the contract caller subclass
will be used to find the contract function by signature,
and forwarded to the contract function when applicable.
