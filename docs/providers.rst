.. _providers:

Providers
=========

The provider is how web3 talks to the blockchain.  Providers take JSON-RPC
requests and return the response.  This is normally done by submitting the
request to an HTTP or IPC socket based server.

.. note::

   web3.py supports one provider per instance. If you have an advanced use case
   that requires multiple providers, create and configure a new web3 instance
   per connection.

If you are already happily connected to your Ethereum node, then you
can skip the rest of the Providers section.

.. _choosing_provider:

Choosing How to Connect to Your Node
------------------------------------

Most nodes have a variety of ways to connect to them. If you have not
decided what kind of node to use, head on over to :ref:`choosing_node`

The most common ways to connect to your node are:

1. IPC (uses local filesystem: fastest and most secure)
2. Websockets (works remotely, faster than HTTP)
3. HTTP (more nodes support it)

If you're not sure how to decide, choose this way:

- If you have the option of running web3.py on the same machine as the node, choose IPC.
- If you must connect to a node on a different computer, use Websockets.
- If your node does not support Websockets, use HTTP.

Most nodes have a way of "turning off" connection options.
We recommend turning off all connection options that you are not using.
This provides a safer setup: it reduces the
number of ways that malicious hackers can try to steal your ether.

Once you have decided how to connect, you specify the details using a Provider.
Providers are web3.py classes that are configured for the kind of connection you want.

See:

- :class:`~web3.providers.ipc.IPCProvider`
- :class:`~web3.providers.persistent.AsyncIPCProvider`
- :class:`~web3.providers.websocket.WebsocketProvider`
- :class:`~web3.providers.persistent.WebsocketProviderV2`
- :class:`~web3.providers.rpc.HTTPProvider`
- :class:`~web3.providers.async_rpc.AsyncHTTPProvider`

Once you have configured your provider, for example:

.. code-block:: python

    from web3 import Web3
    my_provider = Web3.IPCProvider('/my/node/ipc/path')

Then you are ready to initialize your Web3 instance, like so:

.. code-block:: python

    w3 = Web3(my_provider)

Finally, you are ready to :ref:`get started with web3.py<first_w3_use>`.

Provider via Environment Variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can set the environment variable ``WEB3_PROVIDER_URI``
before starting your script, and web3 will look for that provider first.

Valid formats for this environment variable are:

- ``file:///path/to/node/rpc-json/file.ipc``
- ``http://192.168.1.2:8545``
- ``https://node.ontheweb.com``
- ``ws://127.0.0.1:8546``


Auto-initialization Provider Shortcuts
--------------------------------------

Geth dev Proof of Authority
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to a ``geth --dev`` Proof of Authority instance with
the POA middleware loaded by default:

.. code-block:: python

    >>> from web3.auto.gethdev import w3

    # confirm that the connection succeeded
    >>> w3.is_connected()
    True

Or, connect to an async web3 instance:

.. code-block:: python

    >>> from web3.auto.gethdev import async_w3
    >>> await async_w3.provider.connect()

    # confirm that the connection succeeded
    >>> await async_w3.is_connected()
    True


Built In Providers
------------------

Web3 ships with the following providers which are appropriate for connecting to
local and remote JSON-RPC servers.


HTTPProvider
~~~~~~~~~~~~

