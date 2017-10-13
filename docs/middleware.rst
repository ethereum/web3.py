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

Pythonic
~~~~~~~~~~~~

.. py:method:: web3.middleware.pythonic_middleware

    This converts arguments and returned values to python primitives,
    where appropriate. For example, it converts the raw hex string returned by the RPC call
    ``eth_blockNumber`` into an ``int``.

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
