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

    Create this type of contract with:


    .. code-block:: python

        >>> concise = w3.eth.contract(..., ContractFactoryClass=ConciseContract)


    This variation invokes all methods as a call, so if the classic contract had a method like
    ``contract.functions.owner().call()``, you could call it with ``concise.owner()`` instead.

    For access to send a transaction or estimate gas, you can add a keyword argument like so:


    .. code-block:: python

        >>> concise.withdraw(amount, transact={'from': eth.accounts[1], 'gas': 100000, ...})

        >>>  # which is equivalent to this transaction in the classic contract:

        >>> contract.functions.withdraw(amount).transact({'from': eth.accounts[1], 'gas': 100000, ...})


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

.. py:method:: Contract.functions.myMethod(*args, **kwargs).transact(transaction)

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

    If any of the ``args`` or ``kwargs`` specified in the ABI are an ``address`` type, they
    will accept ENS names.

    If a ``gas`` value is not provided, then the ``gas`` value for the
    method transaction will be created using the ``web3.eth.estimateGas()``
    method.

    Returns the transaction hash.

    .. code-block:: python

        >>> token_contract.functions.transfer(web3.eth.accounts[1], 12345).transact()
        "0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd"


.. py:method:: Contract.functions.myMethod(*args, **kwargs).call(transaction)

    Call a contract function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

    This method behaves the same as the :py:meth:`Contract.transact` method,
    with transaction details being passed into the first portion of the
    function call, and function arguments being passed into the second portion.

    Returns the return value of the executed function.

    .. code-block:: python

        >>> my_contract.functions.multiply7(3).call()
        21
        >>> token_contract.functions.myBalance().call({'from': web3.eth.coinbase})
        12345  # the token balance for `web3.eth.coinbase`
        >>> token_contract.functions.myBalance().call({'from': web3.eth.accounts[1]})
        54321  # the token balance for the account `web3.eth.accounts[1]`


.. py:method:: Contract.functions.myMethod(*args, **kwargs).estimateGas(transaction)

    Call a contract function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

    This method behaves the same as the :py:meth:`Contract.transact` method,
    with transaction details being passed into the first portion of the
    function call, and function arguments being passed into the second portion.

    Returns the amount of gas consumed which can be used as a gas estimate for
    executing this transaction publicly.

    .. code-block:: python

        >>> my_contract.estimateGas().multiply7(3)
        42650

.. py:method:: Contract.functions.myMethod(*args, **kwargs).buildTransaction(transaction)

    Builds a transaction dictionary based on the contract function call specified. 

    This method behaves the same as the :py:meth:`Contract.transact` method,
    with transaction details being passed into the first portion of the
    function call, and function arguments being passed into the second portion.

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

Events
------

.. py:classmethod:: Contract.eventFilter(event_name, filter_params=None)

    Creates a new :py:class:`web3.utils.filters.LogFilter` instance.

    The ``event_name`` parameter should be the name of the contract event you
    want to filter on.

    If provided,  ``filter_params`` should be a dictionary specifying
    additional filters for log entries.  The following keys are supported.

    * ``filter``: ``dictionary`` - (optional) Dictionary keys should be
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

    If the :py:attr:`Contract.address` attribute for this contract is
    non-null, the contract address will be added to the ``filter_params``.

.. _event-log-object:

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

        >>> transfer_filter = my_token_contract.eventFilter('Transfer', {'filter': {'_from': '0xdc3a9db694bcdd55ebae4a89b22ac6d12b3f0c24'}})
        >>> transfer_filter.get_new_entries()
        [...]  # array of Event Log Objects that match the filter.

        # wait a while...

        >>> transfer_filter.get_new_entries()
        [...]  # new events since the last call

        >>> transfer_filter.get_all_entries()
        [...]  # all events that match the filter.

.. py:method:: Contract.events.myEvent(*args, **kwargs).processReceipt(transaction_receipt)

   Returns a tuple of :ref:`Event Log Objects <event-log-object>`, emitted from the event (e.g. ``myEvent``), 
   with decoded ouput.

   .. code-block:: python

       >>> tx_hash = contract.functions.myFunction(12345).transact({'to':contract_address})
       >>> tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       >>> rich_logs = contract.events.myEvent().processReceipt(tx_receipt)
       >>> rich_logs[0]['args']
       {'myArg': 12345}