.. py:class:: web3.providers.rpc.HTTPProvider(endpoint_uri[, request_kwargs, session])

    This provider handles interactions with an HTTP or HTTPS based JSON-RPC server.

    * ``endpoint_uri`` should be the full URI to the RPC endpoint such as
      ``'https://localhost:8545'``.  For RPC servers behind HTTP connections
      running on port 80 and HTTPS connections running on port 443 the port can
      be omitted from the URI.
    * ``request_kwargs`` should be a dictionary of keyword arguments which
      will be passed onto each http/https POST request made to your node.
    * ``session`` allows you to pass a ``requests.Session`` object initialized
      as desired.

    .. code-block:: python

        >>> from web3 import Web3
        >>> w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

    Note that you should create only one HTTPProvider with the same provider URL
    per python process, as the HTTPProvider recycles underlying TCP/IP
    network connections, for better performance. Multiple HTTPProviders with different
    URLs will work as expected.

    Under the hood, the ``HTTPProvider`` uses the python requests library for
    making requests.  If you would like to modify how requests are made, you can
    use the ``request_kwargs`` to do so.  A common use case for this is increasing
    the timeout for each request.


    .. code-block:: python

        >>> from web3 import Web3
        >>> w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545", request_kwargs={'timeout': 60}))


    To tune the connection pool size, you can pass your own ``requests.Session``.

    .. code-block:: python

        >>> from web3 import Web3
        >>> adapter = requests.adapters.HTTPAdapter(pool_connections=20, pool_maxsize=20)
        >>> session = requests.Session()
        >>> session.mount('http://', adapter)
        >>> session.mount('https://', adapter)
        >>> w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545", session=session))


IPCProvider
~~~~~~~~~~~

.. py:class:: web3.providers.ipc.IPCProvider(ipc_path=None, timeout=10)

    This provider handles interaction with an IPC Socket based JSON-RPC
    server.

    *  ``ipc_path`` is the filesystem path to the IPC socket:

    .. code-block:: python

        >>> from web3 import Web3
        >>> w3 = Web3(Web3.IPCProvider("~/Library/Ethereum/geth.ipc"))

    If no ``ipc_path`` is specified, it will use a default depending on your operating
    system.

    - On Linux and FreeBSD: ``~/.ethereum/geth.ipc``
    - On Mac OS: ``~/Library/Ethereum/geth.ipc``
    - On Windows: ``\\.\pipe\geth.ipc``


AsyncIPCProvider (beta)
~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: This provider is still in beta. However, it is being actively developed
    and supported and is expected to be stable in the next major version of *web3.py*
    (v7).

.. py:class:: web3.providers.persistent.AsyncIPCProvider(ipc_path=None, request_timeout=10, max_connection_retries=5)

    This provider handles asynchronous, persistent interaction
    with an IPC Socket based JSON-RPC server.

    *  ``ipc_path`` is the filesystem path to the IPC socket:

    This provider inherits from the
    :class:`~web3.providers.persistent.persistent_connection.PersistentConnectionProvider` class. Refer to
    the :class:`~web3.providers.persistent.persistent_connection.PersistentConnectionProvider` documentation
    for details on additional configuration options available for this provider.

    If no ``ipc_path`` is specified, it will use a default depending on your operating
    system.

    - On Linux and FreeBSD: ``~/.ethereum/geth.ipc``
    - On Mac OS: ``~/Library/Ethereum/geth.ipc``
    - On Windows: ``\\.\pipe\geth.ipc``

AsyncIPCProvider Usage
++++++++++++++++++++++

The ``AsyncWeb3`` class may be used as a context manager, utilizing the ``async with``
syntax, when connecting via ``persistent_connection()`` using the
``AsyncIPCProvider``. This will automatically close the connection when the context
manager exits and is the recommended way to initiate a persistent connection to the
provider.

.. code-block:: python

        >>> import asyncio
        >>> from web3 import AsyncWeb3, AsyncIPCProvider

        >>> LOG = True  # toggle debug logging
        >>> if LOG:
        ...     import logging
        ...     logger = logging.getLogger("web3.providers.AsyncIPCProvider")
        ...     logger.setLevel(logging.DEBUG)
        ...     logger.addHandler(logging.StreamHandler())

        >>> async def subscription_context_manager_example():
        ...     async with AsyncWeb3.persistent_connection(
        ...         AsyncIPCProvider('path/to/ipc')
        ...     ) as w3:
        ...         # subscribe to new block headers
        ...         subscription_id = await w3.eth.subscribe("newHeads")
        ...
        ...         async for response in w3.socket.process_subscriptions():
        ...             print(f"{response}\n")
        ...             # handle responses here
        ...
        ...             if some_condition:
        ...                 # unsubscribe from new block headers and break out of
        ...                 # iterator
        ...                 await w3.eth.unsubscribe(subscription_id)
        ...                 break
        ...
        ...         # still an open connection, make any other requests and get
        ...         # responses via send / receive
        ...         latest_block = await w3.eth.get_block("latest")
        ...         print(f"Latest block: {latest_block}")
        ...
        ...         # the connection closes automatically when exiting the context
        ...         # manager (the `async with` block)

        >>> asyncio.run(subscription_context_manager_example())

