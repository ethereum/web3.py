Providers
========

.. py:module:: web3.providers


Providers are in control of the actual interactions with the blockchain.


.. py:currentmodule:: web3.providers.rpc


HTTPProvider
------------

.. py:class:: RPCProvider(endpoint_uri[, request_kwargs])

    This provider handles interactions with an HTTP or HTTPS based JSON-RPC server.

    * ``endpoint_uri`` should be the full URI to the RPC endpoint such as
      ``'https://localhost:8545'``.  For RPC servers behind HTTP connections
      running on port 80 and HTTPS connections running on port 443 the port can
      be omitted from the URI.
    * ``request_kwargs`` this should be a dictionary of keyword arguments which
      will be passed onto the http/https request.


IPCProvider
-----------

.. py:class:: IPCProvider(ipc_path=None, testnet=False):

    This provider handles interaction with an IPC Socket based JSON-RPC
    server.


.. py:currentmodule:: web3.providers.tester


EthereumTesterProvider
----------------------

.. py:class:: EthereumTesterProvider():

    This provider can be used for testing.  It uses an ephemeral blockchain
    backed by the ``ethereum.tester`` module.


TestRPCProvider
---------------

.. py:class:: TestRPCProvider():

    This provider can be used for testing.  It uses an ephemeral blockchain
    backed by the ``ethereum.tester`` module.  This provider will be slower
    than the ``EthereumTesterProvider`` since it uses an HTTP server for RPC
    interactions with.
