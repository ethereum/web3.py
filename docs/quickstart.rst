Quickstart
==========

.. contents:: :local:


Installation
------------

Web3.py can be installed using ``pip`` as follows.

.. code-block:: shell

   $ pip install web3

Or to install with support for the ``TestRPCProvider`` and
``EthereumTesterProvider`` you can use this install command.

.. code-block:: shell

   $ pip install web3[tester]


Or to install with support for gevent based threading:

.. code-block:: shell

   $ pip install web3[gevent]


To enable gevent based threading set the environment variable ``THREADING_BACKEND=gevent``


Installation from source can be done from the root of the project with the
following command.

.. code-block:: shell

   $ python setup.py install


The ``Web3`` object
-------------------

The common entrypoint for interacting with the Web3 library is the ``Web3``
class.  You will need to instantiate a web3 instance.

Web3 takes a connection to existing Ethereum node (*Geth* or *Parity*).
This connection can be either over JSON-RPC using HTTP (TCP/IP)
 or UNIX sockets (IPC).

.. code-block:: python

    >>> from web3 import Web3, KeepAliveRPCProvider, IPCProvider

    # Note that you should create only one RPCProvider per
    # process, as it recycles underlying TCP/IP network connections between
    # your process and Ethereum node
    >>> web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8545'))

    # or for an IPC based connection
    >>> web3 = Web3(IPCProvider())

This ``web3`` instance will now allow you to interact with the Ethereum
blockchain.