If the above initilization pattern doesn't work for your application, the ``__await__()``
method is defined on the ``persistent_connection()`` connection in a manner that awaits
connecting to the socket. You may also choose to instantiate and connect via the
provider in separate lines. Both of these examples are shown below.

.. code-block:: python

    >>> async def alternate_init_example_1():
    ...     # awaiting the persistent connection itself will connect to the socket
    ...     w3 = await AsyncWeb3.persistent_connection(AsyncIPCProvider('path/to/ipc'))
    ...
    ...     # some code here
    ...
    ...     # manual cleanup
    ...     await w3.provider.disconnect()

    # run the example
    >>> asyncio.run(alternate_init_example_1)

    >>> async def alternate_init_example_2():
    ...     # instantiation and connection via the provider as separate lines
    ...     w3 = AsyncWeb3.persistent_connection(AsyncIPCProvider('path/to/ipc'))
    ...     await w3.provider.connect()
    ...
    ...     # some code here
    ...
    ...     # manual cleanup
    ...     await w3.provider.disconnect()

    # run the example
    >>> asyncio.run(alternate_init_example_2)

The ``AsyncIPCProvider`` class uses the
:class:`~web3.providers.persistent.request_processor.RequestProcessor` class under the
hood to sync up the receiving of responses and response processing for one-to-one and
one-to-many request-to-response requests. Refer to the
:class:`~web3.providers.persistent.request_processor.RequestProcessor`
documentation for details.


WebsocketProvider
~~~~~~~~~~~~~~~~~

.. note::

        ``WebsocketProviderV2`` is currently in beta and our goal is to fully replace
        ``WebsocketProvider`` with ``WebsocketProviderV2`` in the next major release
        of web3.py.

.. py:class:: web3.providers.websocket.WebsocketProvider(endpoint_uri[, websocket_timeout, websocket_kwargs])

    This provider handles interactions with an WS or WSS based JSON-RPC server.

    * ``endpoint_uri`` should be the full URI to the RPC endpoint such as
      ``'ws://localhost:8546'``.
    * ``websocket_timeout`` is the timeout in seconds, used when receiving or
      sending data over the connection. Defaults to 10.
    * ``websocket_kwargs`` this should be a dictionary of keyword arguments which
      will be passed onto the ws/wss websocket connection.

    .. code-block:: python

        >>> from web3 import Web3
        >>> w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8546"))

    Under the hood, the ``WebsocketProvider`` uses the python websockets library for
    making requests.  If you would like to modify how requests are made, you can
    use the ``websocket_kwargs`` to do so.  See the `websockets documentation`_ for
    available arguments.

    .. _`websockets documentation`: https://websockets.readthedocs.io/en/stable/reference/asyncio/client.html#websockets.client.WebSocketClientProtocol

    Unlike HTTP connections, the timeout for WS connections is controlled by a
    separate ``websocket_timeout`` argument, as shown below.


    .. code-block:: python

        >>> from web3 import Web3
        >>> w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8546", websocket_timeout=60))


