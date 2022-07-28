Middleware
==========

Web3 manages layers of middlewares by default. They sit between the public Web3 methods and the
:doc:`providers`, which handle native communication with the Ethereum client. Each layer
can modify the request and/or response. Some middlewares are enabled by default, and
others are available for optional use.

Each middleware layer gets invoked before the request reaches the provider, and then
processes the result after the provider returns, in reverse order. However, it is
possible for a middleware to return early from a
call without the request ever getting to the provider (or even reaching the middlewares
that are in deeper layers).

More information is available in the "Internals: :ref:`internals__middlewares`" section.


.. _default_middleware:

Default Middleware
------------------

Some middlewares are added by default if you do not supply any. The defaults
are likely to change regularly, so this list may not include the latest version's defaults.
You can find the latest defaults in the constructor in ``web3/manager.py``

AttributeDict
~~~~~~~~~~~~~~~~~~

.. py:method:: web3.middleware.attrdict_middleware

    This middleware converts the output of a function from a dictionary to an ``AttributeDict``
    which enables dot-syntax access, like ``eth.get_block('latest').number``
    in addition to ``eth.get_block('latest')['number']``.

.eth Name Resolution
~~~~~~~~~~~~~~~~~~~~~

.. py:method:: web3.middleware.name_to_address_middleware

    This middleware converts Ethereum Name Service (ENS) names into the
    address that the name points to. For example :meth:`w3.eth.send_transaction <web3.eth.Eth.send_transaction>` will
    accept .eth names in the 'from' and 'to' fields.

.. note::
    This middleware only converts ENS names if invoked with the mainnet
    (where the ENS contract is deployed), for all other cases will result in an
    ``InvalidAddress`` error

Pythonic
~~~~~~~~~~~~

.. py:method:: web3.middleware.pythonic_middleware

    This converts arguments and returned values to python primitives,
    where appropriate. For example, it converts the raw hex string returned by the RPC call
    ``eth_blockNumber`` into an ``int``.

Gas Price Strategy
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: web3.middleware.gas_price_strategy_middleware

  .. warning::

      Gas price strategy is only supported for legacy transactions. The London fork
      introduced ``maxFeePerGas`` and ``maxPriorityFeePerGas`` transaction parameters
      which should be used over ``gasPrice`` whenever possible.

  This adds a gasPrice to transactions if applicable and when a gas price strategy has
  been set. See :ref:`Gas_Price` for information about how gas price is derived.

Buffered Gas Estimate
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: web3.middleware.buffered_gas_estimate_middleware

    This adds a gas estimate to transactions if ``gas`` is not present in the transaction
    parameters. Sets gas to:
    ``min(w3.eth.estimate_gas + gas_buffer, gas_limit)``
    where the gas_buffer default is 100,000

HTTPRequestRetry
~~~~~~~~~~~~~~~~~~

.. py:method:: web3.middleware.http_retry_request_middleware

    This middleware is a default specifically for HTTPProvider that retries failed
    requests that return the following errors: ``ConnectionError``, ``HTTPError``, ``Timeout``,
    ``TooManyRedirects``. Additionally there is a whitelist that only allows certain
    methods to be retried in order to not resend transactions, excluded methods are:
    ``eth_sendTransaction``, ``personal_signAndSendTransaction``, ``personal_sendTransaction``.

.. _Modifying_Middleware:

Configuring Middleware
-----------------------

Middleware can be added, removed, replaced, and cleared at runtime. To make that easier, you
can name the middleware for later reference. Alternatively, you can use a reference to the
middleware itself.

Middleware Order
~~~~~~~~~~~~~~~~~~

Think of the middleware as being layered in an onion, where you initiate a web3.py request at
the outermost layer of the onion, and the Ethereum node (like geth or parity) receives and responds
to the request inside the innermost layer of the onion. Here is a (simplified) diagram:

