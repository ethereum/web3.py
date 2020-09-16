.. _providers:

Providers
=========

The provider is how web3 talks to the blockchain.  Providers take JSON-RPC
requests and return the response.  This is normally done by submitting the
request to an HTTP or IPC socket based server.

If you are already happily connected to your Ethereum node, then you
can skip the rest of the Providers section.

.. _choosing_provider:

Choosing How to Connect to Your Node
--------------------------------------

Most nodes have a variety of ways to connect to them. If you have not
decided what kind of node to use, head on over to :ref:`choosing_node`

The most common ways to connect to your node are:

1. IPC (uses local filesystem: fastest and most secure)
2. Websockets (works remotely, faster than HTTP)
3. HTTP (more nodes support it)

If you're not sure how to decide, choose this way:

- If you have the option of running Web3.py on the same machine as the node, choose IPC.
- If you must connect to a node on a different computer, use Websockets.
- If your node does not support Websockets, use HTTP.

Most nodes have a way of "turning off" connection options.
We recommend turning off all connection options that you are not using.
This provides a safer setup: it reduces the
number of ways that malicious hackers can try to steal your ether.

Once you have decided how to connect, you specify the details using a Provider.
Providers are Web3.py classes that are configured for the kind of connection you want.

See:

- :class:`~web3.providers.ipc.IPCProvider`
- :class:`~web3.providers.websocket.WebsocketProvider`
- :class:`~web3.providers.rpc.HTTPProvider`

Once you have configured your provider, for example:

.. code-block:: python

    from web3 import Web3
    my_provider = Web3.IPCProvider('/my/node/ipc/path')

Then you are ready to initialize your Web3 instance, like so:

.. code-block:: python

    w3 = Web3(my_provider)

Finally, you are ready to :ref:`get started with Web3.py<first_w3_use>`.

.. _automatic_provider:

Automatic vs Manual Providers
-----------------------------

The ``Web3`` object will look for the Ethereum node in a few
standard locations if no providers are specified. Auto-detection happens
when you initialize like so:

.. code-block:: python

    from web3.auto import w3

    # which is equivalent to:

    from web3 import Web3
    w3 = Web3()

Sometimes, web3 cannot automatically detect where your node is.

- If you are not sure which kind of connection method to use, see
  :ref:`choosing_provider`.
- If you know the connection method, but not the other information
  needed to connect (like the path to the IPC file), you will need to look up
  that information in your node's configuration.
- If you're not sure which node you are using, see :ref:`choosing_node`

For a deeper dive into how automated detection works, see:

.. _automatic_provider_detection:

How Automated Detection Works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Web3 attempts to connect to nodes in the following order, using the first
succesful connection it can make:

1. The connection specified by an environment variable, see :ref:`provider_uri`
2. :class:`~web3.providers.ipc.IPCProvider`, which looks for several IPC file locations.
   ``IPCProvider`` will not automatically detect a testnet connection, it is suggested that the
   user instead uses a ``w3`` instance from ``web3.auto.infura`` (e.g.
   ``from web3.auto.infura.ropsten import w3``) if they want to auto-detect a testnet.
3. :class:`~web3.providers.rpc.HTTPProvider`, which attempts to connect to "http://localhost:8545"
4. ``None`` - if no providers are successful, you can still use Web3 APIs
   that do not require a connection, like:

   - :ref:`overview_type_conversions`
   - :ref:`overview_currency_conversions`
   - :ref:`overview_addresses`
   - :ref:`eth-account`
   - etc.

.. _automatic_provider_detection_examples:

Examples Using Automated Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some nodes provide APIs beyond the standards. Sometimes the same information is provided
in different ways across nodes. If you want to write code that works
across multiple nodes, you may want to look up the node type you are connected to.

For example, the following retrieves the client enode endpoint for both geth and parity:

.. code-block:: python

    from web3.auto import w3

    connected = w3.isConnected()

    if connected and w3.clientVersion.startswith('Parity'):
        enode = w3.parity.enode

    elif connected and w3.clientVersion.startswith('Geth'):
        enode = w3.geth.admin.nodeInfo['enode']

    else:
        enode = None

.. _provider_uri:

Provider via Environment Variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can set the environment variable ``WEB3_PROVIDER_URI``
before starting your script, and web3 will look for that provider first.

Valid formats for this environment variable are:

- ``file:///path/to/node/rpc-json/file.ipc``
- ``http://192.168.1.2:8545``
- ``https://node.ontheweb.com``
- ``ws://127.0.0.1:8546``


.. _custom_auto_providers:

Auto-initialization Provider Shortcuts
--------------------------------------

There are a couple auto-initialization shortcuts for common providers.

Infura Mainnet
~~~~~~~~~~~~~~

To easily connect to the Infura Mainnet remote node, first register for a free
project ID if you don't have one at https://infura.io/register .

Then set the environment variable ``WEB3_INFURA_PROJECT_ID`` with your Project ID::

    $ export WEB3_INFURA_PROJECT_ID=YourProjectID

If you have checked the box in the Infura UI indicating that requests need
an optional secret key, set the environment variable ``WEB3_INFURA_API_SECRET``::

    $ export WEB3_INFURA_API_SECRET=YourProjectSecret

.. code-block:: python

    >>> from web3.auto.infura import w3

    # confirm that the connection succeeded
    >>> w3.isConnected()
    True

Geth dev Proof of Authority
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to a ``geth --dev`` Proof of Authority instance with defaults:

.. code-block:: python

    >>> from web3.auto.gethdev import w3

    # confirm that the connection succeeded
    >>> w3.isConnected()
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

    Note that you should create only one HTTPProvider per python
    process, as the HTTPProvider recycles underlying TCP/IP network connections,
    for better performance.

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

.. py:class:: web3.providers.ipc.IPCProvider(ipc_path=None, testnet=False, timeout=10)

    This provider handles interaction with an IPC Socket based JSON-RPC
    server.

    *  ``ipc_path`` is the filesystem path to the IPC socket:

    .. code-block:: python

        >>> from web3 import Web3
        >>> w3 = Web3(Web3.IPCProvider("~/Library/Ethereum/geth.ipc"))

    If no ``ipc_path`` is specified, it will use the first IPC file
    it can find from this list:

    - On Linux and FreeBSD:

      - ``~/.ethereum/geth.ipc``
      - ``~/.local/share/io.parity.ethereum/jsonrpc.ipc``
      - ``~/.local/share/trinity/mainnet/ipcs-eth1/jsonrpc.ipc``
    - On Mac OS:

      - ``~/Library/Ethereum/geth.ipc``
      - ``~/Library/Application Support/io.parity.ethereum/jsonrpc.ipc``
      - ``~/.local/share/trinity/mainnet/ipcs-eth1/jsonrpc.ipc``
    - On Windows:

      - ``\\\.\pipe\geth.ipc``
      - ``\\\.\pipe\jsonrpc.ipc``


WebsocketProvider
~~~~~~~~~~~~~~~~~

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

    .. _`websockets documentation`: https://websockets.readthedocs.io/en/stable/api.html#websockets.protocol.WebSocketCommonProtocol

    Unlike HTTP connections, the timeout for WS connections is controlled by a
    separate ``websocket_timeout`` argument, as shown below.


    .. code-block:: python

        >>> from web3 import Web3
        >>> w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8546", websocket_timeout=60))

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



AutoProvider
~~~~~~~~~~~~

:class:`~web3.providers.auto.AutoProvider` is the default used when initializing
:class:`web3.Web3` without any providers. There's rarely a reason to use it
explicitly.