Persistent Connection Providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: web3.providers.persistent.persistent_connection.PersistentConnectionProvider(endpoint_uri: str, request_timeout: float = 50.0, subscription_response_queue_size: int = 500)

    This is a base provider class, currently inherited by the ``WebsocketProviderV2``,
    and the ``AsyncIPCProvider``.
    It handles interactions with a persistent connection to a JSON-RPC server. Among
    its configuration, it houses all of the
    :class:`~web3.providers.persistent.request_processor.RequestProcessor` logic for
    handling the asynchronous sending and receiving of requests and responses. See
    the :ref:`internals__persistent_connection_providers` section for more details on
    the internals of persistent connection providers.

    * ``request_timeout`` is the timeout in seconds, used when sending data over the
      connection and waiting for a response to be received from the listener task.
      Defaults to ``50.0``.

    * ``subscription_response_queue_size`` is the size of the queue used to store
      subscription responses, defaults to ``500``. While messages are being consumed,
      this queue should never fill up as it is a transient queue and meant to handle
      asynchronous receiving and processing of responses. When in sync with the
      websocket stream, this queue should only ever store 1 to a few messages at a time.

    * ``silence_listener_task_exceptions`` is a boolean that determines whether
      exceptions raised by the listener task are silenced. Defaults to ``False``,
      raising any exceptions that occur in the listener task.



