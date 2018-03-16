Contracts
=========

.. py:module:: web3.contract


Contract Factories
------------------

These factories are not intended to be initialized directly.
Instead, create contract objects using the :meth:`web3.eth.Eth.contract`
method. By default, the contract factory is :class:`Contract`. See the
example in :class:`ConciseContract` for specifying an alternate factory.

.. py:class:: Contract(address)

    Contract provides a default interface for deploying and interacting with
    Ethereum smart contracts.

    The address parameter can be a hex address or an ENS name, like ``mycontract.eth``.

.. py:class:: ConciseContract(Contract())

    This variation of :class:`Contract` is designed for more succinct read access,
    without making write access more wordy. This comes at a cost of losing
    access to features like ``deploy()`` and properties like ``address``. It is
    recommended to use the classic ``Contract`` for those use cases.

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

.. py:classmethod:: Contract.deploy(transaction=None, args=None)

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

.. py:classmethod:: Contract.events.<event name>.createFilter(filter_params=None)

    Creates a new :py:class:`web3.utils.filters.LogFilter` instance.

    The ``event_name`` parameter should be the name of the contract event you
    want to filter on.

    If provided,  ``filter_params`` should be a dictionary specifying
    additional filters for log entries.  The following keys are supported.

    * ``filter``: ``dictionary`` - (optional) Dictionary keys should be
      argument names for the Event arguments. Dictionary values should be the
      value you want to filter on, or a list of values to be filtered on.
      Lists of values will match log entries whose argument matches any value
      in the list. Indexed and unindexed event arguments are accepted. The
      processing of indexed argument values into hex encoded topics is handled
      internally when using the ``filter`` parameter.
    * ``fromBlock``: ``integer/tag`` - (optional, default: "latest") Integer
      block number, or "latest" for the last mined block or "pending",
      "earliest" for not yet mined transactions.
    * ``toBlock``: ``integer/tag`` - (optional, default: "latest") Integer
      block number, or "latest" for the last mined block or "pending",
      "earliest" for not yet mined transactions.
    * ``address``: ``string`` or list of ``strings``, each 20 Bytes -
      (optional) Contract address or a list of addresses from which logs should
      originate.
    * ``topics``: list of 32 byte ``strings`` or ``null`` - (optional) Array of
      topics that should be used for filtering, with the keccak hash of the event
      signature as the first item, and the remaining items as hex encoded
      argument values. Topics are order-dependent.  This parameter can also be a
      list of topic lists in which case filtering will match any of the provided
      topic arrays. This argument is useful when relying on the internally
      generated topic lists via the ``filter`` argument is not desired. If
      ``topics`` is included with the ``filter`` argument, the ``topics`` list
      will be prepended to any topic lists inferred from the ``filter`` arguments.

    The event topic for the event specified by ``event_name`` will be added to
    the ``filter_params['topics']`` list.

    If the :py:attr:`Contract.address` attribute for this contract is
    non-null, the contract address will be added to the ``filter_params``.



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
      in. null when its pending.
    * ``blockNumber``: Number - the block number where this log was in. null
      when its pending.


    .. code-block:: python

        >>> transfer_filter = my_token_contract.events.Transfer.createFilter({'filter': {'_from': '0xdc3a9db694bcdd55ebae4a89b22ac6d12b3f0c24'}})
        >>> transfer_filter.get_new_entries()
        [...]  # array of Event Log Objects that match the filter.

        # wait a while...

        >>> transfer_filter.get_new_entries()
        [...]  # new events since the last call

        >>> transfer_filter.get_all_entries()
        [...]  # all events that match the filter.

Contract Functions
------------------

.. py:class:: ContractFunction

The named functions exposed through the :py:attr:`Contract.functions` property are of the ContractFunction type. This class it not to be used directly, but instead through :py:attr:`Contract.functions`.

For example:

    .. code-block:: python

        myContract = web3.eth.contract(address=contract_address, abi=contract_abi)
        myContract.functions.multiply7(3).call()

:py:class:`ContractFunction` provides methods to interact with contract functions. Positional and keyword arguments supplied to the contract function subclass will be used to find the contract function by signature, and forwarded to the contract function when applicable.

Methods
"""""""

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


.. py:method:: ContractFunction.call(transaction)

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

The named events exposed through the :py:attr:`Contract.events` property are of the ContractEvents type. This class it not to be used directly, but instead through :py:attr:`Contract.events`.

For example:

    .. code-block:: python

        myContract = web3.eth.contract(address=contract_address, abi=contract_abi)
        tx_hash = myContract.functions.myFunction().transact()
        receipt = web3.eth.getTransactionReceipt(tx_hash)
        myContract.events.myEvent().processReceipt(receipt)

:py:class:`ContractEvent` provides methods to interact with contract events. Positional and keyword arguments supplied to the contract event subclass will be used to find the contract event by signature.

.. py:method:: ContractEvents.myEvent(*args, **kwargs).processReceipt(transaction_receipt)

   Extracts the pertinent logs from a transaction receipt.

   Returns a tuple of :ref:`Event Log Objects <event-log-object>`, emitted from the event (e.g. ``myEvent``), with decoded ouput.

   .. code-block:: python

       >>> tx_hash = contract.functions.myFunction(12345).transact({'to':contract_address})
       >>> tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       >>> rich_logs = contract.events.myEvent().processReceipt(tx_receipt)
       >>> rich_logs[0]['args']
       {'myArg': 12345}
