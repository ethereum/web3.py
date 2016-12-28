Providers
========

.. py:module:: web3.providers


Providers are in control of the actual interactions with the blockchain.


.. py:currentmodule:: web3.providers.rpc


RPCProvider
-----------

.. py:class:: RPCProvider(host="127.0.0.1", port=8545, path="/", ssl=False, connection_timeout=10, network_timeout=10)

    This provider handles interaction with an HTTP or HTTPS based JSON-RPC
    server.


.. py:currentmodule:: web3.providers.ipc


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