WebsocketProviderV2 (beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: This provider is still in beta. However, it is being actively developed
    and supported and is expected to be stable in the next major version of *web3.py*
    (v7).

.. py:class:: web3.providers.persistent.WebsocketProviderV2(endpoint_uri: str, websocket_kwargs: Dict[str, Any] = {}, silence_listener_task_exceptions: bool = False)

    This provider handles interactions with an WS or WSS based JSON-RPC server.

    * ``endpoint_uri`` should be the full URI to the RPC endpoint such as
      ``'ws://localhost:8546'``.
    * ``websocket_kwargs`` this should be a dictionary of keyword arguments which
      will be passed onto the ws/wss websocket connection.

    This provider inherits from the
    :class:`~web3.providers.persistent.persistent_connection.PersistentConnectionProvider` class. Refer to
    the :class:`~web3.providers.persistent.persistent_connection.PersistentConnectionProvider` documentation
    for details on additional configuration options available for this provider.

    Under the hood, the ``WebsocketProviderV2`` uses the python websockets library for
    making requests.  If you would like to modify how requests are made, you can
    use the ``websocket_kwargs`` to do so.  See the `websockets documentation`_ for
    available arguments.


WebsocketProviderV2 Usage
+++++++++++++++++++++++++

The ``AsyncWeb3`` class may be used as a context manager, utilizing the ``async with``
syntax, when connecting via ``persistent_connection()`` using the
``WebsocketProviderV2``. This will automatically close the connection when the context
manager exits and is the recommended way to initiate a persistent connection to the
websocket provider. A similar example, using the ``websockets`` connection as an
asynchronous context manager, can be found in the `websockets connection`_ docs.

.. code-block:: python

        >>> import asyncio
        >>> from web3 import AsyncWeb3
        >>> from web3.providers import WebsocketProviderV2

        >>> LOG = True  # toggle debug logging
        >>> if LOG:
        ...     import logging
        ...     logger = logging.getLogger("web3.providers.WebsocketProviderV2")
        ...     logger.setLevel(logging.DEBUG)
        ...     logger.addHandler(logging.StreamHandler())

        >>> async def ws_v2_subscription_context_manager_example():
        ...     async with AsyncWeb3.persistent_connection(
        ...         WebsocketProviderV2(f"ws://127.0.0.1:8546")
        ...     ) as w3:
        ...         # subscribe to new block headers
        ...         subscription_id = await w3.eth.subscribe("newHeads")
        ...
        ...         async for response in w3.socket.process_subscriptions():
        ...             print(f"{response}\n")
        ...             # handle responses here
        ...
        ...             if some_condition:
        ...                 # unsubscribe from new block headers and break out of
        ...                 # iterator
        ...                 await w3.eth.unsubscribe(subscription_id)
        ...                 break
        ...
        ...         # still an open connection, make any other requests and get
        ...         # responses via send / receive
        ...         latest_block = await w3.eth.get_block("latest")
        ...         print(f"Latest block: {latest_block}")
        ...
        ...         # the connection closes automatically when exiting the context
        ...         # manager (the `async with` block)

        >>> asyncio.run(ws_v2_subscription_context_manager_example())


The ``AsyncWeb3`` class may also be used as an asynchronous iterator, utilizing the
``async for`` syntax, when connecting via ``persistent_connection()`` using the
``WebsocketProviderV2``. This may be used to set up an indefinite websocket connection
and reconnect automatically if the connection is lost. A similar example, using the
``websockets`` connection as an asynchronous iterator, can be found in the
`websockets connection`_ docs.

.. _`websockets connection`: https://websockets.readthedocs.io/en/stable/reference/asyncio/client.html#websockets.client.connect

.. code-block:: python

    >>> import asyncio
    >>> from web3 import AsyncWeb3
    >>> from web3.providers import WebsocketProviderV2
    >>> import websockets

    >>> async def ws_v2_subscription_iterator_example():
    ...     async for w3 in AsyncWeb3.persistent_connection(
    ...         WebsocketProviderV2(f"ws://127.0.0.1:8546")
    ...     ):
    ...         try:
    ...             ...
    ...         except websockets.ConnectionClosed:
    ...             continue

    # run the example
    >>> asyncio.run(ws_v2_subscription_iterator_example())


If neither of the two init patterns above work for your application, the ``__await__()``
method is defined on the ``persistent_connection()`` connection in a manner that awaits
connecting to the websocket. You may also choose to instantiate and connect via the
provider in separate lines. Both of these examples are shown below.

.. code-block:: python

    >>> async def ws_v2_alternate_init_example_1():
    ...     # awaiting the persistent connection itself will connect to the websocket
    ...     w3 = await AsyncWeb3.persistent_connection(WebsocketProviderV2(f"ws://127.0.0.1:8546"))
    ...
    ...     # some code here
    ...
    ...     # manual cleanup
    ...     await w3.provider.disconnect()

    # run the example
    >>> asyncio.run(ws_v2_alternate_init_example_1)

    >>> async def ws_v2_alternate_init_example_2():
    ...     # instantiation and connection via the provider as separate lines
    ...     w3 = AsyncWeb3.persistent_connection(WebsocketProviderV2(f"ws://127.0.0.1:8546"))
    ...     await w3.provider.connect()
    ...
    ...     # some code here
    ...
    ...     # manual cleanup
    ...     await w3.provider.disconnect()

    # run the example
    >>> asyncio.run(ws_v2_alternate_init_example_2)

The ``WebsocketProviderV2`` class uses the
:class:`~web3.providers.persistent.request_processor.RequestProcessor` class under the
hood to sync up the receiving of responses and response processing for one-to-one and
one-to-many request-to-response requests. Refer to the
:class:`~web3.providers.persistent.request_processor.RequestProcessor`
documentation for details.

_PersistentConnectionWeb3 via AsyncWeb3.persistent_connection()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

When an ``AsyncWeb3`` class is connected to a persistent websocket connection, via the
``persistent_connection()`` method, it becomes an instance of the
``_PersistentConnectionWeb3`` class. This class has a few additional methods and
attributes that are not available on the ``AsyncWeb3`` class.

.. py:class:: web3.main._PersistentConnectionWeb3

    .. py:attribute:: ws

        The public API for interacting with the websocket connection is available via
        the ``ws`` attribute of the ``_PersistentConnectionWeb3`` class. This attribute
        is an instance of the
        :class:`~web3.providers.persistent.persistent_connection.PersistentConnection` class and is the main
        interface for interacting with the websocket connection.


Interacting with the Websocket Connection
+++++++++++++++++++++++++++++++++++++++++

.. py:class:: web3.providers.persistent.persistent_connection.PersistentConnection

    This class handles interactions with a websocket connection. It is available
    via the ``ws`` attribute of the ``_PersistentConnectionWeb3`` class. The
    ``PersistentConnection`` class has the following methods and attributes:

    .. py:attribute:: subscriptions

        This attribute returns the current active subscriptions as a dict mapping
        the subscription ``id`` to a dict of metadata about the subscription
        request.

    .. py:method:: process_subscriptions()

        This method is available for listening to websocket subscriptions indefinitely.
        It is an asynchronous iterator that yields strictly one-to-many
        (e.g. ``eth_subscription`` responses) request-to-response messages from the
        websocket connection. To receive responses for one-to-one request-to-response
        calls, use the standard API for making requests via the appropriate module
        (e.g. ``block_num = await w3.eth.block_number``)

        The responses from this method are formatted by web3.py formatters and run
        through the middlewares that were present at the time of subscription.
        An example of its use can be seen above in the `WebsocketProviderV2 Usage`_ section.

    .. py:method:: recv()

        The ``recv()`` method can be used to receive the next message from the
        websocket. The response from this method is formatted by web3.py formatters
        and run through the middlewares before being returned. This is not the
        recommended way to receive a message as the ``process_subscriptions()`` method
        is available for listening to websocket subscriptions and the standard API for
        making requests via the appropriate module
        (e.g. ``block_num = await w3.eth.block_number``) is available for receiving
        responses for one-to-one request-to-response calls.

    .. py:method:: send(method: RPCEndpoint, params: Sequence[Any])

        This method is available strictly for sending raw requests to the websocket,
        if desired. It is not recommended to use this method directly, as the
        responses will not be formatted by web3.py formatters or run through the
        middlewares. Instead, use the methods available on the respective web3
        module. For example, use ``w3.eth.get_block("latest")`` instead of
        ``w3.socket.send("eth_getBlockByNumber", ["latest", True])``.


AutoProvider
~~~~~~~~~~~~

:class:`~web3.providers.auto.AutoProvider` is the default used when initializing
:class:`web3.Web3` without any providers. There's rarely a reason to use it
explicitly.


AsyncHTTPProvider
~~~~~~~~~~~~~~~~~

.. py:class:: web3.providers.async_rpc.AsyncHTTPProvider(endpoint_uri[, request_kwargs])

    This provider handles interactions with an HTTP or HTTPS based JSON-RPC server asynchronously.

    * ``endpoint_uri`` should be the full URI to the RPC endpoint such as
      ``'https://localhost:8545'``.  For RPC servers behind HTTP connections
      running on port 80 and HTTPS connections running on port 443 the port can
      be omitted from the URI.
    * ``request_kwargs`` should be a dictionary of keyword arguments which
      will be passed onto each http/https POST request made to your node.
    * the ``cache_async_session()`` method allows you to use your own ``aiohttp.ClientSession`` object. This is an async method and not part of the constructor

    .. code-block:: python

        >>> from aiohttp import ClientSession
        >>> from web3 import AsyncWeb3, AsyncHTTPProvider

        >>> w3 = AsyncWeb3(AsyncHTTPProvider(endpoint_uri))

        >>> # If you want to pass in your own session:
        >>> custom_session = ClientSession()
        >>> await w3.provider.cache_async_session(custom_session) # This method is an async method so it needs to be handled accordingly

    Under the hood, the ``AsyncHTTPProvider`` uses the python
    `aiohttp <https://docs.aiohttp.org/en/stable/>`_ library for making requests.

.. py:currentmodule:: web3.providers.eth_tester

EthereumTesterProvider
~~~~~~~~~~~~~~~~~~~~~~

.. warning:: Experimental:  This provider is experimental. There are still significant gaps in
    functionality. However it is being actively developed and supported.

.. py:class:: EthereumTesterProvider(eth_tester=None)

    This provider integrates with the ``eth-tester`` library.  The ``eth_tester`` constructor
    argument should be an instance of the :class:`~eth_tester.EthereumTester` or a subclass of
    :class:`~eth_tester.backends.base.BaseChainBackend` class provided by the ``eth-tester`` library.
    If you would like a custom eth-tester instance to test with, see the
    ``eth-tester`` library `documentation <https://github.com/ethereum/eth-tester>`_ for details.

    .. code-block:: python

        >>> from web3 import Web3, EthereumTesterProvider
        >>> w3 = Web3(EthereumTesterProvider())

.. NOTE:: To install the needed dependencies to use EthereumTesterProvider, you can install the
    pip extras package that has the correct interoperable versions of the ``eth-tester``
    and ``py-evm`` dependencies needed to do testing: e.g. ``pip install web3[tester]``
