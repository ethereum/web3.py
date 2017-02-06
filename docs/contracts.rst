Contracts
=========

.. py:module:: web3.contract
.. py:currentmodule:: web3.contract


Contract Factories
------------------

.. py:class:: Contract(address)

    The ``Contract`` class is not intended to be used or instantiated directly.
    Instead you should use the ``web3.eth.contract(...)`` method to generate
    the contract factory classes for your contracts.

    Contract Factories provide an interface for deploying and interacting with
    Ethereum smart contracts.


Properties
----------

Each Contract Factory exposes the following properties.


.. py:attribute:: Contract.address

    The hexidecimal encoded 20 byte address of the contract.  May be ``None``
    if not provided during factory creation.


.. py:attribute:: Contract.abi

    The contract ABI array.


.. py:attribute:: Contract.bytecode

    The contract bytecode string.  May be ``None`` if not provided during
    factory creation.


.. py:attribute:: Contract.bytecode_runtime

    The runtime part of the contract bytecode string.  May be ``None`` if not
    provided during factory creation.


.. py:attribute:: Contract.bytecode_runtime

    The runtime part of the contract bytecode string.  May be ``None`` if not
    provided during factory creation.


Methods
-------

Each Contract Factory exposes the following methods.


.. py:classmethod:: Contract.deploy(transaction=None, arguments=None)

    Construct and send a transaction to deploy the contract.

    If provided ``transaction`` should be a dictionary conforming to the
    ``web3.eth.sendTransaction(transaction)`` method.  This value may not
    contain the keys ``data`` or ``to``.

    If the contract takes constructor arguments they should be provided as a
    list via the ``arguments`` parameter.

    If a ``gas`` value is not provided, then the ``gas`` value for the
    deployment transaction will be created using the ``web3.eth.estimateGas()``
    method.

    Returns the transaction hash for the deploy transaction.

.. py:method:: Contract.transact(transaction).myMethod(*args, **kwargs)

    Execute the specified function by sending a new public transaction.  

    This is executed in two steps.
    
    The first portion of this function call ``transact(transaction)`` takes a
    single parameter which should be a python dictionary conforming to
    the same format as the ``web3.eth.sendTransaction(transaction)`` method.
    This dictionary may not contain the keys ``data`` or ``to``.

    The second portion of the function call ``myMethod(*args, **kwargs)``
    selects the appropriate contract function based on the name and provided
    argument.  Arguments can be provided as positional arguments, keyword
    arguments, or a mix of the two.

    Returns the transaction hash.

    .. code-block:: python

        >>> token_contract.transact().transfer(web3.eth.accounts[1], 12345)
        "0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd"


.. py:method:: Contract.call(transaction).myMethod(*args, **kwargs)

    Call a contract function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

    This method behaves the same as the :py:method::`Contract.transact` method,
    with transaction details being passed into the first portion of the
    function call, and function arguments being passed into the second portion.

    Returns the return value of the executed function.

    .. code-block:: python

        >>> my_contract.call().multiply7(3)
        21
        >>> token_contract.call({'from': web3.eth.coinbase}).myBalance()
        12345  # the token balance for `web3.eth.coinbase`
        >>> token_contract.call({'from': web3.eth.accounts[1]}).myBalance()
        54321  # the token balance for the account `web3.eth.accounts[1]`


.. py:method:: Contract.estimateGas(transaction).myMethod(*args, **kwargs)

    Call a contract function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

    This method behaves the same as the :py:method::`Contract.transact` method,
    with transaction details being passed into the first portion of the
    function call, and function arguments being passed into the second portion.

    Returns the amount of gas consumed which can be used as a gas estimate for
    executing this transaction publicly.

    .. code-block:: python

        >>> my_contract.estimateGas().multiply7(3)
        42650


Events
------

.. py:method::
.. py:classmethod:: Contract.on(event_name, filter_params=None, *callbacks)

    Creates a new :py:class:`web3.utils.filters.LogFilter` instance.

    The ``event_name`` parameter should be the name of the contract event you
    want to filter on.

    If provided,  ``filter_params`` should be a dictionary specifying
    additional filters for log entries.  The following keys are supported.

    * ``filters``: ``dictionary`` - (optional) Dictionary keys should be
      argument names for the Event arguments.  Dictionary values should be the
      value you want to filter on, or a list of values to be filtered on.
      Lists of values will match log entries who's argument matches any value
      in the list.
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
      topics that should be used for filtering.  Topics are order-dependent.
      This parameter can also be a list of topic lists in which case filtering
      will match any of the provided topic arrays.

    The event topic for the event specified by ``event_name`` will be added to
    the ``filter_params['topics']`` list.

    If the :py:attribute:`Contract.address` attribute for this contract is
    non-null, the contract address will be added to the ``filter_params``.

    If provided, the ``*callbacks`` parameter should be callables which accept
    a single Event Log object.  When callbacks are provided, the filter will be
    *started*.  Otherwise the filter will be returned without starting it.

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

        >>> transfer_filter = my_token_contract.on('Transfer', {'filters': {'_from': '0xdc3a9db694bcdd55ebae4a89b22ac6d12b3f0c24'}})
        >>> transfer_filter.get()
        [...]  # array of Event Log Objects that match the filter.
        >>> transfer_filter.watch(my_callback)
        # now `my_callback` will be called each time a new matching event log
        # is encountered.


.. py:method::
.. py:classmethod:: Contract.pastEvents(event_name, filter_params=None, *callbacks)

    Creates a new :py:class:`web3.utils.filters.PastLogFilter` instance which
    will match historical event logs.

    All parameters behave the same as the :py:method::`Contract.on` method.

    .. code-block:: python

        >>> transfer_filter = my_token_contract.pastEvents('Transfer', {'filters': {'_from': '0xdc3a9db694bcdd55ebae4a89b22ac6d12b3f0c24'}})
        >>> transfer_filter.get()
        [...]  # array of Event Log Objects that match the filter for all historical events.
