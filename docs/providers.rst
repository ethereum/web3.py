.. _providers:

Providers
=========

The provider is how web3 talks to the blockchain.  Providers take JSON-RPC
requests and return the response.  This is normally done by submitting the
request to an HTTP or IPC socket based server.

If you are already happily connected to your Ethereum node, then you
can skip the rest of the Providers section.

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

You can manually create a connection by specifying a provider like so:

.. code-block:: python

    from web3 import Web3, HTTPProvider
    provider = HTTPProvider('http://localhost:8545')
    web3 = Web3(provider)

.. _automatic_provider_detection:

How Automated Detection Works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Web3 attempts to connect to nodes in the following order, using the first
succesful connection it can make:

1. The connection specified by an environment variable, see :ref:`provider_uri`
2. :class:`~web3.providers.ipc.IPCProvider`, which looks for several IPC file locations
3. :class:`~web3.providers.rpc.HTTPProvider`, which attempts to connect to "http://localhost:8545"
4. None - if no providers are successful, you can still use Web3 APIs
   that do not require a connection, like:

   - :ref:`overview_type_conversions`
   - :ref:`overview_currency_conversions`
   - :ref:`overview_addresses`
   - :class:`~web3.account.Account`
   - etc.

Built In Providers
------------------

Web3 ships with the following providers which are appropriate for connecting to
local and remote JSON-RPC servers.


HTTPProvider
~~~~~~~~~~~~

.. py:class:: web3.providers.rpc.HTTPProvider(endpoint_uri[, request_kwargs])

    This provider handles interactions with an HTTP or HTTPS based JSON-RPC server.

    * ``endpoint_uri`` should be the full URI to the RPC endpoint such as
      ``'https://localhost:8545'``.  For RPC servers behind HTTP connections
      running on port 80 and HTTPS connections running on port 443 the port can
      be omitted from the URI.
    * ``request_kwargs`` this should be a dictionary of keyword arguments which
      will be passed onto the http/https request.

    .. code-block:: python

        >>> from web3 import Web3
        >>> web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545")

    Under the hood, the ``HTTPProvider`` uses the python requests library for
    making requests.  If you would like to modify how requests are made, you can
    use the ``request_kwargs`` to do so.  A common use case for this is increasing
    the timeout for each request.


    .. code-block:: python

        >>> from web3 import Web3
        >>> web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545", request_kwargs={'timeout': 60}))


IPCProvider
~~~~~~~~~~~

.. py:class:: web3.providers.ipc.IPCProvider(ipc_path=None, testnet=False, timeout=10)

    This provider handles interaction with an IPC Socket based JSON-RPC
    server.

    *  ``ipc_path`` is the filesystem path to the IPC socket.:56

    .. code-block:: python

        >>> from web3 import Web3
        >>> web3 = Web3(Web3.IPCProvider("~/Library/Ethereum/geth.ipc"))

    If no ``ipc_path`` is specified, it will use the first IPC file
    it can find from this list:

    - On Linux:

      - ``~/.ethereum/geth.ipc``
      - ``~/.local/share/io.parity.ethereum/jsonrpc.ipc``
    - On Mac OS:

      - ``~/Library/Ethereum/geth.ipc``
      - ``~/Library/Application Support/io.parity.ethereum/jsonrpc.ipc``
    - On Windows:

      - ``\\\.\pipe\geth.ipc``
      - ``\\\.\pipe\jsonrpc.ipc``


.. py:currentmodule:: web3.providers.eth_tester

EthereumTesterProvider
~~~~~~~~~~~~~~~~~~~~~~

.. warning:: Experimental:  This provider is experimental and should be used with caution.
    However, it is the presumed replacement to :class:`~web3.providers.tester.EthereumTesterProvider`
    and is being actively developed and supported.

.. py:class:: EthereumTesterProvider(eth_tester=None)

    This provider integrates with the ``eth-tester`` library.  The
    ``eth_tester`` constructor argument should be an instance of the
    :class:`~eth_tester.EthereumTester` class provided by the ``eth-tester``
    library.  See the ``eth-tester`` library documentation for
    instructions on how to use the library.

    .. code-block:: python

        >>> from web3 import Web3
        >>> from web3.providers.eth_tester import EthereumTesterProvider
        >>> w3 = Web3(EthereumTesterProvider())



EthereumTesterProvider (legacy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: Deprecated:  This provider is deprecated in favor of
    :class:`~web3.providers.eth_tester.EthereumTesterProvider` and the newly created eth-tester.

.. py:class:: web3.providers.tester.EthereumTesterProvider()

    This provider can be used for testing.  It uses an ephemeral blockchain
    backed by the ``ethereum.tester`` module.


TestRPCProvider
~~~~~~~~~~~~~~~

.. warning:: Deprecated:  This provider is deprecated in favor of
    :class:`~web3.providers.eth_tester.EthereumTesterProvider` and the newly created eth-tester.

.. py:class:: TestRPCProvider()

    This provider can be used for testing.  It uses an ephemeral blockchain
    backed by the ``ethereum.tester`` module.  This provider will be slower
    than the ``EthereumTesterProvider`` since it uses an HTTP server for RPC
    interactions with.


AutoProvider
~~~~~~~~~~~~

:class:`~web3.providers.auto.AutoProvider` is the default used when initializing
:class:`web3.Web3` without any providers. There's rarely a reason to use it
explicitly.


Using Multiple Providers
------------------------

Web3 supports the use of multiple providers.  This is useful for cases where
you wish to delegate requests across different providers.  To use this feature,
simply instantiate your web3 instance with an iterable of provider instances.


.. code-block:: python

    >>> from web3 import Web3, HTTPProvider
    >>> from . import MySpecialProvider
    >>> special_provider = MySpecialProvider()
    >>> infura_provider = HTTPProvider('https://ropsten.infura.io')
    >>> web3 = Web3([special_provider, infura_provider])


When web3 has multiple providers it will iterate over them in order, trying the
RPC request and returning the first response it receives.  Any provider which
*cannot* respond to a request **must** throw a
``web3.exceptions.CannotHandleRequest`` exception.

If none of the configured providers are able to hand the request, then a
``web3.exceptions.UnhandledRequest`` exception will be thrown.