.. code-block:: none

                                         New request from web3.py

                                                     |
                                                     |
                                                     v

                                             `````Layer 2``````
                                      ```````                  ```````
                                 `````               |                ````
                              ````                   v                    ````
                           ```                                                ```
                         `.               ````````Layer 1```````                `.`
                       ``             ````                      `````              .`
                     `.            ```               |               ```            `.`
                    .`          ```                  v                  ```           `.
                  `.          `.`                                         ```           .`
                 ``          .`                  `Layer 0`                  ``           .`
                ``         `.               `````        ``````               .           .`
               `.         ``             ```         |        ```              .`          .
               .         ``            `.`           |           ``             .           .
              .         `.            ``       JSON-RPC call       .`            .          .`
              .         .            ``              |              .            ``          .
             ``         .            .               v               .            .          .
             .         .`           .                                .            .          ``
             .         .            .          Ethereum node         .`           .           .
             .         .            .                                .            .           .
             .         ``           `.               |               .            .           .
             .          .            .`              |              .`            .          .
             `.         .`            .`          Response         .`            .`          .
              .          .             `.`           |           `.`            `.           .
              `.          .              ```         |        ````             `.           .
               .          `.               `````     v     ````               `.           ``
                .           .`                 ```Layer 0``                  ``           `.
                 .           `.                                            `.`           `.
                  .            `.                    |                   `.`            `.
                   .`            ```                 |                 ```             .`
                    `.              ```              v             ````              `.`
                      ``               ``````                 `````                 .`
                        ``                   `````Layer 1`````                   `.`
                          ```                                                  ```
                            ````                     |                      ```
                               `````                 v                  ````
                                   ``````                          `````
                                         `````````Layer 2``````````

                                                     |
                                                     v

                                          Returned value in Web3.py


The middlewares are maintained in ``Web3.middleware_onion``. See
below for the API.

When specifying middlewares in a list, or retrieving the list of middlewares, they will
be returned in the order of outermost layer first and innermost layer last. In the above
example, that means that ``w3.middleware_onion.middlewares`` would return the middlewares in
the order of: ``[2, 1, 0]``.

See "Internals: :ref:`internals__middlewares`" for a deeper dive to how middlewares work.

Middleware Stack API
~~~~~~~~~~~~~~~~~~~~~

To add or remove items in different layers, use the following API:

.. py:method:: Web3.middleware_onion.add(middleware, name=None)

    Middleware will be added to the outermost layer. That means the new middleware will modify the
    request first, and the response last. You can optionally name it with any hashable object,
    typically a string.

    .. code-block:: python

        >>> w3 = Web3(...)
        >>> w3.middleware_onion.add(web3.middleware.pythonic_middleware)
        # or
        >>> w3.middleware_onion.add(web3.middleware.pythonic_middleware, 'pythonic')

.. py:method:: Web3.middleware_onion.inject(middleware, name=None, layer=None)

    Inject a named middleware to an arbitrary layer.

    The current implementation only supports injection at the innermost or
    outermost layers. Note that injecting to the outermost layer is equivalent to calling
    :meth:`Web3.middleware_onion.add` .

    .. code-block:: python

        # Either of these will put the pythonic middleware at the innermost layer
        >>> w3 = Web3(...)
        >>> w3.middleware_onion.inject(web3.middleware.pythonic_middleware, layer=0)
        # or
        >>> w3.middleware_onion.inject(web3.middleware.pythonic_middleware, 'pythonic', layer=0)

.. py:method:: Web3.middleware_onion.remove(middleware)

    Middleware will be removed from whatever layer it was in. If you added the middleware with
    a name, use the name to remove it. If you added the middleware as an object, use the object
    again later to remove it:

    .. code-block:: python

        >>> w3 = Web3(...)
        >>> w3.middleware_onion.remove(web3.middleware.pythonic_middleware)
        # or
        >>> w3.middleware_onion.remove('pythonic')

