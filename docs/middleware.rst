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
~~~~~~~~~~~~

.. py:method:: web3.middleware.attrdict_middleware

    This middleware converts the output of a function from a dictionary to an ``AttributeDict``
    which enables dot-syntax access, like ``eth.getBlock('latest').number``
    in addition to ``eth.getBlock('latest')['number']``.

Pythonic
~~~~~~~~~~~~

.. py:method:: web3.middleware.pythonic_middleware

    This converts arguments and returned values to python primitives,
    where appropriate. For example, it converts the raw hex string returned by the RPC call
    ``eth_blockNumber`` into an ``int``.

Built-in Middleware
------------------

Web3 ships with middleware for custom use, as desired. Middleware can be added after creating
your Web3 object, like:

.. code-block:: python

    w3 = Web3(...)
    w3.add_middleware(my_middleware)

Alternatively, you can pass in middlewares to the Web3 constructor.

.. code-block:: python

    Web3(middlewares=[my_middleware1, my_middleware2])

.. warning::
  This will
  *replace* the default middlewares. To keep the default functionality,
  either use ``add_middleware()`` from above, or add the default middlewares to your list of
  new middlewares.

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
        web3.add_middleware(two_day_stalecheck)

    If the latest block in the blockchain is older than 2 days in this example, then the
    middleware will raise a ``StaleBlockchain`` exception on every call except
    ``web3.eth.getBlock()``.
