Middleware
==========

There is a stack of middlewares managed by Web3. They sit between the public Web3 methods and the
:doc:`providers`, which handle native communication with the Ethereum client. Each layer
can modify the request and/or response. Some middlewares are enabled by default, and
others are available for optional use.

Each middleware in the stack gets invoked before the request reaches the provider, and then
processes the result after the provider returns, in reverse order. However, it is
possible for a middleware to return early from a
call without the request ever getting to the provider (or even reaching the middlewares further down
the stack).

More information is available in the "Internals: :ref:`internals__middlewares`" section.


Default Middleware
------------------

Some middlewares are added by default if you do not supply any. The defaults
are likely to change regularly, so this list may not include the latest version's defaults.
You can find the latest defaults in the constructor in `web3/manager.py`

AttributeDict
~~~~~~~~~~~~~~~~~~

.. py:method:: web3.middleware.attrdict_middleware

    This middleware converts the output of a function from a dictionary to an ``AttributeDict``
    which enables dot-syntax access, like ``eth.getBlock('latest').number``
    in addition to ``eth.getBlock('latest')['number']``.

.eth Name Resolution
~~~~~~~~~~~~~~~~~~~~~

.. py:method:: web3.middleware.name_to_address_middleware

    This middleware converts Ethereum Name Service (ENS) names into the
    address that the name points to. For example :meth:`~web3.Eth.sendTransaction` will
    accept .eth names in the 'from' and 'to' fields.

Pythonic
~~~~~~~~~~~~

.. py:method:: web3.middleware.pythonic_middleware

    This converts arguments and returned values to python primitives,
    where appropriate. For example, it converts the raw hex string returned by the RPC call
    ``eth_blockNumber`` into an ``int``.

Gas Price Strategy
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: web3.middleware.gas_price_strategy_middleware

    This adds a gasPrice to transactions if applicable and when a gas price strategy has
    been set. See :ref:`Gas_Price` for information about how gas price is derived.

HTTPRequestRetry
~~~~~~~~~~~~~~~~~~

.. py:method:: web3.middleware.http_retry_request_middleware

    This middleware is a default specifically for HTTPProvider that retries failed
    requests that return the following errors: `ConnectionError`, `HTTPError`, `Timeout`,
    `TooManyRedirects`. Additionally there is a whitelist that only allows certain
    methods to be retried in order to not resend transactions, excluded methods are:
    `eth_sendTransaction`, `personal_signAndSendTransaction`, `personal_sendTransaction`. 

.. _Modifying_Middleware:

Modifying Middleware
-----------------------

Middleware can be added, removed, replaced, and cleared at runtime. To make that easier, you
can name the middleware for later reference. Alternatively, you can use a reference to the
middleware itself.

.. py:method:: Web3.middleware_stack.add(middleware, name=None)

    Middleware will be added to the top of the stack. That means the new middleware will modify the
    request first, and the response last. You can optionally name it with any hashable object,
    typically a string.

    .. code-block:: python

        >>> w3 = Web3(...)
        >>> w3.middleware_stack.add(web3.middleware.pythonic_middleware)
        # or
        >>> w3.middleware_stack.add(web3.middleware.pythonic_middleware, 'pythonic')

.. py:method:: Web3.middleware_stack.remove(middleware)

    Middleware will be removed from wherever it sat in the stack. If you added the middleware with
    a name, use the name to remove it. If you added the middleware as an object, use the object to
    remove it.

    .. code-block:: python

        >>> w3 = Web3(...)
        >>> w3.middleware_stack.remove(web3.middleware.pythonic_middleware)
        # or
        >>> w3.middleware_stack.remove('pythonic')

.. py:method:: Web3.middleware_stack.replace(old_middleware, new_middleware)

    Middleware will be replaced wherever it sat in the stack. If the middleware was named, it will
    continue to have the same name. If it was un-named, then you will now reference it with the new
    middleware object.

    .. code-block:: python

        >>> from web3.middleware import pythonic_middleware, attrdict_middleware
        >>> w3 = Web3(...)

        >>> w3.middleware_stack.replace(pythonic_middleware, attrdict_middleware)
        # this is now referenced by the new middleware object, so to remove it:
        >>> w3.middleware_stack.remove(attrdict_middleware)

        # or, if it was named

        >>> w3.middleware_stack.replace('pythonic', attrdict_middleware)
        # this is still referenced by the original name, so to remove it:
        >>> w3.middleware_stack.remove('pythonic')

.. py:method:: Web3.middleware_stack.clear()

    Empty all the middlewares, including the default ones.

    .. code-block:: python

        >>> w3 = Web3(...)
        >>> w3.middleware_stack.clear()
        >>> assert len(w3.middleware_stack) == 0


Built-in Middleware
-----------------------

Web3 ships with non-default middleware, for your custom use. In addition to the other ways of
:ref:`Modifying_Middleware`, you can specify a list of middleware when initializing Web3, with:

.. code-block:: python

    Web3(middlewares=[my_middleware1, my_middleware2])

.. warning::
  This will
  *replace* the default middlewares. To keep the default functionality,
  either use ``middleware_stack.add()`` from above, or add the default middlewares to your list of
  new middlewares.

Below is a list of built-in middleware.

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
        web3.middleware_stack.add(two_day_stalecheck)

    If the latest block in the blockchain is older than 2 days in this example, then the
    middleware will raise a ``StaleBlockchain`` exception on every call except
    ``web3.eth.getBlock()``.


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
    method in the ``rpc_whitelist`` for an amount of time defined by
    ``cache_expire_seconds``.

    * ``average_block_time_sample_size`` The number of blocks which should be
      sampled to determine the average block time.
    * ``default_average_block_time`` The initial average block time value to
      use for cases where there is not enough chain history to determine the
      average block time.

    A ready to use version of this middleware can be found at
    ``web3.middlewares.latest_block_based_cache_middleware``.