.. py:method:: Web3.middleware_onion.replace(old_middleware, new_middleware)

    Middleware will be replaced from whatever layer it was in. If the middleware was named, it will
    continue to have the same name. If it was un-named, then you will now reference it with the new
    middleware object.

    .. code-block:: python

        >>> from web3.middleware import pythonic_middleware, attrdict_middleware
        >>> w3 = Web3(...)

        >>> w3.middleware_onion.replace(pythonic_middleware, attrdict_middleware)
        # this is now referenced by the new middleware object, so to remove it:
        >>> w3.middleware_onion.remove(attrdict_middleware)

        # or, if it was named

        >>> w3.middleware_onion.replace('pythonic', attrdict_middleware)
        # this is still referenced by the original name, so to remove it:
        >>> w3.middleware_onion.remove('pythonic')

.. py:method:: Web3.middleware_onion.clear()

    Empty all the middlewares, including the default ones.

    .. code-block:: python

        >>> w3 = Web3(...)
        >>> w3.middleware_onion.clear()
        >>> assert len(w3.middleware_onion) == 0

.. py:attribute:: Web3.middleware_onion.middlewares

    Return all the current middlewares for the ``Web3`` instance in the appropriate order for importing into a new
    ``Web3`` instance.

    .. code-block:: python

        >>> w3_1 = Web3(...)
        # add uniquely named middleware:
        >>> w3_1.middleware_onion.add(web3.middleware.pythonic_middleware, 'test_middleware')
        # export middlewares from first w3 instance
        >>> middlewares = w3_1.middleware_onion.middlewares

        # import into second instance
        >>> w3_2 = Web3(..., middlewares=middlewares)
        >>> assert w3_1.middleware_onion.middlewares == w3_2.middleware_onion.middlewares
        >>> assert w3_2.middleware_onion.get('test_middleware')


Optional Middleware
-----------------------

Web3 ships with non-default middleware, for your custom use. In addition to the other ways of
:ref:`Modifying_Middleware`, you can specify a list of middleware when initializing Web3, with:

.. code-block:: python

    Web3(middlewares=[my_middleware1, my_middleware2])

.. warning::
  This will
  *replace* the default middlewares. To keep the default functionality,
  either use ``middleware_onion.add()`` from above, or add the default middlewares to your list of
  new middlewares.

Below is a list of built-in middleware, which is not enabled by default.

Stalecheck
~~~~~~~~~~~~

.. py:method:: web3.middleware.make_stalecheck_middleware(allowable_delay)

    This middleware checks how stale the blockchain is, and interrupts calls with a failure
    if the blockchain is too old.

    * ``allowable_delay`` is the length in seconds that the blockchain is allowed to be
      behind of ``time.time()``

    Because this middleware takes an argument, you must create the middleware
    with a method call.

    .. code-block:: python

        two_day_stalecheck = make_stalecheck_middleware(60 * 60 * 24 * 2)
        web3.middleware_onion.add(two_day_stalecheck)

    If the latest block in the blockchain is older than 2 days in this example, then the
    middleware will raise a ``StaleBlockchain`` exception on every call except
    ``web3.eth.get_block()``.


Cache
~~~~~~~~~~~

All of the caching middlewares accept these common arguments.

* ``cache_class`` must be a callable which returns an object which implements the dictionary API.
* ``rpc_whitelist`` must be an iterable, preferably a set, of the RPC methods that may be cached.
* ``should_cache_fn`` must be a callable with the signature ``fn(method, params, response)`` which returns whether the response should be cached.


.. py:method:: web3.middleware.construct_simple_cache_middleware(cache_class, rpc_whitelist, should_cache_fn)

    Constructs a middleware which will cache the return values for any RPC
    method in the ``rpc_whitelist``.

    A ready to use version of this middleware can be found at
    ``web3.middlewares.simple_cache_middleware``.


