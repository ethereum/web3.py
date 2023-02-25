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
- :class:`~web3.providers.websocket.WebsocketProvider`
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

To connect to a ``geth --dev`` Proof of Authority instance with defaults:

.. code-block:: python

    >>> from web3.auto.gethdev import w3

    # confirm that the connection succeeded
    >>> w3.is_connected()
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

    .. _`websockets documentation`: https://websockets.readthedocs.io/en/stable/reference/client.html#websockets.client.WebSocketClientProtocol

    Unlike HTTP connections, the timeout for WS connections is controlled by a
    separate ``websocket_timeout`` argument, as shown below.


    .. code-block:: python

        >>> from web3 import Web3
        >>> w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8546", websocket_timeout=60))

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

Supported Methods
^^^^^^^^^^^^^^^^^

Eth
***
- :class:`web3.eth.account <eth_account.account.Account>`
- :meth:`web3.eth.accounts <web3.eth.Eth.accounts>`
- :meth:`web3.eth.block_number <web3.eth.Eth.block_number>`
- :meth:`web3.eth.chain_id <web3.eth.Eth.chain_id>`
- :meth:`web3.eth.coinbase <web3.eth.Eth.coinbase>`
- :meth:`web3.eth.default_account <web3.eth.Eth.default_account>`
- :meth:`web3.eth.default_block <web3.eth.Eth.default_block>`
- :meth:`web3.eth.gas_price <web3.eth.Eth.gas_price>`
- :meth:`web3.eth.hashrate <web3.eth.Eth.hashrate>`
- :meth:`web3.eth.max_priority_fee <web3.eth.Eth.max_priority_fee>`
- :meth:`web3.eth.mining <web3.eth.Eth.mining>`
- :meth:`web3.eth.syncing <web3.eth.Eth.syncing>`
- :meth:`web3.eth.call() <web3.eth.Eth.call>`
- :meth:`web3.eth.estimate_gas() <web3.eth.Eth.estimate_gas>`
- :meth:`web3.eth.generate_gas_price() <web3.eth.Eth.generate_gas_price>`
- :meth:`web3.eth.get_balance() <web3.eth.Eth.get_balance>`
- :meth:`web3.eth.get_block() <web3.eth.Eth.get_block>`
- :meth:`web3.eth.get_code() <web3.eth.Eth.get_code>`
- :meth:`web3.eth.get_logs() <web3.eth.Eth.get_logs>`
- :meth:`web3.eth.get_raw_transaction() <web3.eth.Eth.get_raw_transaction>`
- :meth:`web3.eth.get_raw_transaction_by_block() <web3.eth.Eth.get_raw_transaction_by_block>`
- :meth:`web3.eth.get_transaction() <web3.eth.Eth.get_transaction>`
- :meth:`web3.eth.get_transaction_count() <web3.eth.Eth.get_transaction_count>`
- :meth:`web3.eth.get_transaction_receipt() <web3.eth.Eth.get_transaction_receipt>`
- :meth:`web3.eth.get_storage_at() <web3.eth.Eth.get_storage_at>`
- :meth:`web3.eth.send_transaction() <web3.eth.Eth.send_transaction>`
- :meth:`web3.eth.send_raw_transaction() <web3.eth.Eth.send_raw_transaction>`
- :meth:`web3.eth.wait_for_transaction_receipt() <web3.eth.Eth.wait_for_transaction_receipt>`
- :meth:`web3.eth.sign() <web3.eth.Eth.sign>`
- :meth:`web3.eth.sign_transaction() <web3.eth.Eth.sign_transaction>`
- :meth:`web3.eth.replace_transaction() <web3.eth.Eth.replace_transaction>`
- :meth:`web3.eth.get_uncle_count() <web3.eth.Eth.get_uncle_count>`

Net
***
- :meth:`web3.net.listening() <web3.net.listening>`
- :meth:`web3.net.peer_count() <web3.net.peer_count>`
- :meth:`web3.net.version() <web3.net.version>`

Geth
****
- :meth:`web3.geth.admin.add_peer() <web3.geth.admin.add_peer>`
- :meth:`web3.geth.admin.datadir() <web3.geth.admin.datadir>`
- :meth:`web3.geth.admin.node_info() <web3.geth.admin.node_info>`
- :meth:`web3.geth.admin.peers() <web3.geth.admin.peers>`
- :meth:`web3.geth.admin.start_http() <web3.geth.admin.start_http>`
- :meth:`web3.geth.admin.start_ws() <web3.geth.admin.start_ws>`
- :meth:`web3.geth.admin.stop_http() <web3.geth.admin.stop_http>`
- :meth:`web3.geth.admin.stop_ws() <web3.geth.admin.stop_ws>`
- :meth:`web3.geth.personal.ec_recover()`
- :meth:`web3.geth.personal.import_raw_key() <web3.geth.personal.import_raw_key>`
- :meth:`web3.geth.personal.list_accounts() <web3.geth.personal.list_accounts>`
- :meth:`web3.geth.personal.list_wallets() <web3.geth.personal.list_wallets()>`
- :meth:`web3.geth.personal.lock_account() <web3.geth.personal.lock_account>`
- :meth:`web3.geth.personal.new_account() <web3.geth.personal.new_account>`
- :meth:`web3.geth.personal.send_transaction() <web3.geth.personal.send_transaction>`
- :meth:`web3.geth.personal.sign()`
- :meth:`web3.geth.personal.unlock_account() <web3.geth.personal.unlock_account>`
- :meth:`web3.geth.txpool.inspect() <web3.geth.txpool.TxPool.inspect()>`
- :meth:`web3.geth.txpool.content() <web3.geth.txpool.TxPool.content()>`
- :meth:`web3.geth.txpool.status() <web3.geth.txpool.TxPool.status()>`

Contract
^^^^^^^^
Contract is fully implemented for the Async provider. The only documented exception to this at
the moment is where :class:`ENS` is needed for address lookup. All addresses that are passed to Async
contract should not be :class:`ENS` addresses.

ENS
^^^^^^^^
ENS is fully implemented for the Async provider.

Supported Middleware
^^^^^^^^^^^^^^^^^^^^
- :meth:`Gas Price Strategy <web3.middleware.gas_price_strategy_middleware>`
- :meth:`Buffered Gas Estimate Middleware <web3.middleware.buffered_gas_estimate_middleware>`
- :meth:`Stalecheck Middleware <web3.middleware.make_stalecheck_middleware>`
- :meth:`Attribute Dict Middleware <web3.middleware.attrdict_middleware>`
- :meth:`Validation Middleware <web3.middleware.validation>`
- :ref:`Geth POA Middleware <geth-poa>`
- :meth:`Simple Cache Middleware <web3.middleware.simple_cache_middleware>`


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
