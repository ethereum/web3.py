.. _providers:

Providers
=========

The provider is how web3 talks to the blockchain.  Providers take JSON-RPC
requests and return the response.  This is normally done by submitting the
request to an HTTP or IPC socket based server.

The ``Web3`` object requires at least one provider to be able to function.

.. code-block:: python

    >>> from web3 import Web3, HTTPProvider
    >>> provider = HTTPProvider('http://localhost:8545')
    >>> web3 = Web3(provider)


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
        >>> web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545", request_kwargs={'timeout': 60})


IPCProvider
~~~~~~~~~~~

.. py:class:: IPCProvider(ipc_path=None, testnet=False):

    This provider handles interaction with an IPC Socket based JSON-RPC
    server.

    *  ``ipc_path`` is the filesystem path to the IPC socket.:56

    .. code-block:: python

        >>> from web3 import Web3
        >>> web3 = Web3(Web3.IPCProvider("~/Library/Ethereum/geth.ipc")


.. py:currentmodule:: web3.providers.eth_tester

EthereumTesterProvider
~~~~~~~~~~~~~~~~~~~~~~

.. warning:: Experimental:  This provider is experimental and should be used with caution.

.. py:class:: EthereumTesterProvider(eth_tester)

    This provider integrates with the ``ethereum-tester`` library.  The
    ``eth_tester`` constructor argument should be an instance of the
    ``eth_tester.EthereumTester`` class provided by the ``ethereum-tester``
    library.  See the ``ethereum-tester`` library documentation for
    instructions on how to use the library.

    .. code-block:: python

        >>> from web3 import Web3
        >>> from web3.providers.eth_tester import EthereumTesterProvider
        >>> from eth_tester import EthereumTester
        >>> eth_tester = EthereumTester()
        >>> web3 = Web3(EthereumTesterProvider(eth_tester))



.. py:currentmodule:: web3.providers.tester


EthereumTesterProvider (legacy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: Pending Deprecation:  This provider is being deprecated soon in favor of the newly created ethereum-tester library.

.. py:class:: EthereumTesterProvider():

    This provider can be used for testing.  It uses an ephemeral blockchain
    backed by the ``ethereum.tester`` module.


TestRPCProvider
~~~~~~~~~~~~~~~

.. warning:: Pending Deprecation:  This provider is being deprecated soon in favor of the newly created ethereum-tester library.

.. py:class:: TestRPCProvider():

    This provider can be used for testing.  It uses an ephemeral blockchain
    backed by the ``ethereum.tester`` module.  This provider will be slower
    than the ``EthereumTesterProvider`` since it uses an HTTP server for RPC
    interactions with.


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