.. py:method:: web3.middleware.construct_time_based_cache_middleware(cache_class, cache_expire_seconds, rpc_whitelist, should_cache_fn)

    Constructs a middleware which will cache the return values for any RPC
    method in the ``rpc_whitelist`` for an amount of time defined by
    ``cache_expire_seconds``.

    * ``cache_expire_seconds`` should be the number of seconds a value may
      remain in the cache before being evicted.

    A ready to use version of this middleware can be found at
    ``web3.middlewares.time_based_cache_middleware``.


.. py:method:: web3.middleware.construct_latest_block_based_cache_middleware(cache_class, average_block_time_sample_size, default_average_block_time, rpc_whitelist, should_cache_fn)

    Constructs a middleware which will cache the return values for any RPC
    method in the ``rpc_whitelist`` for the latest block.
    It avoids re-fetching the current latest block for each
    request by tracking the current average block time and only requesting
    a new block when the last seen latest block is older than the average
    block time.

    * ``average_block_time_sample_size`` The number of blocks which should be
      sampled to determine the average block time.
    * ``default_average_block_time`` The initial average block time value to
      use for cases where there is not enough chain history to determine the
      average block time.

    A ready to use version of this middleware can be found at
    ``web3.middlewares.latest_block_based_cache_middleware``.

.. _geth-poa:

Proof of Authority
~~~~~~~~~~~~~~~~~~

.. note::
    It's important to inject the middleware at the 0th layer of the middleware onion:
    `w3.middleware_onion.inject(geth_poa_middleware, layer=0)`

The ``geth_poa_middleware`` is required to connect to ``geth --dev`` or the Rinkeby
public network. It may also be needed for other EVM compatible blockchains like Polygon
or BNB Chain (Binance Smart Chain).

If the middleware is not injected at the 0th layer of the middleware onion, you may get
errors like the example below when interacting with your EVM node.

```web3.exceptions.ExtraDataLengthError: The field extraData is 97 bytes, but should be
32. It is quite likely that you are connected to a POA chain. Refer to
http://web3py.readthedocs.io/en/stable/middleware.html#proof-of-authority
for more details. The full extraData is: HexBytes('...')```


The easiest way to connect to a default ``geth --dev`` instance which loads the middleware is:


.. code-block:: python

    >>> from web3.auto.gethdev import w3

    # confirm that the connection succeeded
    >>> w3.clientVersion
    'Geth/v1.7.3-stable-4bb3c89d/linux-amd64/go1.9'

This example connects to a local ``geth --dev`` instance on Linux with a
unique IPC location and loads the middleware:

.. code-block:: python

    >>> from web3 import Web3, IPCProvider

    # connect to the IPC location started with 'geth --dev --datadir ~/mynode'
    >>> w3 = Web3(IPCProvider('~/mynode/geth.ipc'))

    >>> from web3.middleware import geth_poa_middleware

    # inject the poa compatibility middleware to the innermost layer (0th layer)
    >>> w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # confirm that the connection succeeded
    >>> w3.clientVersion
    'Geth/v1.7.3-stable-4bb3c89d/linux-amd64/go1.9'

Why is ``geth_poa_middleware`` necessary?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''

There is no strong community consensus on a single Proof-of-Authority (PoA) standard yet.
Some nodes have successful experiments running, though. One is go-ethereum (geth),
which uses a prototype PoA for it's development mode and the Rinkeby test network.

Unfortunately, it does deviate from the yellow paper specification, which constrains the
``extraData`` field in each block to a maximum of 32-bytes. Geth's PoA uses more than
32 bytes, so this middleware modifies the block data a bit before returning it.

.. _local-filter:

Locally Managed Log and Block Filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This middleware provides an alternative to ethereum node managed filters. When used, Log and
Block filter logic are handled locally while using the same web3 filter api. Filter results are
retrieved using JSON-RPC endpoints that don't rely on server state.

.. doctest::

    >>> from web3 import Web3, EthereumTesterProvider
    >>> w3 = Web3(EthereumTesterProvider())
    >>> from web3.middleware import local_filter_middleware
    >>> w3.middleware_onion.add(local_filter_middleware)

.. code-block:: python

    #  Normal block and log filter apis behave as before.
    >>> block_filter = w3.eth.filter("latest")

    >>> log_filter = myContract.events.myEvent.build_filter().deploy()

Signing
~~~~~~~

.. py:method:: web3.middleware.construct_sign_and_send_raw_middleware(private_key_or_account)

This middleware automatically captures transactions, signs them, and sends them as raw transactions.
The ``from`` field on the transaction, or ``w3.eth.default_account`` must be set to the address of the private key for
this middleware to have any effect.

   * ``private_key_or_account`` A single private key or a tuple, list or set of private keys.

      Keys can be in any of the following formats:

      * An ``eth_account.LocalAccount`` object
      * An ``eth_keys.PrivateKey`` object
      * A raw private key as a hex string or byte string

.. code-block:: python

   >>> from web3 import Web3, EthereumTesterProvider
   >>> w3 = Web3(EthereumTesterProvider)
   >>> from web3.middleware import construct_sign_and_send_raw_middleware
   >>> from eth_account import Account
   >>> acct = Account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
   >>> w3.middleware_onion.add(construct_sign_and_send_raw_middleware(acct))
   >>> w3.eth.default_account = acct.address

:ref:`Hosted nodes<local_vs_hosted>` (like Infura or Alchemy) only support signed transactions. This often results in ``send_raw_transaction`` being used repeatedly. Instead, we can automate this process with ``construct_sign_and_send_raw_middleware(private_key_or_account)``.

.. code-block:: python

    >>> from web3 import Web3
    >>> w3 = Web3(Web3.HTTPProvider('HTTP_ENDPOINT'))
    >>> from web3.middleware import construct_sign_and_send_raw_middleware
    >>> from eth_account import Account
    >>> import os
    >>> acct = w3.eth.account.from_key(os.environ.get('PRIVATE_KEY'))
    >>> w3.middleware_onion.add(construct_sign_and_send_raw_middleware(acct))
    >>> w3.eth.default_account = acct.address

Now you can send a transaction from acct.address without having to build and sign each raw transaction.

When making use of this signing middleware, when sending dynamic fee transactions (recommended over legacy transactions),
the transaction ``type`` of ``2`` (or ``'0x2'``) is necessary. This is because transaction signing is validated based
on the transaction ``type`` parameter. This value defaults to ``'0x2'`` when ``maxFeePerGas`` and / or
``maxPriorityFeePerGas`` are present as parameters in the transaction as these params imply a dynamic fee transaction.
Since these values effectively replace the legacy ``gasPrice`` value, do not set a ``gasPrice`` for dynamic fee transactions.
Doing so will lead to validation issues.

.. code-block:: python

   # dynamic fee transaction, introduced by EIP-1559:
   >>> dynamic_fee_transaction = {
   ...     'type': '0x2',  # optional - defaults to '0x2' when dynamic fee transaction params are present
   ...     'from': acct.address,  # optional if w3.eth.default_account was set with acct.address
   ...     'to': receiving_account_address,
   ...     'value': 22,
   ...     'maxFeePerGas': 2000000000,  # required for dynamic fee transactions
   ...     'maxPriorityFeePerGas': 1000000000,  # required for dynamic fee transactions
   ... }
   >>> w3.eth.send_transaction(dynamic_fee_transaction)

A legacy transaction still works in the same way as it did before EIP-1559 was introduced:

.. code-block:: python

   >>> legacy_transaction = {
   ...     'to': receiving_account_address,
   ...     'value': 22,
   ...     'gasPrice': 123456,  # optional - if not provided, gas_price_strategy (if exists) or eth_gasPrice is used
   ... }
   >>> w3.eth.send_transaction(legacy_transaction)
